from abc import ABC, abstractmethod
class Cultural(ABC):
    def __init__(self, number_id: int, number_name: str, time: int, number_type: str, artists: set[tuple[str, int]]):
        self.number_id = number_id
        self.time = time
        self.artists = artists
        self.type = number_type
        self.number_name = number_name

    @abstractmethod
    def calculate_rating(self, show_type: str):
        pass

    # Valor esperado del Numero (Subjetivo)