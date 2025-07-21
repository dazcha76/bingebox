from enum import Enum
from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String
from database import Base
from enums import ShowFormat, ShowGenre

class Show(Base):
  __tablename__ = "shows"
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, nullable=False)
  image = Column(String, nullable=True)
  genre = Column(Enum(ShowGenre), nullable=True)
  format = Column(Enum(ShowFormat), nullable=True)
  favorite = Column(Boolean, nullable=False, default=False)

class Episode(Base):
  __tablename__ = "episodes"
  id = Column(Integer, primary_key=True, index=True)
  number = Column(Integer, nullable=True)
  title = Column(String, nullable=False)
  air_date = Column(Date, nullable=True)
  show_id = Column(Integer, ForeignKey("shows.id"), nullable=False)

class Actor(Base):
  __tablename__ = "actors"
  id = Column(Integer, primary_key=True, index=True)
  first_name = Column(String, nullable=False)
  last_name = Column(String, nullable=False)
