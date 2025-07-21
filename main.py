from typing_extensions import Annotated
from fastapi import Depends, FastAPI, HTTPException
from enums import ShowFormat, ShowGenre
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from schemas import ShowBase
import models

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

db_dependency = Annotated[Session, Depends(get_db)]

# ---------- Shows ---------- #

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
  return {"id": db_show.id, "show": db_show.name, "favorite": db_show.favorite}

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

# ---------- Episodes ---------- #

@app.get("/shows/{show_id}/episodes")
async def get_episodes(show_id: int, db: db_dependency):
  show = db.query(models.Show).filter(models.Show.id == show_id).first()
  episodes = db.query(models.Episode).filter(models.Episode.show_id == show_id).all()
  if not episodes:
    raise HTTPException(status_code=404, detail="No episodes found for this show")
  return {"id": show.id, show.name: episodes}

# ---------- Actors ---------- #

@app.get("/shows/{show_id}/actors")
def get_actors_by_show(show_id, db: db_dependency):
  show = db.query(models.Show).filter(models.Show.id == show_id).first()
  if not show:
    return None
  return {"id": show.id, show.name: show.actors}