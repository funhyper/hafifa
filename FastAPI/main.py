from fastapi import FastAPI

# CR: convention is to use snake case for all directory names (not FastAPI)
from FastAPI.repository.sqlite.db_initializer import initialize
from FastAPI.repository.sqlite.sqlite_repository import SqliteTranslationRepository
from FastAPI.translations_api.translations_api import TranslationsAPI
import uvicorn


def main():
    app = FastAPI()
    engine = initialize()
    repository = SqliteTranslationRepository(engine)
    api = TranslationsAPI(repository)
    app.include_router(api.router)
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
