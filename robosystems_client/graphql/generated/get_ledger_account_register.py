from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class GetLedgerAccountRegister(BaseModel):
  account_register: Optional["GetLedgerAccountRegisterAccountRegister"] = Field(
    alias="accountRegister"
  )


class GetLedgerAccountRegisterAccountRegister(BaseModel):
  account: "GetLedgerAccountRegisterAccountRegisterAccount"
  entity_id: Optional[str] = Field(alias="entityId")
  start_date: Optional[str] = Field(alias="startDate")
  end_date: Optional[str] = Field(alias="endDate")
  opening_from: Optional[str] = Field(alias="openingFrom")
  opening_balance: float = Field(alias="openingBalance")
  total_debits: float = Field(alias="totalDebits")
  total_credits: float = Field(alias="totalCredits")
  closing_balance: float = Field(alias="closingBalance")
  line_count: int = Field(alias="lineCount")
  page_opening_balance: float = Field(alias="pageOpeningBalance")
  next_cursor: Optional[str] = Field(alias="nextCursor")
  sliced: bool
  drafts_truncated: bool = Field(alias="draftsTruncated")
  lines: list["GetLedgerAccountRegisterAccountRegisterLines"]
  drafts: list["GetLedgerAccountRegisterAccountRegisterDrafts"]


class GetLedgerAccountRegisterAccountRegisterAccount(BaseModel):
  id: str
  code: Optional[str]
  name: str
  balance_type: str = Field(alias="balanceType")
  trait: Optional[str]
  temporary: bool


class GetLedgerAccountRegisterAccountRegisterLines(BaseModel):
  line_id: str = Field(alias="lineId")
  entry_id: str = Field(alias="entryId")
  entry_number: Optional[str] = Field(alias="entryNumber")
  posting_date: str = Field(alias="postingDate")
  entry_type: str = Field(alias="entryType")
  provenance: Optional[str]
  status: str
  memo: Optional[str]
  description: Optional[str]
  debit: float
  credit: float
  balance: Optional[float]
  triggered_by_event_id: Optional[str] = Field(alias="triggeredByEventId")
  triggered_by_event_type: Optional[str] = Field(alias="triggeredByEventType")
  reversal_of: Optional[str] = Field(alias="reversalOf")
  reversed_by: Optional[str] = Field(alias="reversedBy")
  agent_id: Optional[str] = Field(alias="agentId")
  agent_name: Optional[str] = Field(alias="agentName")
  flow_element_id: Optional[str] = Field(alias="flowElementId")
  dimensions: list["GetLedgerAccountRegisterAccountRegisterLinesDimensions"]


class GetLedgerAccountRegisterAccountRegisterLinesDimensions(BaseModel):
  id: str
  dimension_type: str = Field(alias="dimensionType")
  name: str


class GetLedgerAccountRegisterAccountRegisterDrafts(BaseModel):
  line_id: str = Field(alias="lineId")
  entry_id: str = Field(alias="entryId")
  entry_number: Optional[str] = Field(alias="entryNumber")
  posting_date: str = Field(alias="postingDate")
  entry_type: str = Field(alias="entryType")
  provenance: Optional[str]
  status: str
  memo: Optional[str]
  description: Optional[str]
  debit: float
  credit: float
  balance: Optional[float]
  triggered_by_event_id: Optional[str] = Field(alias="triggeredByEventId")
  triggered_by_event_type: Optional[str] = Field(alias="triggeredByEventType")
  reversal_of: Optional[str] = Field(alias="reversalOf")
  reversed_by: Optional[str] = Field(alias="reversedBy")
  agent_id: Optional[str] = Field(alias="agentId")
  agent_name: Optional[str] = Field(alias="agentName")
  flow_element_id: Optional[str] = Field(alias="flowElementId")
  dimensions: list["GetLedgerAccountRegisterAccountRegisterDraftsDimensions"]


class GetLedgerAccountRegisterAccountRegisterDraftsDimensions(BaseModel):
  id: str
  dimension_type: str = Field(alias="dimensionType")
  name: str


GetLedgerAccountRegister.model_rebuild()
GetLedgerAccountRegisterAccountRegister.model_rebuild()
GetLedgerAccountRegisterAccountRegisterLines.model_rebuild()
GetLedgerAccountRegisterAccountRegisterDrafts.model_rebuild()
