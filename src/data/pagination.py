from typing import Dict
from ..data import Data


class Pagination(Data):
    current_page: int
    pages_count: int
    items_per_page: int
    items_in_current_page: int
    total_items: int

    def __init__(self, current_page: int, pages_count: int, items_per_page: int, items_in_current_page: int,
                 total_items: int):
        self.current_page = current_page
        self.pages_count = pages_count
        self.items_per_page = items_per_page
        self.items_in_current_page = items_in_current_page
        self.total_items = total_items

    def to_dict(self):
        return {
            "current_page": self.current_page,
            "pages_count": self.pages_count,
            "items_per_page": self.items_per_page,
            "items_in_current_page": self.items_in_current_page,
            "total_items": self.total_items,
        }

    @staticmethod
    def parse(json: Dict) -> 'Pagination':
        current_page = None if "currentPage" not in json else json["currentPage"]
        pages_count = None if "pagesCount" not in json else json["pagesCount"]
        items_per_page = None if "itemsPerPage" not in json else json["itemsPerPage"]
        items_in_current_page = None if "itemsInCurrentPage" not in json else json["itemsInCurrentPage"]
        total_items = None if "totalItems" not in json else json["totalItems"]

        return Pagination(
            current_page=current_page,
            pages_count=pages_count,
            items_per_page=items_per_page,
            items_in_current_page=items_in_current_page,
            total_items=total_items
        )
