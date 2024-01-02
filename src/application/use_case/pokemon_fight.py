from random import randint

from src.application.repository.fight_repository.fight_repository import \
    FightRepository
from src.domain.pokemon import Pokemon


class PokemonFight:
    def __init__(self, fight_repository: FightRepository):
        self._fight_repository = fight_repository

    def execute(
        self,
    ):
        battles = self._fight_repository.search_battle_not_started()

        for battle in battles:
            winner = self._select_winner(battle.get("first"), battle.get("second"))
            battle["winner"] = winner.get("name")
        return battles

    def _select_winner(self, pokemon_a, pokemon_b):
        contestends = [pokemon_a, pokemon_b]
        winner = randint(0, len(contestends) - 1)
        return contestends[winner]
