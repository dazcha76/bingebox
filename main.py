from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from datetime import date

class Show(BaseModel):
  name: str
  image: str | None = None
  genre: str | None = None
  type: str | None = None
  seasons: int | None = None
  episodes: int | None = None
  actors: List[str] | None = None
  first_aired: date | None = None
  last_aired: date | None = None

shows = {
  1: {
    "name": "Doctor Who",
    "image": "https://example.com/doctor-who.jpg",
    "genre": "Science Fiction",
    "type": "Series",
    "seasons": 41,
    "episodes": 892,
    "actors": ["Jodie Whittaker", "David Tennant", "Matt Smith"],
    "first_aired": "1963-11-23",
    "last_aired": None,
  },
  2: {
     "name": "Star Trek: The Next Generation",
     "image": "https://example.com/star-trek.jpg",
     "genre": "Science Fiction",
     "type": "Series",
     "seasons": 7,
     "episodes": 178,
     "actors": ["Patrick Stewart", "Jonathan Frakes", "Brent Spiner"],
     "first_aired": "1987-09-28",
     "last_aired": "1994-05-23",
  },
}

app = FastAPI()

@app.get("/shows")
def get_shows(page: int = 1, limit: int = 10):
  skip = (page - 1) * limit
  shows_list = list(shows.values()) 
  return shows_list[skip: skip + limit]

@app.get("/shows/{show_id}")
def get_show(show_id: int):
  return shows.get(show_id)

@app.post("/shows")
def add_show(show: Show):
    new_id = max(shows.keys(), default=0) + 1
    shows[new_id] = show.model_dump()
    return show
