from fastapi import FastAPI

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
    "last_aired": "",
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
  3: {
    "name": "",
    "image": "",
    "genre": "",
    "type": "",
    "seasons": 1,
    "episodes": 1,
    "actors": [],
    "first_aired": "",
    "last_aired": "",
  },
  4: {
    "name": "",
    "image": "",
    "genre": "",
    "type": "",
    "seasons": 2,
    "episodes": 2,
    "actors": [],
    "first_aired": "",
    "last_aired": "",
  },
  5: {
    "name": "",
    "image": "",
    "genre": "",
    "type": "",
    "seasons": 3,
    "episodes": 3,
    "actors": [],
    "first_aired": "",
    "last_aired": "",
  },
  6: {
    "name": "",
    "image": "",
    "genre": "",
    "type": "",
    "seasons": 4,
    "episodes": 4,
    "actors": [],
    "first_aired": "",
    "last_aired": "",
  },
  7: {
    "name": "",
    "image": "",
    "genre": "",
    "type": "",
    "seasons": 5,
    "episodes": 5,
    "actors": [],
    "first_aired": "",
    "last_aired": "",
  },
  8: {
    "name": "",
    "image": "",
    "genre": "",
    "type": "",
    "seasons": 6,
    "episodes": 6,
    "actors": [],
    "first_aired": "",
    "last_aired": "",
  },
  9: {
    "name": "",
    "image": "",
    "genre": "",
    "type": "",
    "seasons": 7,
    "episodes": 7,
    "actors": [],
    "first_aired": "",
    "last_aired": "",
  },
  10: {
    "name": "",
    "image": "",
    "genre": "",
    "type": "",
    "seasons": 8,
    "episodes": 8,
    "actors": [],
    "first_aired": "",
    "last_aired": "",
  }
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