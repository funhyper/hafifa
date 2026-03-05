from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Translation(Base):
    __tablename__ = "translations"
    id: Mapped[int] = mapped_column(primary_key=True)
    src_lang: Mapped[str] = mapped_column(String(50))
    dst_lang: Mapped[str] = mapped_column(String(50))
    origin_word: Mapped[str] = mapped_column(String(50))
    translated_word: Mapped[str] = mapped_column(String(50))
