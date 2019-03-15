from abc import ABC, abstractmethod
from typing import Dict


class Data(ABC):

    @abstractmethod
    def to_dict(self) -> Dict:
        pass

    @staticmethod
    @abstractmethod
    def parse(json: Dict) -> 'Data':
        pass
