from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_rollforward_request_validation_mode_type_0 import (
  UpdateRollforwardRequestValidationModeType0,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.attribution_filter import AttributionFilter


T = TypeVar("T", bound="UpdateRollforwardRequest")


@_attrs_define
class UpdateRollforwardRequest:
  """Update mutable fields on a rollforward block.

  Editable: name, default_change_tag_qname, attribution_filters,
  validation_mode. The BS source is fixed once the block is created
  (changing it would invalidate every previously rendered period); to
  change BS source, delete and re-create.

  **Partial-update semantics**: omitted (``None``) fields mean "leave
  unchanged" — there is no wire-level way to *clear* a previously set
  default change tag or empty the attribution_filters list via this
  endpoint. To remove the default tag entirely, delete and re-create
  the rollforward block. The asymmetry is deliberate: an explicit
  clear-sentinel adds wire-shape complexity for a use case that rarely
  arises in practice (default tags are typically set during initial
  authoring and only swapped, not removed).

      Attributes:
          structure_id (str): Structure ID of the rollforward block.
          name (None | str | Unset):
          default_change_tag_qname (None | str | Unset): New default change tag qname. Pass a value to *change* the
              default; omit (``None``) to leave unchanged. There is no wire-level way to clear a previously set default — see
              the class docstring.
          attribution_filters (list[AttributionFilter] | None | Unset):
          validation_mode (None | Unset | UpdateRollforwardRequestValidationModeType0):
  """

  structure_id: str
  name: None | str | Unset = UNSET
  default_change_tag_qname: None | str | Unset = UNSET
  attribution_filters: list[AttributionFilter] | None | Unset = UNSET
  validation_mode: None | Unset | UpdateRollforwardRequestValidationModeType0 = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    structure_id = self.structure_id

    name: None | str | Unset
    if isinstance(self.name, Unset):
      name = UNSET
    else:
      name = self.name

    default_change_tag_qname: None | str | Unset
    if isinstance(self.default_change_tag_qname, Unset):
      default_change_tag_qname = UNSET
    else:
      default_change_tag_qname = self.default_change_tag_qname

    attribution_filters: list[dict[str, Any]] | None | Unset
    if isinstance(self.attribution_filters, Unset):
      attribution_filters = UNSET
    elif isinstance(self.attribution_filters, list):
      attribution_filters = []
      for attribution_filters_type_0_item_data in self.attribution_filters:
        attribution_filters_type_0_item = attribution_filters_type_0_item_data.to_dict()
        attribution_filters.append(attribution_filters_type_0_item)

    else:
      attribution_filters = self.attribution_filters

    validation_mode: None | str | Unset
    if isinstance(self.validation_mode, Unset):
      validation_mode = UNSET
    elif isinstance(self.validation_mode, UpdateRollforwardRequestValidationModeType0):
      validation_mode = self.validation_mode.value
    else:
      validation_mode = self.validation_mode

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "structure_id": structure_id,
      }
    )
    if name is not UNSET:
      field_dict["name"] = name
    if default_change_tag_qname is not UNSET:
      field_dict["default_change_tag_qname"] = default_change_tag_qname
    if attribution_filters is not UNSET:
      field_dict["attribution_filters"] = attribution_filters
    if validation_mode is not UNSET:
      field_dict["validation_mode"] = validation_mode

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.attribution_filter import AttributionFilter

    d = dict(src_dict)
    structure_id = d.pop("structure_id")

    def _parse_name(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    name = _parse_name(d.pop("name", UNSET))

    def _parse_default_change_tag_qname(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    default_change_tag_qname = _parse_default_change_tag_qname(
      d.pop("default_change_tag_qname", UNSET)
    )

    def _parse_attribution_filters(
      data: object,
    ) -> list[AttributionFilter] | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, list):
          raise TypeError()
        attribution_filters_type_0 = []
        _attribution_filters_type_0 = data
        for attribution_filters_type_0_item_data in _attribution_filters_type_0:
          attribution_filters_type_0_item = AttributionFilter.from_dict(
            attribution_filters_type_0_item_data
          )

          attribution_filters_type_0.append(attribution_filters_type_0_item)

        return attribution_filters_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(list[AttributionFilter] | None | Unset, data)

    attribution_filters = _parse_attribution_filters(
      d.pop("attribution_filters", UNSET)
    )

    def _parse_validation_mode(
      data: object,
    ) -> None | Unset | UpdateRollforwardRequestValidationModeType0:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        validation_mode_type_0 = UpdateRollforwardRequestValidationModeType0(data)

        return validation_mode_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | Unset | UpdateRollforwardRequestValidationModeType0, data)

    validation_mode = _parse_validation_mode(d.pop("validation_mode", UNSET))

    update_rollforward_request = cls(
      structure_id=structure_id,
      name=name,
      default_change_tag_qname=default_change_tag_qname,
      attribution_filters=attribution_filters,
      validation_mode=validation_mode,
    )

    update_rollforward_request.additional_properties = d
    return update_rollforward_request

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
