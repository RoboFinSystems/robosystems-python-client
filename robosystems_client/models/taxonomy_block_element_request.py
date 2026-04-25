from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.taxonomy_block_element_request_metadata import (
    TaxonomyBlockElementRequestMetadata,
  )


T = TypeVar("T", bound="TaxonomyBlockElementRequest")


@_attrs_define
class TaxonomyBlockElementRequest:
  """Element definition inside a Taxonomy Block envelope.

  ``qname`` is the envelope-local identifier — must be unique within the
  envelope's ``elements`` list and is used by association / rule / patch
  payloads as the reference token. ``parent_ref`` may reference another
  envelope-local qname or, for ``reporting_extension`` blocks, a library
  element qname.

      Attributes:
          qname (str): Envelope-local element identifier. Must be unique within the envelope's ``elements`` list. Used as
              the reference token for associations, rules, and update patches.
          name (str): Human-readable element name (e.g. 'Total Assets').
          trait (None | str | Unset): FASB metamodel trait for the element. Required for ``chart_of_accounts`` blocks;
              optional for ``custom_ontology``.
          balance_type (None | str | Unset): 'debit' | 'credit' | null for non-monetary concepts.
          element_type (str | Unset): 'concept' | 'abstract' | 'axis' | 'member' | 'hypercube'. Default: 'concept'.
          period_type (None | str | Unset): 'instant' | 'duration' | null (null = derive from classification during
              validation).
          is_monetary (bool | Unset): True for dollar-denominated concepts. Default: True.
          description (None | str | Unset):
          code (None | str | Unset): Optional chart-of-accounts code (e.g. '1000', '4100-02'). Only meaningful for
              ``chart_of_accounts`` blocks.
          sub_classification (None | str | Unset):
          parent_ref (None | str | Unset): qname of the parent element — either another envelope-local qname or, for
              ``reporting_extension`` blocks, a library element qname.
          metadata (TaxonomyBlockElementRequestMetadata | Unset):
  """

  qname: str
  name: str
  trait: None | str | Unset = UNSET
  balance_type: None | str | Unset = UNSET
  element_type: str | Unset = "concept"
  period_type: None | str | Unset = UNSET
  is_monetary: bool | Unset = True
  description: None | str | Unset = UNSET
  code: None | str | Unset = UNSET
  sub_classification: None | str | Unset = UNSET
  parent_ref: None | str | Unset = UNSET
  metadata: TaxonomyBlockElementRequestMetadata | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    qname = self.qname

    name = self.name

    trait: None | str | Unset
    if isinstance(self.trait, Unset):
      trait = UNSET
    else:
      trait = self.trait

    balance_type: None | str | Unset
    if isinstance(self.balance_type, Unset):
      balance_type = UNSET
    else:
      balance_type = self.balance_type

    element_type = self.element_type

    period_type: None | str | Unset
    if isinstance(self.period_type, Unset):
      period_type = UNSET
    else:
      period_type = self.period_type

    is_monetary = self.is_monetary

    description: None | str | Unset
    if isinstance(self.description, Unset):
      description = UNSET
    else:
      description = self.description

    code: None | str | Unset
    if isinstance(self.code, Unset):
      code = UNSET
    else:
      code = self.code

    sub_classification: None | str | Unset
    if isinstance(self.sub_classification, Unset):
      sub_classification = UNSET
    else:
      sub_classification = self.sub_classification

    parent_ref: None | str | Unset
    if isinstance(self.parent_ref, Unset):
      parent_ref = UNSET
    else:
      parent_ref = self.parent_ref

    metadata: dict[str, Any] | Unset = UNSET
    if not isinstance(self.metadata, Unset):
      metadata = self.metadata.to_dict()

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "qname": qname,
        "name": name,
      }
    )
    if trait is not UNSET:
      field_dict["trait"] = trait
    if balance_type is not UNSET:
      field_dict["balance_type"] = balance_type
    if element_type is not UNSET:
      field_dict["element_type"] = element_type
    if period_type is not UNSET:
      field_dict["period_type"] = period_type
    if is_monetary is not UNSET:
      field_dict["is_monetary"] = is_monetary
    if description is not UNSET:
      field_dict["description"] = description
    if code is not UNSET:
      field_dict["code"] = code
    if sub_classification is not UNSET:
      field_dict["sub_classification"] = sub_classification
    if parent_ref is not UNSET:
      field_dict["parent_ref"] = parent_ref
    if metadata is not UNSET:
      field_dict["metadata"] = metadata

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.taxonomy_block_element_request_metadata import (
      TaxonomyBlockElementRequestMetadata,
    )

    d = dict(src_dict)
    qname = d.pop("qname")

    name = d.pop("name")

    def _parse_trait(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    trait = _parse_trait(d.pop("trait", UNSET))

    def _parse_balance_type(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    balance_type = _parse_balance_type(d.pop("balance_type", UNSET))

    element_type = d.pop("element_type", UNSET)

    def _parse_period_type(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    period_type = _parse_period_type(d.pop("period_type", UNSET))

    is_monetary = d.pop("is_monetary", UNSET)

    def _parse_description(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    description = _parse_description(d.pop("description", UNSET))

    def _parse_code(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    code = _parse_code(d.pop("code", UNSET))

    def _parse_sub_classification(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    sub_classification = _parse_sub_classification(d.pop("sub_classification", UNSET))

    def _parse_parent_ref(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    parent_ref = _parse_parent_ref(d.pop("parent_ref", UNSET))

    _metadata = d.pop("metadata", UNSET)
    metadata: TaxonomyBlockElementRequestMetadata | Unset
    if isinstance(_metadata, Unset):
      metadata = UNSET
    else:
      metadata = TaxonomyBlockElementRequestMetadata.from_dict(_metadata)

    taxonomy_block_element_request = cls(
      qname=qname,
      name=name,
      trait=trait,
      balance_type=balance_type,
      element_type=element_type,
      period_type=period_type,
      is_monetary=is_monetary,
      description=description,
      code=code,
      sub_classification=sub_classification,
      parent_ref=parent_ref,
      metadata=metadata,
    )

    taxonomy_block_element_request.additional_properties = d
    return taxonomy_block_element_request

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
