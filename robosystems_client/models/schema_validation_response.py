from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.schema_validation_response_compatibility_type_0 import (
    SchemaValidationResponseCompatibilityType0,
  )
  from ..models.schema_validation_response_stats_type_0 import (
    SchemaValidationResponseStatsType0,
  )


T = TypeVar("T", bound="SchemaValidationResponse")


@_attrs_define
class SchemaValidationResponse:
  """Response model for schema validation.

  Attributes:
      valid (bool): Whether the schema is valid
      message (str): Validation message
      errors (Union[None, Unset, list[str]]): List of validation errors (only present when valid=false)
      warnings (Union[None, Unset, list[str]]): List of validation warnings (schema is still valid but has potential
          issues)
      stats (Union['SchemaValidationResponseStatsType0', None, Unset]): Schema statistics (only present when
          valid=true)
      compatibility (Union['SchemaValidationResponseCompatibilityType0', None, Unset]): Compatibility check results
          (only when check_compatibility specified)
  """

  valid: bool
  message: str
  errors: Union[None, Unset, list[str]] = UNSET
  warnings: Union[None, Unset, list[str]] = UNSET
  stats: Union["SchemaValidationResponseStatsType0", None, Unset] = UNSET
  compatibility: Union["SchemaValidationResponseCompatibilityType0", None, Unset] = (
    UNSET
  )
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.schema_validation_response_compatibility_type_0 import (
      SchemaValidationResponseCompatibilityType0,
    )
    from ..models.schema_validation_response_stats_type_0 import (
      SchemaValidationResponseStatsType0,
    )

    valid = self.valid

    message = self.message

    errors: Union[None, Unset, list[str]]
    if isinstance(self.errors, Unset):
      errors = UNSET
    elif isinstance(self.errors, list):
      errors = self.errors

    else:
      errors = self.errors

    warnings: Union[None, Unset, list[str]]
    if isinstance(self.warnings, Unset):
      warnings = UNSET
    elif isinstance(self.warnings, list):
      warnings = self.warnings

    else:
      warnings = self.warnings

    stats: Union[None, Unset, dict[str, Any]]
    if isinstance(self.stats, Unset):
      stats = UNSET
    elif isinstance(self.stats, SchemaValidationResponseStatsType0):
      stats = self.stats.to_dict()
    else:
      stats = self.stats

    compatibility: Union[None, Unset, dict[str, Any]]
    if isinstance(self.compatibility, Unset):
      compatibility = UNSET
    elif isinstance(self.compatibility, SchemaValidationResponseCompatibilityType0):
      compatibility = self.compatibility.to_dict()
    else:
      compatibility = self.compatibility

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "valid": valid,
        "message": message,
      }
    )
    if errors is not UNSET:
      field_dict["errors"] = errors
    if warnings is not UNSET:
      field_dict["warnings"] = warnings
    if stats is not UNSET:
      field_dict["stats"] = stats
    if compatibility is not UNSET:
      field_dict["compatibility"] = compatibility

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.schema_validation_response_compatibility_type_0 import (
      SchemaValidationResponseCompatibilityType0,
    )
    from ..models.schema_validation_response_stats_type_0 import (
      SchemaValidationResponseStatsType0,
    )

    d = dict(src_dict)
    valid = d.pop("valid")

    message = d.pop("message")

    def _parse_errors(data: object) -> Union[None, Unset, list[str]]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, list):
          raise TypeError()
        errors_type_0 = cast(list[str], data)

        return errors_type_0
      except:  # noqa: E722
        pass
      return cast(Union[None, Unset, list[str]], data)

    errors = _parse_errors(d.pop("errors", UNSET))

    def _parse_warnings(data: object) -> Union[None, Unset, list[str]]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, list):
          raise TypeError()
        warnings_type_0 = cast(list[str], data)

        return warnings_type_0
      except:  # noqa: E722
        pass
      return cast(Union[None, Unset, list[str]], data)

    warnings = _parse_warnings(d.pop("warnings", UNSET))

    def _parse_stats(
      data: object,
    ) -> Union["SchemaValidationResponseStatsType0", None, Unset]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        stats_type_0 = SchemaValidationResponseStatsType0.from_dict(data)

        return stats_type_0
      except:  # noqa: E722
        pass
      return cast(Union["SchemaValidationResponseStatsType0", None, Unset], data)

    stats = _parse_stats(d.pop("stats", UNSET))

    def _parse_compatibility(
      data: object,
    ) -> Union["SchemaValidationResponseCompatibilityType0", None, Unset]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        compatibility_type_0 = SchemaValidationResponseCompatibilityType0.from_dict(
          data
        )

        return compatibility_type_0
      except:  # noqa: E722
        pass
      return cast(
        Union["SchemaValidationResponseCompatibilityType0", None, Unset], data
      )

    compatibility = _parse_compatibility(d.pop("compatibility", UNSET))

    schema_validation_response = cls(
      valid=valid,
      message=message,
      errors=errors,
      warnings=warnings,
      stats=stats,
      compatibility=compatibility,
    )

    schema_validation_response.additional_properties = d
    return schema_validation_response

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
