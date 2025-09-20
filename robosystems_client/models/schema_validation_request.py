from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.schema_validation_request_schema_definition_type_0 import (
    SchemaValidationRequestSchemaDefinitionType0,
  )


T = TypeVar("T", bound="SchemaValidationRequest")


@_attrs_define
class SchemaValidationRequest:
  """Request model for schema validation.

  Attributes:
      schema_definition (Union['SchemaValidationRequestSchemaDefinitionType0', str]): Schema definition as JSON dict
          or JSON/YAML string
      format_ (Union[Unset, str]): Schema format: json, yaml, or dict Default: 'json'.
      check_compatibility (Union[None, Unset, list[str]]): List of existing schema extensions to check compatibility
          with
  """

  schema_definition: Union["SchemaValidationRequestSchemaDefinitionType0", str]
  format_: Union[Unset, str] = "json"
  check_compatibility: Union[None, Unset, list[str]] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.schema_validation_request_schema_definition_type_0 import (
      SchemaValidationRequestSchemaDefinitionType0,
    )

    schema_definition: Union[dict[str, Any], str]
    if isinstance(self.schema_definition, SchemaValidationRequestSchemaDefinitionType0):
      schema_definition = self.schema_definition.to_dict()
    else:
      schema_definition = self.schema_definition

    format_ = self.format_

    check_compatibility: Union[None, Unset, list[str]]
    if isinstance(self.check_compatibility, Unset):
      check_compatibility = UNSET
    elif isinstance(self.check_compatibility, list):
      check_compatibility = self.check_compatibility

    else:
      check_compatibility = self.check_compatibility

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "schema_definition": schema_definition,
      }
    )
    if format_ is not UNSET:
      field_dict["format"] = format_
    if check_compatibility is not UNSET:
      field_dict["check_compatibility"] = check_compatibility

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.schema_validation_request_schema_definition_type_0 import (
      SchemaValidationRequestSchemaDefinitionType0,
    )

    d = dict(src_dict)

    def _parse_schema_definition(
      data: object,
    ) -> Union["SchemaValidationRequestSchemaDefinitionType0", str]:
      try:
        if not isinstance(data, dict):
          raise TypeError()
        schema_definition_type_0 = (
          SchemaValidationRequestSchemaDefinitionType0.from_dict(data)
        )

        return schema_definition_type_0
      except:  # noqa: E722
        pass
      return cast(Union["SchemaValidationRequestSchemaDefinitionType0", str], data)

    schema_definition = _parse_schema_definition(d.pop("schema_definition"))

    format_ = d.pop("format", UNSET)

    def _parse_check_compatibility(data: object) -> Union[None, Unset, list[str]]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, list):
          raise TypeError()
        check_compatibility_type_0 = cast(list[str], data)

        return check_compatibility_type_0
      except:  # noqa: E722
        pass
      return cast(Union[None, Unset, list[str]], data)

    check_compatibility = _parse_check_compatibility(
      d.pop("check_compatibility", UNSET)
    )

    schema_validation_request = cls(
      schema_definition=schema_definition,
      format_=format_,
      check_compatibility=check_compatibility,
    )

    schema_validation_request.additional_properties = d
    return schema_validation_request

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
