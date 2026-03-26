from abc import ABC, abstractmethod


class MapChangeListener(ABC):
    @abstractmethod
    def on_map_change(self, game_board: GameBoard) -> None:
        raise NotImplementedError
