from fastapi import APIRouter

from FastAPI.repository.abstract.translation_repository_base import TranslationRepositoryBase


class TranslationsAPI:
    def __init__(self, repository: TranslationRepositoryBase):
        self.repository = repository
        self.router = APIRouter()
        self.router.add_api_route("/api/translations/", self.get_translation, methods=["GET"])
        self.router.add_api_route("/api/translations/", self.post_translation, methods=["POST"])
        self.router.add_api_route("/api/translations/", self.change_translation, methods=["PUT"])
        self.router.add_api_route("/api/translations/", self.delete_translation, methods=["DELETE"])

    def get_translation(self, src_lang: str, dst_lang: str, original_word: str) -> dict:
        word = self.repository.get_translation(src_lang, dst_lang, original_word)
        if word:
            return {"translation": word}

        return {"error": "Translation not found"}

    def post_translation(self, src_lang: str, dst_lang: str, original_word: str, translated_word: str) -> dict:
        if self.repository.add_translation(src_lang, dst_lang, original_word, translated_word):
            return {"status": "success"}
        return {"error": "Translation already exists"}

    def change_translation(self, src_lang: str, dst_lang: str, original_word: str, new_word: str) -> dict:
        if self.repository.change_translation(src_lang, dst_lang, original_word, new_word):
            return {"status": "success"}
        return {"error": "Translation doesn't exists"}

    def delete_translation(self, src_lang: str, dst_lang: str, original_word: str) -> dict:
        if self.repository.delete_translation(src_lang, dst_lang, original_word):
            return {"status": "success"}
        return {"error": "Translation doesn't exists"}


