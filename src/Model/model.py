import numpy as np
from numpy import random
import random as rd
from Entities.cultural_number import *
from typing import List, Tuple
class Model:
    def __init__(self, cultural_numbers : List[Cultural], max_time: int,
                 min_count_numbers: int, max_count_numbers: int, show_type: str):
        self.cultural_numbers = cultural_numbers
        self.max_time = max_time
        self.min_count_numbers = min_count_numbers
        self.max_count_numbers = max_count_numbers
        self.show_type = show_type

        self.ratings = []
        self.best_solution = []
        self.best_score = 0

    def fill_ratings(self):
        for cultural in self.cultural_numbers:
            self.ratings.append(cultural.calculate_rating(self.show_type))

    def type_time_relationship(self, current_solution: List[Cultural], current_number: Cultural) -> int:
        if current_solution:
            time_rating = 0
            for i in range(len(current_solution)):
                if current_solution[i].type == current_number.type:
                    time_rating = i
            return time_rating
        return 0

    def artist_time_relationship(self, current_solution: List[Cultural], current_number: Cultural) -> int:
        if current_solution:
            time_rating = 0
            for i in range(len(current_solution)):
                inter = len(current_solution[i].artists.intersection(current_number.artists))
                if inter > 0:
                    time_rating = i
            return time_rating
        return 0

    def get_init_population(self, population_size: int) -> Tuple[List[float], List[List[Cultural]]]:
        scores = []
        population = []
        while population_size > 0:
            solution_size = np.random.randint(self.min_count_numbers, self.max_count_numbers)
            remaining_time = self.max_time
            available_numbers = self.cultural_numbers.copy()
            solution = []
            score = 0
            while len(solution) < solution_size:
                if not available_numbers:
                    break
                np.random.shuffle(available_numbers)
                candidate = available_numbers.pop()
                if candidate.time <= remaining_time:
                    remaining_time -= candidate.time
                    type_pen = self.type_time_relationship(solution, candidate)
                    artist_pen = self.artist_time_relationship(solution, candidate)
                    score = score + self.ratings[candidate.number_id] - type_pen - artist_pen
                    solution.append(candidate)
            if  len(solution) >= self.min_count_numbers:
                population.append(solution)
                scores.append(score)
            population_size -= 1
        return scores, population

    def tournament(self, population: List[List[Cultural]], scores: List[float]):
        size = len(population) // 2
        while size > 0:
            i = np.random.randint(0, len(population) - 1)
            j = np.random.randint(0, len(population) - 1)
            while i == j:
                j = np.random.randint(0, len(population) - 1)
            if scores[i] > scores[j]:
                remove_index = j
            else:
                remove_index = i
            scores.pop(remove_index)
            population.pop(remove_index)
            size -= 1

    def crossover(self, parent1: List[Cultural], parent2: List[Cultural]) -> List[Cultural]:
        midpoint1 = np.random.randint(0, len(parent1) - 1)
        midpoint2 = np.random.randint(0, len(parent2) - 1)
        segment1 = parent1[:midpoint1]
        segment2 = parent2[midpoint2:]
        offspring = segment1 + segment2

        unique_offspring = list({cultural.number_id: cultural for cultural in offspring}.values())
        total_time = sum(cultural.time for cultural in unique_offspring)
        while total_time > self.max_time:
            removed = unique_offspring.pop()
            total_time -= removed.time

        while len(unique_offspring) < self.min_count_numbers:
            extra = np.random.choice(self.cultural_numbers)
            if total_time + extra.time <= self.max_time:
                unique_offspring.append(extra)
                total_time += extra.time

        return unique_offspring

    def merge(self, population: List[List[Cultural]]) -> List[List[Cultural]]:
        new_population = []
        while len(population) > 1:
            list_one = population.pop(0)
            list_last = population.pop()
            new_population.append(self.crossover(list_one, list_last))
        if population:
            new_population.append(population.pop())
        return new_population

    def mutate(self, population: List[List[Cultural]], mutation_rate=0.2):
        for solution in population:
            if rd.random() < mutation_rate:
                idx1, idx2 = rd.sample(range(len(solution)), 2)
                solution[idx1], solution[idx2] = solution[idx2], solution[idx1]
        return population

    def evaluate(self, population: List[List[Cultural]]):
        for number_list in population:
            score = 0
            for i in range(len(number_list)):
                time_pen = self.type_time_relationship(number_list[:i], number_list[i])
                artist_pen = self.artist_time_relationship(number_list[:i], number_list[i])
                score = score + self.ratings[number_list[i].number_id] - time_pen - artist_pen
            if score > self.best_score:
                self.best_score = score
                self.best_solution = number_list


    def get_show(self, count_gen = 2) -> List[Cultural]:
        self.fill_ratings()
        scores, population = self.get_init_population(random.randint(50,100))
        while count_gen > 0:
            self.tournament(population, scores)
            merge = self.merge(population)
            self.mutate(merge)
            self.evaluate(merge)
            count_gen -= 1
        return self.best_solution, max(scores)