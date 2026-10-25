from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.operation_resume_request_input import OperationResumeRequestInput


T = TypeVar("T", bound="OperationResumeRequest")


@_attrs_define
class OperationResumeRequest:
  """Answer for an operation paused at a checkpoint (`awaiting_input`).

  Attributes:
      input_ (OperationResumeRequestInput | Unset): The decision the paused run asked for, in whatever shape its
          prompt described. Delivered to the task as `params['resume']['input']`.
  """

  input_: OperationResumeRequestInput | Unset = UNSET

  def to_dict(self) -> dict[str, Any]:
    input_: dict[str, Any] | Unset = UNSET
    if not isinstance(self.input_, Unset):
      input_ = self.input_.to_dict()

    field_dict: dict[str, Any] = {}

    field_dict.update({})
    if input_ is not UNSET:
      field_dict["input"] = input_

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.operation_resume_request_input import OperationResumeRequestInput

    d = dict(src_dict)
    _input_ = d.pop("input", UNSET)
    input_: OperationResumeRequestInput | Unset
    if isinstance(_input_, Unset):
      input_ = UNSET
    else:
      input_ = OperationResumeRequestInput.from_dict(_input_)

    operation_resume_request = cls(
      input_=input_,
    )

    return operation_resume_request
