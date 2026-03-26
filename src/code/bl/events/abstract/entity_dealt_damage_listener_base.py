from abc import ABC, abstractmethod


class EntityDealtDamageListenerBase(ABC):
    @abstractmethod
    def on_entity_dealt_damage(self, fight: Fight) -> None:
        raise NotImplementedError
