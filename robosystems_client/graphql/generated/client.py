from typing import Any

from .base_client import BaseClient
from .get_ledger_summary import GetLedgerSummary
from .operations import GET_LEDGER_SUMMARY_GQL


def gql(q: str) -> str:
  return q


class Client(BaseClient):
  def get_ledger_summary(self, **kwargs: Any) -> GetLedgerSummary:
    variables: dict[str, object] = {}
    response = self.execute(
      query=GET_LEDGER_SUMMARY_GQL,
      operation_name="GetLedgerSummary",
      variables=variables,
      **kwargs,
    )
    data = self.get_data(response)
    return GetLedgerSummary.model_validate(data)
