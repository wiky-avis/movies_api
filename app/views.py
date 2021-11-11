from http import HTTPStatus
from typing import Any, Dict, List

from flask import abort, jsonify, request
from flask_cors import CORS

from app import app
from app.actions import GetMovieDetail, GetMoviesList
from app.forms import SearchMoviesForm
from app.resources import Resources
from app.schemas import ShortMovie

CORS(app)
resources = Resources()


def validation_errors_to_dict(errors: dict) -> List[dict]:
    validation_errors = []
    for field_name, field_errors in errors.items():
        for err in field_errors:
            validation_errors.append({'loc': ['query', field_name], 'msg': err})
    return validation_errors


@app.route("/api/movies", methods=["GET"], strict_slashes=False)
def movies_list() -> List[ShortMovie]:
    # Получает данные из ES об отфильтрованном по request.args списке фильмов
    form = SearchMoviesForm(request.args)
    validation_errors = []
    if not form.validate():
        validation_errors = validation_errors_to_dict(form.errors)
    if validation_errors:
        return jsonify(detail=validation_errors), HTTPStatus.UNPROCESSABLE_ENTITY

    get_movies_list = GetMoviesList(resources)
    movies = get_movies_list()

    return jsonify([m.to_dict() for m in movies])


@app.route("/api/movies/<movie_id>", methods=["GET"])
def movie_details(movie_id: str) -> Dict[str, Any]:
    # Получает данные из ES об одном фильме
    get_movie_by_id = GetMovieDetail(resources)
    movie = get_movie_by_id(movie_id=movie_id)
    if movie is None:
        abort(HTTPStatus.NOT_FOUND)
    return movie.to_dict()
