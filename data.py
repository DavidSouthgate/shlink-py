from typing import Dict


class Data:

    def to_dict(self) -> Dict:
        return {}

    @staticmethod
    def parse(json: Dict) -> 'Data':
        return Data()
