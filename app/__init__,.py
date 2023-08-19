from fastapi import (
    FastAPI,
)


application = FastAPI(
    title='Movies reviwer',
    description='Manage your reviews of the films you have watched.',
    version="0.0.1",
)
