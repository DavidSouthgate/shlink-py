from .shlink import Shlink
import os
import json


def main():

    # Load URL and API Key from file
    with open(os.path.dirname(os.path.realpath(__file__)) + "/../config", 'r') as file:
        data = file.read()
    pos = data.index(",")
    url = data[:pos]
    api_key = data[pos+1:]

    shlink = Shlink(
        url=url,
        api_key=api_key
    )

    result = shlink.list_short_urls()
    print(json.dumps(result.to_dict(), indent=4))


if __name__ == "__main__":
    main()
