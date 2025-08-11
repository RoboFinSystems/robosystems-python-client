from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.agent_message import AgentMessage
  from ..models.agent_request_context_type_0 import AgentRequestContextType0


T = TypeVar("T", bound="AgentRequest")


@_attrs_define
class AgentRequest:
  """Request model for financial agent interactions.

  Attributes:
      message (str): Financial analysis query
      history (Union[Unset, list['AgentMessage']]): Conversation history
      context (Union['AgentRequestContextType0', None, Unset]): Additional context for analysis (e.g., include_schema,
          limit_results)
      force_extended_analysis (Union[Unset, bool]): Force extended analysis mode with comprehensive research (like
          Claude Desktop's deep research) Default: False.
  """

  message: str
  history: Union[Unset, list["AgentMessage"]] = UNSET
  context: Union["AgentRequestContextType0", None, Unset] = UNSET
  force_extended_analysis: Union[Unset, bool] = False
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.agent_request_context_type_0 import AgentRequestContextType0

    message = self.message

    history: Union[Unset, list[dict[str, Any]]] = UNSET
    if not isinstance(self.history, Unset):
      history = []
      for history_item_data in self.history:
        history_item = history_item_data.to_dict()
        history.append(history_item)

    context: Union[None, Unset, dict[str, Any]]
    if isinstance(self.context, Unset):
      context = UNSET
    elif isinstance(self.context, AgentRequestContextType0):
      context = self.context.to_dict()
    else:
      context = self.context

    force_extended_analysis = self.force_extended_analysis

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "message": message,
      }
    )
    if history is not UNSET:
      field_dict["history"] = history
    if context is not UNSET:
      field_dict["context"] = context
    if force_extended_analysis is not UNSET:
      field_dict["force_extended_analysis"] = force_extended_analysis

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.agent_message import AgentMessage
    from ..models.agent_request_context_type_0 import AgentRequestContextType0

    d = dict(src_dict)
    message = d.pop("message")

    history = []
    _history = d.pop("history", UNSET)
    for history_item_data in _history or []:
      history_item = AgentMessage.from_dict(history_item_data)

      history.append(history_item)

    def _parse_context(data: object) -> Union["AgentRequestContextType0", None, Unset]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        context_type_0 = AgentRequestContextType0.from_dict(data)

        return context_type_0
      except:  # noqa: E722
        pass
      return cast(Union["AgentRequestContextType0", None, Unset], data)

    context = _parse_context(d.pop("context", UNSET))

    force_extended_analysis = d.pop("force_extended_analysis", UNSET)

    agent_request = cls(
      message=message,
      history=history,
      context=context,
      force_extended_analysis=force_extended_analysis,
    )

    agent_request.additional_properties = d
    return agent_request

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
