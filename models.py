from pydantic import BaseModel, Field
from typing import List
from datetime import date

# ---------- Shows ----------
class ShowBase(BaseModel):
  name: str
  image: str = None
  genre: int = None
  format: int = None

class ShowCreate(ShowBase):
  pass

class ShowOut(ShowBase):
  id: int
  favorite: bool = Field(default=False)
  actors: List["ActorOut"] = None

  class Config:
    orm_mode = True

# ---------- Episodes ----------
class EpisodeBase(BaseModel):
  number: int = None
  title: str = None
  air_date: date = None

class EpisodeCreate(EpisodeBase):
  show_id: int

class EpisodeOut(EpisodeBase):
  id: int
  show_id: int

  class Config:
    orm_mode = True

# ---------- Actors ----------
class ActorBase(BaseModel):
  first_name: str
  last_name: str

class ActorCreate(ActorBase):
  pass

class ActorOut(ActorBase):
  id: int
  shows: List[ShowOut] = None

  class Config:
    orm_mode = True

# ---------- Genre ---------- 
class GenreBase(BaseModel):
    name: str

class GenreCreate(GenreBase):
    pass

class GenreOut(GenreBase):
    id: int
    class Config:
        orm_mode = True

# ---------- Format ----------   
class FormatBase(BaseModel):
    name: str

class FormatCreate(FormatBase):
    pass

class FormatOut(FormatBase):
    id: int
    class Config:
        orm_mode = True

ShowOut.model_rebuild()
ActorOut.model_rebuild()
