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
  structure_id: Optional[str] = Field(alias="structureId")
  event_id: Optional[str] = Field(alias="eventId")
  document_id: Optional[str] = Field(alias="documentId")
  note: Optional[str]


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


class ListLedgerReconciliationsReconciliationsReconciliationsDifferencesComponents(
  BaseModel
):
  name: str
  amount: float
  structure_id: Optional[str] = Field(alias="structureId")
  event_id: Optional[str] = Field(alias="eventId")
  document_id: Optional[str] = Field(alias="documentId")
  note: Optional[str]


ListLedgerReconciliations.model_rebuild()
ListLedgerReconciliationsReconciliations.model_rebuild()
ListLedgerReconciliationsReconciliationsReconciliations.model_rebuild()
ListLedgerReconciliationsReconciliationsReconciliationsDifferences.model_rebuild()
