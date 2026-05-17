from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.operator_mode import OperatorMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.operator_response_error_details_type_0 import (
    OperatorResponseErrorDetailsType0,
  )
  from ..models.operator_response_metadata_type_0 import OperatorResponseMetadataType0
  from ..models.operator_response_tokens_used_type_0 import (
    OperatorResponseTokensUsedType0,
  )


T = TypeVar("T", bound="OperatorResponse")


@_attrs_define
class OperatorResponse:
  """Response model for operator interactions.

  Attributes:
      content (str): The operator's response content
      operator_used (str): The operator type that handled the request
      mode_used (OperatorMode): Operator execution modes.
      metadata (None | OperatorResponseMetadataType0 | Unset): Response metadata including routing info
      tokens_used (None | OperatorResponseTokensUsedType0 | Unset): Token usage statistics
      confidence_score (float | None | Unset): Confidence score of the response (0.0-1.0 scale)
      operation_id (None | str | Unset): Operation ID for SSE monitoring
      is_partial (bool | Unset): Whether this is a partial response Default: False.
      error_details (None | OperatorResponseErrorDetailsType0 | Unset): Error details if any
      execution_time (float | None | Unset): Execution time in seconds
      timestamp (datetime.datetime | Unset): Response timestamp
  """

  content: str
  operator_used: str
  mode_used: OperatorMode
  metadata: None | OperatorResponseMetadataType0 | Unset = UNSET
  tokens_used: None | OperatorResponseTokensUsedType0 | Unset = UNSET
  confidence_score: float | None | Unset = UNSET
  operation_id: None | str | Unset = UNSET
  is_partial: bool | Unset = False
  error_details: None | OperatorResponseErrorDetailsType0 | Unset = UNSET
  execution_time: float | None | Unset = UNSET
  timestamp: datetime.datetime | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.operator_response_error_details_type_0 import (
      OperatorResponseErrorDetailsType0,
    )
    from ..models.operator_response_metadata_type_0 import OperatorResponseMetadataType0
    from ..models.operator_response_tokens_used_type_0 import (
      OperatorResponseTokensUsedType0,
    )

    content = self.content

    operator_used = self.operator_used

    mode_used = self.mode_used.value

    metadata: dict[str, Any] | None | Unset
    if isinstance(self.metadata, Unset):
      metadata = UNSET
    elif isinstance(self.metadata, OperatorResponseMetadataType0):
      metadata = self.metadata.to_dict()
    else:
      metadata = self.metadata

    tokens_used: dict[str, Any] | None | Unset
    if isinstance(self.tokens_used, Unset):
      tokens_used = UNSET
    elif isinstance(self.tokens_used, OperatorResponseTokensUsedType0):
      tokens_used = self.tokens_used.to_dict()
    else:
      tokens_used = self.tokens_used

    confidence_score: float | None | Unset
    if isinstance(self.confidence_score, Unset):
      confidence_score = UNSET
    else:
      confidence_score = self.confidence_score

    operation_id: None | str | Unset
    if isinstance(self.operation_id, Unset):
      operation_id = UNSET
    else:
      operation_id = self.operation_id

    is_partial = self.is_partial

    error_details: dict[str, Any] | None | Unset
    if isinstance(self.error_details, Unset):
      error_details = UNSET
    elif isinstance(self.error_details, OperatorResponseErrorDetailsType0):
      error_details = self.error_details.to_dict()
    else:
      error_details = self.error_details

    execution_time: float | None | Unset
    if isinstance(self.execution_time, Unset):
      execution_time = UNSET
    else:
      execution_time = self.execution_time

    timestamp: str | Unset = UNSET
    if not isinstance(self.timestamp, Unset):
      timestamp = self.timestamp.isoformat()

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "content": content,
        "operator_used": operator_used,
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
    from ..models.operator_response_error_details_type_0 import (
      OperatorResponseErrorDetailsType0,
    )
    from ..models.operator_response_metadata_type_0 import OperatorResponseMetadataType0
    from ..models.operator_response_tokens_used_type_0 import (
      OperatorResponseTokensUsedType0,
    )

    d = dict(src_dict)
    content = d.pop("content")

    operator_used = d.pop("operator_used")

    mode_used = OperatorMode(d.pop("mode_used"))

    def _parse_metadata(data: object) -> None | OperatorResponseMetadataType0 | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        metadata_type_0 = OperatorResponseMetadataType0.from_dict(data)

        return metadata_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | OperatorResponseMetadataType0 | Unset, data)

    metadata = _parse_metadata(d.pop("metadata", UNSET))

    def _parse_tokens_used(
      data: object,
    ) -> None | OperatorResponseTokensUsedType0 | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        tokens_used_type_0 = OperatorResponseTokensUsedType0.from_dict(data)

        return tokens_used_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | OperatorResponseTokensUsedType0 | Unset, data)

    tokens_used = _parse_tokens_used(d.pop("tokens_used", UNSET))

    def _parse_confidence_score(data: object) -> float | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(float | None | Unset, data)

    confidence_score = _parse_confidence_score(d.pop("confidence_score", UNSET))

    def _parse_operation_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    operation_id = _parse_operation_id(d.pop("operation_id", UNSET))

    is_partial = d.pop("is_partial", UNSET)

    def _parse_error_details(
      data: object,
    ) -> None | OperatorResponseErrorDetailsType0 | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        error_details_type_0 = OperatorResponseErrorDetailsType0.from_dict(data)

        return error_details_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | OperatorResponseErrorDetailsType0 | Unset, data)

    error_details = _parse_error_details(d.pop("error_details", UNSET))

    def _parse_execution_time(data: object) -> float | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(float | None | Unset, data)

    execution_time = _parse_execution_time(d.pop("execution_time", UNSET))

    _timestamp = d.pop("timestamp", UNSET)
    timestamp: datetime.datetime | Unset
    if isinstance(_timestamp, Unset):
      timestamp = UNSET
    else:
      timestamp = isoparse(_timestamp)

    operator_response = cls(
      content=content,
      operator_used=operator_used,
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

    operator_response.additional_properties = d
    return operator_response

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
