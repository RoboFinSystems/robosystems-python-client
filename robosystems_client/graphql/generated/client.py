from typing import Any, Optional, Union

from .base_client import BaseClient
from .base_model import UNSET, UnsetType
from .enums import ReportDownloadFormat
from .get_information_block import GetInformationBlock
from .get_investor_holdings import GetInvestorHoldings
from .get_investor_portfolio_block import GetInvestorPortfolioBlock
from .get_investor_position import GetInvestorPosition
from .get_investor_security import GetInvestorSecurity
from .get_ledger_account_rollups import GetLedgerAccountRollups
from .get_ledger_account_tree import GetLedgerAccountTree
from .get_ledger_agent import GetLedgerAgent
from .get_ledger_closing_book_structures import GetLedgerClosingBookStructures
from .get_ledger_entity import GetLedgerEntity
from .get_ledger_event_block import GetLedgerEventBlock
from .get_ledger_fiscal_calendar import GetLedgerFiscalCalendar
from .get_ledger_mapped_trial_balance import GetLedgerMappedTrialBalance
from .get_ledger_mapping import GetLedgerMapping
from .get_ledger_mapping_coverage import GetLedgerMappingCoverage
from .get_ledger_period_close_status import GetLedgerPeriodCloseStatus
from .get_ledger_period_drafts import GetLedgerPeriodDrafts
from .get_ledger_publish_list import GetLedgerPublishList
from .get_ledger_report import GetLedgerReport
from .get_ledger_report_download_url import GetLedgerReportDownloadUrl
from .get_ledger_report_package import GetLedgerReportPackage
from .get_ledger_reporting_taxonomy import GetLedgerReportingTaxonomy
from .get_ledger_statement import GetLedgerStatement
from .get_ledger_summary import GetLedgerSummary
from .get_ledger_transaction import GetLedgerTransaction
from .get_ledger_trial_balance import GetLedgerTrialBalance
from .get_library_element import GetLibraryElement
from .get_library_element_arcs import GetLibraryElementArcs
from .get_library_element_classifications import GetLibraryElementClassifications
from .get_library_element_equivalents import GetLibraryElementEquivalents
from .get_library_taxonomy import GetLibraryTaxonomy
from .list_information_blocks import ListInformationBlocks
from .list_investor_portfolios import ListInvestorPortfolios
from .list_investor_positions import ListInvestorPositions
from .list_investor_securities import ListInvestorSecurities
from .list_ledger_accounts import ListLedgerAccounts
from .list_ledger_agents import ListLedgerAgents
from .list_ledger_elements import ListLedgerElements
from .list_ledger_entities import ListLedgerEntities
from .list_ledger_event_blocks import ListLedgerEventBlocks
from .list_ledger_mappings import ListLedgerMappings
from .list_ledger_publish_lists import ListLedgerPublishLists
from .list_ledger_reports import ListLedgerReports
from .list_ledger_structures import ListLedgerStructures
from .list_ledger_taxonomies import ListLedgerTaxonomies
from .list_ledger_transactions import ListLedgerTransactions
from .list_ledger_unmapped_elements import ListLedgerUnmappedElements
from .list_library_elements import ListLibraryElements
from .list_library_structures import ListLibraryStructures
from .list_library_taxonomies import ListLibraryTaxonomies
from .list_library_taxonomy_arcs import ListLibraryTaxonomyArcs
from .mapping_candidates import MappingCandidates
from .operations import (
  GET_INFORMATION_BLOCK_GQL,
  GET_INVESTOR_HOLDINGS_GQL,
  GET_INVESTOR_PORTFOLIO_BLOCK_GQL,
  GET_INVESTOR_POSITION_GQL,
  GET_INVESTOR_SECURITY_GQL,
  GET_LEDGER_ACCOUNT_ROLLUPS_GQL,
  GET_LEDGER_ACCOUNT_TREE_GQL,
  GET_LEDGER_AGENT_GQL,
  GET_LEDGER_CLOSING_BOOK_STRUCTURES_GQL,
  GET_LEDGER_ENTITY_GQL,
  GET_LEDGER_EVENT_BLOCK_GQL,
  GET_LEDGER_FISCAL_CALENDAR_GQL,
  GET_LEDGER_MAPPED_TRIAL_BALANCE_GQL,
  GET_LEDGER_MAPPING_COVERAGE_GQL,
  GET_LEDGER_MAPPING_GQL,
  GET_LEDGER_PERIOD_CLOSE_STATUS_GQL,
  GET_LEDGER_PERIOD_DRAFTS_GQL,
  GET_LEDGER_PUBLISH_LIST_GQL,
  GET_LEDGER_REPORT_DOWNLOAD_URL_GQL,
  GET_LEDGER_REPORT_GQL,
  GET_LEDGER_REPORT_PACKAGE_GQL,
  GET_LEDGER_REPORTING_TAXONOMY_GQL,
  GET_LEDGER_STATEMENT_GQL,
  GET_LEDGER_SUMMARY_GQL,
  GET_LEDGER_TRANSACTION_GQL,
  GET_LEDGER_TRIAL_BALANCE_GQL,
  GET_LIBRARY_ELEMENT_ARCS_GQL,
  GET_LIBRARY_ELEMENT_CLASSIFICATIONS_GQL,
  GET_LIBRARY_ELEMENT_EQUIVALENTS_GQL,
  GET_LIBRARY_ELEMENT_GQL,
  GET_LIBRARY_TAXONOMY_GQL,
  LIST_INFORMATION_BLOCKS_GQL,
  LIST_INVESTOR_PORTFOLIOS_GQL,
  LIST_INVESTOR_POSITIONS_GQL,
  LIST_INVESTOR_SECURITIES_GQL,
  LIST_LEDGER_ACCOUNTS_GQL,
  LIST_LEDGER_AGENTS_GQL,
  LIST_LEDGER_ELEMENTS_GQL,
  LIST_LEDGER_ENTITIES_GQL,
  LIST_LEDGER_EVENT_BLOCKS_GQL,
  LIST_LEDGER_MAPPINGS_GQL,
  LIST_LEDGER_PUBLISH_LISTS_GQL,
  LIST_LEDGER_REPORTS_GQL,
  LIST_LEDGER_STRUCTURES_GQL,
  LIST_LEDGER_TAXONOMIES_GQL,
  LIST_LEDGER_TRANSACTIONS_GQL,
  LIST_LEDGER_UNMAPPED_ELEMENTS_GQL,
  LIST_LIBRARY_ELEMENTS_GQL,
  LIST_LIBRARY_STRUCTURES_GQL,
  LIST_LIBRARY_TAXONOMIES_GQL,
  LIST_LIBRARY_TAXONOMY_ARCS_GQL,
  MAPPING_CANDIDATES_GQL,
  SEARCH_LIBRARY_ELEMENTS_GQL,
)
from .search_library_elements import SearchLibraryElements


def gql(q: str) -> str:
  return q


class Client(BaseClient):
  def get_investor_holdings(
    self, portfolio_id: str, **kwargs: Any
  ) -> GetInvestorHoldings:
    variables: dict[str, object] = {"portfolioId": portfolio_id}
    response = self.execute(
      query=GET_INVESTOR_HOLDINGS_GQL,
      operation_name="GetInvestorHoldings",
      variables=variables,
      **kwargs,
    )
    data = self.get_data(response)
    return GetInvestorHoldings.model_validate(data)

  def get_investor_portfolio_block(
    self, portfolio_id: str, **kwargs: Any
  ) -> GetInvestorPortfolioBlock:
    variables: dict[str, object] = {"portfolioId": portfolio_id}
    response = self.execute(
      query=GET_INVESTOR_PORTFOLIO_BLOCK_GQL,
      operation_name="GetInvestorPortfolioBlock",
      variables=variables,
      **kwargs,
    )
    data = self.get_data(response)
    return GetInvestorPortfolioBlock.model_validate(data)

  def get_investor_position(
    self, position_id: str, **kwargs: Any
  ) -> GetInvestorPosition:
    variables: dict[str, object] = {"positionId": position_id}
    response = self.execute(
      query=GET_INVESTOR_POSITION_GQL,
      operation_name="GetInvestorPosition",
      variables=variables,
      **kwargs,
    )
    data = self.get_data(response)
    return GetInvestorPosition.model_validate(data)

  def get_investor_security(
    self, security_id: str, **kwargs: Any
  ) -> GetInvestorSecurity:
    variables: dict[str, object] = {"securityId": security_id}
    response = self.execute(
      query=GET_INVESTOR_SECURITY_GQL,
      operation_name="GetInvestorSecurity",
      variables=variables,
      **kwargs,
    )
    data = self.get_data(response)
    return GetInvestorSecurity.model_validate(data)

  def list_investor_portfolios(
    self, limit: int, offset: int, **kwargs: Any
  ) -> ListInvestorPortfolios:
    variables: dict[str, object] = {"limit": limit, "offset": offset}
    response = self.execute(
      query=LIST_INVESTOR_PORTFOLIOS_GQL,
      operation_name="ListInvestorPortfolios",
      variables=variables,
      **kwargs,
    )
    data = self.get_data(response)
    return ListInvestorPortfolios.model_validate(data)

  def list_investor_positions(
    self,
    limit: int,
    offset: int,
    portfolio_id: Union[Optional[str], UnsetType] = UNSET,
    security_id: Union[Optional[str], UnsetType] = UNSET,
    status: Union[Optional[str], UnsetType] = UNSET,
    **kwargs: Any,
  ) -> ListInvestorPositions:
    variables: dict[str, object] = {
      "portfolioId": portfolio_id,
      "securityId": security_id,
      "status": status,
      "limit": limit,
      "offset": offset,
    }
    response = self.execute(
      query=LIST_INVESTOR_POSITIONS_GQL,
      operation_name="ListInvestorPositions",
      variables=variables,
      **kwargs,
    )
    data = self.get_data(response)
    return ListInvestorPositions.model_validate(data)

  def list_investor_securities(
    self,
    limit: int,
    offset: int,
    entity_id: Union[Optional[str], UnsetType] = UNSET,
    security_type: Union[Optional[str], UnsetType] = UNSET,
    is_active: Union[Optional[bool], UnsetType] = UNSET,
    **kwargs: Any,
  ) -> ListInvestorSecurities:
    variables: dict[str, object] = {
      "entityId": entity_id,
      "securityType": security_type,
      "isActive": is_active,
      "limit": limit,
      "offset": offset,
    }
    response = self.execute(
      query=LIST_INVESTOR_SECURITIES_GQL,
      operation_name="ListInvestorSecurities",
      variables=variables,
      **kwargs,
    )
    data = self.get_data(response)
    return ListInvestorSecurities.model_validate(data)

  def get_information_block(
    self,
    id: str,
    series: bool,
    scenario_id: Union[Optional[str], UnsetType] = UNSET,
    series_history: Union[Optional[int], UnsetType] = UNSET,
    series_forecast: Union[Optional[int], UnsetType] = UNSET,
    **kwargs: Any,
  ) -> GetInformationBlock:
    variables: dict[str, object] = {
      "id": id,
      "scenarioId": scenario_id,
      "series": series,
      "seriesHistory": series_history,
      "seriesForecast": series_forecast,
    }
    response = self.execute(
      query=GET_INFORMATION_BLOCK_GQL,
      operation_name="GetInformationBlock",
      variables=variables,
      **kwargs,
    )
    data = self.get_data(response)
    return GetInformationBlock.model_validate(data)

  def get_ledger_account_rollups(
    self,
    mapping_id: Union[Optional[str], UnsetType] = UNSET,
    start_date: Union[Optional[str], UnsetType] = UNSET,
    end_date: Union[Optional[str], UnsetType] = UNSET,
    **kwargs: Any,
  ) -> GetLedgerAccountRollups:
    variables: dict[str, object] = {
      "mappingId": mapping_id,
      "startDate": start_date,
      "endDate": end_date,
    }
    response = self.execute(
      query=GET_LEDGER_ACCOUNT_ROLLUPS_GQL,
      operation_name="GetLedgerAccountRollups",
      variables=variables,
      **kwargs,
    )
    data = self.get_data(response)
    return GetLedgerAccountRollups.model_validate(data)

  def get_ledger_account_tree(self, **kwargs: Any) -> GetLedgerAccountTree:
    variables: dict[str, object] = {}
    response = self.execute(
      query=GET_LEDGER_ACCOUNT_TREE_GQL,
      operation_name="GetLedgerAccountTree",
      variables=variables,
      **kwargs,
    )
    data = self.get_data(response)
    return GetLedgerAccountTree.model_validate(data)

  def get_ledger_agent(self, id: str, **kwargs: Any) -> GetLedgerAgent:
    variables: dict[str, object] = {"id": id}
    response = self.execute(
      query=GET_LEDGER_AGENT_GQL,
      operation_name="GetLedgerAgent",
      variables=variables,
      **kwargs,
    )
    data = self.get_data(response)
    return GetLedgerAgent.model_validate(data)

  def get_ledger_closing_book_structures(
    self, **kwargs: Any
  ) -> GetLedgerClosingBookStructures:
    variables: dict[str, object] = {}
    response = self.execute(
      query=GET_LEDGER_CLOSING_BOOK_STRUCTURES_GQL,
      operation_name="GetLedgerClosingBookStructures",
      variables=variables,
      **kwargs,
    )
    data = self.get_data(response)
    return GetLedgerClosingBookStructures.model_validate(data)

  def get_ledger_entity(self, **kwargs: Any) -> GetLedgerEntity:
    variables: dict[str, object] = {}
    response = self.execute(
      query=GET_LEDGER_ENTITY_GQL,
      operation_name="GetLedgerEntity",
      variables=variables,
      **kwargs,
    )
    data = self.get_data(response)
    return GetLedgerEntity.model_validate(data)

  def get_ledger_event_block(self, id: str, **kwargs: Any) -> GetLedgerEventBlock:
    variables: dict[str, object] = {"id": id}
    response = self.execute(
      query=GET_LEDGER_EVENT_BLOCK_GQL,
      operation_name="GetLedgerEventBlock",
      variables=variables,
      **kwargs,
    )
    data = self.get_data(response)
    return GetLedgerEventBlock.model_validate(data)

  def get_ledger_fiscal_calendar(self, **kwargs: Any) -> GetLedgerFiscalCalendar:
    variables: dict[str, object] = {}
    response = self.execute(
      query=GET_LEDGER_FISCAL_CALENDAR_GQL,
      operation_name="GetLedgerFiscalCalendar",
      variables=variables,
      **kwargs,
    )
    data = self.get_data(response)
    return GetLedgerFiscalCalendar.model_validate(data)

  def get_ledger_mapped_trial_balance(
    self,
    mapping_id: str,
    start_date: Union[Optional[str], UnsetType] = UNSET,
    end_date: Union[Optional[str], UnsetType] = UNSET,
    **kwargs: Any,
  ) -> GetLedgerMappedTrialBalance:
    variables: dict[str, object] = {
      "mappingId": mapping_id,
      "startDate": start_date,
      "endDate": end_date,
    }
    response = self.execute(
      query=GET_LEDGER_MAPPED_TRIAL_BALANCE_GQL,
      operation_name="GetLedgerMappedTrialBalance",
      variables=variables,
      **kwargs,
    )
    data = self.get_data(response)
    return GetLedgerMappedTrialBalance.model_validate(data)

  def get_ledger_mapping(self, mapping_id: str, **kwargs: Any) -> GetLedgerMapping:
    variables: dict[str, object] = {"mappingId": mapping_id}
    response = self.execute(
      query=GET_LEDGER_MAPPING_GQL,
      operation_name="GetLedgerMapping",
      variables=variables,
      **kwargs,
    )
    data = self.get_data(response)
    return GetLedgerMapping.model_validate(data)

  def get_ledger_mapping_coverage(
    self, mapping_id: str, **kwargs: Any
  ) -> GetLedgerMappingCoverage:
    variables: dict[str, object] = {"mappingId": mapping_id}
    response = self.execute(
      query=GET_LEDGER_MAPPING_COVERAGE_GQL,
      operation_name="GetLedgerMappingCoverage",
      variables=variables,
      **kwargs,
    )
    data = self.get_data(response)
    return GetLedgerMappingCoverage.model_validate(data)

  def get_ledger_period_close_status(
    self, period_start: str, period_end: str, **kwargs: Any
  ) -> GetLedgerPeriodCloseStatus:
    variables: dict[str, object] = {
      "periodStart": period_start,
      "periodEnd": period_end,
    }
    response = self.execute(
      query=GET_LEDGER_PERIOD_CLOSE_STATUS_GQL,
      operation_name="GetLedgerPeriodCloseStatus",
      variables=variables,
      **kwargs,
    )
    data = self.get_data(response)
    return GetLedgerPeriodCloseStatus.model_validate(data)

  def get_ledger_period_drafts(
    self, period: str, **kwargs: Any
  ) -> GetLedgerPeriodDrafts:
    variables: dict[str, object] = {"period": period}
    response = self.execute(
      query=GET_LEDGER_PERIOD_DRAFTS_GQL,
      operation_name="GetLedgerPeriodDrafts",
      variables=variables,
      **kwargs,
    )
    data = self.get_data(response)
    return GetLedgerPeriodDrafts.model_validate(data)

  def get_ledger_publish_list(
    self, list_id: str, **kwargs: Any
  ) -> GetLedgerPublishList:
    variables: dict[str, object] = {"listId": list_id}
    response = self.execute(
      query=GET_LEDGER_PUBLISH_LIST_GQL,
      operation_name="GetLedgerPublishList",
      variables=variables,
      **kwargs,
    )
    data = self.get_data(response)
    return GetLedgerPublishList.model_validate(data)

  def get_ledger_report(self, report_id: str, **kwargs: Any) -> GetLedgerReport:
    variables: dict[str, object] = {"reportId": report_id}
    response = self.execute(
      query=GET_LEDGER_REPORT_GQL,
      operation_name="GetLedgerReport",
      variables=variables,
      **kwargs,
    )
    data = self.get_data(response)
    return GetLedgerReport.model_validate(data)

  def get_ledger_report_download_url(
    self,
    report_id: str,
    format: Union[Optional[ReportDownloadFormat], UnsetType] = UNSET,
    expires_in: Union[Optional[int], UnsetType] = UNSET,
    **kwargs: Any,
  ) -> GetLedgerReportDownloadUrl:
    variables: dict[str, object] = {
      "reportId": report_id,
      "format": format,
      "expiresIn": expires_in,
    }
    response = self.execute(
      query=GET_LEDGER_REPORT_DOWNLOAD_URL_GQL,
      operation_name="GetLedgerReportDownloadUrl",
      variables=variables,
      **kwargs,
    )
    data = self.get_data(response)
    return GetLedgerReportDownloadUrl.model_validate(data)

  def get_ledger_report_package(
    self, report_id: str, **kwargs: Any
  ) -> GetLedgerReportPackage:
    variables: dict[str, object] = {"reportId": report_id}
    response = self.execute(
      query=GET_LEDGER_REPORT_PACKAGE_GQL,
      operation_name="GetLedgerReportPackage",
      variables=variables,
      **kwargs,
    )
    data = self.get_data(response)
    return GetLedgerReportPackage.model_validate(data)

  def get_ledger_reporting_taxonomy(self, **kwargs: Any) -> GetLedgerReportingTaxonomy:
    variables: dict[str, object] = {}
    response = self.execute(
      query=GET_LEDGER_REPORTING_TAXONOMY_GQL,
      operation_name="GetLedgerReportingTaxonomy",
      variables=variables,
      **kwargs,
    )
    data = self.get_data(response)
    return GetLedgerReportingTaxonomy.model_validate(data)

  def get_ledger_statement(
    self, report_id: str, block_type: str, **kwargs: Any
  ) -> GetLedgerStatement:
    variables: dict[str, object] = {"reportId": report_id, "blockType": block_type}
    response = self.execute(
      query=GET_LEDGER_STATEMENT_GQL,
      operation_name="GetLedgerStatement",
      variables=variables,
      **kwargs,
    )
    data = self.get_data(response)
    return GetLedgerStatement.model_validate(data)

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

  def get_ledger_transaction(
    self, transaction_id: str, **kwargs: Any
  ) -> GetLedgerTransaction:
    variables: dict[str, object] = {"transactionId": transaction_id}
    response = self.execute(
      query=GET_LEDGER_TRANSACTION_GQL,
      operation_name="GetLedgerTransaction",
      variables=variables,
      **kwargs,
    )
    data = self.get_data(response)
    return GetLedgerTransaction.model_validate(data)

  def get_ledger_trial_balance(
    self,
    start_date: Union[Optional[str], UnsetType] = UNSET,
    end_date: Union[Optional[str], UnsetType] = UNSET,
    **kwargs: Any,
  ) -> GetLedgerTrialBalance:
    variables: dict[str, object] = {"startDate": start_date, "endDate": end_date}
    response = self.execute(
      query=GET_LEDGER_TRIAL_BALANCE_GQL,
      operation_name="GetLedgerTrialBalance",
      variables=variables,
      **kwargs,
    )
    data = self.get_data(response)
    return GetLedgerTrialBalance.model_validate(data)

  def list_information_blocks(
    self,
    block_type: Union[Optional[str], UnsetType] = UNSET,
    category: Union[Optional[str], UnsetType] = UNSET,
    limit: Union[Optional[int], UnsetType] = UNSET,
    offset: Union[Optional[int], UnsetType] = UNSET,
    **kwargs: Any,
  ) -> ListInformationBlocks:
    variables: dict[str, object] = {
      "blockType": block_type,
      "category": category,
      "limit": limit,
      "offset": offset,
    }
    response = self.execute(
      query=LIST_INFORMATION_BLOCKS_GQL,
      operation_name="ListInformationBlocks",
      variables=variables,
      **kwargs,
    )
    data = self.get_data(response)
    return ListInformationBlocks.model_validate(data)

  def list_ledger_accounts(
    self,
    limit: int,
    offset: int,
    classification: Union[Optional[str], UnsetType] = UNSET,
    is_active: Union[Optional[bool], UnsetType] = UNSET,
    **kwargs: Any,
  ) -> ListLedgerAccounts:
    variables: dict[str, object] = {
      "classification": classification,
      "isActive": is_active,
      "limit": limit,
      "offset": offset,
    }
    response = self.execute(
      query=LIST_LEDGER_ACCOUNTS_GQL,
      operation_name="ListLedgerAccounts",
      variables=variables,
      **kwargs,
    )
    data = self.get_data(response)
    return ListLedgerAccounts.model_validate(data)

  def list_ledger_agents(
    self,
    limit: int,
    offset: int,
    agent_type: Union[Optional[str], UnsetType] = UNSET,
    source: Union[Optional[str], UnsetType] = UNSET,
    is_active: Union[Optional[bool], UnsetType] = UNSET,
    **kwargs: Any,
  ) -> ListLedgerAgents:
    variables: dict[str, object] = {
      "agentType": agent_type,
      "source": source,
      "isActive": is_active,
      "limit": limit,
      "offset": offset,
    }
    response = self.execute(
      query=LIST_LEDGER_AGENTS_GQL,
      operation_name="ListLedgerAgents",
      variables=variables,
      **kwargs,
    )
    data = self.get_data(response)
    return ListLedgerAgents.model_validate(data)

  def list_ledger_elements(
    self,
    limit: int,
    offset: int,
    taxonomy_id: Union[Optional[str], UnsetType] = UNSET,
    source: Union[Optional[str], UnsetType] = UNSET,
    classification: Union[Optional[str], UnsetType] = UNSET,
    is_abstract: Union[Optional[bool], UnsetType] = UNSET,
    **kwargs: Any,
  ) -> ListLedgerElements:
    variables: dict[str, object] = {
      "taxonomyId": taxonomy_id,
      "source": source,
      "classification": classification,
      "isAbstract": is_abstract,
      "limit": limit,
      "offset": offset,
    }
    response = self.execute(
      query=LIST_LEDGER_ELEMENTS_GQL,
      operation_name="ListLedgerElements",
      variables=variables,
      **kwargs,
    )
    data = self.get_data(response)
    return ListLedgerElements.model_validate(data)

  def list_ledger_entities(
    self, source: Union[Optional[str], UnsetType] = UNSET, **kwargs: Any
  ) -> ListLedgerEntities:
    variables: dict[str, object] = {"source": source}
    response = self.execute(
      query=LIST_LEDGER_ENTITIES_GQL,
      operation_name="ListLedgerEntities",
      variables=variables,
      **kwargs,
    )
    data = self.get_data(response)
    return ListLedgerEntities.model_validate(data)

  def list_ledger_event_blocks(
    self,
    limit: int,
    offset: int,
    event_type: Union[Optional[str], UnsetType] = UNSET,
    event_category: Union[Optional[str], UnsetType] = UNSET,
    status: Union[Optional[str], UnsetType] = UNSET,
    agent_id: Union[Optional[str], UnsetType] = UNSET,
    source: Union[Optional[str], UnsetType] = UNSET,
    **kwargs: Any,
  ) -> ListLedgerEventBlocks:
    variables: dict[str, object] = {
      "eventType": event_type,
      "eventCategory": event_category,
      "status": status,
      "agentId": agent_id,
      "source": source,
      "limit": limit,
      "offset": offset,
    }
    response = self.execute(
      query=LIST_LEDGER_EVENT_BLOCKS_GQL,
      operation_name="ListLedgerEventBlocks",
      variables=variables,
      **kwargs,
    )
    data = self.get_data(response)
    return ListLedgerEventBlocks.model_validate(data)

  def list_ledger_mappings(self, **kwargs: Any) -> ListLedgerMappings:
    variables: dict[str, object] = {}
    response = self.execute(
      query=LIST_LEDGER_MAPPINGS_GQL,
      operation_name="ListLedgerMappings",
      variables=variables,
      **kwargs,
    )
    data = self.get_data(response)
    return ListLedgerMappings.model_validate(data)

  def list_ledger_publish_lists(
    self, limit: int, offset: int, **kwargs: Any
  ) -> ListLedgerPublishLists:
    variables: dict[str, object] = {"limit": limit, "offset": offset}
    response = self.execute(
      query=LIST_LEDGER_PUBLISH_LISTS_GQL,
      operation_name="ListLedgerPublishLists",
      variables=variables,
      **kwargs,
    )
    data = self.get_data(response)
    return ListLedgerPublishLists.model_validate(data)

  def list_ledger_reports(self, **kwargs: Any) -> ListLedgerReports:
    variables: dict[str, object] = {}
    response = self.execute(
      query=LIST_LEDGER_REPORTS_GQL,
      operation_name="ListLedgerReports",
      variables=variables,
      **kwargs,
    )
    data = self.get_data(response)
    return ListLedgerReports.model_validate(data)

  def list_ledger_structures(
    self,
    taxonomy_id: Union[Optional[str], UnsetType] = UNSET,
    block_type: Union[Optional[str], UnsetType] = UNSET,
    **kwargs: Any,
  ) -> ListLedgerStructures:
    variables: dict[str, object] = {
      "taxonomyId": taxonomy_id,
      "blockType": block_type,
    }
    response = self.execute(
      query=LIST_LEDGER_STRUCTURES_GQL,
      operation_name="ListLedgerStructures",
      variables=variables,
      **kwargs,
    )
    data = self.get_data(response)
    return ListLedgerStructures.model_validate(data)

  def list_ledger_taxonomies(
    self, taxonomy_type: Union[Optional[str], UnsetType] = UNSET, **kwargs: Any
  ) -> ListLedgerTaxonomies:
    variables: dict[str, object] = {"taxonomyType": taxonomy_type}
    response = self.execute(
      query=LIST_LEDGER_TAXONOMIES_GQL,
      operation_name="ListLedgerTaxonomies",
      variables=variables,
      **kwargs,
    )
    data = self.get_data(response)
    return ListLedgerTaxonomies.model_validate(data)

  def list_ledger_transactions(
    self,
    limit: int,
    offset: int,
    type_: Union[Optional[str], UnsetType] = UNSET,
    start_date: Union[Optional[str], UnsetType] = UNSET,
    end_date: Union[Optional[str], UnsetType] = UNSET,
    **kwargs: Any,
  ) -> ListLedgerTransactions:
    variables: dict[str, object] = {
      "type": type_,
      "startDate": start_date,
      "endDate": end_date,
      "limit": limit,
      "offset": offset,
    }
    response = self.execute(
      query=LIST_LEDGER_TRANSACTIONS_GQL,
      operation_name="ListLedgerTransactions",
      variables=variables,
      **kwargs,
    )
    data = self.get_data(response)
    return ListLedgerTransactions.model_validate(data)

  def list_ledger_unmapped_elements(
    self, mapping_id: Union[Optional[str], UnsetType] = UNSET, **kwargs: Any
  ) -> ListLedgerUnmappedElements:
    variables: dict[str, object] = {"mappingId": mapping_id}
    response = self.execute(
      query=LIST_LEDGER_UNMAPPED_ELEMENTS_GQL,
      operation_name="ListLedgerUnmappedElements",
      variables=variables,
      **kwargs,
    )
    data = self.get_data(response)
    return ListLedgerUnmappedElements.model_validate(data)

  def mapping_candidates(self, classification: str, **kwargs: Any) -> MappingCandidates:
    variables: dict[str, object] = {"classification": classification}
    response = self.execute(
      query=MAPPING_CANDIDATES_GQL,
      operation_name="MappingCandidates",
      variables=variables,
      **kwargs,
    )
    data = self.get_data(response)
    return MappingCandidates.model_validate(data)

  def get_library_element(
    self,
    id: Union[Optional[str], UnsetType] = UNSET,
    qname: Union[Optional[str], UnsetType] = UNSET,
    **kwargs: Any,
  ) -> GetLibraryElement:
    variables: dict[str, object] = {"id": id, "qname": qname}
    response = self.execute(
      query=GET_LIBRARY_ELEMENT_GQL,
      operation_name="GetLibraryElement",
      variables=variables,
      **kwargs,
    )
    data = self.get_data(response)
    return GetLibraryElement.model_validate(data)

  def get_library_element_arcs(self, id: str, **kwargs: Any) -> GetLibraryElementArcs:
    variables: dict[str, object] = {"id": id}
    response = self.execute(
      query=GET_LIBRARY_ELEMENT_ARCS_GQL,
      operation_name="GetLibraryElementArcs",
      variables=variables,
      **kwargs,
    )
    data = self.get_data(response)
    return GetLibraryElementArcs.model_validate(data)

  def get_library_element_classifications(
    self, id: str, **kwargs: Any
  ) -> GetLibraryElementClassifications:
    variables: dict[str, object] = {"id": id}
    response = self.execute(
      query=GET_LIBRARY_ELEMENT_CLASSIFICATIONS_GQL,
      operation_name="GetLibraryElementClassifications",
      variables=variables,
      **kwargs,
    )
    data = self.get_data(response)
    return GetLibraryElementClassifications.model_validate(data)

  def get_library_element_equivalents(
    self, id: str, **kwargs: Any
  ) -> GetLibraryElementEquivalents:
    variables: dict[str, object] = {"id": id}
    response = self.execute(
      query=GET_LIBRARY_ELEMENT_EQUIVALENTS_GQL,
      operation_name="GetLibraryElementEquivalents",
      variables=variables,
      **kwargs,
    )
    data = self.get_data(response)
    return GetLibraryElementEquivalents.model_validate(data)

  def get_library_taxonomy(
    self,
    include_element_count: bool,
    id: Union[Optional[str], UnsetType] = UNSET,
    standard: Union[Optional[str], UnsetType] = UNSET,
    version: Union[Optional[str], UnsetType] = UNSET,
    **kwargs: Any,
  ) -> GetLibraryTaxonomy:
    variables: dict[str, object] = {
      "id": id,
      "standard": standard,
      "version": version,
      "includeElementCount": include_element_count,
    }
    response = self.execute(
      query=GET_LIBRARY_TAXONOMY_GQL,
      operation_name="GetLibraryTaxonomy",
      variables=variables,
      **kwargs,
    )
    data = self.get_data(response)
    return GetLibraryTaxonomy.model_validate(data)

  def list_library_elements(
    self,
    limit: int,
    offset: int,
    include_labels: bool,
    include_references: bool,
    taxonomy_id: Union[Optional[str], UnsetType] = UNSET,
    source: Union[Optional[str], UnsetType] = UNSET,
    classification: Union[Optional[str], UnsetType] = UNSET,
    activity_type: Union[Optional[str], UnsetType] = UNSET,
    element_type: Union[Optional[str], UnsetType] = UNSET,
    is_abstract: Union[Optional[bool], UnsetType] = UNSET,
    **kwargs: Any,
  ) -> ListLibraryElements:
    variables: dict[str, object] = {
      "taxonomyId": taxonomy_id,
      "source": source,
      "classification": classification,
      "activityType": activity_type,
      "elementType": element_type,
      "isAbstract": is_abstract,
      "limit": limit,
      "offset": offset,
      "includeLabels": include_labels,
      "includeReferences": include_references,
    }
    response = self.execute(
      query=LIST_LIBRARY_ELEMENTS_GQL,
      operation_name="ListLibraryElements",
      variables=variables,
      **kwargs,
    )
    data = self.get_data(response)
    return ListLibraryElements.model_validate(data)

  def list_library_structures(
    self,
    taxonomy_id: Union[Optional[str], UnsetType] = UNSET,
    block_type: Union[Optional[str], UnsetType] = UNSET,
    **kwargs: Any,
  ) -> ListLibraryStructures:
    variables: dict[str, object] = {
      "taxonomyId": taxonomy_id,
      "blockType": block_type,
    }
    response = self.execute(
      query=LIST_LIBRARY_STRUCTURES_GQL,
      operation_name="ListLibraryStructures",
      variables=variables,
      **kwargs,
    )
    data = self.get_data(response)
    return ListLibraryStructures.model_validate(data)

  def list_library_taxonomies(
    self,
    include_element_count: bool,
    standard: Union[Optional[str], UnsetType] = UNSET,
    **kwargs: Any,
  ) -> ListLibraryTaxonomies:
    variables: dict[str, object] = {
      "standard": standard,
      "includeElementCount": include_element_count,
    }
    response = self.execute(
      query=LIST_LIBRARY_TAXONOMIES_GQL,
      operation_name="ListLibraryTaxonomies",
      variables=variables,
      **kwargs,
    )
    data = self.get_data(response)
    return ListLibraryTaxonomies.model_validate(data)

  def list_library_taxonomy_arcs(
    self,
    taxonomy_id: str,
    limit: int,
    offset: int,
    association_type: Union[Optional[str], UnsetType] = UNSET,
    structure_id: Union[Optional[str], UnsetType] = UNSET,
    **kwargs: Any,
  ) -> ListLibraryTaxonomyArcs:
    variables: dict[str, object] = {
      "taxonomyId": taxonomy_id,
      "associationType": association_type,
      "structureId": structure_id,
      "limit": limit,
      "offset": offset,
    }
    response = self.execute(
      query=LIST_LIBRARY_TAXONOMY_ARCS_GQL,
      operation_name="ListLibraryTaxonomyArcs",
      variables=variables,
      **kwargs,
    )
    data = self.get_data(response)
    return ListLibraryTaxonomyArcs.model_validate(data)

  def search_library_elements(
    self,
    query: str,
    limit: int,
    source: Union[Optional[str], UnsetType] = UNSET,
    **kwargs: Any,
  ) -> SearchLibraryElements:
    variables: dict[str, object] = {
      "query": query,
      "source": source,
      "limit": limit,
    }
    response = self.execute(
      query=SEARCH_LIBRARY_ELEMENTS_GQL,
      operation_name="SearchLibraryElements",
      variables=variables,
      **kwargs,
    )
    data = self.get_data(response)
    return SearchLibraryElements.model_validate(data)
