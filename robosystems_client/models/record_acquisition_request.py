from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.acquisition_allocation import AcquisitionAllocation


T = TypeVar("T", bound="RecordAcquisitionRequest")


@_attrs_define
class RecordAcquisitionRequest:
  """A member bought from its outside owners: what the parent paid them,
  and how the excess over its share of the member's equity at acquisition is
  allocated. The engine never invents a fair value; each comes from the
  person, with the basis.

      Attributes:
          entity_id (str): The member acquired, consolidated in full, with `joined_on` set and its opening balance
              recorded at acquisition.
          consideration (int): Cents the parent paid the sellers for its interest. Its investment line names the seller,
              not the member, which is why it is given here.
          basis (str): Where the consideration and fair values come from: the purchase agreement, a valuation.
          nci_fair_value (int | None | Unset): Cents: the fair value of the outside owners' interest at acquisition, for
              goodwill on the whole business (ASC 805). Omitted, the outside owners carry their share of the identifiable net
              assets and goodwill is the parent's alone.
          allocations (list[AcquisitionAllocation] | Unset): Fair-value step-ups; what is left of the excess is goodwill.
          confirm_bargain_purchase (bool | Unset): Required when the parent paid less than its share of the fair value of
              what it acquired. ASC 805 has the acquirer reassess before recognizing the gain; set it only after that review.
              Default: False.
  """

  entity_id: str
  consideration: int
  basis: str
  nci_fair_value: int | None | Unset = UNSET
  allocations: list[AcquisitionAllocation] | Unset = UNSET
  confirm_bargain_purchase: bool | Unset = False
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    entity_id = self.entity_id

    consideration = self.consideration

    basis = self.basis

    nci_fair_value: int | None | Unset
    if isinstance(self.nci_fair_value, Unset):
      nci_fair_value = UNSET
    else:
      nci_fair_value = self.nci_fair_value

    allocations: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.allocations, Unset):
      allocations = []
      for allocations_item_data in self.allocations:
        allocations_item = allocations_item_data.to_dict()
        allocations.append(allocations_item)

    confirm_bargain_purchase = self.confirm_bargain_purchase

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "entity_id": entity_id,
        "consideration": consideration,
        "basis": basis,
      }
    )
    if nci_fair_value is not UNSET:
      field_dict["nci_fair_value"] = nci_fair_value
    if allocations is not UNSET:
      field_dict["allocations"] = allocations
    if confirm_bargain_purchase is not UNSET:
      field_dict["confirm_bargain_purchase"] = confirm_bargain_purchase

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.acquisition_allocation import AcquisitionAllocation

    d = dict(src_dict)
    entity_id = d.pop("entity_id")

    consideration = d.pop("consideration")

    basis = d.pop("basis")

    def _parse_nci_fair_value(data: object) -> int | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(int | None | Unset, data)

    nci_fair_value = _parse_nci_fair_value(d.pop("nci_fair_value", UNSET))

    _allocations = d.pop("allocations", UNSET)
    allocations: list[AcquisitionAllocation] | Unset = UNSET
    if _allocations is not UNSET:
      allocations = []
      for allocations_item_data in _allocations:
        allocations_item = AcquisitionAllocation.from_dict(allocations_item_data)

        allocations.append(allocations_item)

    confirm_bargain_purchase = d.pop("confirm_bargain_purchase", UNSET)

    record_acquisition_request = cls(
      entity_id=entity_id,
      consideration=consideration,
      basis=basis,
      nci_fair_value=nci_fair_value,
      allocations=allocations,
      confirm_bargain_purchase=confirm_bargain_purchase,
    )

    record_acquisition_request.additional_properties = d
    return record_acquisition_request

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
