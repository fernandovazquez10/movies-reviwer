from app import application


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        'main:application'
    )
