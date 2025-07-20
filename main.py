from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from datetime import date
from data import shows
from enums import ShowFormat, ShowGenre

class Show(BaseModel):
  name: str
  image: str | None = None
  genre: ShowGenre = None
  format: ShowFormat = None
  seasons: int | None = None
  episodes: int | None = None
  actors: List[str] | None = None
  first_aired: date | None = None
  last_aired: date | None = None

app = FastAPI()

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
def add_show(show: Show):
    new_id = max(shows.keys(), default=0) + 1
    shows[new_id] = show.model_dump()
    return show
