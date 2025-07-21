from faker import Faker
from database import SessionLocal
from enums import ShowFormat, ShowGenre
import models
import random

fake = Faker()
db = SessionLocal()

real_tv_shows = [
    "Breaking Bad",
    "Stranger Things",
    "Game of Thrones",
    "The Office",
    "Friends",
    "The Crown",
    "The Mandalorian",
    "Sherlock",
    "Westworld",
    "The Simpsons"
]

for name in real_tv_shows:
  show = models.Show(
    name=name,
    image=fake.image_url(),
    genre=random.choice(list(ShowGenre)).value,
    format=random.choice(list(ShowFormat)).value,
    favorite=fake.boolean(),
  )
  db.add(show)

db.commit()
db.close()
