from elasticsearch import Elasticsearch
from flask.views import MethodView

from app.common.resources import Resources, Search


class ResourcesMixin:
    @property
    def resources(self) -> Resources:
        return Resources(
            es_client=Elasticsearch(),
            search=Search
        )


class MovieHandler(ResourcesMixin, MethodView):
    pass
