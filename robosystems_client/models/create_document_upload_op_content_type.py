from enum import Enum


class CreateDocumentUploadOpContentType(str, Enum):
  APPLICATIONPDF = "application/pdf"
  IMAGEJPEG = "image/jpeg"
  IMAGEPNG = "image/png"

  def __str__(self) -> str:
    return str(self.value)
