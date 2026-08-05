from enum import Enum


class ReportDownloadFormat(str, Enum):
  JSONLD = "JSONLD"
  HOLON_JSONLD = "HOLON_JSONLD"
  XBRL_2_1 = "XBRL_2_1"
