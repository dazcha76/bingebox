from datetime import date
from typing_extensions import Annotated
from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
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

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/shows")
def get_shows(
  db: db_dependency,
  page: int = 1,
  limit: int = 10,
  genre: ShowGenre | None = None,
  format: ShowFormat | None = None
):
  skip = (page - 1) * limit
  query = db.query(models.Show)

  if genre:
      query = query.filter(models.Show.genre == genre)
  if format:
      query = query.filter(models.Show.format == format)

  shows = query.offset(skip).limit(limit).all()
  return shows

@app.get("/shows/{show_id}")
async def get_show(show_id: int, db: db_dependency):
  result = db.query(models.Show).filter(models.Show.id == show_id).first()
  if not result:
    raise HTTPException(status_code=404, detail="Show is not found")
  return result

@app.post("/shows")
async def add_show(show: ShowBase, db: db_dependency):
  try:
    new_show = models.Show(
      name=show.name,
      image=show.image,
      genre=show.genre,
      format=show.format,
      favorite=show.favorite
    )
    db.add(new_show)
    db.commit()
    db.refresh(new_show)
    return new_show
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
