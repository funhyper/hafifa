from abc import ABC, abstractmethod

from code.bl.game_board.game_board import GameBoard


class BoardProviderBase(ABC):
    @abstractmethod
    def get_board(self) -> GameBoard:
        raise NotImplementedError