from fastapi import (
    FastAPI,
)

from .config import settings

docs_url = None
redoc_url = None
if settings.DEBUG:
    docs_url = "/docs"
    redoc_url= "/redoc"

application = FastAPI(
    title='Movies reviwer',
    description='Manage your reviews of the films you have watched.',
    version="0.0.1",
    redoc_url=redoc_url,
    docs_url=docs_url,
)
