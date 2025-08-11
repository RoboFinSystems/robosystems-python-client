from enum import Enum


class ResponseMode(str, Enum):
  ASYNC = "async"
  AUTO = "auto"
  STREAM = "stream"
  SYNC = "sync"

  def __str__(self) -> str:
    return str(self.value)
