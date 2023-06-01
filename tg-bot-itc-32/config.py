import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv(".env")

BOT_TOKEN = os.getenv("BOT_TOKEN")

BASE_DIR = Path(__file__).resolve().parent
MEDIA_DIR = BASE_DIR / "media/"
MUSICS_DIR = MEDIA_DIR / "musics/"

engine = create_engine("sqlite:///app.db")
Base: object = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)
