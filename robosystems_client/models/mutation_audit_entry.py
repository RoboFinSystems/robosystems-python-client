from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mutation_audit_entry_status import MutationAuditEntryStatus
from ..models.mutation_audit_entry_surface import MutationAuditEntrySurface
from ..types import UNSET, Unset

T = TypeVar("T", bound="MutationAuditEntry")


@_attrs_define
class MutationAuditEntry:
  """One mutating call on the graph.

  Attributes:
      id (str): Audit entry identifier
      occurred_at (datetime.datetime): When the call finished
      surface (MutationAuditEntrySurface): Where the call came from: 'api' for a REST operation, 'mcp' for an external
          MCP client, 'operator' for an in-app AI operator run such as the console's /do
      operation_name (str): The operation or MCP tool that ran
      status (MutationAuditEntryStatus): Whether the call succeeded; a failed call changed nothing it reports.
          'pending' means the call started background work; follow its operation_id for the outcome
      duration_ms (float): How long the call took
      error_code (None | str | Unset): Why a failed call failed
      user_id (None | str | Unset): The user the call ran as
      auth_method (None | str | Unset): How the caller authenticated, for example 'api_key' or 'oauth'
      api_key_prefix (None | str | Unset): The first characters of the API key used, when one was
      request_id (None | str | Unset): The HTTP request that made the call
      operation_id (None | str | Unset): The REST operation's envelope id, or the operator run's operation id: every
          write an operator run makes shares it
      operator_type (None | str | Unset): The operator that made the call, for surface 'operator'
      arguments_fingerprint (None | str | Unset): SHA-256 of the call's arguments. The arguments themselves are not
          stored
      object_ids (list[str] | Unset): Identifiers of the objects the call touched
  """

  id: str
  occurred_at: datetime.datetime
  surface: MutationAuditEntrySurface
  operation_name: str
  status: MutationAuditEntryStatus
  duration_ms: float
  error_code: None | str | Unset = UNSET
  user_id: None | str | Unset = UNSET
  auth_method: None | str | Unset = UNSET
  api_key_prefix: None | str | Unset = UNSET
  request_id: None | str | Unset = UNSET
  operation_id: None | str | Unset = UNSET
  operator_type: None | str | Unset = UNSET
  arguments_fingerprint: None | str | Unset = UNSET
  object_ids: list[str] | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    id = self.id

    occurred_at = self.occurred_at.isoformat()

    surface = self.surface.value

    operation_name = self.operation_name

    status = self.status.value

    duration_ms = self.duration_ms

    error_code: None | str | Unset
    if isinstance(self.error_code, Unset):
      error_code = UNSET
    else:
      error_code = self.error_code

    user_id: None | str | Unset
    if isinstance(self.user_id, Unset):
      user_id = UNSET
    else:
      user_id = self.user_id

    auth_method: None | str | Unset
    if isinstance(self.auth_method, Unset):
      auth_method = UNSET
    else:
      auth_method = self.auth_method

    api_key_prefix: None | str | Unset
    if isinstance(self.api_key_prefix, Unset):
      api_key_prefix = UNSET
    else:
      api_key_prefix = self.api_key_prefix

    request_id: None | str | Unset
    if isinstance(self.request_id, Unset):
      request_id = UNSET
    else:
      request_id = self.request_id

    operation_id: None | str | Unset
    if isinstance(self.operation_id, Unset):
      operation_id = UNSET
    else:
      operation_id = self.operation_id

    operator_type: None | str | Unset
    if isinstance(self.operator_type, Unset):
      operator_type = UNSET
    else:
      operator_type = self.operator_type

    arguments_fingerprint: None | str | Unset
    if isinstance(self.arguments_fingerprint, Unset):
      arguments_fingerprint = UNSET
    else:
      arguments_fingerprint = self.arguments_fingerprint

    object_ids: list[str] | Unset = UNSET
    if not isinstance(self.object_ids, Unset):
      object_ids = self.object_ids

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "id": id,
        "occurred_at": occurred_at,
        "surface": surface,
        "operation_name": operation_name,
        "status": status,
        "duration_ms": duration_ms,
      }
    )
    if error_code is not UNSET:
      field_dict["error_code"] = error_code
    if user_id is not UNSET:
      field_dict["user_id"] = user_id
    if auth_method is not UNSET:
      field_dict["auth_method"] = auth_method
    if api_key_prefix is not UNSET:
      field_dict["api_key_prefix"] = api_key_prefix
    if request_id is not UNSET:
      field_dict["request_id"] = request_id
    if operation_id is not UNSET:
      field_dict["operation_id"] = operation_id
    if operator_type is not UNSET:
      field_dict["operator_type"] = operator_type
    if arguments_fingerprint is not UNSET:
      field_dict["arguments_fingerprint"] = arguments_fingerprint
    if object_ids is not UNSET:
      field_dict["object_ids"] = object_ids

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    id = d.pop("id")

    occurred_at = datetime.datetime.fromisoformat(d.pop("occurred_at"))

    surface = MutationAuditEntrySurface(d.pop("surface"))

    operation_name = d.pop("operation_name")

    status = MutationAuditEntryStatus(d.pop("status"))

    duration_ms = d.pop("duration_ms")

    def _parse_error_code(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    error_code = _parse_error_code(d.pop("error_code", UNSET))

    def _parse_user_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    user_id = _parse_user_id(d.pop("user_id", UNSET))

    def _parse_auth_method(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    auth_method = _parse_auth_method(d.pop("auth_method", UNSET))

    def _parse_api_key_prefix(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    api_key_prefix = _parse_api_key_prefix(d.pop("api_key_prefix", UNSET))

    def _parse_request_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    request_id = _parse_request_id(d.pop("request_id", UNSET))

    def _parse_operation_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    operation_id = _parse_operation_id(d.pop("operation_id", UNSET))

    def _parse_operator_type(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    operator_type = _parse_operator_type(d.pop("operator_type", UNSET))

    def _parse_arguments_fingerprint(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    arguments_fingerprint = _parse_arguments_fingerprint(
      d.pop("arguments_fingerprint", UNSET)
    )

    object_ids = cast(list[str], d.pop("object_ids", UNSET))

    mutation_audit_entry = cls(
      id=id,
      occurred_at=occurred_at,
      surface=surface,
      operation_name=operation_name,
      status=status,
      duration_ms=duration_ms,
      error_code=error_code,
      user_id=user_id,
      auth_method=auth_method,
      api_key_prefix=api_key_prefix,
      request_id=request_id,
      operation_id=operation_id,
      operator_type=operator_type,
      arguments_fingerprint=arguments_fingerprint,
      object_ids=object_ids,
    )

    mutation_audit_entry.additional_properties = d
    return mutation_audit_entry

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
