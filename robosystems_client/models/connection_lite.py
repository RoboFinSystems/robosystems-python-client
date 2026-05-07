from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.classification_lite import ClassificationLite


T = TypeVar("T", bound="ConnectionLite")


@_attrs_define
class ConnectionLite:
  """Connection (= Association) projection.

  Renamed at the API boundary to match Charlie's ontology vocabulary.
  The underlying storage table is still ``associations``.

      Attributes:
          id (str):
          from_element_id (str):
          to_element_id (str):
          association_type (str): presentation | calculation | mapping | equivalence | general-special | essence-alias
          arcrole (None | str | Unset):
          order_value (float | None | Unset):
          weight (float | None | Unset):
          classifications (list[ClassificationLite] | Unset): Association-level classifications — concept_arrangement,
              member_arrangement, named_disclosure rows from the junction. Empty for library-seeded associations that haven't
              been classified yet.
  """

  id: str
  from_element_id: str
  to_element_id: str
  association_type: str
  arcrole: None | str | Unset = UNSET
  order_value: float | None | Unset = UNSET
  weight: float | None | Unset = UNSET
  classifications: list[ClassificationLite] | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    id = self.id

    from_element_id = self.from_element_id

    to_element_id = self.to_element_id

    association_type = self.association_type

    arcrole: None | str | Unset
    if isinstance(self.arcrole, Unset):
      arcrole = UNSET
    else:
      arcrole = self.arcrole

    order_value: float | None | Unset
    if isinstance(self.order_value, Unset):
      order_value = UNSET
    else:
      order_value = self.order_value

    weight: float | None | Unset
    if isinstance(self.weight, Unset):
      weight = UNSET
    else:
      weight = self.weight

    classifications: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.classifications, Unset):
      classifications = []
      for classifications_item_data in self.classifications:
        classifications_item = classifications_item_data.to_dict()
        classifications.append(classifications_item)

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "id": id,
        "from_element_id": from_element_id,
        "to_element_id": to_element_id,
        "association_type": association_type,
      }
    )
    if arcrole is not UNSET:
      field_dict["arcrole"] = arcrole
    if order_value is not UNSET:
      field_dict["order_value"] = order_value
    if weight is not UNSET:
      field_dict["weight"] = weight
    if classifications is not UNSET:
      field_dict["classifications"] = classifications

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.classification_lite import ClassificationLite

    d = dict(src_dict)
    id = d.pop("id")

    from_element_id = d.pop("from_element_id")

    to_element_id = d.pop("to_element_id")

    association_type = d.pop("association_type")

    def _parse_arcrole(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    arcrole = _parse_arcrole(d.pop("arcrole", UNSET))

    def _parse_order_value(data: object) -> float | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(float | None | Unset, data)

    order_value = _parse_order_value(d.pop("order_value", UNSET))

    def _parse_weight(data: object) -> float | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(float | None | Unset, data)

    weight = _parse_weight(d.pop("weight", UNSET))

    _classifications = d.pop("classifications", UNSET)
    classifications: list[ClassificationLite] | Unset = UNSET
    if _classifications is not UNSET:
      classifications = []
      for classifications_item_data in _classifications:
        classifications_item = ClassificationLite.from_dict(classifications_item_data)

        classifications.append(classifications_item)

    connection_lite = cls(
      id=id,
      from_element_id=from_element_id,
      to_element_id=to_element_id,
      association_type=association_type,
      arcrole=arcrole,
      order_value=order_value,
      weight=weight,
      classifications=classifications,
    )

    connection_lite.additional_properties = d
    return connection_lite

  @property
  def additional_keys(self) -> list[str]:
    return list(self.additional_properties.keys())

  def __getitem__(self, key: str) -> Any:
    return self.additional_properties[key]

  def __setitem__(self, key: str, value: Any) -> None:
    self.additional_properties[key] = value

  def __delitem__(self, key: str) -> None:
    del self.additional_properties[key]

  def __contains__(self, key: str) -> bool:
    return key in self.additional_properties
