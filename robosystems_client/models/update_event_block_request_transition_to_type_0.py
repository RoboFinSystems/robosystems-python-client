from enum import Enum


class UpdateEventBlockRequestTransitionToType0(str, Enum):
  CLASSIFIED = "classified"
  COMMITTED = "committed"
  FULFILLED = "fulfilled"
  PENDING = "pending"
  SUPERSEDED = "superseded"
  VOIDED = "voided"

  def __str__(self) -> str:
    return str(self.value)
