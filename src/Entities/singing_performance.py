from src.Entities.cultural_number import *
from src.Services.web_rating import *
from src.Services.compatibilty import *

class singing_performance(Cultural):
    def __init__(self, number_id: int, number_name: str, time: int, number_type: str, artists: set[tuple[str, int]],
                 song_name: str, gender: str, composed: bool):
        super().__init__(number_id, number_name, time, number_type, artists)
        self.song_name = song_name
        self.gender = gender
        self.composed = composed

    def calculate_rating(self, show_type: str):
        population_rating = 0
        if self.composed:
            population_rating += self.composed_rating()
        else:
            population_rating += web_rating(self.song_name)
        compatibility = get_compatibility_gender_show_type(self.gender, show_type)
        return population_rating + compatibility

    def composed_rating(self):
        population_rating = 0
        for artist, population in self.artists:
            population_rating += population
        return population_rating / len(self.artists)