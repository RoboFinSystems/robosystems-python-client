from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.agent_response_metadata_type_0 import AgentResponseMetadataType0


T = TypeVar("T", bound="AgentResponse")


@_attrs_define
class AgentResponse:
  """Response model for financial agent interactions.

  Attributes:
      response (str): Financial analysis response
      metadata (Union['AgentResponseMetadataType0', None, Unset]): Analysis metadata (e.g., analysis_type, graph_id)
      operation_id (Union[None, Unset, str]): SSE operation ID for monitoring extended analysis via
          /v1/operations/{operation_id}/stream
      is_partial (Union[Unset, bool]): Whether this is a partial response with more analysis coming Default: False.
  """

  response: str
  metadata: Union["AgentResponseMetadataType0", None, Unset] = UNSET
  operation_id: Union[None, Unset, str] = UNSET
  is_partial: Union[Unset, bool] = False
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.agent_response_metadata_type_0 import AgentResponseMetadataType0

    response = self.response

    metadata: Union[None, Unset, dict[str, Any]]
    if isinstance(self.metadata, Unset):
      metadata = UNSET
    elif isinstance(self.metadata, AgentResponseMetadataType0):
      metadata = self.metadata.to_dict()
    else:
      metadata = self.metadata

    operation_id: Union[None, Unset, str]
    if isinstance(self.operation_id, Unset):
      operation_id = UNSET
    else:
      operation_id = self.operation_id

    is_partial = self.is_partial

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "response": response,
      }
    )
    if metadata is not UNSET:
      field_dict["metadata"] = metadata
    if operation_id is not UNSET:
      field_dict["operation_id"] = operation_id
    if is_partial is not UNSET:
      field_dict["is_partial"] = is_partial

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.agent_response_metadata_type_0 import AgentResponseMetadataType0

    d = dict(src_dict)
    response = d.pop("response")

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

    def _parse_operation_id(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    operation_id = _parse_operation_id(d.pop("operation_id", UNSET))

    is_partial = d.pop("is_partial", UNSET)

    agent_response = cls(
      response=response,
      metadata=metadata,
      operation_id=operation_id,
      is_partial=is_partial,
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
