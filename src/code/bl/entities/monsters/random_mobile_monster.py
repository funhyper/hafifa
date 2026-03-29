from code.bl.entities.abstract.movable_monster_base import MovableMonsterBase
from code.bl.entities.monsters.regular_monster import RegularMonster
from code.bl.util.move import Move
from code.bl.util.point import Point
from code.bl.util.random_provider import RandomProvider


class RandomMobileMonster(RegularMonster, MovableMonsterBase):
    def __init__(self, attack_damage: int, random_provider: RandomProvider, health: int = 100):
        super().__init__(attack_damage, health)
        self.random_provider = random_provider

    def get_next_move(self, current_location: Point) -> Move:
        return self.random_provider.get_random_move()