from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="FileStatusUpdate")


@_attrs_define
class FileStatusUpdate:
  """
  Attributes:
      status (str): File status: 'uploaded' (ready for ingest), 'disabled' (exclude from ingest), 'archived' (soft
          deleted)
  """

  status: str

  def to_dict(self) -> dict[str, Any]:
    status = self.status

    field_dict: dict[str, Any] = {}

    field_dict.update(
      {
        "status": status,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    status = d.pop("status")

    file_status_update = cls(
      status=status,
    )

    return file_status_update
