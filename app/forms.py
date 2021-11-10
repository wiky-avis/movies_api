from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, StringField
from wtforms.validators import NumberRange
from app.const import SortOrder, SortField


class SearchMoviesForm(FlaskForm):
    limit = IntegerField("limit", [NumberRange(min=0)], default=50)
    page = IntegerField("page", [NumberRange(min=1)], default=1)
    search = StringField("search", default="")
    sort = SelectField(
        "sort",
        choices=[
            ("id", SortField.ID),
            ("title", SortField.TITLE),
            ("imdb_rating", SortField.IMDB_RATING)
        ],
        default=SortField.ID
    )
    sort_order = SelectField(
        "sort_order",
        choices=[
            ("asc", SortOrder.ASC),
            ("desc", SortOrder.DESC)
        ],
        default=SortOrder.ASC
    )
