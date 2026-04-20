from enum import Enum


class CreateElementRequestSource(str, Enum):
  FAC = "fac"
  IFRS = "ifrs"
  IMPORT = "import"
  NATIVE = "native"
  PLAID = "plaid"
  QUICKBOOKS = "quickbooks"
  RS_GAAP = "rs-gaap"
  US_GAAP = "us-gaap"
  XERO = "xero"

  def __str__(self) -> str:
    return str(self.value)
