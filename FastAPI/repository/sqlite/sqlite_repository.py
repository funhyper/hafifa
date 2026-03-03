from sqlalchemy.orm import Session
from sqlalchemy import Engine, select

from FastAPI.repository.abstract.translation_repository_base import TranslationRepositoryBase
from FastAPI.repository.sqlite.db_initializer import Translation


class SqliteTranslationRepository(TranslationRepositoryBase):

    def __init__(self, engine: Engine):
        self._engine = engine

    def add_translation(self, src_lang: str, dst_lang: str, origin_word: str, translated_word: str) -> bool:
        with Session(self._engine) as session:
            if self.get_translation(src_lang, dst_lang, origin_word):
                return False
            translation = Translation(
                src_lang=src_lang,
                dst_lang=dst_lang,
                origin_word=origin_word,
                translated_word=translated_word
            )
            session.add(translation)
            session.commit()
        return True

    def get_translation(self, src_lang: str, dst_lang: str, origin_word: str) -> str | None:
        with Session(self._engine) as session:
            stmt = select(Translation).where(Translation.src_lang == src_lang, Translation.dst_lang == dst_lang, Translation.origin_word == origin_word)
            if translation := session.scalar(stmt):
                return translation.translated_word
            return None



    def change_translation(self, src_lang: str, dst_lang: str, origin_word: str, new_word: str) -> bool:
        with Session(self._engine) as session:
            stmt = select(Translation).where(Translation.src_lang == src_lang, Translation.dst_lang == dst_lang, Translation.origin_word == origin_word)
            entry = session.scalar(stmt)
            if not entry:
                return False
            entry.translated_word = new_word
            session.commit()
            return True

    def delete_translation(self, src_lang: str, dst_lang: str, origin_word: str) -> bool:
        with Session(self._engine) as session:
            stmt = select(Translation).where(Translation.src_lang == src_lang, Translation.dst_lang == dst_lang)
            entry = session.scalar(stmt)
            if not entry:
                return False
            session.delete(entry)
            session.commit()
            return True

