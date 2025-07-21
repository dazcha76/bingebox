from datetime import date
from typing_extensions import Annotated
from fastapi import Depends, FastAPI
from pydantic import BaseModel
from data import shows
from enums import ShowFormat, ShowGenre
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class ShowBase(BaseModel):
  name: str
  image: str | None = None
  genre: ShowGenre | None = None
  format: ShowFormat | None = None
  favorite: bool = False

class EpisodeBase(BaseModel):
  number: int | None = None
  title: str
  air_date: date | None = None

class ActorBase(BaseModel):
  first_name: str
  last_name: str

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/shows")
def get_shows(
  page: int = 1,
  limit: int = 10,
  genre: ShowGenre = None,
  format: ShowFormat = None
):
  skip = (page - 1) * limit
  show_list = list(shows.values()) 

  if genre:
    show_list = list(filter(lambda show: show["genre"] == genre.value, show_list))
  
  if format:
    show_list = list(filter(lambda show: show["format"] == format.value, show_list))
  
  return show_list[skip: skip + limit]

@app.get("/shows/{show_id}")
def get_show(show_id: int):
  return shows.get(show_id)

@app.post("/shows")
async def add_show(show: ShowBase, db: db_dependency):
  db_show = models.Show(
    name=show.name,
    image=show.image,
    genre=show.genre.value if show.genre else None,
    format=show.format.value if show.format else None,
    favorite=show.favorite
  )
  db.add(db_show)
  db.commit()
  db.refresh(db_show)
