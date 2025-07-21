from datetime import date
from pydantic import BaseModel
from enums import ShowFormat, ShowGenre

class ShowBase(BaseModel):
  name: str
  image: str | None = None
  genre: ShowGenre | None = None
  format: ShowFormat | None = None
  favorite: bool = False

  model_config = {
    "json_schema_extra": {
      "examples": [
        {
          "available genre values": [
            "Action",
            "Adventure",
            "Animation",
            "Comedy",
            "Crime",
            "Drama",
            "Fantasy",
            "Mystery",
            "Romance",
            "Sci-Fi"
          ],
          "available format values": [
            "Game Show",
            "Mini-series",
            "Reality Show",
            "Series",
            "Talk Show"
          ]
        }
      ]
    }
  }

class EpisodeBase(BaseModel):
  number: int | None = None
  title: str
  air_date: date | None = None

class ActorBase(BaseModel):
  first_name: str
  last_name: str