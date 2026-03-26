from code.bl.events.abstract.fight_end_listener_base import FightEndListenerBase
from code.bl.events.abstract.entity_dealt_damage_listener_base import EntityDealtDamageListenerBase
from code.bl.events.abstract.map_change_listener_base import MapChangeListener
from code.bl.events.abstract.player_turn_in_fight_listener_base import PlayerTurnInFightListenerBase
from code.bl.events.abstract.player_turn_listener_base import PlayerTurnListenerBase


class EventManager:
    def __init__(self):
        self.map_change_listeners: list[MapChangeListener] = []
        self.player_turn_in_fight_listeners: list[PlayerTurnInFightListenerBase] = []
        self.entity_dealt_damage_listeners: list[EntityDealtDamageListenerBase] = []
        self.fight_end_listeners: list[FightEndListenerBase] = []
        self.player_turn_listeners: list[PlayerTurnListenerBase] = []

    def notify_map_change(self, game_board: GameBoard) -> None:
        for listener in self.map_change_listeners:
            listener.on_map_change(game_board)

    def notify_player_turn_in_fight(self, fight: Fight) -> None:
        for listener in self.player_turn_in_fight_listeners:
            listener.on_player_turn_in_fight(fight)

    def notify_entity_dealt_damage(self, fight: Fight) -> None:
        for listener in self.entity_dealt_damage_listeners:
            listener.on_entity_dealt_damage(fight)

    def notify_fight_end(self, fight: Fight) -> None:
        for listener in self.fight_end_listeners:
            listener.on_fight_end(fight)

    def notify_player_turn(self) -> None:
        for listener in self.player_turn_listeners:
            listener.on_player_turn()