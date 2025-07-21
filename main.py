from typing_extensions import Annotated
from fastapi import Depends, FastAPI, HTTPException
from enums import ShowFormat, ShowGenre
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

from schemas import ShowBase

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

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
  favorite: bool | None = None,
  genre: ShowGenre | None = None,
  format: ShowFormat | None = None
):
  skip = (page - 1) * limit
  query = db.query(models.Show)

  if genre:
    query = query.filter(models.Show.genre == genre)
  if format:
    query = query.filter(models.Show.format == format)
  if favorite is not None:
    query = query.filter(models.Show.favorite == favorite)

  shows = query.offset(skip).limit(limit).all()
  return shows

@app.get("/shows/{show_id}")
async def get_show(show_id: int, db: db_dependency):
  show = db.query(models.Show).filter(models.Show.id == show_id).first()
  if not show:
    raise HTTPException(status_code=404, detail="Show is not found")
  return show

@app.patch("/shows/{show_id}")
async def toggle_favorites(show_id: int, db: db_dependency):
  db_show = db.query(models.Show).filter(models.Show.id == show_id).first()
  if not db_show:
    raise HTTPException(status_code=404, detail="Show not found")
  db_show.favorite = not db_show.favorite
  db.commit()
  db.refresh(db_show)
  return {"show": db_show.name, "favorite": db_show.favorite}

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
