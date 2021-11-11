from wtforms import Form, IntegerField, SelectField, StringField
from wtforms.validators import NumberRange

from app.common.constants.sort_movies import SortField, SortOrder


class SearchMoviesForm(Form):
    limit = IntegerField("limit", [NumberRange(min=0)], default=50)
    page = IntegerField("page", [NumberRange(min=1)], default=1)
    search = StringField("search", default="")
    sort = SelectField(
        "sort",
        choices=[
            (SortField.ID.value, SortField.ID.value),
            (SortField.TITLE.value, SortField.TITLE.value),
            (SortField.IMDB_RATING.value, SortField.IMDB_RATING.value),
        ],
        default=SortField.ID.value,
    )
    sort_order = SelectField(
        "sort_order",
        choices=[
            (SortOrder.ASC.value, SortOrder.ASC.value),
            (SortOrder.DESC.value, SortOrder.DESC.value),
        ],
        default=SortOrder.ASC.value,
    )
