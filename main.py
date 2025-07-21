from datetime import date
from fastapi import FastAPI
from pydantic import BaseModel
from data import shows
from enums import ShowFormat, ShowGenre

app = FastAPI()

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
def add_show(show: ShowBase):
  new_id = max(shows.keys(), default=0) + 1
  shows[new_id] = show.model_dump()
  return show
