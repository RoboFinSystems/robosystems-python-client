from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.taxonomy_block_association_request_association_type import (
  TaxonomyBlockAssociationRequestAssociationType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.taxonomy_block_association_request_metadata import (
    TaxonomyBlockAssociationRequestMetadata,
  )


T = TypeVar("T", bound="TaxonomyBlockAssociationRequest")


@_attrs_define
class TaxonomyBlockAssociationRequest:
  """Association (arc) between two elements, scoped to a structure.

  Attributes:
      structure_ref (str): Envelope-local structure name (references a structure declared in the same envelope).
      from_ref (str): qname of the source element.
      to_ref (str): qname of the target element.
      association_type (TaxonomyBlockAssociationRequestAssociationType): DB ``associations.association_type`` enum.
          ``presentation`` = parent-child hierarchy; ``calculation`` = summation arc.
      order_value (float | None | Unset):
      arcrole (None | str | Unset):
      weight (float | None | Unset): Calculation-arc coefficient (+1 / -1 for summation, other values for weighted
          rollups). Null for non-calculation arcs.
      metadata (TaxonomyBlockAssociationRequestMetadata | Unset):
  """

  structure_ref: str
  from_ref: str
  to_ref: str
  association_type: TaxonomyBlockAssociationRequestAssociationType
  order_value: float | None | Unset = UNSET
  arcrole: None | str | Unset = UNSET
  weight: float | None | Unset = UNSET
  metadata: TaxonomyBlockAssociationRequestMetadata | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    structure_ref = self.structure_ref

    from_ref = self.from_ref

    to_ref = self.to_ref

    association_type = self.association_type.value

    order_value: float | None | Unset
    if isinstance(self.order_value, Unset):
      order_value = UNSET
    else:
      order_value = self.order_value

    arcrole: None | str | Unset
    if isinstance(self.arcrole, Unset):
      arcrole = UNSET
    else:
      arcrole = self.arcrole

    weight: float | None | Unset
    if isinstance(self.weight, Unset):
      weight = UNSET
    else:
      weight = self.weight

    metadata: dict[str, Any] | Unset = UNSET
    if not isinstance(self.metadata, Unset):
      metadata = self.metadata.to_dict()

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "structure_ref": structure_ref,
        "from_ref": from_ref,
        "to_ref": to_ref,
        "association_type": association_type,
      }
    )
    if order_value is not UNSET:
      field_dict["order_value"] = order_value
    if arcrole is not UNSET:
      field_dict["arcrole"] = arcrole
    if weight is not UNSET:
      field_dict["weight"] = weight
    if metadata is not UNSET:
      field_dict["metadata"] = metadata

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.taxonomy_block_association_request_metadata import (
      TaxonomyBlockAssociationRequestMetadata,
    )

    d = dict(src_dict)
    structure_ref = d.pop("structure_ref")

    from_ref = d.pop("from_ref")

    to_ref = d.pop("to_ref")

    association_type = TaxonomyBlockAssociationRequestAssociationType(
      d.pop("association_type")
    )

    def _parse_order_value(data: object) -> float | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(float | None | Unset, data)

    order_value = _parse_order_value(d.pop("order_value", UNSET))

    def _parse_arcrole(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    arcrole = _parse_arcrole(d.pop("arcrole", UNSET))

    def _parse_weight(data: object) -> float | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(float | None | Unset, data)

    weight = _parse_weight(d.pop("weight", UNSET))

    _metadata = d.pop("metadata", UNSET)
    metadata: TaxonomyBlockAssociationRequestMetadata | Unset
    if isinstance(_metadata, Unset):
      metadata = UNSET
    else:
      metadata = TaxonomyBlockAssociationRequestMetadata.from_dict(_metadata)

    taxonomy_block_association_request = cls(
      structure_ref=structure_ref,
      from_ref=from_ref,
      to_ref=to_ref,
      association_type=association_type,
      order_value=order_value,
      arcrole=arcrole,
      weight=weight,
      metadata=metadata,
    )

    taxonomy_block_association_request.additional_properties = d
    return taxonomy_block_association_request

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
