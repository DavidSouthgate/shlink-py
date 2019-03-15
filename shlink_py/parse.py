from datetime import datetime
from typing import Optional


class Parse:

    @staticmethod
    def datetime(s: str) -> Optional[datetime]:
        if s is None:
            return None
        s = s[:22] + s[23:]
        return datetime.strptime(s, '%Y-%m-%dT%H:%M:%S%z')
