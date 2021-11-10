from typing import Optional, List

from app.const import SortOrder, SortField
from app.schemas import Movie, Writer, Actor, ShortMovie
from elasticsearch import Elasticsearch


def get_movie_by_id(movie_id: str, es_client: Elasticsearch) -> Optional[Movie]:
    query = {
        "match": {
            "id": movie_id
        }
    }
    result = es_client.search(index="movies", query=query)
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


def get_movies_list(
        es_client: Elasticsearch,
        search_query: Optional[str] = None,
        sort_order: SortOrder = SortOrder.ASC,
        sort: SortField = SortField.ID,
        page: int = 1,
        limit: int = 50
) -> List[ShortMovie]:
    request_data = {
        "size": limit,
        "from": (page - 1) * limit,
        "sort": [
            {
                sort: sort_order
            }
        ],
        "_source": ["id", "title", "imdb_rating"],
    }

    if search_query:
        request_data["query"] = {
                "multi_match": {
                    "query": search_query,
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
    data = es_client.search(body=request_data, index="movies")
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
