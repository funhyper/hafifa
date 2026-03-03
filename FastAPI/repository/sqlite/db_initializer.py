import sqlalchemy
from sqlalchemy import Engine, String
from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.testing.schema import mapped_column


def initialize() -> Engine:
    engine = sqlalchemy.create_engine("sqlite:///translations.db", echo=True)
    Base.metadata.create_all(engine)
    return engine


# CR: i think it would make sense to move the models to a separate file and not together with the initializer
class Base(DeclarativeBase):
    pass


class Translation(Base):
    __tablename__ = "translations"
    id: Mapped[int] = mapped_column(primary_key=True)
    src_lang: Mapped[str] = mapped_column(String(50))
    dst_lang: Mapped[str] = mapped_column(String(50))
    origin_word: Mapped[str] = mapped_column(String(50))
    translated_word: Mapped[str] = mapped_column(String(50))
