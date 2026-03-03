from sqlalchemy.orm import Session
from sqlalchemy import Engine, select

from FastAPI.repository.abstract.translation_repository_base import TranslationRepositoryBase
from FastAPI.repository.sqlite.db_initializer import Translation


# CR: is there anything here that is specific to Sqlite? why not just SQLTranslationRepository?
class SqliteTranslationRepository(TranslationRepositoryBase):

    def __init__(self, engine: Engine):
        self._engine = engine

    def add_translation(self, src_lang: str, dst_lang: str, origin_word: str, translated_word: str) -> bool:
        with Session(self._engine) as session:
            if self.get_translation(src_lang, dst_lang, origin_word):
                # CR: its a bit hard to understand from this boolean what it means. How about raising a custom exception instead?
                # e.g. raise TranslationConflictException("This word already has a translation") more readable no? it'll
                # also allow us to have different failure types and handle them differently (more OCP)
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
            # CR: dont shorten variable names
            stmt = select(Translation).where(Translation.src_lang == src_lang, Translation.dst_lang == dst_lang, Translation.origin_word == origin_word)
            if translation := session.scalar(stmt):
                return translation.translated_word
            # CR: another example why working with exceptions is nice, here you suddenly have a different convention
            # than the other functions - you don't return a bool that signals if it worked or not
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

