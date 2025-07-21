from pydantic import BaseModel
from datetime import date
from enums import ShowFormat, ShowGenre

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