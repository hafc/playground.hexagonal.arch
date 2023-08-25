from enum import Enum, unique


@unique
class Status(Enum):
    active = "active"
    stoped = "stoped"
    creating = "creating"
    error = "error"
    deleted = "deleted"
