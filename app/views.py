from flask import jsonify, request
from app import app
from elasticsearch import Elasticsearch
from typing import Dict, Any, List
from flask_cors import CORS

from app.actions import get_movie_by_id, get_movies_list
from app.const import SortField, SortOrder
from app.forms import SearchMoviesForm
from app.schemas import ShortMovie

CORS(app)
es_client = Elasticsearch()


@app.route("/api/movies", methods=["GET"], strict_slashes=False)
def movies_list() -> List[ShortMovie]:
    # Получает данные из ES об отфильтрованном по request.args списке фильмов
    form = SearchMoviesForm(request.args)
    movies = get_movies_list(
        search_query=form.search.data,
        sort_order=SortOrder(form.sort_order.data),
        sort=SortField(form.sort.data),
        page=form.page.data,
        limit=form.limit.data,
    )
    return movies


@app.route("/api/movies/<movie_id>", methods=["GET"])
def movie_details(movie_id: str) -> Dict[str, Any]:
    # Получает данные из ES об одном фильме
    result = get_movie_by_id(es_client=es_client, movie_id=movie_id)
    return result.to_dict()
