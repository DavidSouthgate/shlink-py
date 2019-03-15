from typing import Any, Dict, Callable, List, Union
from ..data import Data
from ..data.pagination import Pagination
from ..data.error import Error


class PagedData(Data):
    data: List[Any] = None
    pagination: Pagination = None

    def __init__(self, data: Any = None, pagination: Pagination = None):
        if data is None:
            data = []
        self.data = data
        self.pagination = pagination

    def to_dict(self):
        data = []
        for d in self.data:
            data.append(d.to_dict())
        return {
            "data": data,
            "pagination": self.pagination.to_dict()
        }

    @staticmethod
    def parse(json: Dict, data_parse: Callable[[Dict], Data] = lambda x: Data()) -> Union['PagedData', 'Error']:
        if "error" in json:
            return Error.parse(json)
        data = []
        for d in json["shortUrls"]["data"]:
            data.append(data_parse(d))
        return PagedData(
            data=data,
            pagination=Pagination.parse(json["shortUrls"]["pagination"])
        )
