from flask import Blueprint

from app.api.v1.handlers.movies import MovieDetailApi, MovieListApi

bp = Blueprint(name="movies_service_v1", import_name="movies_service", url_prefix="/api/v1")


bp.add_url_rule(rule="/movies", view_func=MovieListApi.as_view("movies_list"), endpoint="movies_list")
bp.add_url_rule(
    rule="/movies/<movie_id>", view_func=MovieDetailApi.as_view("movie_detail"), endpoint="movies_detail"
)
