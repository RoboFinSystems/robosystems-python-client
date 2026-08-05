__all__ = ["GET_LEDGER_SUMMARY_GQL"]

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
