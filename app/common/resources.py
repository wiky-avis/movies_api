from dataclasses import dataclass
from typing import Optional

from elasticsearch import Elasticsearch

from app.common.constants.sort_movies import SortField, SortOrder


@dataclass
class Search:
    search_query: Optional[str] = None
    sort_order: SortOrder = SortOrder.ASC
    sort: SortField = SortField.ID
    page: int = 1
    limit: int = 50


@dataclass
class Resources:
    es_client: Optional[Elasticsearch] = None
    search: Optional[Search] = None
