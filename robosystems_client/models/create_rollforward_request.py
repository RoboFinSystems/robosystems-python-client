from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_rollforward_request_validation_mode import (
  CreateRollforwardRequestValidationMode,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.attribution_filter import AttributionFilter


T = TypeVar("T", bound="CreateRollforwardRequest")


@_attrs_define
class CreateRollforwardRequest:
  """Create a rollforward Information Block.

  Mirrors :class:`CreateScheduleRequest` in shape. The block decomposes
  the period change in ``bs_source_qname`` across the declared
  attribution filters. Residual (Δ BS - Σ filter matches) falls back to
  the default change tag — or, if no default is declared, surfaces as
  an unattributed fact tagged with a synthetic residual concept.

      Attributes:
          name (str): Human-readable block name.
          bs_source_qname (str): QName of the balance-sheet element whose period delta this block decomposes. Resolved to
              ``bs_source_element_id`` at create time.
          default_change_tag_qname (None | str | Unset): QName of the fallback flow concept (Tier 1 default change tag).
              Residual amount — Δ BS minus the sum of filter-matched amounts — is attributed to this concept. When omitted,
              residual surfaces unattributed; the validation_mode setting governs whether that's a hard error.
          attribution_filters (list[AttributionFilter] | Unset): Filter predicates routing LineItems to flow concepts.
          validation_mode (CreateRollforwardRequestValidationMode | Unset): How the renderer arbitrates when Σ filter
              matches != Δ BS. ``strict`` raises; ``residual_as_default`` emits the residual as a default-tag fact (the common
              case); ``warn_only`` logs and lets the imbalance pass. Default:
              CreateRollforwardRequestValidationMode.RESIDUAL_AS_DEFAULT.
          taxonomy_id (None | str | Unset): Owning taxonomy id (auto-resolved from ``bs_source_qname`` when omitted).
  """

  name: str
  bs_source_qname: str
  default_change_tag_qname: None | str | Unset = UNSET
  attribution_filters: list[AttributionFilter] | Unset = UNSET
  validation_mode: CreateRollforwardRequestValidationMode | Unset = (
    CreateRollforwardRequestValidationMode.RESIDUAL_AS_DEFAULT
  )
  taxonomy_id: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    name = self.name

    bs_source_qname = self.bs_source_qname

    default_change_tag_qname: None | str | Unset
    if isinstance(self.default_change_tag_qname, Unset):
      default_change_tag_qname = UNSET
    else:
      default_change_tag_qname = self.default_change_tag_qname

    attribution_filters: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.attribution_filters, Unset):
      attribution_filters = []
      for attribution_filters_item_data in self.attribution_filters:
        attribution_filters_item = attribution_filters_item_data.to_dict()
        attribution_filters.append(attribution_filters_item)

    validation_mode: str | Unset = UNSET
    if not isinstance(self.validation_mode, Unset):
      validation_mode = self.validation_mode.value

    taxonomy_id: None | str | Unset
    if isinstance(self.taxonomy_id, Unset):
      taxonomy_id = UNSET
    else:
      taxonomy_id = self.taxonomy_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "name": name,
        "bs_source_qname": bs_source_qname,
      }
    )
    if default_change_tag_qname is not UNSET:
      field_dict["default_change_tag_qname"] = default_change_tag_qname
    if attribution_filters is not UNSET:
      field_dict["attribution_filters"] = attribution_filters
    if validation_mode is not UNSET:
      field_dict["validation_mode"] = validation_mode
    if taxonomy_id is not UNSET:
      field_dict["taxonomy_id"] = taxonomy_id

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.attribution_filter import AttributionFilter

    d = dict(src_dict)
    name = d.pop("name")

    bs_source_qname = d.pop("bs_source_qname")

    def _parse_default_change_tag_qname(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    default_change_tag_qname = _parse_default_change_tag_qname(
      d.pop("default_change_tag_qname", UNSET)
    )

    _attribution_filters = d.pop("attribution_filters", UNSET)
    attribution_filters: list[AttributionFilter] | Unset = UNSET
    if _attribution_filters is not UNSET:
      attribution_filters = []
      for attribution_filters_item_data in _attribution_filters:
        attribution_filters_item = AttributionFilter.from_dict(
          attribution_filters_item_data
        )

        attribution_filters.append(attribution_filters_item)

    _validation_mode = d.pop("validation_mode", UNSET)
    validation_mode: CreateRollforwardRequestValidationMode | Unset
    if isinstance(_validation_mode, Unset):
      validation_mode = UNSET
    else:
      validation_mode = CreateRollforwardRequestValidationMode(_validation_mode)

    def _parse_taxonomy_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    taxonomy_id = _parse_taxonomy_id(d.pop("taxonomy_id", UNSET))

    create_rollforward_request = cls(
      name=name,
      bs_source_qname=bs_source_qname,
      default_change_tag_qname=default_change_tag_qname,
      attribution_filters=attribution_filters,
      validation_mode=validation_mode,
      taxonomy_id=taxonomy_id,
    )

    create_rollforward_request.additional_properties = d
    return create_rollforward_request

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
