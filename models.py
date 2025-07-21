from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String, Table
from sqlalchemy.types import Enum as SqlEnum
from database import Base
from enums import ShowFormat, ShowGenre
from sqlalchemy.orm import relationship

show_actor = Table(
  "show_actor",
  Base.metadata,
  Column("show_id", Integer, ForeignKey("shows.id"), primary_key=True),
  Column("actor_id", Integer, ForeignKey("actors.id"), primary_key=True),
)

class Show(Base):
  __tablename__ = "shows"
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, nullable=False)
  image = Column(String, nullable=True)
  genre = Column(SqlEnum(ShowGenre), nullable=True)
  format = Column(SqlEnum(ShowFormat), nullable=True)
  favorite = Column(Boolean, nullable=False, default=False)

  actors = relationship(
    "Actor",
    secondary=show_actor,
    back_populates="shows"
  )

class Episode(Base):
  __tablename__ = "episodes"
  id = Column(Integer, primary_key=True, index=True)
  ep_number = Column(Integer, nullable=True)
  title = Column(String, nullable=False)
  air_date = Column(Date, nullable=True)
  show_id = Column(Integer, ForeignKey("shows.id"), nullable=False)

class Actor(Base):
  __tablename__ = "actors"
  id = Column(Integer, primary_key=True, index=True)
  first_name = Column(String, nullable=False)
  last_name = Column(String, nullable=False)

  shows = relationship(
    "Show",
    secondary=show_actor,
    back_populates="actors"
  )