from typing import Any, Optional

from pydantic import Field

from .base_model import BaseModel


class ListInformationBlocks(BaseModel):
  information_blocks: list["ListInformationBlocksInformationBlocks"] = Field(
    alias="informationBlocks"
  )


class ListInformationBlocksInformationBlocks(BaseModel):
  id: str
  block_type: str = Field(alias="blockType")
  name: str
  display_name: str = Field(alias="displayName")
  category: str
  taxonomy_id: Optional[str] = Field(alias="taxonomyId")
  taxonomy_name: Optional[str] = Field(alias="taxonomyName")
  information_model: "ListInformationBlocksInformationBlocksInformationModel" = Field(
    alias="informationModel"
  )
  artifact: "ListInformationBlocksInformationBlocksArtifact"
  elements: list["ListInformationBlocksInformationBlocksElements"]
  connections: list["ListInformationBlocksInformationBlocksConnections"]
  facts: list["ListInformationBlocksInformationBlocksFacts"]
  rules: list["ListInformationBlocksInformationBlocksRules"]
  fact_set: Optional["ListInformationBlocksInformationBlocksFactSet"] = Field(
    alias="factSet"
  )
  verification_results: list[
    "ListInformationBlocksInformationBlocksVerificationResults"
  ] = Field(alias="verificationResults")
  verification_summary: Optional[
    "ListInformationBlocksInformationBlocksVerificationSummary"
  ] = Field(alias="verificationSummary")
  view: "ListInformationBlocksInformationBlocksView"


class ListInformationBlocksInformationBlocksInformationModel(BaseModel):
  concept_arrangement: Optional[str] = Field(alias="conceptArrangement")
  member_arrangement: Optional[str] = Field(alias="memberArrangement")


class ListInformationBlocksInformationBlocksArtifact(BaseModel):
  topic: Optional[str]
  renderer_note: Optional[str] = Field(alias="rendererNote")
  template: Optional[Any]
  mechanics: Any


class ListInformationBlocksInformationBlocksElements(BaseModel):
  id: str
  qname: Optional[str]
  name: str
  code: Optional[str]
  element_type: str = Field(alias="elementType")
  is_abstract: bool = Field(alias="isAbstract")
  is_monetary: bool = Field(alias="isMonetary")
  balance_type: Optional[str] = Field(alias="balanceType")
  period_type: Optional[str] = Field(alias="periodType")


class ListInformationBlocksInformationBlocksConnections(BaseModel):
  id: str
  from_element_id: str = Field(alias="fromElementId")
  to_element_id: str = Field(alias="toElementId")
  association_type: str = Field(alias="associationType")
  arcrole: Optional[str]
  order_value: Optional[float] = Field(alias="orderValue")
  weight: Optional[float]


class ListInformationBlocksInformationBlocksFacts(BaseModel):
  id: str
  element_id: str = Field(alias="elementId")
  value: Optional[float]
  text_value: Optional[str] = Field(alias="textValue")
  fact_type: str = Field(alias="factType")
  content_type: Optional[str] = Field(alias="contentType")
  period_start: Optional[str] = Field(alias="periodStart")
  period_end: str = Field(alias="periodEnd")
  period_type: str = Field(alias="periodType")
  unit: str
  fact_scope: str = Field(alias="factScope")
  fact_set_id: Optional[str] = Field(alias="factSetId")


class ListInformationBlocksInformationBlocksRules(BaseModel):
  id: str
  rule_category: str = Field(alias="ruleCategory")
  rule_pattern: Optional[str] = Field(alias="rulePattern")
  rule_check_kind: Optional[str] = Field(alias="ruleCheckKind")
  rule_expression: str = Field(alias="ruleExpression")
  rule_message: Optional[str] = Field(alias="ruleMessage")
  rule_severity: str = Field(alias="ruleSeverity")
  rule_origin: str = Field(alias="ruleOrigin")
  rule_target: Optional["ListInformationBlocksInformationBlocksRulesRuleTarget"] = (
    Field(alias="ruleTarget")
  )
  rule_variables: list["ListInformationBlocksInformationBlocksRulesRuleVariables"] = (
    Field(alias="ruleVariables")
  )


class ListInformationBlocksInformationBlocksRulesRuleTarget(BaseModel):
  target_kind: str = Field(alias="targetKind")
  target_ref_id: str = Field(alias="targetRefId")


class ListInformationBlocksInformationBlocksRulesRuleVariables(BaseModel):
  variable_name: str = Field(alias="variableName")
  variable_qname: Optional[str] = Field(alias="variableQname")


class ListInformationBlocksInformationBlocksFactSet(BaseModel):
  id: str
  structure_id: Optional[str] = Field(alias="structureId")
  period_start: Optional[str] = Field(alias="periodStart")
  period_end: str = Field(alias="periodEnd")
  factset_type: str = Field(alias="factsetType")
  entity_id: str = Field(alias="entityId")
  report_id: Optional[str] = Field(alias="reportId")
  provenance: Optional[Any]


class ListInformationBlocksInformationBlocksVerificationResults(BaseModel):
  id: str
  rule_id: str = Field(alias="ruleId")
  structure_id: Optional[str] = Field(alias="structureId")
  fact_set_id: Optional[str] = Field(alias="factSetId")
  status: str
  message: Optional[str]
  period_start: Optional[str] = Field(alias="periodStart")
  period_end: Optional[str] = Field(alias="periodEnd")
  evaluated_at: Optional[str] = Field(alias="evaluatedAt")


class ListInformationBlocksInformationBlocksVerificationSummary(BaseModel):
  total: int
  passed: int
  failed: int
  errored: int
  skipped: int
  by_category: list[
    "ListInformationBlocksInformationBlocksVerificationSummaryByCategory"
  ] = Field(alias="byCategory")


class ListInformationBlocksInformationBlocksVerificationSummaryByCategory(BaseModel):
  category: str
  total: int
  passed: int
  failed: int
  errored: int
  skipped: int


class ListInformationBlocksInformationBlocksView(BaseModel):
  rendering: Optional["ListInformationBlocksInformationBlocksViewRendering"]


class ListInformationBlocksInformationBlocksViewRendering(BaseModel):
  rows: list["ListInformationBlocksInformationBlocksViewRenderingRows"]
  periods: list["ListInformationBlocksInformationBlocksViewRenderingPeriods"]
  validation: Optional["ListInformationBlocksInformationBlocksViewRenderingValidation"]
  unmapped_count: int = Field(alias="unmappedCount")


class ListInformationBlocksInformationBlocksViewRenderingRows(BaseModel):
  element_id: str = Field(alias="elementId")
  element_qname: Optional[str] = Field(alias="elementQname")
  element_name: str = Field(alias="elementName")
  classification: Optional[str]
  balance_type: Optional[str] = Field(alias="balanceType")
  values: list[Optional[float]]
  text_value: Optional[str] = Field(alias="textValue")
  is_subtotal: bool = Field(alias="isSubtotal")
  depth: int


class ListInformationBlocksInformationBlocksViewRenderingPeriods(BaseModel):
  start: str
  end: str
  label: Optional[str]


class ListInformationBlocksInformationBlocksViewRenderingValidation(BaseModel):
  passed: bool
  checks: list[str]
  failures: list[str]
  warnings: list[str]


ListInformationBlocks.model_rebuild()
ListInformationBlocksInformationBlocks.model_rebuild()
ListInformationBlocksInformationBlocksRules.model_rebuild()
ListInformationBlocksInformationBlocksVerificationSummary.model_rebuild()
ListInformationBlocksInformationBlocksView.model_rebuild()
ListInformationBlocksInformationBlocksViewRendering.model_rebuild()
