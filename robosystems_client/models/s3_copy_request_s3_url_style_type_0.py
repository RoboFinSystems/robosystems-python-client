from enum import Enum


class S3CopyRequestS3UrlStyleType0(str, Enum):
  PATH = "path"
  VHOST = "vhost"

  def __str__(self) -> str:
    return str(self.value)
