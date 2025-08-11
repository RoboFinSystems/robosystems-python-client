from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.credit_summary import CreditSummary


T = TypeVar("T", bound="RepositoryCreditsResponse")


@_attrs_define
class RepositoryCreditsResponse:
  """Response for repository-specific credits.

  Attributes:
      repository_type (str): Repository type
      has_access (bool): Whether user has access
      message (Union[Unset, str]): Access message
      credits_ (Union[Unset, CreditSummary]): Credit balance summary.
  """

  repository_type: str
  has_access: bool
  message: Union[Unset, str] = UNSET
  credits_: Union[Unset, "CreditSummary"] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    repository_type = self.repository_type

    has_access = self.has_access

    message = self.message

    credits_: Union[Unset, dict[str, Any]] = UNSET
    if not isinstance(self.credits_, Unset):
      credits_ = self.credits_.to_dict()

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "repository_type": repository_type,
        "has_access": has_access,
      }
    )
    if message is not UNSET:
      field_dict["message"] = message
    if credits_ is not UNSET:
      field_dict["credits"] = credits_

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.credit_summary import CreditSummary

    d = dict(src_dict)
    repository_type = d.pop("repository_type")

    has_access = d.pop("has_access")

    message = d.pop("message", UNSET)

    _credits_ = d.pop("credits", UNSET)
    credits_: Union[Unset, CreditSummary]
    if isinstance(_credits_, Unset):
      credits_ = UNSET
    else:
      credits_ = CreditSummary.from_dict(_credits_)

    repository_credits_response = cls(
      repository_type=repository_type,
      has_access=has_access,
      message=message,
      credits_=credits_,
    )

    repository_credits_response.additional_properties = d
    return repository_credits_response

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
