from enum import Enum


class CreateEventBlockRequestResourceTypeType0(str, Enum):
  GOODS = "goods"
  INFORMATION = "information"
  LABOR = "labor"
  MONEY = "money"
  OBLIGATION = "obligation"
  RIGHT = "right"
  SERVICES = "services"

  def __str__(self) -> str:
    return str(self.value)
