from typing import Dict, List, Any
from datetime import datetime
from urllib.parse import quote
from .data import PagedData
from .data import ShortUrl
from .request import Request


class Shlink:
    _api_key: str = None
    _url: str = None

    def __init__(self, api_key: str, url: str) -> None:
        self._api_key = api_key
        self._url = url.rstrip("/")

    def list_short_urls(self) -> PagedData:
        """
        List all of the short URLs
        :return:
        """
        return PagedData.parse(self._get("/rest/v1/short-urls"), lambda x: ShortUrl.parse(x))

    def add_short_url(self, long_url: str, tags: List[str] = None, valid_since: datetime = None,
                      valid_until: datetime = None, custom_slug: str = None, max_visits: int = None,
                      find_if_exists: bool = None):
        """
        Add a short URL
        :param long_url:
        :param tags:
        :param valid_since:
        :param valid_until:
        :param custom_slug:
        :param max_visits:
        :param find_if_exists:
        :return:
        """
        data = {}
        self._data_param(data, "longUrl", long_url)
        self._data_param(data, "tags", tags)
        self._data_param(data, "validSince", str(valid_since))
        self._data_param(data, "validUntil", str(valid_until))
        self._data_param(data, "customSlug", custom_slug)
        self._data_param(data, "maxVisits", max_visits)
        self._data_param(data, "findIfExists", find_if_exists)
        return ShortUrl.parse(self._post("/rest/v1/short-urls", data))

    def get_short_url(self, short_code: str):
        return ShortUrl.parse(self._get("/rest/v1/short-urls/" + quote(short_code)))

    ################

    def _get(self, path: str, headers: Dict[str, str] = None) -> Dict:
        return Request.get(url=self._url, api_key=self._api_key, path=path, headers=headers)

    def _post(self, path: str, data: Dict = None, headers: Dict = None) -> Dict:
        return Request.post(url=self._url, api_key=self._api_key, path=path, data=data, headers=headers)

    @staticmethod
    def _data_param(data: Dict[str, Any], key: str, value: Any):
        if value is not None:
            data[key] = value
