from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AgentMetadataResponse")


@_attrs_define
class AgentMetadataResponse:
  """Response for agent metadata.

  Attributes:
      name (str): Agent name
      description (str): Agent description
      version (str): Agent version
      capabilities (list[str]): Agent capabilities
      supported_modes (list[str]): Supported execution modes
      requires_credits (bool): Whether agent requires credits
      author (Union[None, Unset, str]): Agent author
      tags (Union[Unset, list[str]]): Agent tags
  """

  name: str
  description: str
  version: str
  capabilities: list[str]
  supported_modes: list[str]
  requires_credits: bool
  author: Union[None, Unset, str] = UNSET
  tags: Union[Unset, list[str]] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    name = self.name

    description = self.description

    version = self.version

    capabilities = self.capabilities

    supported_modes = self.supported_modes

    requires_credits = self.requires_credits

    author: Union[None, Unset, str]
    if isinstance(self.author, Unset):
      author = UNSET
    else:
      author = self.author

    tags: Union[Unset, list[str]] = UNSET
    if not isinstance(self.tags, Unset):
      tags = self.tags

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "name": name,
        "description": description,
        "version": version,
        "capabilities": capabilities,
        "supported_modes": supported_modes,
        "requires_credits": requires_credits,
      }
    )
    if author is not UNSET:
      field_dict["author"] = author
    if tags is not UNSET:
      field_dict["tags"] = tags

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    name = d.pop("name")

    description = d.pop("description")

    version = d.pop("version")

    capabilities = cast(list[str], d.pop("capabilities"))

    supported_modes = cast(list[str], d.pop("supported_modes"))

    requires_credits = d.pop("requires_credits")

    def _parse_author(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    author = _parse_author(d.pop("author", UNSET))

    tags = cast(list[str], d.pop("tags", UNSET))

    agent_metadata_response = cls(
      name=name,
      description=description,
      version=version,
      capabilities=capabilities,
      supported_modes=supported_modes,
      requires_credits=requires_credits,
      author=author,
      tags=tags,
    )

    agent_metadata_response.additional_properties = d
    return agent_metadata_response

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
