__all__ = [
  "GET_INFORMATION_BLOCK_GQL",
  "GET_INVESTOR_HOLDINGS_GQL",
  "GET_INVESTOR_PORTFOLIO_BLOCK_GQL",
  "GET_INVESTOR_POSITION_GQL",
  "GET_INVESTOR_SECURITY_GQL",
  "GET_LEDGER_ACCOUNT_ROLLUPS_GQL",
  "GET_LEDGER_ACCOUNT_TREE_GQL",
  "GET_LEDGER_AGENT_GQL",
  "GET_LEDGER_CLOSING_BOOK_STRUCTURES_GQL",
  "GET_LEDGER_ENTITY_GQL",
  "GET_LEDGER_EVENT_BLOCK_GQL",
  "GET_LEDGER_FISCAL_CALENDAR_GQL",
  "GET_LEDGER_MAPPED_TRIAL_BALANCE_GQL",
  "GET_LEDGER_MAPPING_COVERAGE_GQL",
  "GET_LEDGER_MAPPING_GQL",
  "GET_LEDGER_PERIOD_CLOSE_STATUS_GQL",
  "GET_LEDGER_PERIOD_DRAFTS_GQL",
  "GET_LEDGER_PUBLISH_LIST_GQL",
  "GET_LEDGER_REPORTING_TAXONOMY_GQL",
  "GET_LEDGER_REPORT_DOWNLOAD_URL_GQL",
  "GET_LEDGER_REPORT_GQL",
  "GET_LEDGER_REPORT_PACKAGE_GQL",
  "GET_LEDGER_STATEMENT_GQL",
  "GET_LEDGER_SUMMARY_GQL",
  "GET_LEDGER_TRANSACTION_GQL",
  "GET_LEDGER_TRIAL_BALANCE_GQL",
  "GET_LIBRARY_ELEMENT_ARCS_GQL",
  "GET_LIBRARY_ELEMENT_EQUIVALENTS_GQL",
  "GET_LIBRARY_ELEMENT_GQL",
  "GET_LIBRARY_TAXONOMY_GQL",
  "LIST_INFORMATION_BLOCKS_GQL",
  "LIST_INVESTOR_PORTFOLIOS_GQL",
  "LIST_INVESTOR_POSITIONS_GQL",
  "LIST_INVESTOR_SECURITIES_GQL",
  "LIST_LEDGER_ACCOUNTS_GQL",
  "LIST_LEDGER_AGENTS_GQL",
  "LIST_LEDGER_ELEMENTS_GQL",
  "LIST_LEDGER_ENTITIES_GQL",
  "LIST_LEDGER_EVENT_BLOCKS_GQL",
  "LIST_LEDGER_MAPPINGS_GQL",
  "LIST_LEDGER_PUBLISH_LISTS_GQL",
  "LIST_LEDGER_REPORTS_GQL",
  "LIST_LEDGER_STRUCTURES_GQL",
  "LIST_LEDGER_TAXONOMIES_GQL",
  "LIST_LEDGER_TRANSACTIONS_GQL",
  "LIST_LEDGER_UNMAPPED_ELEMENTS_GQL",
  "LIST_LIBRARY_ELEMENTS_GQL",
  "LIST_LIBRARY_TAXONOMIES_GQL",
  "LIST_LIBRARY_TAXONOMY_ARCS_GQL",
  "SEARCH_LIBRARY_ELEMENTS_GQL",
]

GET_INVESTOR_HOLDINGS_GQL = """
query GetInvestorHoldings($portfolioId: String!) {
  holdings(portfolioId: $portfolioId) {
    totalEntities
    totalPositions
    holdings {
      entityId
      entityName
      sourceGraphId
      totalCostBasisDollars
      totalCurrentValueDollars
      positionCount
      securities {
        securityId
        securityName
        securityType
        quantity
        quantityType
        costBasisDollars
        currentValueDollars
      }
    }
  }
}
"""

GET_INVESTOR_PORTFOLIO_BLOCK_GQL = """
query GetInvestorPortfolioBlock($portfolioId: String!) {
  portfolioBlock(portfolioId: $portfolioId) {
    id
    name
    description
    strategy
    inceptionDate
    baseCurrency
    owner {
      id
      name
      sourceGraphId
    }
    positions {
      id
      quantity
      quantityType
      costBasisDollars
      currentValueDollars
      valuationDate
      valuationSource
      acquisitionDate
      status
      notes
      security {
        id
        name
        securityType
        securitySubtype
        isActive
        sourceGraphId
        issuer {
          id
          name
          sourceGraphId
        }
      }
    }
    totalCostBasisDollars
    totalCurrentValueDollars
    activePositionCount
    createdAt
    updatedAt
  }
}
"""

GET_INVESTOR_POSITION_GQL = """
query GetInvestorPosition($positionId: String!) {
  position(positionId: $positionId) {
    id
    portfolioId
    securityId
    securityName
    entityName
    quantity
    quantityType
    costBasis
    costBasisDollars
    currency
    currentValue
    currentValueDollars
    valuationDate
    valuationSource
    acquisitionDate
    dispositionDate
    status
    notes
    createdAt
    updatedAt
  }
}
"""

GET_INVESTOR_SECURITY_GQL = """
query GetInvestorSecurity($securityId: String!) {
  security(securityId: $securityId) {
    id
    entityId
    entityName
    sourceGraphId
    name
    securityType
    securitySubtype
    terms
    isActive
    authorizedShares
    outstandingShares
    createdAt
    updatedAt
  }
}
"""

LIST_INVESTOR_PORTFOLIOS_GQL = """
query ListInvestorPortfolios($limit: Int! = 100, $offset: Int! = 0) {
  portfolios(limit: $limit, offset: $offset) {
    portfolios {
      id
      name
      description
      strategy
      inceptionDate
      baseCurrency
      createdAt
      updatedAt
    }
    pagination {
      total
      limit
      offset
      hasMore
    }
  }
}
"""

LIST_INVESTOR_POSITIONS_GQL = """
query ListInvestorPositions($portfolioId: String, $securityId: String, $status: String, $limit: Int! = 100, $offset: Int! = 0) {
  positions(
    portfolioId: $portfolioId
    securityId: $securityId
    status: $status
    limit: $limit
    offset: $offset
  ) {
    positions {
      id
      portfolioId
      securityId
      securityName
      entityName
      quantity
      quantityType
      costBasis
      costBasisDollars
      currency
      currentValue
      currentValueDollars
      valuationDate
      valuationSource
      acquisitionDate
      dispositionDate
      status
      notes
      createdAt
      updatedAt
    }
    pagination {
      total
      limit
      offset
      hasMore
    }
  }
}
"""

LIST_INVESTOR_SECURITIES_GQL = """
query ListInvestorSecurities($entityId: String, $securityType: String, $isActive: Boolean, $limit: Int! = 100, $offset: Int! = 0) {
  securities(
    entityId: $entityId
    securityType: $securityType
    isActive: $isActive
    limit: $limit
    offset: $offset
  ) {
    securities {
      id
      entityId
      entityName
      sourceGraphId
      name
      securityType
      securitySubtype
      terms
      isActive
      authorizedShares
      outstandingShares
      createdAt
      updatedAt
    }
    pagination {
      total
      limit
      offset
      hasMore
    }
  }
}
"""

GET_INFORMATION_BLOCK_GQL = """
query GetInformationBlock($id: ID!) {
  informationBlock(id: $id) {
    id
    blockType
    name
    displayName
    category
    taxonomyId
    taxonomyName
    informationModel {
      conceptArrangement
      memberArrangement
    }
    artifact {
      topic
      rendererNote
      template
      mechanics
    }
    elements {
      id
      qname
      name
      code
      elementType
      isAbstract
      isMonetary
      balanceType
      periodType
    }
    connections {
      id
      fromElementId
      toElementId
      associationType
      arcrole
      orderValue
      weight
    }
    facts {
      id
      elementId
      value
      textValue
      factType
      contentType
      periodStart
      periodEnd
      periodType
      unit
      factScope
      factSetId
    }
    rules {
      id
      ruleCategory
      rulePattern
      ruleCheckKind
      ruleExpression
      ruleMessage
      ruleSeverity
      ruleOrigin
      ruleTarget {
        targetKind
        targetRefId
      }
      ruleVariables {
        variableName
        variableQname
      }
    }
    factSet {
      id
      structureId
      periodStart
      periodEnd
      factsetType
      entityId
      reportId
      provenance
    }
    verificationResults {
      id
      ruleId
      structureId
      factSetId
      status
      message
      periodStart
      periodEnd
      evaluatedAt
    }
    verificationSummary {
      total
      passed
      failed
      errored
      skipped
      byCategory {
        category
        total
        passed
        failed
        errored
        skipped
      }
    }
    view {
      rendering {
        rows {
          elementId
          elementQname
          elementName
          classification
          balanceType
          values
          textValue
          isSubtotal
          depth
        }
        periods {
          start
          end
          label
        }
        validation {
          passed
          checks
          failures
          warnings
        }
        unmappedCount
      }
    }
  }
}
"""

GET_LEDGER_ACCOUNT_ROLLUPS_GQL = """
query GetLedgerAccountRollups($mappingId: String, $startDate: Date, $endDate: Date) {
  accountRollups(mappingId: $mappingId, startDate: $startDate, endDate: $endDate) {
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
"""

GET_LEDGER_ACCOUNT_TREE_GQL = """
query GetLedgerAccountTree {
  accountTree {
    totalAccounts
    roots {
      id
      code
      name
      trait
      accountType
      balanceType
      depth
      isActive
      children {
        id
        code
        name
        trait
        accountType
        balanceType
        depth
        isActive
        children {
          id
          code
          name
          trait
          accountType
          balanceType
          depth
          isActive
          children {
            id
            code
            name
            trait
            accountType
            balanceType
            depth
            isActive
          }
        }
      }
    }
  }
}
"""

GET_LEDGER_AGENT_GQL = """
query GetLedgerAgent($id: String!) {
  agent(id: $id) {
    id
    agentType
    name
    legalName
    taxId
    registrationNumber
    duns
    lei
    email
    phone
    address
    source
    externalId
    isActive
    is1099Recipient
    createdAt
    updatedAt
    createdBy
  }
}
"""

GET_LEDGER_CLOSING_BOOK_STRUCTURES_GQL = """
query GetLedgerClosingBookStructures {
  closingBookStructures {
    hasData
    categories {
      label
      items {
        id
        name
        itemType
        blockType
        reportId
        status
      }
    }
  }
}
"""

GET_LEDGER_ENTITY_GQL = """
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
"""

GET_LEDGER_EVENT_BLOCK_GQL = """
query GetLedgerEventBlock($id: String!) {
  eventBlock(id: $id) {
    id
    eventType
    eventCategory
    eventClass
    status
    occurredAt
    effectiveAt
    source
    externalId
    externalUrl
    amount
    currency
    description
    metadata
    dimensionIds
    agentId
    resourceType
    resourceElementId
    replacedByEventId
    replacesEventId
    obligatedByEventId
    dischargesEventId
    createdAt
    createdBy
  }
}
"""

GET_LEDGER_FISCAL_CALENDAR_GQL = """
query GetLedgerFiscalCalendar {
  fiscalCalendar {
    graphId
    fiscalYearStartMonth
    closedThrough
    closeTarget
    gapPeriods
    catchUpSequence
    closeableNow
    blockers
    lastCloseAt
    initializedAt
    lastSyncAt
    periods {
      name
      startDate
      endDate
      status
      closedAt
    }
  }
}
"""

GET_LEDGER_MAPPED_TRIAL_BALANCE_GQL = """
query GetLedgerMappedTrialBalance($mappingId: String!, $startDate: Date, $endDate: Date) {
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
"""

GET_LEDGER_MAPPING_GQL = """
query GetLedgerMapping($mappingId: String!) {
  mapping(mappingId: $mappingId) {
    id
    name
    blockType
    taxonomyId
    totalAssociations
    associations {
      id
      structureId
      fromElementId
      fromElementName
      fromElementQname
      toElementId
      toElementName
      toElementQname
      associationType
      orderValue
      weight
      confidence
      suggestedBy
      approvedBy
    }
  }
}
"""

GET_LEDGER_MAPPING_COVERAGE_GQL = """
query GetLedgerMappingCoverage($mappingId: String!) {
  mappingCoverage(mappingId: $mappingId) {
    mappingId
    totalCoaElements
    mappedCount
    unmappedCount
    coveragePercent
    highConfidence
    mediumConfidence
    lowConfidence
  }
}
"""

GET_LEDGER_PERIOD_CLOSE_STATUS_GQL = """
query GetLedgerPeriodCloseStatus($periodStart: Date!, $periodEnd: Date!) {
  periodCloseStatus(periodStart: $periodStart, periodEnd: $periodEnd) {
    fiscalPeriodStart
    fiscalPeriodEnd
    periodStatus
    totalDraft
    totalPosted
    schedules {
      structureId
      structureName
      amount
      status
      entryId
      reversalEntryId
      reversalStatus
    }
  }
}
"""

GET_LEDGER_PERIOD_DRAFTS_GQL = """
query GetLedgerPeriodDrafts($period: String!) {
  periodDrafts(period: $period) {
    period
    periodStart
    periodEnd
    draftCount
    totalDebit
    totalCredit
    allBalanced
    qbWritebackConnectionId
    qbWritePolicy
    qbPublishCount
    localOnlyCount
    drafts {
      entryId
      postingDate
      type
      memo
      provenance
      sourceStructureId
      sourceStructureName
      totalDebit
      totalCredit
      balanced
      willPublishToQb
      lineItems {
        lineItemId
        elementId
        elementCode
        elementName
        debitAmount
        creditAmount
        description
      }
    }
  }
}
"""

GET_LEDGER_PUBLISH_LIST_GQL = """
query GetLedgerPublishList($listId: String!) {
  publishList(listId: $listId) {
    id
    name
    description
    memberCount
    createdBy
    createdAt
    updatedAt
    members {
      id
      targetGraphId
      targetGraphName
      targetOrgName
      addedBy
      addedAt
    }
  }
}
"""

GET_LEDGER_REPORT_GQL = """
query GetLedgerReport($reportId: String!) {
  report(reportId: $reportId) {
    id
    name
    taxonomyId
    generationStatus
    periodType
    periodStart
    periodEnd
    comparative
    mappingId
    aiGenerated
    createdAt
    lastGenerated
    entityName
    filingStatus
    filedAt
    filedBy
    supersedesId
    supersededById
    sourceGraphId
    sourceReportId
    sharedAt
    periods {
      start
      end
      label
    }
    structures {
      id
      name
      blockType
    }
  }
}
"""

GET_LEDGER_REPORT_DOWNLOAD_URL_GQL = """
query GetLedgerReportDownloadUrl($reportId: String!, $format: ReportDownloadFormat = JSONLD, $expiresIn: Int = 300) {
  reportDownloadUrl(reportId: $reportId, format: $format, expiresIn: $expiresIn) {
    downloadUrl
    expiresAt
    contentType
    format
    generationCount
  }
}
"""

GET_LEDGER_REPORT_PACKAGE_GQL = """
query GetLedgerReportPackage($reportId: String!) {
  reportPackage(reportId: $reportId) {
    id
    name
    description
    taxonomyId
    periodType
    periodStart
    periodEnd
    generationStatus
    lastGenerated
    filingStatus
    filedAt
    filedBy
    supersedesId
    supersededById
    sourceGraphId
    sourceReportId
    sharedAt
    entityName
    aiGenerated
    createdAt
    createdBy
    items {
      factSetId
      structureId
      displayOrder
      block {
        id
        blockType
        name
        displayName
        category
        taxonomyId
        taxonomyName
        informationModel {
          conceptArrangement
          memberArrangement
        }
        artifact {
          topic
          rendererNote
          template
          mechanics
        }
        elements {
          id
          qname
          name
          code
          elementType
          isAbstract
          isMonetary
          balanceType
          periodType
        }
        connections {
          id
          fromElementId
          toElementId
          associationType
          arcrole
          orderValue
          weight
        }
        facts {
          id
          elementId
          value
          textValue
          factType
          contentType
          periodStart
          periodEnd
          periodType
          unit
          factScope
          factSetId
        }
        rules {
          id
          ruleCategory
          rulePattern
          ruleCheckKind
          ruleExpression
          ruleMessage
          ruleSeverity
          ruleOrigin
          ruleTarget {
            targetKind
            targetRefId
          }
          ruleVariables {
            variableName
            variableQname
          }
        }
        factSet {
          id
          structureId
          periodStart
          periodEnd
          factsetType
          entityId
          reportId
          provenance
        }
        verificationResults {
          id
          ruleId
          structureId
          factSetId
          status
          message
          periodStart
          periodEnd
          evaluatedAt
        }
        verificationSummary {
          total
          passed
          failed
          errored
          skipped
          byCategory {
            category
            total
            passed
            failed
            errored
            skipped
          }
        }
        view {
          rendering {
            rows {
              elementId
              elementQname
              elementName
              classification
              balanceType
              values
              textValue
              isSubtotal
              depth
            }
            periods {
              start
              end
              label
            }
            validation {
              passed
              checks
              failures
              warnings
            }
            unmappedCount
          }
        }
      }
    }
  }
}
"""

GET_LEDGER_REPORTING_TAXONOMY_GQL = """
query GetLedgerReportingTaxonomy {
  reportingTaxonomy {
    id
    name
    description
    taxonomyType
    version
    standard
    namespaceUri
    isShared
    isActive
    isLocked
    sourceTaxonomyId
    targetTaxonomyId
  }
}
"""

GET_LEDGER_STATEMENT_GQL = """
query GetLedgerStatement($reportId: String!, $blockType: String!) {
  statement(reportId: $reportId, blockType: $blockType) {
    reportId
    structureId
    structureName
    blockType
    unmappedCount
    periods {
      start
      end
      label
    }
    rows {
      elementId
      elementQname
      elementName
      trait
      values
      isSubtotal
      depth
    }
    validation {
      passed
      checks
      failures
      warnings
    }
  }
}
"""

GET_LEDGER_SUMMARY_GQL = """
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
"""

GET_LEDGER_TRANSACTION_GQL = """
query GetLedgerTransaction($transactionId: String!) {
  transaction(transactionId: $transactionId) {
    id
    number
    type
    category
    amount
    currency
    date
    dueDate
    merchantName
    referenceNumber
    description
    source
    sourceId
    status
    postedAt
    entries {
      id
      number
      type
      postingDate
      memo
      status
      postedAt
      lineItems {
        id
        accountId
        accountName
        accountCode
        debitAmount
        creditAmount
        description
        lineOrder
      }
    }
  }
}
"""

GET_LEDGER_TRIAL_BALANCE_GQL = """
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
"""

LIST_INFORMATION_BLOCKS_GQL = """
query ListInformationBlocks($blockType: String, $category: String, $limit: Int, $offset: Int) {
  informationBlocks(
    blockType: $blockType
    category: $category
    limit: $limit
    offset: $offset
  ) {
    id
    blockType
    name
    displayName
    category
    taxonomyId
    taxonomyName
    informationModel {
      conceptArrangement
      memberArrangement
    }
    artifact {
      topic
      rendererNote
      template
      mechanics
    }
    elements {
      id
      qname
      name
      code
      elementType
      isAbstract
      isMonetary
      balanceType
      periodType
    }
    connections {
      id
      fromElementId
      toElementId
      associationType
      arcrole
      orderValue
      weight
    }
    facts {
      id
      elementId
      value
      textValue
      factType
      contentType
      periodStart
      periodEnd
      periodType
      unit
      factScope
      factSetId
    }
    rules {
      id
      ruleCategory
      rulePattern
      ruleCheckKind
      ruleExpression
      ruleMessage
      ruleSeverity
      ruleOrigin
      ruleTarget {
        targetKind
        targetRefId
      }
      ruleVariables {
        variableName
        variableQname
      }
    }
    factSet {
      id
      structureId
      periodStart
      periodEnd
      factsetType
      entityId
      reportId
      provenance
    }
    verificationResults {
      id
      ruleId
      structureId
      factSetId
      status
      message
      periodStart
      periodEnd
      evaluatedAt
    }
    verificationSummary {
      total
      passed
      failed
      errored
      skipped
      byCategory {
        category
        total
        passed
        failed
        errored
        skipped
      }
    }
    view {
      rendering {
        rows {
          elementId
          elementQname
          elementName
          classification
          balanceType
          values
          textValue
          isSubtotal
          depth
        }
        periods {
          start
          end
          label
        }
        validation {
          passed
          checks
          failures
          warnings
        }
        unmappedCount
      }
    }
  }
}
"""

LIST_LEDGER_ACCOUNTS_GQL = """
query ListLedgerAccounts($classification: String, $isActive: Boolean, $limit: Int! = 100, $offset: Int! = 0) {
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
    pagination {
      total
      limit
      offset
      hasMore
    }
  }
}
"""

LIST_LEDGER_AGENTS_GQL = """
query ListLedgerAgents($agentType: String, $source: String, $isActive: Boolean = true, $limit: Int! = 50, $offset: Int! = 0) {
  agents(
    agentType: $agentType
    source: $source
    isActive: $isActive
    limit: $limit
    offset: $offset
  ) {
    id
    agentType
    name
    legalName
    taxId
    registrationNumber
    duns
    lei
    email
    phone
    address
    source
    externalId
    isActive
    is1099Recipient
    createdAt
    updatedAt
    createdBy
  }
}
"""

LIST_LEDGER_ELEMENTS_GQL = """
query ListLedgerElements($taxonomyId: String, $source: String, $classification: String, $isAbstract: Boolean, $limit: Int! = 100, $offset: Int! = 0) {
  elements(
    taxonomyId: $taxonomyId
    source: $source
    classification: $classification
    isAbstract: $isAbstract
    limit: $limit
    offset: $offset
  ) {
    elements {
      id
      code
      name
      description
      qname
      namespace
      trait
      subClassification
      balanceType
      periodType
      isAbstract
      elementType
      source
      taxonomyId
      parentId
      depth
      isActive
      externalId
      externalSource
    }
    pagination {
      total
      limit
      offset
      hasMore
    }
  }
}
"""

LIST_LEDGER_ENTITIES_GQL = """
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
"""

LIST_LEDGER_EVENT_BLOCKS_GQL = """
query ListLedgerEventBlocks($eventType: String, $eventCategory: String, $status: String, $agentId: String, $source: String, $limit: Int! = 50, $offset: Int! = 0) {
  eventBlocks(
    eventType: $eventType
    eventCategory: $eventCategory
    status: $status
    agentId: $agentId
    source: $source
    limit: $limit
    offset: $offset
  ) {
    id
    eventType
    eventCategory
    eventClass
    status
    occurredAt
    effectiveAt
    source
    externalId
    externalUrl
    amount
    currency
    description
    metadata
    dimensionIds
    agentId
    resourceType
    resourceElementId
    replacedByEventId
    replacesEventId
    obligatedByEventId
    dischargesEventId
    createdAt
    createdBy
  }
}
"""

LIST_LEDGER_MAPPINGS_GQL = """
query ListLedgerMappings {
  mappings {
    structures {
      id
      name
      description
      blockType
      taxonomyId
      isActive
    }
  }
}
"""

LIST_LEDGER_PUBLISH_LISTS_GQL = """
query ListLedgerPublishLists($limit: Int! = 100, $offset: Int! = 0) {
  publishLists(limit: $limit, offset: $offset) {
    publishLists {
      id
      name
      description
      memberCount
      createdBy
      createdAt
      updatedAt
    }
    pagination {
      total
      limit
      offset
      hasMore
    }
  }
}
"""

LIST_LEDGER_REPORTS_GQL = """
query ListLedgerReports {
  reports {
    reports {
      id
      name
      taxonomyId
      generationStatus
      periodType
      periodStart
      periodEnd
      comparative
      mappingId
      aiGenerated
      createdAt
      lastGenerated
      entityName
      sourceGraphId
      sourceReportId
      sharedAt
      periods {
        start
        end
        label
      }
      structures {
        id
        name
        blockType
      }
    }
  }
}
"""

LIST_LEDGER_STRUCTURES_GQL = """
query ListLedgerStructures($taxonomyId: String, $blockType: String) {
  structures(taxonomyId: $taxonomyId, blockType: $blockType) {
    structures {
      id
      name
      description
      blockType
      taxonomyId
      isActive
    }
  }
}
"""

LIST_LEDGER_TAXONOMIES_GQL = """
query ListLedgerTaxonomies($taxonomyType: String) {
  taxonomies(taxonomyType: $taxonomyType) {
    taxonomies {
      id
      name
      description
      taxonomyType
      version
      standard
      namespaceUri
      isShared
      isActive
      isLocked
      sourceTaxonomyId
      targetTaxonomyId
    }
  }
}
"""

LIST_LEDGER_TRANSACTIONS_GQL = """
query ListLedgerTransactions($type: String, $startDate: Date, $endDate: Date, $limit: Int! = 100, $offset: Int! = 0) {
  transactions(
    type: $type
    startDate: $startDate
    endDate: $endDate
    limit: $limit
    offset: $offset
  ) {
    transactions {
      id
      number
      type
      category
      amount
      currency
      date
      dueDate
      merchantName
      referenceNumber
      description
      source
      status
    }
    pagination {
      total
      limit
      offset
      hasMore
    }
  }
}
"""

LIST_LEDGER_UNMAPPED_ELEMENTS_GQL = """
query ListLedgerUnmappedElements($mappingId: String) {
  unmappedElements(mappingId: $mappingId) {
    id
    code
    name
    trait
    balanceType
    externalSource
    suggestedTargets {
      elementId
      qname
      name
      confidence
    }
  }
}
"""

GET_LIBRARY_ELEMENT_GQL = """
query GetLibraryElement($id: ID, $qname: String) {
  libraryElement(id: $id, qname: $qname) {
    id
    qname
    namespace
    name
    trait
    balanceType
    periodType
    isAbstract
    isMonetary
    elementType
    source
    taxonomyId
    parentId
    labels {
      role
      language
      text
    }
    references {
      refType
      citation
      uri
    }
  }
}
"""

GET_LIBRARY_ELEMENT_ARCS_GQL = """
query GetLibraryElementArcs($id: ID!) {
  libraryElementArcs(id: $id) {
    id
    direction
    associationType
    arcrole
    taxonomyId
    taxonomyStandard
    taxonomyName
    structureId
    structureName
    peer {
      id
      qname
      name
      trait
      source
    }
  }
}
"""

GET_LIBRARY_ELEMENT_EQUIVALENTS_GQL = """
query GetLibraryElementEquivalents($id: ID!) {
  libraryElementEquivalents(id: $id) {
    element {
      id
      qname
      name
      trait
      source
    }
    equivalents {
      id
      qname
      name
      trait
      source
    }
  }
}
"""

GET_LIBRARY_TAXONOMY_GQL = """
query GetLibraryTaxonomy($id: ID, $standard: String, $version: String, $includeElementCount: Boolean! = false) {
  libraryTaxonomy(
    id: $id
    standard: $standard
    version: $version
    includeElementCount: $includeElementCount
  ) {
    id
    name
    description
    standard
    version
    namespaceUri
    taxonomyType
    isShared
    isActive
    isLocked
    elementCount
  }
}
"""

LIST_LIBRARY_ELEMENTS_GQL = """
query ListLibraryElements($taxonomyId: ID, $source: String, $classification: String, $activityType: String, $elementType: String, $isAbstract: Boolean, $limit: Int! = 50, $offset: Int! = 0, $includeLabels: Boolean! = false, $includeReferences: Boolean! = false) {
  libraryElements(
    taxonomyId: $taxonomyId
    source: $source
    classification: $classification
    activityType: $activityType
    elementType: $elementType
    isAbstract: $isAbstract
    limit: $limit
    offset: $offset
    includeLabels: $includeLabels
    includeReferences: $includeReferences
  ) {
    id
    qname
    namespace
    name
    trait
    balanceType
    periodType
    isAbstract
    isMonetary
    elementType
    source
    taxonomyId
    parentId
    labels @include(if: $includeLabels) {
      role
      language
      text
    }
    references @include(if: $includeReferences) {
      refType
      citation
      uri
    }
  }
}
"""

LIST_LIBRARY_TAXONOMIES_GQL = """
query ListLibraryTaxonomies($standard: String, $includeElementCount: Boolean! = false) {
  libraryTaxonomies(
    standard: $standard
    includeElementCount: $includeElementCount
  ) {
    id
    name
    description
    standard
    version
    namespaceUri
    taxonomyType
    isShared
    isActive
    isLocked
    elementCount
  }
}
"""

LIST_LIBRARY_TAXONOMY_ARCS_GQL = """
query ListLibraryTaxonomyArcs($taxonomyId: ID!, $associationType: String, $limit: Int! = 200, $offset: Int! = 0) {
  libraryTaxonomyArcCount(taxonomyId: $taxonomyId)
  libraryTaxonomyArcs(
    taxonomyId: $taxonomyId
    associationType: $associationType
    limit: $limit
    offset: $offset
  ) {
    id
    structureId
    structureName
    fromElementId
    fromElementQname
    fromElementName
    toElementId
    toElementQname
    toElementName
    associationType
    arcrole
    orderValue
    weight
  }
}
"""

SEARCH_LIBRARY_ELEMENTS_GQL = """
query SearchLibraryElements($query: String!, $source: String, $limit: Int! = 50) {
  searchLibraryElements(query: $query, source: $source, limit: $limit) {
    id
    qname
    namespace
    name
    trait
    balanceType
    periodType
    isAbstract
    isMonetary
    elementType
    source
    taxonomyId
    parentId
    labels {
      role
      language
      text
    }
    references {
      refType
      citation
      uri
    }
  }
}
"""
