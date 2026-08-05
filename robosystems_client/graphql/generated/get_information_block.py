from typing import Any, Optional

from pydantic import Field

from .base_model import BaseModel


class GetInformationBlock(BaseModel):
  information_block: Optional["GetInformationBlockInformationBlock"] = Field(
    alias="informationBlock"
  )


class GetInformationBlockInformationBlock(BaseModel):
  id: str
  block_type: str = Field(alias="blockType")
  name: str
  display_name: str = Field(alias="displayName")
  category: str
  taxonomy_id: Optional[str] = Field(alias="taxonomyId")
  taxonomy_name: Optional[str] = Field(alias="taxonomyName")
  information_model: "GetInformationBlockInformationBlockInformationModel" = Field(
    alias="informationModel"
  )
  artifact: "GetInformationBlockInformationBlockArtifact"
  elements: list["GetInformationBlockInformationBlockElements"]
  connections: list["GetInformationBlockInformationBlockConnections"]
  facts: list["GetInformationBlockInformationBlockFacts"]
  rules: list["GetInformationBlockInformationBlockRules"]
  fact_set: Optional["GetInformationBlockInformationBlockFactSet"] = Field(
    alias="factSet"
  )
  verification_results: list[
    "GetInformationBlockInformationBlockVerificationResults"
  ] = Field(alias="verificationResults")
  verification_summary: Optional[
    "GetInformationBlockInformationBlockVerificationSummary"
  ] = Field(alias="verificationSummary")
  view: "GetInformationBlockInformationBlockView"


class GetInformationBlockInformationBlockInformationModel(BaseModel):
  concept_arrangement: Optional[str] = Field(alias="conceptArrangement")
  member_arrangement: Optional[str] = Field(alias="memberArrangement")


class GetInformationBlockInformationBlockArtifact(BaseModel):
  topic: Optional[str]
  renderer_note: Optional[str] = Field(alias="rendererNote")
  template: Optional[Any]
  mechanics: Any


class GetInformationBlockInformationBlockElements(BaseModel):
  id: str
  qname: Optional[str]
  name: str
  code: Optional[str]
  element_type: str = Field(alias="elementType")
  is_abstract: bool = Field(alias="isAbstract")
  is_monetary: bool = Field(alias="isMonetary")
  balance_type: Optional[str] = Field(alias="balanceType")
  period_type: Optional[str] = Field(alias="periodType")


class GetInformationBlockInformationBlockConnections(BaseModel):
  id: str
  from_element_id: str = Field(alias="fromElementId")
  to_element_id: str = Field(alias="toElementId")
  association_type: str = Field(alias="associationType")
  arcrole: Optional[str]
  order_value: Optional[float] = Field(alias="orderValue")
  weight: Optional[float]


class GetInformationBlockInformationBlockFacts(BaseModel):
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


class GetInformationBlockInformationBlockRules(BaseModel):
  id: str
  rule_category: str = Field(alias="ruleCategory")
  rule_pattern: Optional[str] = Field(alias="rulePattern")
  rule_check_kind: Optional[str] = Field(alias="ruleCheckKind")
  rule_expression: str = Field(alias="ruleExpression")
  rule_message: Optional[str] = Field(alias="ruleMessage")
  rule_severity: str = Field(alias="ruleSeverity")
  rule_origin: str = Field(alias="ruleOrigin")
  rule_target: Optional["GetInformationBlockInformationBlockRulesRuleTarget"] = Field(
    alias="ruleTarget"
  )
  rule_variables: list["GetInformationBlockInformationBlockRulesRuleVariables"] = Field(
    alias="ruleVariables"
  )


class GetInformationBlockInformationBlockRulesRuleTarget(BaseModel):
  target_kind: str = Field(alias="targetKind")
  target_ref_id: str = Field(alias="targetRefId")


class GetInformationBlockInformationBlockRulesRuleVariables(BaseModel):
  variable_name: str = Field(alias="variableName")
  variable_qname: Optional[str] = Field(alias="variableQname")


class GetInformationBlockInformationBlockFactSet(BaseModel):
  id: str
  structure_id: Optional[str] = Field(alias="structureId")
  period_start: Optional[str] = Field(alias="periodStart")
  period_end: str = Field(alias="periodEnd")
  factset_type: str = Field(alias="factsetType")
  entity_id: str = Field(alias="entityId")
  report_id: Optional[str] = Field(alias="reportId")
  provenance: Optional[Any]


class GetInformationBlockInformationBlockVerificationResults(BaseModel):
  id: str
  rule_id: str = Field(alias="ruleId")
  structure_id: Optional[str] = Field(alias="structureId")
  fact_set_id: Optional[str] = Field(alias="factSetId")
  status: str
  message: Optional[str]
  period_start: Optional[str] = Field(alias="periodStart")
  period_end: Optional[str] = Field(alias="periodEnd")
  evaluated_at: Optional[str] = Field(alias="evaluatedAt")


class GetInformationBlockInformationBlockVerificationSummary(BaseModel):
  total: int
  passed: int
  failed: int
  errored: int
  skipped: int
  by_category: list[
    "GetInformationBlockInformationBlockVerificationSummaryByCategory"
  ] = Field(alias="byCategory")


class GetInformationBlockInformationBlockVerificationSummaryByCategory(BaseModel):
  category: str
  total: int
  passed: int
  failed: int
  errored: int
  skipped: int


class GetInformationBlockInformationBlockView(BaseModel):
  rendering: Optional["GetInformationBlockInformationBlockViewRendering"]


class GetInformationBlockInformationBlockViewRendering(BaseModel):
  rows: list["GetInformationBlockInformationBlockViewRenderingRows"]
  periods: list["GetInformationBlockInformationBlockViewRenderingPeriods"]
  validation: Optional["GetInformationBlockInformationBlockViewRenderingValidation"]
  unmapped_count: int = Field(alias="unmappedCount")


class GetInformationBlockInformationBlockViewRenderingRows(BaseModel):
  element_id: str = Field(alias="elementId")
  element_qname: Optional[str] = Field(alias="elementQname")
  element_name: str = Field(alias="elementName")
  classification: Optional[str]
  balance_type: Optional[str] = Field(alias="balanceType")
  values: list[Optional[float]]
  text_value: Optional[str] = Field(alias="textValue")
  is_subtotal: bool = Field(alias="isSubtotal")
  depth: int


class GetInformationBlockInformationBlockViewRenderingPeriods(BaseModel):
  start: str
  end: str
  label: Optional[str]


class GetInformationBlockInformationBlockViewRenderingValidation(BaseModel):
  passed: bool
  checks: list[str]
  failures: list[str]
  warnings: list[str]


GetInformationBlock.model_rebuild()
GetInformationBlockInformationBlock.model_rebuild()
GetInformationBlockInformationBlockRules.model_rebuild()
GetInformationBlockInformationBlockVerificationSummary.model_rebuild()
GetInformationBlockInformationBlockView.model_rebuild()
GetInformationBlockInformationBlockViewRendering.model_rebuild()
