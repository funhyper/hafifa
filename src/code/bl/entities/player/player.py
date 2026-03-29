from code.bl.entities.entity import Entity


class Player(Entity):
    def __init__(self, health: int = 100) -> None:
        super().__init__(health)
        self.kills = 0
