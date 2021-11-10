from typing import Optional
from app.schemas import Movie, Writer, Actor
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
