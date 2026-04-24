from enum import Enum


class TaxonomyBlockRuleRequestRuleCategory(str, Enum):
  AUTOMATEDACCOUNTINGANDREPORTINGCHECKS = "AutomatedAccountingAndReportingChecks"
  DISCLOSUREMECHANICSRULE = "DisclosureMechanicsRule"
  FUNDAMENTALACCOUNTINGCONCEPTRELATION = "FundamentalAccountingConceptRelation"
  PEERCONSISTENCYRULE = "PeerConsistencyRule"
  PRIORPERIODCONSISTENCYRULE = "PriorPeriodConsistencyRule"
  REPORTINGSYSTEMSPECIFICRULE = "ReportingSystemSpecificRule"
  REPORTLEVELMODELSTRUCTURERULE = "ReportLevelModelStructureRule"
  TODOMANUALTASK = "ToDoManualTask"
  XBRLTECHNICALSYNTAXRULE = "XBRLTechnicalSyntaxRule"

  def __str__(self) -> str:
    return str(self.value)
