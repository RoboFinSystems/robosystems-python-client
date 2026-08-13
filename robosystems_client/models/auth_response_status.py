from enum import Enum


class AuthResponseStatus(str, Enum):
  AUTHENTICATED = "authenticated"
  MFA_ENROLLMENT_REQUIRED = "mfa_enrollment_required"
  MFA_REQUIRED = "mfa_required"

  def __str__(self) -> str:
    return str(self.value)
