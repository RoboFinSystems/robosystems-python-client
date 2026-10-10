from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class ListLedgerReconciliations(BaseModel):
  reconciliations: Optional["ListLedgerReconciliationsReconciliations"]


class ListLedgerReconciliationsReconciliations(BaseModel):
  period: str
  as_of: str = Field(alias="asOf")
  notes: list[str]
  reconciliations: list["ListLedgerReconciliationsReconciliationsReconciliations"]


class ListLedgerReconciliationsReconciliationsReconciliations(BaseModel):
  structure_id: str = Field(alias="structureId")
  name: str
  scope: str
  method: str
  element_id: Optional[str] = Field(alias="elementId")
  required_for_close: bool = Field(alias="requiredForClose")
  materiality: float
  statement_cycle: Optional[str] = Field(alias="statementCycle")
  period: str
  as_of: str = Field(alias="asOf")
  status: str
  unreconciled_difference: Optional[float] = Field(alias="unreconciledDifference")
  accounts_compared: Optional[int] = Field(alias="accountsCompared")
  accounts_different: Optional[int] = Field(alias="accountsDifferent")
  ledger_balance: Optional[float] = Field(alias="ledgerBalance")
  independent_balance: Optional[float] = Field(alias="independentBalance")
  balance_as_of: Optional[str] = Field(alias="balanceAsOf")
  components: list["ListLedgerReconciliationsReconciliationsReconciliationsComponents"]
  roll_forward: Optional[
    "ListLedgerReconciliationsReconciliationsReconciliationsRollForward"
  ] = Field(alias="rollForward")
  source: Optional[str]
  compared_at: Optional[str] = Field(alias="comparedAt")
  fact_set_id: Optional[str] = Field(alias="factSetId")
  compared_by: Optional[str] = Field(alias="comparedBy")
  compared_via: Optional[str] = Field(alias="comparedVia")
  review_required: bool = Field(alias="reviewRequired")
  separate_reviewer: bool = Field(alias="separateReviewer")
  reviewed_by: Optional[str] = Field(alias="reviewedBy")
  reviewed_at: Optional[str] = Field(alias="reviewedAt")
  self_reviewed: Optional[bool] = Field(alias="selfReviewed")
  differences: list[
    "ListLedgerReconciliationsReconciliationsReconciliationsDifferences"
  ]


class ListLedgerReconciliationsReconciliationsReconciliationsComponents(BaseModel):
  name: str
  amount: float
  kind: Optional[str]
  posting_date: Optional[str] = Field(alias="postingDate")
  entry_id: Optional[str] = Field(alias="entryId")
  structure_id: Optional[str] = Field(alias="structureId")
  event_id: Optional[str] = Field(alias="eventId")
  document_id: Optional[str] = Field(alias="documentId")
  note: Optional[str]


class ListLedgerReconciliationsReconciliationsReconciliationsRollForward(BaseModel):
  statement_as_of: str = Field(alias="statementAsOf")
  through: str
  bank_lines: int = Field(alias="bankLines")
  bank_activity: float = Field(alias="bankActivity")
  bank_balance: float = Field(alias="bankBalance")
  ledger_balance: float = Field(alias="ledgerBalance")
  outstanding: float
  feed_balance: Optional[float] = Field(alias="feedBalance")
  feed_balance_read_on: Optional[str] = Field(alias="feedBalanceReadOn")


class ListLedgerReconciliationsReconciliationsReconciliationsDifferences(BaseModel):
  element_id: Optional[str] = Field(alias="elementId")
  account_code: Optional[str] = Field(alias="accountCode")
  account_name: str = Field(alias="accountName")
  source_account_id: Optional[str] = Field(alias="sourceAccountId")
  statement: Optional[str]
  ledger_balance: float = Field(alias="ledgerBalance")
  independent_balance: float = Field(alias="independentBalance")
  difference: float
  status: str
  as_of: Optional[str] = Field(alias="asOf")
  components: list[
    "ListLedgerReconciliationsReconciliationsReconciliationsDifferencesComponents"
  ]
  roll_forward: Optional[
    "ListLedgerReconciliationsReconciliationsReconciliationsDifferencesRollForward"
  ] = Field(alias="rollForward")


class ListLedgerReconciliationsReconciliationsReconciliationsDifferencesComponents(
  BaseModel
):
  name: str
  amount: float
  kind: Optional[str]
  posting_date: Optional[str] = Field(alias="postingDate")
  entry_id: Optional[str] = Field(alias="entryId")
  structure_id: Optional[str] = Field(alias="structureId")
  event_id: Optional[str] = Field(alias="eventId")
  document_id: Optional[str] = Field(alias="documentId")
  note: Optional[str]


class ListLedgerReconciliationsReconciliationsReconciliationsDifferencesRollForward(
  BaseModel
):
  statement_as_of: str = Field(alias="statementAsOf")
  through: str
  bank_lines: int = Field(alias="bankLines")
  bank_activity: float = Field(alias="bankActivity")
  bank_balance: float = Field(alias="bankBalance")
  ledger_balance: float = Field(alias="ledgerBalance")
  outstanding: float
  feed_balance: Optional[float] = Field(alias="feedBalance")
  feed_balance_read_on: Optional[str] = Field(alias="feedBalanceReadOn")


ListLedgerReconciliations.model_rebuild()
ListLedgerReconciliationsReconciliations.model_rebuild()
ListLedgerReconciliationsReconciliationsReconciliations.model_rebuild()
ListLedgerReconciliationsReconciliationsReconciliationsDifferences.model_rebuild()
