import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.health_status_details_type_0 import HealthStatusDetailsType0


T = TypeVar("T", bound="HealthStatus")


@_attrs_define
class HealthStatus:
  """Health check status information.

  Attributes:
      status (str): Current health status
      timestamp (datetime.datetime): Time of health check
      details (Union['HealthStatusDetailsType0', None, Unset]): Additional health check details
  """

  status: str
  timestamp: datetime.datetime
  details: Union["HealthStatusDetailsType0", None, Unset] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.health_status_details_type_0 import HealthStatusDetailsType0

    status = self.status

    timestamp = self.timestamp.isoformat()

    details: Union[None, Unset, dict[str, Any]]
    if isinstance(self.details, Unset):
      details = UNSET
    elif isinstance(self.details, HealthStatusDetailsType0):
      details = self.details.to_dict()
    else:
      details = self.details

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "status": status,
        "timestamp": timestamp,
      }
    )
    if details is not UNSET:
      field_dict["details"] = details

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.health_status_details_type_0 import HealthStatusDetailsType0

    d = dict(src_dict)
    status = d.pop("status")

    timestamp = isoparse(d.pop("timestamp"))

    def _parse_details(data: object) -> Union["HealthStatusDetailsType0", None, Unset]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        details_type_0 = HealthStatusDetailsType0.from_dict(data)

        return details_type_0
      except:  # noqa: E722
        pass
      return cast(Union["HealthStatusDetailsType0", None, Unset], data)

    details = _parse_details(d.pop("details", UNSET))

    health_status = cls(
      status=status,
      timestamp=timestamp,
      details=details,
    )

    health_status.additional_properties = d
    return health_status

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
