import uvicorn
from fastapi import FastAPI, Depends

from hafifa.FastAPI.repository.abstract.translation_repository_base import TranslationRepositoryBase
from hafifa.FastAPI.repository.sql.db_initializer import sqlite_initializer
from hafifa.FastAPI.repository.sql.sql_repository import SQLTranslationRepository
from hafifa.FastAPI.utils.exceptions import TranslationNotFoundException, TranslationAlreadyExistsException
from hafifa.FastAPI.utils.status import Status

STATUS_TO_MSG = {Status.SUCCESS: "success", Status.TRANSLATION_EXISTS: "translation already exists",
                 Status.TRANSLATION_NOT_FOUND: "translation not found"}
app = FastAPI()


def get_repository() -> TranslationRepositoryBase:
    return SQLTranslationRepository(sqlite_initializer())


@app.get("/api/get_translation/")
def get_translation(src_lang: str, dst_lang: str, original_word: str,
                    repository: TranslationRepositoryBase = Depends(get_repository)) -> dict:
    try:
        word = repository.get_translation(src_lang, dst_lang, original_word)
    except TranslationNotFoundException:
        return {"status": STATUS_TO_MSG[Status.TRANSLATION_NOT_FOUND]}
    else:
        return {"translation": word, "status": STATUS_TO_MSG[Status.SUCCESS]}


@app.post("/api/add_translation/")
def post_translation(src_lang: str, dst_lang: str, original_word: str, translated_word: str,
                     repository: TranslationRepositoryBase = Depends(get_repository)) -> dict:
    try:
        repository.add_translation(src_lang, dst_lang, original_word, translated_word)
    except TranslationAlreadyExistsException:
        return {"status": STATUS_TO_MSG[Status.TRANSLATION_EXISTS]}
    else:
        return {"status": STATUS_TO_MSG[Status.SUCCESS]}


@app.put("/api/change_translation/")
def change_translation(src_lang: str, dst_lang: str, original_word: str, new_word: str,
                       repository: TranslationRepositoryBase = Depends(get_repository)) -> dict:
    try:
        repository.change_translation(src_lang, dst_lang, original_word, new_word)
    except TranslationNotFoundException:
        return {"error": STATUS_TO_MSG[Status.TRANSLATION_NOT_FOUND]}
    else:
        return {"status": STATUS_TO_MSG[Status.SUCCESS]}


@app.delete("/api/delete_translation/")
def delete_translation(src_lang: str, dst_lang: str, original_word: str,
                       repository: TranslationRepositoryBase = Depends(get_repository)) -> dict:
    try:
        repository.delete_translation(src_lang, dst_lang, original_word)
    except TranslationNotFoundException:
        return {"status": STATUS_TO_MSG[Status.TRANSLATION_NOT_FOUND]}
    else:
        return {"status": STATUS_TO_MSG[Status.SUCCESS]}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
