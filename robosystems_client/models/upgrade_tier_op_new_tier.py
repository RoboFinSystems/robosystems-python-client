from enum import Enum


class UpgradeTierOpNewTier(str, Enum):
  LADYBUG_LARGE = "ladybug-large"
  LADYBUG_STANDARD = "ladybug-standard"
  LADYBUG_XLARGE = "ladybug-xlarge"

  def __str__(self) -> str:
    return str(self.value)
