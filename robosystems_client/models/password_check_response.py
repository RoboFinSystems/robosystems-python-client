from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.password_check_response_character_types import (
    PasswordCheckResponseCharacterTypes,
  )


T = TypeVar("T", bound="PasswordCheckResponse")


@_attrs_define
class PasswordCheckResponse:
  """Password strength check response model.

  Attributes:
      is_valid (bool): Whether password meets requirements
      strength (str): Password strength level
      score (int): Password strength score (0-100)
      errors (list[str]): Validation errors
      suggestions (list[str]): Improvement suggestions
      character_types (PasswordCheckResponseCharacterTypes): Character type analysis
  """

  is_valid: bool
  strength: str
  score: int
  errors: list[str]
  suggestions: list[str]
  character_types: "PasswordCheckResponseCharacterTypes"
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    is_valid = self.is_valid

    strength = self.strength

    score = self.score

    errors = self.errors

    suggestions = self.suggestions

    character_types = self.character_types.to_dict()

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "is_valid": is_valid,
        "strength": strength,
        "score": score,
        "errors": errors,
        "suggestions": suggestions,
        "character_types": character_types,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.password_check_response_character_types import (
      PasswordCheckResponseCharacterTypes,
    )

    d = dict(src_dict)
    is_valid = d.pop("is_valid")

    strength = d.pop("strength")

    score = d.pop("score")

    errors = cast(list[str], d.pop("errors"))

    suggestions = cast(list[str], d.pop("suggestions"))

    character_types = PasswordCheckResponseCharacterTypes.from_dict(
      d.pop("character_types")
    )

    password_check_response = cls(
      is_valid=is_valid,
      strength=strength,
      score=score,
      errors=errors,
      suggestions=suggestions,
      character_types=character_types,
    )

    password_check_response.additional_properties = d
    return password_check_response

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
