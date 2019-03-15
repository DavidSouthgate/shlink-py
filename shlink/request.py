import requests
from typing import Dict
from json.decoder import JSONDecodeError
from requests import Response, ConnectionError


class Request:

    @staticmethod
    def get(url: str, api_key: str, path: str, headers: Dict[str, str] = None) -> Dict:
        if headers is None:
            headers = {}
        headers["X-Api-Key"] = api_key
        try:
            response = requests.get(url + path, headers=headers)
        except ConnectionError as e:
            return {
                "error": "CONNECTION_ERROR",
                "message": e.__str__()
            }
        return Request._response_to_json(response)

    @staticmethod
    def post(url: str, api_key: str, path: str, data: Dict = None, headers: Dict = None) -> Dict:
        if data is None:
            data = {}
        if headers is None:
            headers = {}
        headers["X-Api-Key"] = api_key
        response = requests.post(url + path, data=data, headers=headers)
        return Request._response_to_json(response)

    @staticmethod
    def _response_to_json(response: 'Response') -> Dict:
        try:
            return response.json()
        except JSONDecodeError:
            if response.status_code == 500:
                return {
                    "error": "RESPONSE_500",
                    "message": "Error 500 was returned. Were all of the parameters given valid?"
                }

            return {
                "error": "RESPONSE_INVALID",
                "message": "API response was invalid. Is the server URL correct and up?"
            }