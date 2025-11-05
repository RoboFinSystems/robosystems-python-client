from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.backup_limits import BackupLimits
  from ..models.copy_operation_limits import CopyOperationLimits
  from ..models.credit_limits import CreditLimits
  from ..models.query_limits import QueryLimits
  from ..models.rate_limits import RateLimits
  from ..models.storage_limits import StorageLimits


T = TypeVar("T", bound="GraphLimitsResponse")


@_attrs_define
class GraphLimitsResponse:
  """Response model for comprehensive graph operational limits.

  Attributes:
      graph_id (str): Graph database identifier
      subscription_tier (str): User's subscription tier
      graph_tier (str): Graph's database tier
      is_shared_repository (bool): Whether this is a shared repository
      storage (StorageLimits): Storage limits information.
      queries (QueryLimits): Query operation limits.
      copy_operations (CopyOperationLimits): Copy/ingestion operation limits.
      backups (BackupLimits): Backup operation limits.
      rate_limits (RateLimits): API rate limits.
      credits_ (Union['CreditLimits', None, Unset]): AI credit limits (if applicable)
  """

  graph_id: str
  subscription_tier: str
  graph_tier: str
  is_shared_repository: bool
  storage: "StorageLimits"
  queries: "QueryLimits"
  copy_operations: "CopyOperationLimits"
  backups: "BackupLimits"
  rate_limits: "RateLimits"
  credits_: Union["CreditLimits", None, Unset] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.credit_limits import CreditLimits

    graph_id = self.graph_id

    subscription_tier = self.subscription_tier

    graph_tier = self.graph_tier

    is_shared_repository = self.is_shared_repository

    storage = self.storage.to_dict()

    queries = self.queries.to_dict()

    copy_operations = self.copy_operations.to_dict()

    backups = self.backups.to_dict()

    rate_limits = self.rate_limits.to_dict()

    credits_: Union[None, Unset, dict[str, Any]]
    if isinstance(self.credits_, Unset):
      credits_ = UNSET
    elif isinstance(self.credits_, CreditLimits):
      credits_ = self.credits_.to_dict()
    else:
      credits_ = self.credits_

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "graph_id": graph_id,
        "subscription_tier": subscription_tier,
        "graph_tier": graph_tier,
        "is_shared_repository": is_shared_repository,
        "storage": storage,
        "queries": queries,
        "copy_operations": copy_operations,
        "backups": backups,
        "rate_limits": rate_limits,
      }
    )
    if credits_ is not UNSET:
      field_dict["credits"] = credits_

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.backup_limits import BackupLimits
    from ..models.copy_operation_limits import CopyOperationLimits
    from ..models.credit_limits import CreditLimits
    from ..models.query_limits import QueryLimits
    from ..models.rate_limits import RateLimits
    from ..models.storage_limits import StorageLimits

    d = dict(src_dict)
    graph_id = d.pop("graph_id")

    subscription_tier = d.pop("subscription_tier")

    graph_tier = d.pop("graph_tier")

    is_shared_repository = d.pop("is_shared_repository")

    storage = StorageLimits.from_dict(d.pop("storage"))

    queries = QueryLimits.from_dict(d.pop("queries"))

    copy_operations = CopyOperationLimits.from_dict(d.pop("copy_operations"))

    backups = BackupLimits.from_dict(d.pop("backups"))

    rate_limits = RateLimits.from_dict(d.pop("rate_limits"))

    def _parse_credits_(data: object) -> Union["CreditLimits", None, Unset]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        credits_type_0 = CreditLimits.from_dict(data)

        return credits_type_0
      except:  # noqa: E722
        pass
      return cast(Union["CreditLimits", None, Unset], data)

    credits_ = _parse_credits_(d.pop("credits", UNSET))

    graph_limits_response = cls(
      graph_id=graph_id,
      subscription_tier=subscription_tier,
      graph_tier=graph_tier,
      is_shared_repository=is_shared_repository,
      storage=storage,
      queries=queries,
      copy_operations=copy_operations,
      backups=backups,
      rate_limits=rate_limits,
      credits_=credits_,
    )

    graph_limits_response.additional_properties = d
    return graph_limits_response

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
