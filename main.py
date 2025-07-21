from fastapi import FastAPI
from data import shows
from enums import ShowFormat, ShowGenre
from models import ShowBase

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
def add_show(show: ShowBase):
  new_id = max(shows.keys(), default=0) + 1
  shows[new_id] = show.model_dump()
  return show
