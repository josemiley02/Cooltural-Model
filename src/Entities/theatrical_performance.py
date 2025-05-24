from src.Entities.cultural_number import *
from src.Services.compatibilty import *
class theatrical_performance(Cultural):
    def __init__(self, number_id: int, number_name: str, time: int, number_type: str, artists: set[tuple[str, int]],
                 type_performance: str, genders: set[str]):
        super().__init__(number_id, number_name, time, number_type, artists)
        self.type_performance = type_performance
        self.genders = genders

    def calculate_rating(self, show_type: str):
        comp_gender = self.calculate_compatibility_gender(show_type)
        comp_type = self.calculate_compatibility_theatrical_type(show_type)
        return comp_type + comp_gender

    def calculate_compatibility_gender(self, show_type):
        comp_gender = 0
        for gender in self.genders:
            comp_gender += get_compatibility_theatrical_gender(gender, show_type)
        return comp_gender / len(self.genders)

    def calculate_compatibility_theatrical_type(self, show_type):
        return get_compatibility_type_theatric(self.type_performance, show_type)