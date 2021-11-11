from enum import Enum


class SortField(str, Enum):
    ID = "id"
    TITLE = "title"
    IMDB_RATING = "imdb_rating"


class SortOrder(str, Enum):
    ASC = "asc"
    DESC = "desc"
