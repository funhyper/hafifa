from abc import ABC, abstractmethod

from code.bl.tiles.abstract.tile_base import TileBase


class TileFactoryBase(ABC):
    @abstractmethod
    def get_tile(self) -> TileBase:
        raise NotImplementedError()