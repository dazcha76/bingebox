from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import settings

url=settings.POSTGRES_URL()

engine = create_engine(url)

SessionLocal = sessionmaker(autocmmit=False, autoflush=False, bind=engine)

Base = declarative_base()