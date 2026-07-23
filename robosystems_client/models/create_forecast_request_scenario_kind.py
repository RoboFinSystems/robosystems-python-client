from enum import Enum


class CreateForecastRequestScenarioKind(str, Enum):
  BUDGET = "budget"
  FORECAST = "forecast"
  PROJECTION = "projection"

  def __str__(self) -> str:
    return str(self.value)
