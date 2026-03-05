import sqlalchemy
from sqlalchemy import Engine, String

from hafifa.FastAPI.repository.sql.db_modules import Base


def sqlite_initializer() -> Engine:
    engine = sqlalchemy.create_engine("sqlite:///translations.db", echo=True)
    Base.metadata.create_all(engine)
    return engine



