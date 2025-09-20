from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

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
      repository (str): Repository identifier
      has_access (bool): Whether user has access
      message (Union[None, Unset, str]): Access message
      credits_ (Union['CreditSummary', None, Unset]): Credit summary if access available
  """

  repository: str
  has_access: bool
  message: Union[None, Unset, str] = UNSET
  credits_: Union["CreditSummary", None, Unset] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.credit_summary import CreditSummary

    repository = self.repository

    has_access = self.has_access

    message: Union[None, Unset, str]
    if isinstance(self.message, Unset):
      message = UNSET
    else:
      message = self.message

    credits_: Union[None, Unset, dict[str, Any]]
    if isinstance(self.credits_, Unset):
      credits_ = UNSET
    elif isinstance(self.credits_, CreditSummary):
      credits_ = self.credits_.to_dict()
    else:
      credits_ = self.credits_

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "repository": repository,
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
    repository = d.pop("repository")

    has_access = d.pop("has_access")

    def _parse_message(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    message = _parse_message(d.pop("message", UNSET))

    def _parse_credits_(data: object) -> Union["CreditSummary", None, Unset]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        credits_type_0 = CreditSummary.from_dict(data)

        return credits_type_0
      except:  # noqa: E722
        pass
      return cast(Union["CreditSummary", None, Unset], data)

    credits_ = _parse_credits_(d.pop("credits", UNSET))

    repository_credits_response = cls(
      repository=repository,
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
