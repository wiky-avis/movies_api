from flask import jsonify, request
from app import app
from elasticsearch import Elasticsearch
from typing import Dict, Any
from flask_cors import CORS

from app.actions import get_movie_by_id

CORS(app)
es_client = Elasticsearch()


@app.route("/api/movies", methods=["GET"], strict_slashes=False)
def movies_list() -> Dict[str, Any]:
    # Получает данные из ES об отфильтрованном по request.args списке фильмов
    page: int = 1
    limit: int = 50
    result = es_client.search(
        body={
            "size": limit,
            "from": (page - 1) * limit,
            "_source": ["id", "title", "imdb_rating"],
            "query": {
                "multi_match": {
                    "query": "campfir",
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
        },
        index="movies"
    )
    return result


@app.route("/api/movies/<movie_id>", methods=["GET"])
def movie_details(movie_id: str) -> Dict[str, Any]:
    # Получает данные из ES об одном фильме
    result = get_movie_by_id(es_client=es_client, movie_id=movie_id)
    return result.to_dict()
