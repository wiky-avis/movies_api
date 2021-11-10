from flask import jsonify, request
from app import app


@app.route('/api/movies/<movie_id>', methods=['GET'])
def movie_details(movie_id: str) -> str:
    # Код, получающий данные из ES об одном фильме
    result = {}
    return jsonify(result)


@app.route('/api/movies', methods=['GET'], strict_slashes=False)
def movies_list() -> str:
    # Код, получающий данные из ES об отфильтрованном по request.args спискефильмов
    result = {}
    return jsonify(result)
