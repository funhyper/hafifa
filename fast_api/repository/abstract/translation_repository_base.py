from abc import ABC, abstractmethod


class TranslationRepositoryBase(ABC):
    @abstractmethod
    def add_translation(self, src_lang: str, dst_lang: str, original_word: str, translated_word: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def get_translation(self, src_lang: str, dst_lang: str, original_word: str) -> str | None:
        raise NotImplementedError

    @abstractmethod
    def change_translation(self, src_lang: str, dst_lang: str, original_word: str, translated_word: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def delete_translation(self, src_lang: str, dst_lang: str, original_word: str) -> None:
        raise NotImplementedError