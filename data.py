from enums import ShowFormat, ShowGenre

shows = {
  1: {
    "name": "Doctor Who",
    "image": "https://example.com/doctor-who.jpg",
    "genre": ShowGenre.SCI_FI,
    "format": ShowFormat.SERIES,
    "seasons": 41,
    "episodes": 892,
    "actors": ["Jodie Whittaker", "David Tennant", "Matt Smith"],
    "first_aired": "1963-11-23",
    "last_aired": None,
  },
  2: {
     "name": "Star Trek: The Next Generation",
     "image": "https://example.com/star-trek.jpg",
     "genre": ShowGenre.SCI_FI,
     "format": ShowFormat.SERIES,
     "seasons": 7,
     "episodes": 178,
     "actors": ["Patrick Stewart", "Jonathan Frakes", "Brent Spiner"],
     "first_aired": "1987-09-28",
     "last_aired": "1994-05-23",
  },
}
