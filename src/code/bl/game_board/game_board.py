from code.bl.entities.entity import Entity
from code.bl.entities.player.player import Player
from code.bl.excpetions.game_board_excpetions import EntityNotFoundException
from code.bl.tiles.abstract.tile_base import TileBase
from code.bl.util.move import Move
from code.bl.util.point import Point


class GameBoard:
    def __init__(self, board: dict[Point, TileBase]) -> None:
        self.board = board

    def move_entity(self, entity: Entity, move: Move) -> None:
        current_entity_point = self._get_entity_point(entity)
        self.board[current_entity_point].on_tile_entity = None
        new_entity_point = self.board[current_entity_point].get_point_after_move(current_entity_point, move)
        self.board[new_entity_point].on_tile_entity = entity

    def _get_entity_point(self, entity: Entity) -> Point:
        for point in self.board.keys():
            if self.board[point].on_tile_entity == entity:
                return point
        raise EntityNotFoundException("Entity not found")












