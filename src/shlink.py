import requests
from typing import Dict, List, Any
from .data import PagedData
from .data import ShortUrl
from urllib.parse import quote


class Shlink:
    _api_key: str = None
    _url: str = None

    def __init__(self, api_key: str, url: str) -> None:
        self._api_key = api_key
        self._url = url

    def _get(self, path: str, headers: Dict[str, str] = None) -> Dict:
        if headers is None:
            headers = {}
        headers["X-Api-Key"] = self._api_key
        return requests.get(self._url + path, headers=headers).json()

    def _post(self, path: str, data: Dict = None, headers: Dict = None) -> Dict:
        if data is None:
            data = {}
        if headers is None:
            headers = {}
        headers["X-Api-Key"] = self._api_key
        return requests.post(self._url + path, data=data, headers=headers).json()

    @staticmethod
    def _data_param(data: Dict[str, Any], key: str, value: Any):
        if value is not None:
            data[key] = value

    def list_short_urls(self) -> PagedData:
        """
        List all of the short URLs
        :return:
        """
        json = self._get("/rest/v1/short-urls")
        return PagedData.parse(
            json["shortUrls"],
            lambda x: ShortUrl.parse(x)
        )

    def add_short_url(self, long_url: str, tags: List[str] = None, valid_since: str = None, valid_until: str = None,
                      custom_slug: str = None, max_visits: int = None, find_if_exists: bool = None):
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
        self._data_param(data, "validSince", valid_since)
        self._data_param(data, "validUntil", valid_until)
        self._data_param(data, "customSlug", custom_slug)
        self._data_param(data, "maxVisits", max_visits)
        self._data_param(data, "findIfExists", find_if_exists)

        return ShortUrl.parse(self._post("/rest/v1/short-urls", data))

    def get_short_url(self, short_code: str):
        return ShortUrl.parse(self._get("/rest/v1/short-urls/" + quote(short_code)))
