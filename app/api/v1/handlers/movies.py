from http import HTTPStatus
from typing import Any, Dict, List

from flask import abort, jsonify, request

from app.api.base.handler import MovieHandler
from app.api.v1.forms.search_movies import SearchMoviesForm
from app.common.actions.movies import GetMovieDetail, GetMoviesList
from app.common.validators.validation_errors import validation_errors_to_dict


class MovieListApi(MovieHandler):
    def get(self) -> List[dict]:
        """
        Получает данные из ES об отфильтрованном по request.args списке фильмов
        """
        form = SearchMoviesForm(request.args)
        validation_errors = []
        if not form.validate():
            validation_errors = validation_errors_to_dict(form.errors)
        if validation_errors:
            return (
                jsonify(detail=validation_errors),
                HTTPStatus.UNPROCESSABLE_ENTITY,
            )

        get_movies_list = GetMoviesList(self.resources)
        movies = get_movies_list()

        return jsonify([m.to_dict() for m in movies])


class MovieDetailApi(MovieHandler):
    def get(self, movie_id: str) -> Dict[str, Any]:
        """
        Получает данные из ES об одном фильме
        """
        get_movie_by_id = GetMovieDetail(self.resources)
        movie = get_movie_by_id(movie_id=movie_id)
        if movie is None:
            abort(HTTPStatus.NOT_FOUND)
        return movie.to_dict()
