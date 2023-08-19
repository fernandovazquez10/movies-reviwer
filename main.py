from app import application
from app.config import settings


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        'main:application',
        host=settings.HOST, 
        port=settings.PORT, 
        reload=settings.RELOAD,
    )
