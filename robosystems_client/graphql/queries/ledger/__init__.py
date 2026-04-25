"""Ledger-domain GraphQL queries and parsers.

All 29 ledger reads from the `/extensions/{graph_id}/graphql` endpoint
live here as module-level query constants plus a `parse_*` helper per
query that reshapes the camelCase JSON into snake_case dicts.

Unlike the TypeScript client (which uses GraphQL Code Generator to
produce typed `DocumentNode`s and strict per-query types), the Python
client returns `dict[str, Any]` or `list[dict]` because the backend
Pydantic response models never make it through OpenAPI (the extensions
read routes are GraphQL only). Consumers who want typed shapes can
wrap these dicts in their own models; the facade preserves key names.
"""

from __future__ import annotations

from typing import Any

from ...client import keys_to_snake


# ── Entity ──────────────────────────────────────────────────────────────

GET_ENTITY_QUERY = """
query GetLedgerEntity {
  entity {
    id
    name
    legalName
    uri
    cik
    ticker
    exchange
    sic
    sicDescription
    category
    stateOfIncorporation
    fiscalYearEnd
    taxId
    lei
    industry
    entityType
    phone
    website
    status
    isParent
    parentEntityId
    source
    sourceId
    sourceGraphId
    connectionId
    addressLine1
    addressCity
    addressState
    addressPostalCode
    addressCountry
    createdAt
    updatedAt
  }
}
""".strip()


def parse_entity(data: dict[str, Any]) -> dict[str, Any] | None:
  entity = data.get("entity")
  return keys_to_snake(entity) if entity is not None else None


LIST_ENTITIES_QUERY = """
query ListLedgerEntities($source: String) {
  entities(source: $source) {
    id
    name
    legalName
    ticker
    cik
    industry
    entityType
    status
    isParent
    parentEntityId
    source
    sourceGraphId
    connectionId
    createdAt
    updatedAt
  }
}
""".strip()


def parse_entities(data: dict[str, Any]) -> list[dict[str, Any]]:
  return [keys_to_snake(e) for e in data.get("entities", [])]


# ── Summary ────────────────────────────────────────────────────────────

GET_SUMMARY_QUERY = """
query GetLedgerSummary {
  summary {
    graphId
    accountCount
    transactionCount
    entryCount
    lineItemCount
    earliestTransactionDate
    latestTransactionDate
    connectionCount
    lastSyncAt
  }
}
""".strip()


def parse_summary(data: dict[str, Any]) -> dict[str, Any] | None:
  summary = data.get("summary")
  return keys_to_snake(summary) if summary is not None else None


# ── Accounts ───────────────────────────────────────────────────────────

LIST_ACCOUNTS_QUERY = """
query ListLedgerAccounts(
  $classification: String
  $isActive: Boolean
  $limit: Int! = 100
  $offset: Int! = 0
) {
  accounts(
    classification: $classification
    isActive: $isActive
    limit: $limit
    offset: $offset
  ) {
    accounts {
      id
      code
      name
      description
      trait
      subClassification
      balanceType
      parentId
      depth
      currency
      isActive
      isPlaceholder
      accountType
      externalId
      externalSource
    }
    pagination { total limit offset hasMore }
  }
}
""".strip()


def parse_accounts(data: dict[str, Any]) -> dict[str, Any] | None:
  accounts = data.get("accounts")
  return keys_to_snake(accounts) if accounts is not None else None


GET_ACCOUNT_TREE_QUERY = """
query GetLedgerAccountTree {
  accountTree {
    totalAccounts
    roots {
      id code name trait accountType balanceType depth isActive
      children {
        id code name trait accountType balanceType depth isActive
        children {
          id code name trait accountType balanceType depth isActive
          children {
            id code name trait accountType balanceType depth isActive
          }
        }
      }
    }
  }
}
""".strip()


def parse_account_tree(data: dict[str, Any]) -> dict[str, Any] | None:
  tree = data.get("accountTree")
  return keys_to_snake(tree) if tree is not None else None


GET_ACCOUNT_ROLLUPS_QUERY = """
query GetLedgerAccountRollups(
  $mappingId: String
  $startDate: Date
  $endDate: Date
) {
  accountRollups(
    mappingId: $mappingId
    startDate: $startDate
    endDate: $endDate
  ) {
    mappingId
    mappingName
    totalMapped
    totalUnmapped
    groups {
      reportingElementId
      reportingName
      reportingQname
      trait
      balanceType
      total
      accounts {
        elementId
        accountName
        accountCode
        totalDebits
        totalCredits
        netBalance
      }
    }
  }
}
""".strip()


def parse_account_rollups(data: dict[str, Any]) -> dict[str, Any] | None:
  rollups = data.get("accountRollups")
  return keys_to_snake(rollups) if rollups is not None else None


# ── Trial balance ──────────────────────────────────────────────────────

GET_TRIAL_BALANCE_QUERY = """
query GetLedgerTrialBalance($startDate: Date, $endDate: Date) {
  trialBalance(startDate: $startDate, endDate: $endDate) {
    totalDebits
    totalCredits
    rows {
      accountId
      accountCode
      accountName
      trait
      accountType
      totalDebits
      totalCredits
      netBalance
    }
  }
}
""".strip()


def parse_trial_balance(data: dict[str, Any]) -> dict[str, Any] | None:
  tb = data.get("trialBalance")
  return keys_to_snake(tb) if tb is not None else None


GET_MAPPED_TRIAL_BALANCE_QUERY = """
query GetLedgerMappedTrialBalance(
  $mappingId: String!
  $startDate: Date
  $endDate: Date
) {
  mappedTrialBalance(
    mappingId: $mappingId
    startDate: $startDate
    endDate: $endDate
  ) {
    mappingId
    rows {
      reportingElementId
      qname
      reportingName
      trait
      balanceType
      totalDebits
      totalCredits
      netBalance
    }
  }
}
""".strip()


def parse_mapped_trial_balance(data: dict[str, Any]) -> dict[str, Any] | None:
  mtb = data.get("mappedTrialBalance")
  return keys_to_snake(mtb) if mtb is not None else None


# ── Transactions ───────────────────────────────────────────────────────

LIST_TRANSACTIONS_QUERY = """
query ListLedgerTransactions(
  $type: String
  $startDate: Date
  $endDate: Date
  $limit: Int! = 100
  $offset: Int! = 0
) {
  transactions(
    type: $type
    startDate: $startDate
    endDate: $endDate
    limit: $limit
    offset: $offset
  ) {
    transactions {
      id number type category amount currency date dueDate
      merchantName referenceNumber description source status
    }
    pagination { total limit offset hasMore }
  }
}
""".strip()


def parse_transactions(data: dict[str, Any]) -> dict[str, Any] | None:
  txs = data.get("transactions")
  return keys_to_snake(txs) if txs is not None else None


GET_TRANSACTION_QUERY = """
query GetLedgerTransaction($transactionId: String!) {
  transaction(transactionId: $transactionId) {
    id number type category amount currency date dueDate
    merchantName referenceNumber description source sourceId status postedAt
    entries {
      id number type postingDate memo status postedAt
      lineItems {
        id accountId accountName accountCode
        debitAmount creditAmount description lineOrder
      }
    }
  }
}
""".strip()


def parse_transaction(data: dict[str, Any]) -> dict[str, Any] | None:
  tx = data.get("transaction")
  return keys_to_snake(tx) if tx is not None else None


# ── Taxonomy ───────────────────────────────────────────────────────────

GET_REPORTING_TAXONOMY_QUERY = """
query GetLedgerReportingTaxonomy {
  reportingTaxonomy {
    id name description taxonomyType version standard namespaceUri
    isShared isActive isLocked sourceTaxonomyId targetTaxonomyId
  }
}
""".strip()


def parse_reporting_taxonomy(data: dict[str, Any]) -> dict[str, Any] | None:
  t = data.get("reportingTaxonomy")
  return keys_to_snake(t) if t is not None else None


LIST_TAXONOMIES_QUERY = """
query ListLedgerTaxonomies($taxonomyType: String) {
  taxonomies(taxonomyType: $taxonomyType) {
    taxonomies {
      id name description taxonomyType version standard namespaceUri
      isShared isActive isLocked sourceTaxonomyId targetTaxonomyId
    }
  }
}
""".strip()


def parse_taxonomies(data: dict[str, Any]) -> list[dict[str, Any]]:
  t = data.get("taxonomies") or {}
  return [keys_to_snake(x) for x in t.get("taxonomies", [])]


# ── Elements ───────────────────────────────────────────────────────────

LIST_ELEMENTS_QUERY = """
query ListLedgerElements(
  $taxonomyId: String
  $source: String
  $classification: String
  $isAbstract: Boolean
  $limit: Int! = 100
  $offset: Int! = 0
) {
  elements(
    taxonomyId: $taxonomyId
    source: $source
    classification: $classification
    isAbstract: $isAbstract
    limit: $limit
    offset: $offset
  ) {
    elements {
      id code name description qname namespace
      trait subClassification balanceType periodType
      isAbstract elementType source taxonomyId parentId depth
      isActive externalId externalSource
    }
    pagination { total limit offset hasMore }
  }
}
""".strip()


def parse_elements(data: dict[str, Any]) -> dict[str, Any] | None:
  e = data.get("elements")
  return keys_to_snake(e) if e is not None else None


LIST_UNMAPPED_ELEMENTS_QUERY = """
query ListLedgerUnmappedElements($mappingId: String) {
  unmappedElements(mappingId: $mappingId) {
    id code name trait balanceType externalSource
    suggestedTargets { elementId qname name confidence }
  }
}
""".strip()


def parse_unmapped_elements(data: dict[str, Any]) -> list[dict[str, Any]]:
  return [keys_to_snake(e) for e in data.get("unmappedElements", [])]


# ── Structures / mappings ─────────────────────────────────────────────

LIST_STRUCTURES_QUERY = """
query ListLedgerStructures($taxonomyId: String, $structureType: String) {
  structures(taxonomyId: $taxonomyId, structureType: $structureType) {
    structures {
      id name description structureType taxonomyId isActive
    }
  }
}
""".strip()


def parse_structures(data: dict[str, Any]) -> list[dict[str, Any]]:
  s = data.get("structures") or {}
  return [keys_to_snake(x) for x in s.get("structures", [])]


LIST_MAPPINGS_QUERY = """
query ListLedgerMappings {
  mappings {
    structures {
      id name description structureType taxonomyId isActive
    }
  }
}
""".strip()


def parse_mappings(data: dict[str, Any]) -> list[dict[str, Any]]:
  m = data.get("mappings") or {}
  return [keys_to_snake(x) for x in m.get("structures", [])]


GET_MAPPING_QUERY = """
query GetLedgerMapping($mappingId: String!) {
  mapping(mappingId: $mappingId) {
    id name structureType taxonomyId totalAssociations
    associations {
      id structureId
      fromElementId fromElementName fromElementQname
      toElementId toElementName toElementQname
      associationType orderValue weight confidence
      suggestedBy approvedBy
    }
  }
}
""".strip()


def parse_mapping(data: dict[str, Any]) -> dict[str, Any] | None:
  m = data.get("mapping")
  return keys_to_snake(m) if m is not None else None


GET_MAPPING_COVERAGE_QUERY = """
query GetLedgerMappingCoverage($mappingId: String!) {
  mappingCoverage(mappingId: $mappingId) {
    mappingId totalCoaElements mappedCount unmappedCount
    coveragePercent highConfidence mediumConfidence lowConfidence
  }
}
""".strip()


def parse_mapping_coverage(data: dict[str, Any]) -> dict[str, Any] | None:
  c = data.get("mappingCoverage")
  return keys_to_snake(c) if c is not None else None


# ── Information Blocks ─────────────────────────────────────────────────

GET_INFORMATION_BLOCK_QUERY = """
query GetInformationBlock($id: ID!) {
  informationBlock(id: $id) {
    id blockType name displayName category
    taxonomyId taxonomyName
    informationModel { conceptArrangement memberArrangement }
    artifact { topic parentheticalNote template mechanics }
    elements {
      id qname name code elementType
      isAbstract isMonetary balanceType periodType
    }
    connections {
      id fromElementId toElementId associationType
      arcrole orderValue weight
    }
    facts {
      id elementId value periodStart periodEnd
      periodType unit factScope factSetId
    }
  }
}
""".strip()


def parse_information_block(data: dict[str, Any]) -> dict[str, Any] | None:
  block = data.get("informationBlock")
  return keys_to_snake(block) if block is not None else None


LIST_INFORMATION_BLOCKS_QUERY = """
query ListInformationBlocks(
  $blockType: String
  $category: String
  $limit: Int
  $offset: Int
) {
  informationBlocks(
    blockType: $blockType
    category: $category
    limit: $limit
    offset: $offset
  ) {
    id blockType name displayName category
    taxonomyId taxonomyName
    informationModel { conceptArrangement memberArrangement }
    artifact { topic parentheticalNote template mechanics }
    elements {
      id qname name code elementType
      isAbstract isMonetary balanceType periodType
    }
    connections {
      id fromElementId toElementId associationType
      arcrole orderValue weight
    }
    facts {
      id elementId value periodStart periodEnd
      periodType unit factScope factSetId
    }
  }
}
""".strip()


def parse_information_blocks(data: dict[str, Any]) -> list[dict[str, Any]]:
  blocks = data.get("informationBlocks") or []
  return [keys_to_snake(b) for b in blocks]


# ── Period close ───────────────────────────────────────────────────────

GET_PERIOD_CLOSE_STATUS_QUERY = """
query GetLedgerPeriodCloseStatus($periodStart: Date!, $periodEnd: Date!) {
  periodCloseStatus(periodStart: $periodStart, periodEnd: $periodEnd) {
    fiscalPeriodStart fiscalPeriodEnd periodStatus totalDraft totalPosted
    schedules {
      structureId structureName amount status
      entryId reversalEntryId reversalStatus
    }
  }
}
""".strip()


def parse_period_close_status(data: dict[str, Any]) -> dict[str, Any] | None:
  s = data.get("periodCloseStatus")
  return keys_to_snake(s) if s is not None else None


GET_PERIOD_DRAFTS_QUERY = """
query GetLedgerPeriodDrafts($period: String!) {
  periodDrafts(period: $period) {
    period periodStart periodEnd draftCount
    totalDebit totalCredit allBalanced
    drafts {
      entryId postingDate type memo provenance
      sourceStructureId sourceStructureName
      totalDebit totalCredit balanced
      lineItems {
        lineItemId elementId elementCode elementName
        debitAmount creditAmount description
      }
    }
  }
}
""".strip()


def parse_period_drafts(data: dict[str, Any]) -> dict[str, Any] | None:
  d = data.get("periodDrafts")
  return keys_to_snake(d) if d is not None else None


# ── Closing book ───────────────────────────────────────────────────────

GET_CLOSING_BOOK_STRUCTURES_QUERY = """
query GetLedgerClosingBookStructures {
  closingBookStructures {
    hasData
    categories {
      label
      items {
        id name itemType structureType reportId status
      }
    }
  }
}
""".strip()


def parse_closing_book_structures(data: dict[str, Any]) -> dict[str, Any] | None:
  s = data.get("closingBookStructures")
  return keys_to_snake(s) if s is not None else None


# ── Fiscal calendar ────────────────────────────────────────────────────

GET_FISCAL_CALENDAR_QUERY = """
query GetLedgerFiscalCalendar {
  fiscalCalendar {
    graphId fiscalYearStartMonth closedThrough closeTarget
    gapPeriods catchUpSequence closeableNow blockers
    lastCloseAt initializedAt lastSyncAt
    periods { name startDate endDate status closedAt }
  }
}
""".strip()


def parse_fiscal_calendar(data: dict[str, Any]) -> dict[str, Any] | None:
  c = data.get("fiscalCalendar")
  return keys_to_snake(c) if c is not None else None


# ── Reports ────────────────────────────────────────────────────────────

LIST_REPORTS_QUERY = """
query ListLedgerReports {
  reports {
    reports {
      id name taxonomyId generationStatus periodType
      periodStart periodEnd comparative mappingId aiGenerated
      createdAt lastGenerated entityName
      sourceGraphId sourceReportId sharedAt
      periods { start end label }
      structures { id name structureType }
    }
  }
}
""".strip()


def parse_reports(data: dict[str, Any]) -> list[dict[str, Any]]:
  r = data.get("reports") or {}
  return [keys_to_snake(x) for x in r.get("reports", [])]


GET_REPORT_QUERY = """
query GetLedgerReport($reportId: String!) {
  report(reportId: $reportId) {
    id name taxonomyId generationStatus periodType
    periodStart periodEnd comparative mappingId aiGenerated
    createdAt lastGenerated entityName
    sourceGraphId sourceReportId sharedAt
    periods { start end label }
    structures { id name structureType }
  }
}
""".strip()


def parse_report(data: dict[str, Any]) -> dict[str, Any] | None:
  r = data.get("report")
  return keys_to_snake(r) if r is not None else None


GET_STATEMENT_QUERY = """
query GetLedgerStatement($reportId: String!, $structureType: String!) {
  statement(reportId: $reportId, structureType: $structureType) {
    reportId structureId structureName structureType unmappedCount
    periods { start end label }
    rows {
      elementId elementQname elementName trait
      values isSubtotal depth
    }
    validation { passed checks failures warnings }
  }
}
""".strip()


def parse_statement(data: dict[str, Any]) -> dict[str, Any] | None:
  s = data.get("statement")
  return keys_to_snake(s) if s is not None else None


# ── Publish lists ──────────────────────────────────────────────────────

LIST_PUBLISH_LISTS_QUERY = """
query ListLedgerPublishLists($limit: Int! = 100, $offset: Int! = 0) {
  publishLists(limit: $limit, offset: $offset) {
    publishLists {
      id name description memberCount
      createdBy createdAt updatedAt
    }
    pagination { total limit offset hasMore }
  }
}
""".strip()


def parse_publish_lists(data: dict[str, Any]) -> dict[str, Any] | None:
  pl = data.get("publishLists")
  return keys_to_snake(pl) if pl is not None else None


GET_PUBLISH_LIST_QUERY = """
query GetLedgerPublishList($listId: String!) {
  publishList(listId: $listId) {
    id name description memberCount
    createdBy createdAt updatedAt
    members {
      id targetGraphId targetGraphName targetOrgName
      addedBy addedAt
    }
  }
}
""".strip()


def parse_publish_list(data: dict[str, Any]) -> dict[str, Any] | None:
  pl = data.get("publishList")
  return keys_to_snake(pl) if pl is not None else None
