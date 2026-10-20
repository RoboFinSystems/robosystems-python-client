from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class AgedReceivables(BaseModel):
  aged_receivables: "AgedReceivablesAgedReceivables" = Field(alias="agedReceivables")


class AgedReceivablesAgedReceivables(BaseModel):
  kind: str
  as_of: str = Field(alias="asOf")
  scope: str
  entity_id: Optional[str] = Field(alias="entityId")
  member_entity_ids: list[str] = Field(alias="memberEntityIds")
  buckets: "AgedReceivablesAgedReceivablesBuckets"
  agents: list["AgedReceivablesAgedReceivablesAgents"]
  defaulted_due_date_count: int = Field(alias="defaultedDueDateCount")
  intercompany: list["AgedReceivablesAgedReceivablesIntercompany"]
  pairs: list["AgedReceivablesAgedReceivablesPairs"]
  tie_outs: list["AgedReceivablesAgedReceivablesTieOuts"] = Field(alias="tieOuts")


class AgedReceivablesAgedReceivablesBuckets(BaseModel):
  current_cents: int = Field(alias="currentCents")
  one_to_thirty_cents: int = Field(alias="oneToThirtyCents")
  thirty_one_to_sixty_cents: int = Field(alias="thirtyOneToSixtyCents")
  sixty_one_to_ninety_cents: int = Field(alias="sixtyOneToNinetyCents")
  over_ninety_cents: int = Field(alias="overNinetyCents")
  unapplied_credit_cents: int = Field(alias="unappliedCreditCents")
  total_cents: int = Field(alias="totalCents")


class AgedReceivablesAgedReceivablesAgents(BaseModel):
  agent_id: Optional[str] = Field(alias="agentId")
  agent_name: Optional[str] = Field(alias="agentName")
  open_item_count: int = Field(alias="openItemCount")
  oldest_due_date: Optional[str] = Field(alias="oldestDueDate")
  buckets: "AgedReceivablesAgedReceivablesAgentsBuckets"


class AgedReceivablesAgedReceivablesAgentsBuckets(BaseModel):
  current_cents: int = Field(alias="currentCents")
  one_to_thirty_cents: int = Field(alias="oneToThirtyCents")
  thirty_one_to_sixty_cents: int = Field(alias="thirtyOneToSixtyCents")
  sixty_one_to_ninety_cents: int = Field(alias="sixtyOneToNinetyCents")
  over_ninety_cents: int = Field(alias="overNinetyCents")
  unapplied_credit_cents: int = Field(alias="unappliedCreditCents")
  total_cents: int = Field(alias="totalCents")


class AgedReceivablesAgedReceivablesIntercompany(BaseModel):
  event_id: str = Field(alias="eventId")
  entity_id: str = Field(alias="entityId")
  agent_id: Optional[str] = Field(alias="agentId")
  occurred_on: str = Field(alias="occurredOn")
  document_number: Optional[str] = Field(alias="documentNumber")
  description: Optional[str]
  original_cents: int = Field(alias="originalCents")
  settled_cents: int = Field(alias="settledCents")
  open_cents: int = Field(alias="openCents")
  currency: str
  due_date: str = Field(alias="dueDate")
  due_date_basis: str = Field(alias="dueDateBasis")
  days_past_due: int = Field(alias="daysPastDue")
  bucket: str


class AgedReceivablesAgedReceivablesPairs(BaseModel):
  creditor_entity_id: str = Field(alias="creditorEntityId")
  debtor_entity_id: str = Field(alias="debtorEntityId")
  receivable_cents: int = Field(alias="receivableCents")
  payable_cents: int = Field(alias="payableCents")
  difference_cents: int = Field(alias="differenceCents")


class AgedReceivablesAgedReceivablesTieOuts(BaseModel):
  entity_id: str = Field(alias="entityId")
  accounts: list["AgedReceivablesAgedReceivablesTieOutsAccounts"]
  control_balance_cents: Optional[int] = Field(alias="controlBalanceCents")
  open_items_cents: int = Field(alias="openItemsCents")
  difference_cents: Optional[int] = Field(alias="differenceCents")


class AgedReceivablesAgedReceivablesTieOutsAccounts(BaseModel):
  element_id: str = Field(alias="elementId")
  code: Optional[str]
  name: str


AgedReceivables.model_rebuild()
AgedReceivablesAgedReceivables.model_rebuild()
AgedReceivablesAgedReceivablesAgents.model_rebuild()
AgedReceivablesAgedReceivablesTieOuts.model_rebuild()
