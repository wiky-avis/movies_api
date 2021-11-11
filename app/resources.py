from dataclasses import dataclass
from typing import Optional

from elasticsearch import Elasticsearch

from app.const import SortField, SortOrder


@dataclass
class Search:
    search_query: Optional[str] = None
    sort_order: SortOrder = SortOrder.ASC
    sort: SortField = SortField.ID
    page: int = 1
    limit: int = 50


@dataclass
class Resources:
    es_client: Optional[Elasticsearch] = Elasticsearch()
    search: Optional[Search] = Search
