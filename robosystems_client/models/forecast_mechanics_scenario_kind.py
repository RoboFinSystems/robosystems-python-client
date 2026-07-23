from enum import Enum


class ForecastMechanicsScenarioKind(str, Enum):
  BUDGET = "budget"
  FORECAST = "forecast"
  PROJECTION = "projection"

  def __str__(self) -> str:
    return str(self.value)
