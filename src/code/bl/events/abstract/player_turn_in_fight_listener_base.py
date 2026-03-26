from abc import ABC, abstractmethod


class PlayerTurnInFightListenerBase(ABC):
    @abstractmethod
    def on_player_turn_in_fight(self, fight: Fight) -> None:
        raise NotImplementedError