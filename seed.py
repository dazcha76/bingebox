from faker import Faker
from database import SessionLocal
from enums import ShowFormat, ShowGenre
from data import real_actors, real_tv_shows
import models
import random

fake = Faker()
db = SessionLocal()

# ------ Seed Tv Shows ------ #

for name in real_tv_shows:
  show = models.Show(
    name=name,
    image=fake.image_url(),
    genre=random.choice(list(ShowGenre)).value,
    format=random.choice(list(ShowFormat)).value,
    favorite=fake.boolean(),
  )
  db.add(show)

# ------ Seed Actors ------ #

for actor_data in real_actors:
  actor = models.Actor(
    first_name=actor_data["first_name"],
    last_name=actor_data["last_name"]
  )
  db.add(actor)

# ------ Seed Show_Actors ------ #

shows = db.query(models.Show).all()
actors = db.query(models.Actor).all()

for show in shows:
  assigned_actors = random.sample(actors, k=random.randint(1, min(3, len(actors))))
  for actor in assigned_actors:
    show.actors.append(actor)

# ------ Seed Episodes ------ #

shows = db.query(models.Show).all()

for _ in range(20):
  show = random.choice(shows)
  episode_number = random.randint(1, 10)
  title = fake.sentence(nb_words=5)
  air_date = fake.date_this_decade()

  episode = models.Episode(
    ep_number=episode_number,
    title=title,
    air_date=air_date,
    show_id=show.id
  )
  db.add(episode)

db.commit()
db.close()
