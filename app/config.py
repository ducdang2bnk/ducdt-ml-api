import os


class Config:
    HOST = os.getenv("HOST", "127.0.0.1")
    PORT = int(os.getenv("PORT", 8000))
    RELOAD = os.getenv("RELOAD", "true").lower() in ("true", "1", "t")


config = Config()
