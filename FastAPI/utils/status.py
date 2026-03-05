from enum import Enum


class Status(Enum):
    SUCCESS = 0,
    TRANSLATION_NOT_FOUND = 1,
    TRANSLATION_EXISTS = 2
