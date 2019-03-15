from typing import Dict
from ..data import Data


class Error(Data):
    code: str
    message: str

    def __init__(self, code: str, message: str):
        self.code = code
        self.message = message

    def to_dict(self) -> Dict:
        return {
            "code": self.code,
            "message": self.message
        }

    @staticmethod
    def parse(json: Dict) -> 'Error':
        code = None if "error" not in json else json["error"]
        message = None if "message" not in json else json["message"]

        return Error(code=code, message=message)
