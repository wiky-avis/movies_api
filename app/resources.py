from dataclasses import dataclass
from elasticsearch import Elasticsearch
from typing import Optional

from app.const import SortOrder, SortField


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
