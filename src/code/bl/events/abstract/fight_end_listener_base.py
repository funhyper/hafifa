from abc import ABC, abstractmethod


class FightEndListenerBase(ABC):
    @abstractmethod
    def on_fight_end(self, fight: Fight) -> None:
        raise NotImplementedError