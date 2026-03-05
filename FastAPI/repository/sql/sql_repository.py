from sqlalchemy.orm import Session
from sqlalchemy import Engine, select

from hafifa.FastAPI.repository.abstract.translation_repository_base import TranslationRepositoryBase
from hafifa.FastAPI.repository.sql.db_modules import Translation
from hafifa.FastAPI.utils.exceptions import TranslationAlreadyExistsException, TranslationNotFoundException


class SQLTranslationRepository(TranslationRepositoryBase):

    def __init__(self, engine: Engine):
        self._engine = engine

    def add_translation(self, src_lang: str, dst_lang: str, origin_word: str, translated_word: str) -> None:
        with Session(self._engine) as session:
            try:
                self.get_translation(src_lang, dst_lang, origin_word)
            except TranslationNotFoundException:
                translation = Translation(
                    src_lang=src_lang,
                    dst_lang=dst_lang,
                    origin_word=origin_word,
                    translated_word=translated_word
                )
                session.add(translation)
                session.commit()
            else:
                raise TranslationAlreadyExistsException()

    def get_translation(self, src_lang: str, dst_lang: str, origin_word: str) -> str:
        with Session(self._engine) as session:
            statement = select(Translation).where(Translation.src_lang == src_lang, Translation.dst_lang == dst_lang,
                                                  Translation.origin_word == origin_word)
            if translation := session.scalar(statement):
                return translation.translated_word
            raise TranslationNotFoundException()

    def change_translation(self, src_lang: str, dst_lang: str, origin_word: str, new_word: str) -> None:
        with Session(self._engine) as session:
            stmt = select(Translation).where(Translation.src_lang == src_lang, Translation.dst_lang == dst_lang,
                                             Translation.origin_word == origin_word)
            entry = session.scalar(stmt)
            if not entry:
                raise TranslationNotFoundException()
            entry.translated_word = new_word
            session.commit()

    def delete_translation(self, src_lang: str, dst_lang: str, origin_word: str) -> None:
        with Session(self._engine) as session:
            stmt = select(Translation).where(Translation.src_lang == src_lang, Translation.dst_lang == dst_lang)
            entry = session.scalar(stmt)
            if not entry:
                raise TranslationNotFoundException()
            session.delete(entry)
            session.commit()
