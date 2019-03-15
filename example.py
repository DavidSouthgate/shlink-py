import json
import sys
from datetime import datetime
from shlink import Shlink
from shlink.data import Error

shlink = Shlink(
    url="https://example.com/",
    api_key="000000000-0000-0000-0000-000000000000"
)

# LIST_SHORT_URLS
result = shlink.list_short_urls()
print(json.dumps(result.to_dict()))
if isinstance(result, Error):
    sys.exit(1)

# ADD_SHORT_URL
result = shlink.add_short_url(
    long_url="http://example.com/",
    tags=[
        "example"
    ],
    valid_since=datetime(2019, 3, 14),
    valid_until=datetime(2019, 3, 20),
    custom_slug="example",
    max_visits=100,
    find_if_exists=False
)
print(json.dumps(result.to_dict()))
if isinstance(result, Error):
    sys.exit(2)

# GET_SHORT_URL
result = shlink.get_short_url("example")
print(json.dumps(result.to_dict()))
if isinstance(result, Error):
    sys.exit(3)

