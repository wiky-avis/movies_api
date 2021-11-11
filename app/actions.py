from abc import ABC, abstractmethod
from typing import List, Optional

from app.const import SortField
from app.resources import Resources
from app.schemas import Actor, Movie, ShortMovie, Writer


class Action(ABC):
    def __await__(self):
        return self.__call__()

    @abstractmethod
    async def __call__(self, *args, **kwargs):
        raise NotImplementedError


class GetMovieDetail(Action):

    def __init__(self, resources: Resources):
        self.resources = resources

    def __call__(self, movie_id: str = None) -> Optional[Movie]:
            query = {
                "match": {
                    "id": movie_id
                }
            }
            result = self.resources.es_client.search(index="movies", query=query)
            result = result["hits"]["hits"]
            if not result:
                return None

            movie_raw = result[0]['_source']
            return Movie(
                id=movie_raw["id"],
                title=movie_raw["title"],
                description=movie_raw["description"],
                imdb_rating=movie_raw["imdb_rating"],
                writers=[Writer(**x) for x in movie_raw["writers"]],
                actors=[Actor(**x) for x in movie_raw["actors"]],
                genres=movie_raw["genre"],
                directors=movie_raw["director"]
            )


class GetMoviesList(Action):

    def __init__(self, resources: Resources):
        self.resources = resources

    def __call__(self) -> List[ShortMovie]:

        sort_value = self.resources.search.sort.value
        if sort_value == SortField.TITLE.value:
            sort_value = f"{SortField.TITLE.value}.raw"
        request_data = {
            "size": self.resources.search.limit,
            "from": (self.resources.search.page - 1) * self.resources.search.limit,
            "sort": [
                {
                    sort_value: self.resources.search.sort_order.value
                }
            ],
            "_source": ["id", "title", "imdb_rating"],
        }

        if self.resources.search.search_query:
            request_data["query"] = {
                "multi_match": {
                    "query": self.resources.search.search_query,
                    "fuzziness": "auto",
                    "fields": [
                        "title^5",
                        "description^4",
                        "genre^3",
                        "actors_names^3",
                        "writers_names^2",
                        "director"
                    ]
                }
            }
        data = self.resources.es_client.search(body=request_data, index="movies")
        result = data['hits']['hits']

        movies = []
        if result:
            for record in result:
                movie_raw = record['_source']
                movies.append(ShortMovie(
                    id=movie_raw['id'],
                    title=movie_raw['title'],
                    imdb_rating=movie_raw['imdb_rating']
                ))
        return movies
