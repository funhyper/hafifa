from fastapi import FastAPI, Depends
from fast_api.repository.abstract.translation_repository_base import TranslationRepositoryBase
from fast_api.translations_api.api_dependencies import get_repository
from fast_api.translations_api.response_provider import ResponseProvider
from fast_api.utils.exceptions import TranslationNotFoundException, TranslationAlreadyExistsException


app = FastAPI()
response_provider = ResponseProvider()

@app.get("/api/get_translation/")
def get_translation(src_lang: str, dst_lang: str, original_word: str,
                    repository: TranslationRepositoryBase = Depends(get_repository)) -> dict:
    try:
        word = repository.get_translation(src_lang, dst_lang, original_word)
    except TranslationNotFoundException:
        return response_provider.create_failure_response("Translation not found")
    else:
        return response_provider.create_successful_response(translation=word)


@app.post("/api/add_translation/")
def post_translation(src_lang: str, dst_lang: str, original_word: str, translated_word: str,
                     repository: TranslationRepositoryBase = Depends(get_repository)) -> dict:
    try:
        repository.add_translation(src_lang, dst_lang, original_word, translated_word)
    except TranslationAlreadyExistsException:
        return response_provider.create_failure_response("Translation already exists")
    else:
        return response_provider.create_successful_response()


@app.put("/api/change_translation/")
def change_translation(src_lang: str, dst_lang: str, original_word: str, new_word: str,
                       repository: TranslationRepositoryBase = Depends(get_repository)) -> dict:
    try:
        repository.change_translation(src_lang, dst_lang, original_word, new_word)
    except TranslationNotFoundException:
        return response_provider.create_failure_response("Translation not found")
    else:
        return response_provider.create_successful_response()


@app.delete("/api/delete_translation/")
def delete_translation(src_lang: str, dst_lang: str, original_word: str,
                       repository: TranslationRepositoryBase = Depends(get_repository)) -> dict:
    try:
        repository.delete_translation(src_lang, dst_lang, original_word)
    except TranslationNotFoundException:
        return response_provider.create_failure_response("Translation not found")
    else:
        return response_provider.create_successful_response()

