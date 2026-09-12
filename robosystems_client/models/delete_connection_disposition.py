from enum import Enum


class DeleteConnectionDisposition(str, Enum):
  DISCONNECT = "disconnect"
  SEVER = "sever"

  def __str__(self) -> str:
    return str(self.value)
