from flask import jsonify, request
from app import app
from elasticsearch import Elasticsearch
from typing import Dict, Any

es_client = Elasticsearch()


@app.route('/api/movies', methods=['GET'], strict_slashes=False)
def movies_list() -> Dict[str, Any]:
    # Получает данные из ES об отфильтрованном по request.args списке фильмов
    result = es_client.search(
        index="movies", query={"match_all": {}}
    )
    return result


@app.route('/api/movies/<movie_id>', methods=['GET'])
def movie_details(movie_id: str) -> Dict[str, Any]:
    # Получает данные из ES об одном фильме
    query = {
        "match": {
            "id": movie_id
        }
    }
    result = es_client.search(index="movies", query=query)
    return result
