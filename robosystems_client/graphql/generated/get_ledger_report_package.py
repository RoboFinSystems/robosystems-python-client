from typing import Any, Optional

from pydantic import Field

from .base_model import BaseModel


class GetLedgerReportPackage(BaseModel):
  report_package: Optional["GetLedgerReportPackageReportPackage"] = Field(
    alias="reportPackage"
  )


class GetLedgerReportPackageReportPackage(BaseModel):
  id: str
  name: str
  description: Optional[str]
  taxonomy_id: str = Field(alias="taxonomyId")
  period_type: str = Field(alias="periodType")
  period_start: Optional[str] = Field(alias="periodStart")
  period_end: Optional[str] = Field(alias="periodEnd")
  generation_status: str = Field(alias="generationStatus")
  last_generated: Optional[str] = Field(alias="lastGenerated")
  filing_status: str = Field(alias="filingStatus")
  filed_at: Optional[str] = Field(alias="filedAt")
  filed_by: Optional[str] = Field(alias="filedBy")
  supersedes_id: Optional[str] = Field(alias="supersedesId")
  superseded_by_id: Optional[str] = Field(alias="supersededById")
  source_graph_id: Optional[str] = Field(alias="sourceGraphId")
  source_report_id: Optional[str] = Field(alias="sourceReportId")
  shared_at: Optional[str] = Field(alias="sharedAt")
  entity_name: Optional[str] = Field(alias="entityName")
  ai_generated: bool = Field(alias="aiGenerated")
  created_at: str = Field(alias="createdAt")
  created_by: str = Field(alias="createdBy")
  items: list["GetLedgerReportPackageReportPackageItems"]


class GetLedgerReportPackageReportPackageItems(BaseModel):
  fact_set_id: str = Field(alias="factSetId")
  structure_id: Optional[str] = Field(alias="structureId")
  display_order: int = Field(alias="displayOrder")
  block: "GetLedgerReportPackageReportPackageItemsBlock"


class GetLedgerReportPackageReportPackageItemsBlock(BaseModel):
  id: str
  block_type: str = Field(alias="blockType")
  name: str
  display_name: str = Field(alias="displayName")
  category: str
  taxonomy_id: Optional[str] = Field(alias="taxonomyId")
  taxonomy_name: Optional[str] = Field(alias="taxonomyName")
  information_model: "GetLedgerReportPackageReportPackageItemsBlockInformationModel" = (
    Field(alias="informationModel")
  )
  artifact: "GetLedgerReportPackageReportPackageItemsBlockArtifact"
  elements: list["GetLedgerReportPackageReportPackageItemsBlockElements"]
  connections: list["GetLedgerReportPackageReportPackageItemsBlockConnections"]
  facts: list["GetLedgerReportPackageReportPackageItemsBlockFacts"]
  rules: list["GetLedgerReportPackageReportPackageItemsBlockRules"]
  fact_set: Optional["GetLedgerReportPackageReportPackageItemsBlockFactSet"] = Field(
    alias="factSet"
  )
  verification_results: list[
    "GetLedgerReportPackageReportPackageItemsBlockVerificationResults"
  ] = Field(alias="verificationResults")
  verification_summary: Optional[
    "GetLedgerReportPackageReportPackageItemsBlockVerificationSummary"
  ] = Field(alias="verificationSummary")
  view: "GetLedgerReportPackageReportPackageItemsBlockView"


class GetLedgerReportPackageReportPackageItemsBlockInformationModel(BaseModel):
  concept_arrangement: Optional[str] = Field(alias="conceptArrangement")
  member_arrangement: Optional[str] = Field(alias="memberArrangement")


class GetLedgerReportPackageReportPackageItemsBlockArtifact(BaseModel):
  topic: Optional[str]
  renderer_note: Optional[str] = Field(alias="rendererNote")
  template: Optional[Any]
  mechanics: Any


class GetLedgerReportPackageReportPackageItemsBlockElements(BaseModel):
  id: str
  qname: Optional[str]
  name: str
  code: Optional[str]
  element_type: str = Field(alias="elementType")
  is_abstract: bool = Field(alias="isAbstract")
  is_monetary: bool = Field(alias="isMonetary")
  balance_type: Optional[str] = Field(alias="balanceType")
  period_type: Optional[str] = Field(alias="periodType")


class GetLedgerReportPackageReportPackageItemsBlockConnections(BaseModel):
  id: str
  from_element_id: str = Field(alias="fromElementId")
  to_element_id: str = Field(alias="toElementId")
  association_type: str = Field(alias="associationType")
  arcrole: Optional[str]
  order_value: Optional[float] = Field(alias="orderValue")
  weight: Optional[float]


class GetLedgerReportPackageReportPackageItemsBlockFacts(BaseModel):
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


class GetLedgerReportPackageReportPackageItemsBlockRules(BaseModel):
  id: str
  rule_category: str = Field(alias="ruleCategory")
  rule_pattern: Optional[str] = Field(alias="rulePattern")
  rule_check_kind: Optional[str] = Field(alias="ruleCheckKind")
  rule_expression: str = Field(alias="ruleExpression")
  rule_message: Optional[str] = Field(alias="ruleMessage")
  rule_severity: str = Field(alias="ruleSeverity")
  rule_origin: str = Field(alias="ruleOrigin")
  rule_target: Optional[
    "GetLedgerReportPackageReportPackageItemsBlockRulesRuleTarget"
  ] = Field(alias="ruleTarget")
  rule_variables: list[
    "GetLedgerReportPackageReportPackageItemsBlockRulesRuleVariables"
  ] = Field(alias="ruleVariables")


class GetLedgerReportPackageReportPackageItemsBlockRulesRuleTarget(BaseModel):
  target_kind: str = Field(alias="targetKind")
  target_ref_id: str = Field(alias="targetRefId")


class GetLedgerReportPackageReportPackageItemsBlockRulesRuleVariables(BaseModel):
  variable_name: str = Field(alias="variableName")
  variable_qname: Optional[str] = Field(alias="variableQname")


class GetLedgerReportPackageReportPackageItemsBlockFactSet(BaseModel):
  id: str
  structure_id: Optional[str] = Field(alias="structureId")
  period_start: Optional[str] = Field(alias="periodStart")
  period_end: str = Field(alias="periodEnd")
  factset_type: str = Field(alias="factsetType")
  entity_id: str = Field(alias="entityId")
  report_id: Optional[str] = Field(alias="reportId")
  provenance: Optional[Any]


class GetLedgerReportPackageReportPackageItemsBlockVerificationResults(BaseModel):
  id: str
  rule_id: str = Field(alias="ruleId")
  structure_id: Optional[str] = Field(alias="structureId")
  fact_set_id: Optional[str] = Field(alias="factSetId")
  status: str
  message: Optional[str]
  period_start: Optional[str] = Field(alias="periodStart")
  period_end: Optional[str] = Field(alias="periodEnd")
  evaluated_at: Optional[str] = Field(alias="evaluatedAt")


class GetLedgerReportPackageReportPackageItemsBlockVerificationSummary(BaseModel):
  total: int
  passed: int
  failed: int
  errored: int
  skipped: int
  by_category: list[
    "GetLedgerReportPackageReportPackageItemsBlockVerificationSummaryByCategory"
  ] = Field(alias="byCategory")


class GetLedgerReportPackageReportPackageItemsBlockVerificationSummaryByCategory(
  BaseModel
):
  category: str
  total: int
  passed: int
  failed: int
  errored: int
  skipped: int


class GetLedgerReportPackageReportPackageItemsBlockView(BaseModel):
  rendering: Optional["GetLedgerReportPackageReportPackageItemsBlockViewRendering"]


class GetLedgerReportPackageReportPackageItemsBlockViewRendering(BaseModel):
  rows: list["GetLedgerReportPackageReportPackageItemsBlockViewRenderingRows"]
  periods: list["GetLedgerReportPackageReportPackageItemsBlockViewRenderingPeriods"]
  validation: Optional[
    "GetLedgerReportPackageReportPackageItemsBlockViewRenderingValidation"
  ]
  unmapped_count: int = Field(alias="unmappedCount")


class GetLedgerReportPackageReportPackageItemsBlockViewRenderingRows(BaseModel):
  element_id: str = Field(alias="elementId")
  element_qname: Optional[str] = Field(alias="elementQname")
  element_name: str = Field(alias="elementName")
  classification: Optional[str]
  balance_type: Optional[str] = Field(alias="balanceType")
  values: list[Optional[float]]
  text_value: Optional[str] = Field(alias="textValue")
  is_subtotal: bool = Field(alias="isSubtotal")
  depth: int


class GetLedgerReportPackageReportPackageItemsBlockViewRenderingPeriods(BaseModel):
  start: str
  end: str
  label: Optional[str]


class GetLedgerReportPackageReportPackageItemsBlockViewRenderingValidation(BaseModel):
  passed: bool
  checks: list[str]
  failures: list[str]
  warnings: list[str]


GetLedgerReportPackage.model_rebuild()
GetLedgerReportPackageReportPackage.model_rebuild()
GetLedgerReportPackageReportPackageItems.model_rebuild()
GetLedgerReportPackageReportPackageItemsBlock.model_rebuild()
GetLedgerReportPackageReportPackageItemsBlockRules.model_rebuild()
GetLedgerReportPackageReportPackageItemsBlockVerificationSummary.model_rebuild()
GetLedgerReportPackageReportPackageItemsBlockView.model_rebuild()
GetLedgerReportPackageReportPackageItemsBlockViewRendering.model_rebuild()
