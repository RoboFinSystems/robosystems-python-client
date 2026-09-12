from enum import Enum


class InitializeChartOfAccountsRequestTemplate(str, Enum):
  PRODUCT = "product"
  SAAS = "saas"
  SERVICES = "services"

  def __str__(self) -> str:
    return str(self.value)
