import os
from pathlib import Path


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-only-karigar-key")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///karigar_ai.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEMO_MODE = os.getenv("DEMO_MODE", "true").lower() == "true"
    UPLOAD_FOLDER = Path(__file__).resolve().parent.parent / "uploads"
