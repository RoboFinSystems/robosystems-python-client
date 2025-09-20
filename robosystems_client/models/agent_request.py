from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.agent_mode import AgentMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.agent_message import AgentMessage
  from ..models.agent_request_context_type_0 import AgentRequestContextType0
  from ..models.selection_criteria import SelectionCriteria


T = TypeVar("T", bound="AgentRequest")


@_attrs_define
class AgentRequest:
  """Request model for agent interactions.

  Attributes:
      message (str): The query or message to process
      history (Union[Unset, list['AgentMessage']]): Conversation history
      context (Union['AgentRequestContextType0', None, Unset]): Additional context for analysis (e.g., enable_rag,
          include_schema)
      mode (Union[AgentMode, None, Unset]): Execution mode Default: AgentMode.STANDARD.
      agent_type (Union[None, Unset, str]): Specific agent type to use (optional)
      selection_criteria (Union['SelectionCriteria', None, Unset]): Criteria for agent selection
      force_extended_analysis (Union[Unset, bool]): Force extended analysis mode with comprehensive research Default:
          False.
      enable_rag (Union[Unset, bool]): Enable RAG context enrichment Default: True.
      stream (Union[Unset, bool]): Enable streaming response Default: False.
  """

  message: str
  history: Union[Unset, list["AgentMessage"]] = UNSET
  context: Union["AgentRequestContextType0", None, Unset] = UNSET
  mode: Union[AgentMode, None, Unset] = AgentMode.STANDARD
  agent_type: Union[None, Unset, str] = UNSET
  selection_criteria: Union["SelectionCriteria", None, Unset] = UNSET
  force_extended_analysis: Union[Unset, bool] = False
  enable_rag: Union[Unset, bool] = True
  stream: Union[Unset, bool] = False
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.agent_request_context_type_0 import AgentRequestContextType0
    from ..models.selection_criteria import SelectionCriteria

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

    mode: Union[None, Unset, str]
    if isinstance(self.mode, Unset):
      mode = UNSET
    elif isinstance(self.mode, AgentMode):
      mode = self.mode.value
    else:
      mode = self.mode

    agent_type: Union[None, Unset, str]
    if isinstance(self.agent_type, Unset):
      agent_type = UNSET
    else:
      agent_type = self.agent_type

    selection_criteria: Union[None, Unset, dict[str, Any]]
    if isinstance(self.selection_criteria, Unset):
      selection_criteria = UNSET
    elif isinstance(self.selection_criteria, SelectionCriteria):
      selection_criteria = self.selection_criteria.to_dict()
    else:
      selection_criteria = self.selection_criteria

    force_extended_analysis = self.force_extended_analysis

    enable_rag = self.enable_rag

    stream = self.stream

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
    if mode is not UNSET:
      field_dict["mode"] = mode
    if agent_type is not UNSET:
      field_dict["agent_type"] = agent_type
    if selection_criteria is not UNSET:
      field_dict["selection_criteria"] = selection_criteria
    if force_extended_analysis is not UNSET:
      field_dict["force_extended_analysis"] = force_extended_analysis
    if enable_rag is not UNSET:
      field_dict["enable_rag"] = enable_rag
    if stream is not UNSET:
      field_dict["stream"] = stream

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.agent_message import AgentMessage
    from ..models.agent_request_context_type_0 import AgentRequestContextType0
    from ..models.selection_criteria import SelectionCriteria

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

    def _parse_mode(data: object) -> Union[AgentMode, None, Unset]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        mode_type_0 = AgentMode(data)

        return mode_type_0
      except:  # noqa: E722
        pass
      return cast(Union[AgentMode, None, Unset], data)

    mode = _parse_mode(d.pop("mode", UNSET))

    def _parse_agent_type(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    agent_type = _parse_agent_type(d.pop("agent_type", UNSET))

    def _parse_selection_criteria(
      data: object,
    ) -> Union["SelectionCriteria", None, Unset]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        selection_criteria_type_0 = SelectionCriteria.from_dict(data)

        return selection_criteria_type_0
      except:  # noqa: E722
        pass
      return cast(Union["SelectionCriteria", None, Unset], data)

    selection_criteria = _parse_selection_criteria(d.pop("selection_criteria", UNSET))

    force_extended_analysis = d.pop("force_extended_analysis", UNSET)

    enable_rag = d.pop("enable_rag", UNSET)

    stream = d.pop("stream", UNSET)

    agent_request = cls(
      message=message,
      history=history,
      context=context,
      mode=mode,
      agent_type=agent_type,
      selection_criteria=selection_criteria,
      force_extended_analysis=force_extended_analysis,
      enable_rag=enable_rag,
      stream=stream,
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
