from enum import Enum


class ReportLifecycle(str, Enum):
  CURRENT = "CURRENT"
  ARCHIVED = "ARCHIVED"
  ALL = "ALL"


class ReportDownloadFormat(str, Enum):
  HOLON_JSONLD = "HOLON_JSONLD"
  HOLON_JSONLD_LINEAGE = "HOLON_JSONLD_LINEAGE"
  XBRL_2_1 = "XBRL_2_1"
  TAVI = "TAVI"
