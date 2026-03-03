from fastapi import APIRouter

from FastAPI.repository.abstract.translation_repository_base import TranslationRepositoryBase


# CR: our convention is to use the method syntax e.g.
# @app.get("/api/translations/")
# def get_translation(...): ...
# just so you get the hang of it, why don't you translate this to use that syntax

class TranslationsAPI:
    def __init__(self, repository: TranslationRepositoryBase):
        self.repository = repository
        self.router = APIRouter()
        # CR: I think its a bit confusing to give all the different endpoints the same name (even with the different method type)
        # it doesn't hurt to be more explicit and call them more indicatively e.g. get_translation add_translation
        self.router.add_api_route("/api/translations/", self.get_translation, methods=["GET"])
        self.router.add_api_route("/api/translations/", self.post_translation, methods=["POST"])
        self.router.add_api_route("/api/translations/", self.change_translation, methods=["PUT"])
        self.router.add_api_route("/api/translations/", self.delete_translation, methods=["DELETE"])

    def get_translation(self, src_lang: str, dst_lang: str, original_word: str) -> dict:
        word = self.repository.get_translation(src_lang, dst_lang, original_word)
        if word:
            # CR: I like what you did in the other places with the status, I think it would make sense for every
            # response to have a status, so here too
            return {"translation": word}
        # CR: and here too, why not add "status": "error"?
        return {"error": "Translation not found"}

    def post_translation(self, src_lang: str, dst_lang: str, original_word: str, translated_word: str) -> dict:
        if self.repository.add_translation(src_lang, dst_lang, original_word, translated_word):
            # CR: how about moving this out to a const? it's used in a bunch of places. or even better - an enum of Statuses
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


