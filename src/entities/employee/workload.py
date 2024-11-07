from enum import Enum


class Workload(str, Enum):
    NONE = 'No work'
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'
    OVERWORK = 'overwork'
    