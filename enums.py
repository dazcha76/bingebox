from enum import Enum

class ShowFormat(str, Enum):
  GAME_SHOW = "Game Show"
  MINI_SERIES = "Mini-series"
  REALITY_SHOW = "Reality Show"
  SERIES = "Series"
  TALK_SHOW = "Talk Show"

class ShowGenre(str, Enum):
  ACTION = "Action"
  ADVENTURE = "Adventure"
  ANIMATION = "Animation"
  COMEDY = "Comedy"
  CRIME = "Crime"
  DRAMA = "Drama"
  FANTASY = "Fantasy"
  MYSTERY = "Mystery"
  ROMANCE = "Romance"
  SCI_FI = "Sci-Fi"
