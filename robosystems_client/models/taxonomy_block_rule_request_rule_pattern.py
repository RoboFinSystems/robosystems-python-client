from enum import Enum


class TaxonomyBlockRuleRequestRulePattern(str, Enum):
  ADJUSTMENT = "Adjustment"
  COEXISTS = "CoExists"
  EQUALTO = "EqualTo"
  EXISTS = "Exists"
  GREATERTHAN = "GreaterThan"
  GREATERTHANOREQUALTOZERO = "GreaterThanOrEqualToZero"
  LESSTHAN = "LessThan"
  ROLLFORWARD = "RollForward"
  ROLLUP = "RollUp"
  SUMEQUALS = "SumEquals"
  VARIANCE = "Variance"

  def __str__(self) -> str:
    return str(self.value)
