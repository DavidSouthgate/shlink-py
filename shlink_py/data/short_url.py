from datetime import datetime
from typing import List, Optional, Dict, Union
from ..parse import Parse
from ..data import Data
from ..data.error import Error


class ShortUrl(Data):
    short_code: Optional[str] = None
    short_url: Optional[str] = None
    long_url: Optional[str] = None
    date_created: Optional[datetime] = None
    visits_count: Optional[str] = None
    tags: List[str] = None
    original_url: Optional[str] = None

    def __init__(self, short_code: Optional[str] = None, short_url: Optional[str] = None,
                 long_url: Optional[str] = None, date_created: Optional[datetime] = None,
                 visits_count: Optional[str] = None, tags: List[str] = None, original_url: Optional[str] = None
                 ) -> None:
        super().__init__()
        if tags is None:
            tags = []
        self.short_code = short_code
        self.short_url = short_url
        self.long_url = long_url
        self.date_created = date_created
        self.visits_count = visits_count
        self.tags = tags
        self.original_url = original_url

    def to_dict(self):
        date_created = None
        if self.date_created is not None:
            date_created = str(self.date_created)
        return {
            "short_code": self.short_code,
            "short_url": self.short_url,
            "long_url": self.long_url,
            "date_created": date_created,
            "visits_count": self.visits_count,
            "tags": self.tags,
            "original_url": self.original_url,
        }

    @staticmethod
    def parse(json: Dict) -> Union['Error', 'ShortUrl']:
        if "error" in json:
            return Error.parse(json)

        short_code = None if "shortCode" not in json else json["shortCode"]
        short_url = None if "shortUrl" not in json else json["shortUrl"]
        long_url = None if "longUrl" not in json else json["longUrl"]
        date_created = None if "dateCreated" not in json else json["dateCreated"]
        visits_count = None if "visitsCount" not in json else json["visitsCount"]
        tags = [] if "tags" not in json else json["tags"]
        original_url = None if "originalUrl" not in json else json["originalUrl"]
        date_created = Parse.datetime(date_created)

        return ShortUrl(
            short_code=short_code,
            short_url=short_url,
            long_url=long_url,
            date_created=date_created,
            visits_count=visits_count,
            tags=tags,
            original_url=original_url
        )
