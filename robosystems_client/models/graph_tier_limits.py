from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.graph_tier_backup import GraphTierBackup
  from ..models.graph_tier_copy_operations import GraphTierCopyOperations


T = TypeVar("T", bound="GraphTierLimits")


@_attrs_define
class GraphTierLimits:
  """Resource limits for a tier.

  Attributes:
      storage_gb (int): Storage limit in GB
      monthly_credits (int): Monthly credit allocation
      max_subgraphs (Union[None, int]): Maximum subgraphs (null for unlimited)
      copy_operations (GraphTierCopyOperations): Copy operation limits for a tier.
      backup (GraphTierBackup): Backup configuration for a tier.
  """

  storage_gb: int
  monthly_credits: int
  max_subgraphs: Union[None, int]
  copy_operations: "GraphTierCopyOperations"
  backup: "GraphTierBackup"
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    storage_gb = self.storage_gb

    monthly_credits = self.monthly_credits

    max_subgraphs: Union[None, int]
    max_subgraphs = self.max_subgraphs

    copy_operations = self.copy_operations.to_dict()

    backup = self.backup.to_dict()

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "storage_gb": storage_gb,
        "monthly_credits": monthly_credits,
        "max_subgraphs": max_subgraphs,
        "copy_operations": copy_operations,
        "backup": backup,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.graph_tier_backup import GraphTierBackup
    from ..models.graph_tier_copy_operations import GraphTierCopyOperations

    d = dict(src_dict)
    storage_gb = d.pop("storage_gb")

    monthly_credits = d.pop("monthly_credits")

    def _parse_max_subgraphs(data: object) -> Union[None, int]:
      if data is None:
        return data
      return cast(Union[None, int], data)

    max_subgraphs = _parse_max_subgraphs(d.pop("max_subgraphs"))

    copy_operations = GraphTierCopyOperations.from_dict(d.pop("copy_operations"))

    backup = GraphTierBackup.from_dict(d.pop("backup"))

    graph_tier_limits = cls(
      storage_gb=storage_gb,
      monthly_credits=monthly_credits,
      max_subgraphs=max_subgraphs,
      copy_operations=copy_operations,
      backup=backup,
    )

    graph_tier_limits.additional_properties = d
    return graph_tier_limits

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
