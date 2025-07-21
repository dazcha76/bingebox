from faker import Faker
from database import SessionLocal
from enums import ShowFormat, ShowGenre
from data import real_actors, real_tv_shows
import models
import random

fake = Faker()
db = SessionLocal()

# ------ Seed tv shows ------ #

for name in real_tv_shows:
  show = models.Show(
    name=name,
    image=fake.image_url(),
    genre=random.choice(list(ShowGenre)).value,
    format=random.choice(list(ShowFormat)).value,
    favorite=fake.boolean(),
  )
  db.add(show)

# ------ Seed actors ------ #

for actor_data in real_actors:
  actor = models.Actor(
    first_name=actor_data["first_name"],
    last_name=actor_data["last_name"]
  )
  db.add(actor)

# ------ Seed episodes ------ #

shows = db.query(models.Show).all()

for _ in range(len(shows)):
  show = random.choice(shows)
  episode_number = random.randint(1, 10)
  title = fake.sentence(nb_words=5)
  air_date = fake.date_this_decade()

  episode = models.Episode(
    number=episode_number,
    title=title,
    air_date=air_date,
    show_id=show.id
  )
  db.add(episode)

db.commit()
db.close()
