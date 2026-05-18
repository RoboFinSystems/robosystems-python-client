from enum import Enum


class CreateEventBlockRequestEventActionType0(str, Enum):
  ACCEPT = "accept"
  CITE = "cite"
  COMBINE = "combine"
  CONSUME = "consume"
  COPY = "copy"
  DELIVERSERVICE = "deliverService"
  DROPOFF = "dropoff"
  LOWER = "lower"
  MODIFY = "modify"
  MOVE = "move"
  PICKUP = "pickup"
  PRODUCE = "produce"
  RAISE = "raise"
  SEPARATE = "separate"
  TRANSFER = "transfer"
  TRANSFERALLRIGHTS = "transferAllRights"
  TRANSFERCUSTODY = "transferCustody"
  USE = "use"
  WORK = "work"

  def __str__(self) -> str:
    return str(self.value)
