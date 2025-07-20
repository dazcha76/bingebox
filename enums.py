from enum import Enum

class ShowFormat(str, Enum):
    ANTHOLOGY = "Anthology"
    DOCUMENTARY = "Documentary"
    GAME_SHOW = "Game Show"
    MINI_SERIES = "Mini-series"
    REALITY_SHOW = "Reality Show"
    SERIES = "Series"
    SPECIAL = "Special"
    TALK_SHOW = "Talk Show"
    WEB_SERIES = "Web Series"


class ShowGenre(str, Enum):
    ACTION = "Action"
    ADVENTURE = "Adventure"
    ANIMATION = "Animation"
    COMEDY = "Comedy"
    CRIME = "Crime"
    DOCUMENTARY = "Documentary"
    DRAMA = "Drama"
    FAMILY = "Family"
    FANTASY = "Fantasy"
    HORROR = "Horror"
    MUSICAL = "Musical"
    MYSTERY = "Mystery"
    ROMANCE = "Romance"
    SCI_FI = "Sci-Fi"
    THRILLER = "Thriller"
