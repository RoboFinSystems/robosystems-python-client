from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.rendering_lite import RenderingLite


T = TypeVar("T", bound="ViewProjections")


@_attrs_define
class ViewProjections:
  """Charlie's six ``type-of View`` arms, surfaced at the envelope boundary.

  Each projection is computed server-side at envelope-build time when
  its source data is available. The frontend's ``BlockView`` dispatcher
  routes to the projection component matching the user's selected view
  mode; missing projections (those still in backlog) render as empty
  states without breaking the dispatcher.

  Today: ``rendering`` is computed for the statement family.
  Other arms (``fact_table``, ``model_structure``, ``verification_results``,
  ``report_elements``, ``business_rules``) come online as their backend
  support lands; ``fact_table`` is trivially derivable from
  ``InformationBlockEnvelope.facts`` and may stay as a frontend-only
  projection.

      Attributes:
          rendering (None | RenderingLite | Unset):
  """

  rendering: None | RenderingLite | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.rendering_lite import RenderingLite

    rendering: dict[str, Any] | None | Unset
    if isinstance(self.rendering, Unset):
      rendering = UNSET
    elif isinstance(self.rendering, RenderingLite):
      rendering = self.rendering.to_dict()
    else:
      rendering = self.rendering

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update({})
    if rendering is not UNSET:
      field_dict["rendering"] = rendering

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.rendering_lite import RenderingLite

    d = dict(src_dict)

    def _parse_rendering(data: object) -> None | RenderingLite | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        rendering_type_0 = RenderingLite.from_dict(data)

        return rendering_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | RenderingLite | Unset, data)

    rendering = _parse_rendering(d.pop("rendering", UNSET))

    view_projections = cls(
      rendering=rendering,
    )

    view_projections.additional_properties = d
    return view_projections

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
