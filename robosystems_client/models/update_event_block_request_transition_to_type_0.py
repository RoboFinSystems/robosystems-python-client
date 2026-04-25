from enum import Enum


class UpdateEventBlockRequestTransitionToType0(str, Enum):
  COMMITTED = "committed"
  FULFILLED = "fulfilled"
  PENDING = "pending"
  SUPERSEDED = "superseded"
  VOIDED = "voided"

  def __str__(self) -> str:
    return str(self.value)
