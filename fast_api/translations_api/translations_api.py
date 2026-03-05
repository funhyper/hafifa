from typing import Any

import uvicorn
from fastapi import FastAPI, Depends


from fast_api.repository.abstract.translation_repository_base import TranslationRepositoryBase
from fast_api.repository.sql.db_initializer import sqlite_initializer
from fast_api.repository.sql.sql_repository import SQLTranslationRepository
from fast_api.utils.exceptions import TranslationNotFoundException, TranslationAlreadyExistsException
from fast_api.utils.status import Status

# CR: I think a cleaner approach would be somthing like this: (obviously in a different file)
STATUS = "status"
REASON = "reason"


def create_successful_response(**kwargs) -> dict[str, Any]:
    return {
        STATUS: Status.SUCCESS.value,
        **kwargs,
    }


def create_failed_response(message: str) -> dict[str, str]:
    # To me it makes more sense to put "translation already exists" as the reason, and have the status be "failed" either way.
    # That way the code which uses the API can handle any exception without needing to know them all & update when
    # there is a new one
    return {
        STATUS: Status.Fail.value,  # and change the value in the enum to be "failed"
        REASON: message,
    }

# The advantage to doing it this way is:
# * I have one clear place which defines how my response messages look, and not scattered all over
# * If I want to change something I'll only need to change it here
# * Less repetitive when creating an endpoint
# * I can't accidentally misspell "status" somewhere
# * It's more SRP - each endpoint only needs to implement the logic and not how the response message will look

# Another option would be to create a class of type Response and then SuccessfulResponse and FailureResponse (instead of the functions)


STATUS_TO_MSG = {Status.SUCCESS: "success", Status.TRANSLATION_EXISTS: "translation already exists",
                 Status.TRANSLATION_NOT_FOUND: "translation not found"}
app = FastAPI()


# CR: I'd move this to a dependencies file
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


# CR: this can stay in main.py (otherwise its hard to find where to run the app from)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
