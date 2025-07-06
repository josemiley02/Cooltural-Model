from Entities.cultural_number import *
from Services.web_rating import *
from Services.compatibilty import *

class dancing_performance(Cultural):
    def __init__(self, number_id: int, number_name:str, time: int, number_type: str, artists: set[tuple[str, int]],
                 songs: set[str], styles: set[str], count_dancers=0):
        super().__init__(number_id, number_name, time, number_type, artists)
        self.songs = songs
        self.styles = styles
        self.count_dancers = count_dancers

    def calculate_rating(self, show_type: str):
        population_rating = self.calculate_population_songs()
        compatibility_rating = self.calculate_compatibility(show_type)
        time_person_rating = self.time_person_rating()
        return population_rating + compatibility_rating + time_person_rating

    def calculate_population_songs(self):
        web = 0
        for song in self.songs:
            web += web_rating(song)
        return web / len(self.songs)

    def calculate_compatibility(self, show_type: str):
        compatibility = 0
        for style in self.styles:
            compatibility += get_compatibility_style_show_type(style, show_type)
        return compatibility / len(self.styles)

    ## Cambiar a una Normal
    ## Probar Interpolacion en 2 variable
    def time_person_rating(self):
        return self.time * len(self.songs) / max(self.count_dancers, len(self.artists))