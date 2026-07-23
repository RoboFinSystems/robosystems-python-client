from enum import Enum


class StructureUpdatePatchConceptArrangementType0(str, Enum):
  ADJUSTMENT = "adjustment"
  ARITHMETIC = "arithmetic"
  COMPOUND_FACT = "compound_fact"
  GRID = "grid"
  LEVEL1_TEXTBLOCK = "level1_textblock"
  LEVEL2_TEXTBLOCK = "level2_textblock"
  LEVEL3_TEXTBLOCK = "level3_textblock"
  LEVEL4_DETAIL = "level4_detail"
  ROLL_FORWARD = "roll_forward"
  ROLL_FORWARD_INFO = "roll_forward_info"
  ROLL_UP = "roll_up"
  SET = "set"
  TABLE_EQUIVALENT_TEXTBLOCK = "table_equivalent_textblock"
  TEXT_BLOCK = "text_block"
  VARIANCE = "variance"

  def __str__(self) -> str:
    return str(self.value)
