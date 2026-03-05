from fast_api.repository.abstract.translation_repository_base import TranslationRepositoryBase
from fast_api.repository.sql.db_initializer import sqlite_initializer
from fast_api.repository.sql.sql_repository import SQLTranslationRepository


def get_repository() -> TranslationRepositoryBase:
    return SQLTranslationRepository(sqlite_initializer())
