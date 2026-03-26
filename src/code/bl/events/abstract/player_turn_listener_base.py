from abc import ABC, abstractmethod


class PlayerTurnListenerBase(ABC):
    @abstractmethod
    def on_player_turn(self):
        raise NotImplementedError
