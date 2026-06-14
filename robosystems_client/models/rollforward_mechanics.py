from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rollforward_mechanics_validation_mode import (
  RollforwardMechanicsValidationMode,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.attribution_filter import AttributionFilter


T = TypeVar("T", bound="RollforwardMechanics")


@_attrs_define
class RollforwardMechanics:
  """Filter-based attribution mechanics for ``block_type='rollforward'``.

  Filter-based attribution: each block decomposes one BS source
  element's period delta into a list of flow concepts via declared
  :class:`AttributionFilter` predicates. The renderer evaluates the
  filters against ledger LineItems at envelope-build time, emits one
  attributed fact per filter per period, and arbitrates any residual
  against the default change tag fallback.

  Reads directly from the typed ``structures.artifact_mechanics`` JSONB
  column. ``attribution_filters`` rides as nested JSON; the predicate
  union widens as new predicate shapes are added — currently only
  ``line_item_metadata_field`` is carried.

      Attributes:
          bs_source_element_id (str): Element id of the balance-sheet source whose period delta this block decomposes.
              Resolved from ``bs_source_qname`` at create time.
          bs_source_qname (str): QName of the BS source element (e.g. ``mini:CashAndCashEquivalents``). Round-tripped for
              caller convenience; ``bs_source_element_id`` is authoritative.
          kind (Literal['rollforward'] | Unset):  Default: 'rollforward'.
          default_change_tag_element_id (None | str | Unset): Element id of the default change tag — the fallback flow
              concept that receives any residual (Δ BS − Σ filter matches). Null when no default is declared; behavior on
              residual then follows ``validation_mode``.
          default_change_tag_qname (None | str | Unset): QName of the default change tag (e.g. ``rs-
              gaap:IncreaseDecreaseInCashAndCashEquivalents``). Round-tripped for caller convenience and operator-readable
              envelopes; ``default_change_tag_element_id`` is authoritative. Null iff ``default_change_tag_element_id`` is
              null.
          attribution_filters (list[AttributionFilter] | Unset): Filter predicates routing LineItems to flow concepts. The
              renderer evaluates each filter against the period's LineItems, aggregates signed amounts, and emits one fact per
              filter per period.
          validation_mode (RollforwardMechanicsValidationMode | Unset): Renderer arbitration policy when Σ filter matches
              != Δ BS. ``strict`` raises; ``residual_as_default`` emits the residual as a default-tag fact (the common case);
              ``warn_only`` logs and lets the imbalance pass. Default: RollforwardMechanicsValidationMode.RESIDUAL_AS_DEFAULT.
  """

  bs_source_element_id: str
  bs_source_qname: str
  kind: Literal["rollforward"] | Unset = "rollforward"
  default_change_tag_element_id: None | str | Unset = UNSET
  default_change_tag_qname: None | str | Unset = UNSET
  attribution_filters: list[AttributionFilter] | Unset = UNSET
  validation_mode: RollforwardMechanicsValidationMode | Unset = (
    RollforwardMechanicsValidationMode.RESIDUAL_AS_DEFAULT
  )
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    bs_source_element_id = self.bs_source_element_id

    bs_source_qname = self.bs_source_qname

    kind = self.kind

    default_change_tag_element_id: None | str | Unset
    if isinstance(self.default_change_tag_element_id, Unset):
      default_change_tag_element_id = UNSET
    else:
      default_change_tag_element_id = self.default_change_tag_element_id

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

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "bs_source_element_id": bs_source_element_id,
        "bs_source_qname": bs_source_qname,
      }
    )
    if kind is not UNSET:
      field_dict["kind"] = kind
    if default_change_tag_element_id is not UNSET:
      field_dict["default_change_tag_element_id"] = default_change_tag_element_id
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
    bs_source_element_id = d.pop("bs_source_element_id")

    bs_source_qname = d.pop("bs_source_qname")

    kind = cast(Literal["rollforward"] | Unset, d.pop("kind", UNSET))
    if kind != "rollforward" and not isinstance(kind, Unset):
      raise ValueError(f"kind must match const 'rollforward', got '{kind}'")

    def _parse_default_change_tag_element_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    default_change_tag_element_id = _parse_default_change_tag_element_id(
      d.pop("default_change_tag_element_id", UNSET)
    )

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
    validation_mode: RollforwardMechanicsValidationMode | Unset
    if isinstance(_validation_mode, Unset):
      validation_mode = UNSET
    else:
      validation_mode = RollforwardMechanicsValidationMode(_validation_mode)

    rollforward_mechanics = cls(
      bs_source_element_id=bs_source_element_id,
      bs_source_qname=bs_source_qname,
      kind=kind,
      default_change_tag_element_id=default_change_tag_element_id,
      default_change_tag_qname=default_change_tag_qname,
      attribution_filters=attribution_filters,
      validation_mode=validation_mode,
    )

    rollforward_mechanics.additional_properties = d
    return rollforward_mechanics

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
