from dataclasses import dataclass
from typing import List


@dataclass
class ShortMovie:
    id: str
    title: str
    imdb_rating: float

    def to_dict(self) -> dict:
        return dict(id=self.id, title=self.title, imdb_rating=self.imdb_rating)


@dataclass
class Writer:
    id: str
    name: str

    def to_dict(self) -> dict:
        return dict(id=self.id, name=self.name)


@dataclass
class Actor:
    id: str
    name: str

    def to_dict(self) -> dict:
        return dict(id=self.id, name=self.name)


@dataclass
class Movies:
    id: str
    title: str
    description: str
    imdb_rating: float
    writers: List[Writer]
    actors: List[Actor]
    genres: List[str]
    directors: List[str]

    def to_dict(self) -> dict:
        return dict(
            id=self.id,
            title=self.title,
            description=self.description,
            imdb_rating=self.imdb_rating,
            writers=self.writers,
            actors=self.actors,
            genre=self.genres,
            director=self.directors
        )
