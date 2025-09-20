import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.agent_mode import AgentMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.agent_response_error_details_type_0 import (
    AgentResponseErrorDetailsType0,
  )
  from ..models.agent_response_metadata_type_0 import AgentResponseMetadataType0
  from ..models.agent_response_tokens_used_type_0 import AgentResponseTokensUsedType0


T = TypeVar("T", bound="AgentResponse")


@_attrs_define
class AgentResponse:
  """Response model for agent interactions.

  Attributes:
      content (str): The agent's response content
      agent_used (str): The agent type that handled the request
      mode_used (AgentMode): Agent execution modes.
      metadata (Union['AgentResponseMetadataType0', None, Unset]): Response metadata including routing info
      tokens_used (Union['AgentResponseTokensUsedType0', None, Unset]): Token usage statistics
      confidence_score (Union[None, Unset, float]): Confidence score of the response
      operation_id (Union[None, Unset, str]): Operation ID for SSE monitoring
      is_partial (Union[Unset, bool]): Whether this is a partial response Default: False.
      error_details (Union['AgentResponseErrorDetailsType0', None, Unset]): Error details if any
      execution_time (Union[None, Unset, float]): Execution time in seconds
      timestamp (Union[Unset, datetime.datetime]): Response timestamp
  """

  content: str
  agent_used: str
  mode_used: AgentMode
  metadata: Union["AgentResponseMetadataType0", None, Unset] = UNSET
  tokens_used: Union["AgentResponseTokensUsedType0", None, Unset] = UNSET
  confidence_score: Union[None, Unset, float] = UNSET
  operation_id: Union[None, Unset, str] = UNSET
  is_partial: Union[Unset, bool] = False
  error_details: Union["AgentResponseErrorDetailsType0", None, Unset] = UNSET
  execution_time: Union[None, Unset, float] = UNSET
  timestamp: Union[Unset, datetime.datetime] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.agent_response_error_details_type_0 import (
      AgentResponseErrorDetailsType0,
    )
    from ..models.agent_response_metadata_type_0 import AgentResponseMetadataType0
    from ..models.agent_response_tokens_used_type_0 import AgentResponseTokensUsedType0

    content = self.content

    agent_used = self.agent_used

    mode_used = self.mode_used.value

    metadata: Union[None, Unset, dict[str, Any]]
    if isinstance(self.metadata, Unset):
      metadata = UNSET
    elif isinstance(self.metadata, AgentResponseMetadataType0):
      metadata = self.metadata.to_dict()
    else:
      metadata = self.metadata

    tokens_used: Union[None, Unset, dict[str, Any]]
    if isinstance(self.tokens_used, Unset):
      tokens_used = UNSET
    elif isinstance(self.tokens_used, AgentResponseTokensUsedType0):
      tokens_used = self.tokens_used.to_dict()
    else:
      tokens_used = self.tokens_used

    confidence_score: Union[None, Unset, float]
    if isinstance(self.confidence_score, Unset):
      confidence_score = UNSET
    else:
      confidence_score = self.confidence_score

    operation_id: Union[None, Unset, str]
    if isinstance(self.operation_id, Unset):
      operation_id = UNSET
    else:
      operation_id = self.operation_id

    is_partial = self.is_partial

    error_details: Union[None, Unset, dict[str, Any]]
    if isinstance(self.error_details, Unset):
      error_details = UNSET
    elif isinstance(self.error_details, AgentResponseErrorDetailsType0):
      error_details = self.error_details.to_dict()
    else:
      error_details = self.error_details

    execution_time: Union[None, Unset, float]
    if isinstance(self.execution_time, Unset):
      execution_time = UNSET
    else:
      execution_time = self.execution_time

    timestamp: Union[Unset, str] = UNSET
    if not isinstance(self.timestamp, Unset):
      timestamp = self.timestamp.isoformat()

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "content": content,
        "agent_used": agent_used,
        "mode_used": mode_used,
      }
    )
    if metadata is not UNSET:
      field_dict["metadata"] = metadata
    if tokens_used is not UNSET:
      field_dict["tokens_used"] = tokens_used
    if confidence_score is not UNSET:
      field_dict["confidence_score"] = confidence_score
    if operation_id is not UNSET:
      field_dict["operation_id"] = operation_id
    if is_partial is not UNSET:
      field_dict["is_partial"] = is_partial
    if error_details is not UNSET:
      field_dict["error_details"] = error_details
    if execution_time is not UNSET:
      field_dict["execution_time"] = execution_time
    if timestamp is not UNSET:
      field_dict["timestamp"] = timestamp

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.agent_response_error_details_type_0 import (
      AgentResponseErrorDetailsType0,
    )
    from ..models.agent_response_metadata_type_0 import AgentResponseMetadataType0
    from ..models.agent_response_tokens_used_type_0 import AgentResponseTokensUsedType0

    d = dict(src_dict)
    content = d.pop("content")

    agent_used = d.pop("agent_used")

    mode_used = AgentMode(d.pop("mode_used"))

    def _parse_metadata(
      data: object,
    ) -> Union["AgentResponseMetadataType0", None, Unset]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        metadata_type_0 = AgentResponseMetadataType0.from_dict(data)

        return metadata_type_0
      except:  # noqa: E722
        pass
      return cast(Union["AgentResponseMetadataType0", None, Unset], data)

    metadata = _parse_metadata(d.pop("metadata", UNSET))

    def _parse_tokens_used(
      data: object,
    ) -> Union["AgentResponseTokensUsedType0", None, Unset]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        tokens_used_type_0 = AgentResponseTokensUsedType0.from_dict(data)

        return tokens_used_type_0
      except:  # noqa: E722
        pass
      return cast(Union["AgentResponseTokensUsedType0", None, Unset], data)

    tokens_used = _parse_tokens_used(d.pop("tokens_used", UNSET))

    def _parse_confidence_score(data: object) -> Union[None, Unset, float]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, float], data)

    confidence_score = _parse_confidence_score(d.pop("confidence_score", UNSET))

    def _parse_operation_id(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    operation_id = _parse_operation_id(d.pop("operation_id", UNSET))

    is_partial = d.pop("is_partial", UNSET)

    def _parse_error_details(
      data: object,
    ) -> Union["AgentResponseErrorDetailsType0", None, Unset]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        error_details_type_0 = AgentResponseErrorDetailsType0.from_dict(data)

        return error_details_type_0
      except:  # noqa: E722
        pass
      return cast(Union["AgentResponseErrorDetailsType0", None, Unset], data)

    error_details = _parse_error_details(d.pop("error_details", UNSET))

    def _parse_execution_time(data: object) -> Union[None, Unset, float]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, float], data)

    execution_time = _parse_execution_time(d.pop("execution_time", UNSET))

    _timestamp = d.pop("timestamp", UNSET)
    timestamp: Union[Unset, datetime.datetime]
    if isinstance(_timestamp, Unset):
      timestamp = UNSET
    else:
      timestamp = isoparse(_timestamp)

    agent_response = cls(
      content=content,
      agent_used=agent_used,
      mode_used=mode_used,
      metadata=metadata,
      tokens_used=tokens_used,
      confidence_score=confidence_score,
      operation_id=operation_id,
      is_partial=is_partial,
      error_details=error_details,
      execution_time=execution_time,
      timestamp=timestamp,
    )

    agent_response.additional_properties = d
    return agent_response

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
