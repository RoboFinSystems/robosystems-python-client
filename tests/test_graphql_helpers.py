"""Unit tests for ``robosystems_client.graphql.client`` module-level helpers.

These helpers sit on the GraphQL → Pydantic boundary. ``camel_to_snake``
and ``keys_to_snake`` normalize the camelCase field names Strawberry
emits into the snake_case shape the generated ``from_dict`` helpers
expect. ``strip_none_vars`` drops ``None`` variables so the facade's
"``None`` means not provided" convention doesn't accidentally surface as
explicit GraphQL ``null`` in resolvers that distinguish the two.
"""

from __future__ import annotations

import pytest

from robosystems_client.graphql.client import (
  camel_to_snake,
  keys_to_snake,
  strip_none_vars,
)


@pytest.mark.unit
class TestCamelToSnake:
  """``camel_to_snake`` must handle acronyms without shredding them.

  A naive regex like ``(?<!^)(?=[A-Z])`` would turn ``getCIK`` into
  ``get_c_i_k``. The acronym-aware two-group pattern handles CIK / URI /
  XML / SIC / LEI cases that appear in the real backend schema.
  """

  def test_simple_camel_case(self):
    assert camel_to_snake("fooBar") == "foo_bar"
    assert camel_to_snake("legalName") == "legal_name"
    assert camel_to_snake("isActive") == "is_active"

  def test_already_snake_case(self):
    assert camel_to_snake("already_snake") == "already_snake"
    assert camel_to_snake("id") == "id"

  def test_trailing_acronym(self):
    assert camel_to_snake("getCIK") == "get_cik"
    assert camel_to_snake("parentLEI") == "parent_lei"
    assert camel_to_snake("parentSIC") == "parent_sic"

  def test_leading_acronym(self):
    assert camel_to_snake("XMLData") == "xml_data"
    assert camel_to_snake("URIPath") == "uri_path"

  def test_middle_acronym(self):
    assert camel_to_snake("parseXMLData") == "parse_xml_data"
    assert camel_to_snake("fetchJSONResponse") == "fetch_json_response"

  def test_single_letter_words(self):
    assert camel_to_snake("aB") == "a_b"
    assert camel_to_snake("xYZ") == "x_yz"


@pytest.mark.unit
class TestKeysToSnake:
  def test_flat_dict(self):
    assert keys_to_snake({"legalName": "ACME", "entityId": "ent_1"}) == {
      "legal_name": "ACME",
      "entity_id": "ent_1",
    }

  def test_nested_dict(self):
    result = keys_to_snake(
      {
        "entityId": "ent_1",
        "metadata": {"sourceGraphId": "kg_1", "parentCIK": "0001234567"},
      }
    )
    assert result == {
      "entity_id": "ent_1",
      "metadata": {"source_graph_id": "kg_1", "parent_cik": "0001234567"},
    }

  def test_list_of_dicts(self):
    result = keys_to_snake(
      [{"entityId": "ent_1"}, {"entityId": "ent_2", "isActive": True}]
    )
    assert result == [
      {"entity_id": "ent_1"},
      {"entity_id": "ent_2", "is_active": True},
    ]

  def test_preserves_scalars(self):
    assert keys_to_snake("unchanged") == "unchanged"
    assert keys_to_snake(42) == 42
    assert keys_to_snake(None) is None
    assert keys_to_snake(True) is True


@pytest.mark.unit
class TestStripNoneVars:
  def test_removes_none_values(self):
    assert strip_none_vars(
      {"entityId": None, "limit": 100, "offset": 0, "securityType": None}
    ) == {"limit": 100, "offset": 0}

  def test_keeps_falsy_but_not_none(self):
    # False, 0, "", and [] are all valid variable values that must not
    # be stripped — only None means "not provided".
    result = strip_none_vars({"isActive": False, "limit": 0, "search": "", "tags": []})
    assert result == {"isActive": False, "limit": 0, "search": "", "tags": []}

  def test_all_none(self):
    assert strip_none_vars({"a": None, "b": None}) == {}

  def test_empty(self):
    assert strip_none_vars({}) == {}
