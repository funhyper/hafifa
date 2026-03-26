import random


class RandomProvider:
    def get_random_number(self, start: int, end: int) -> int:
        return random.randint(start, end)