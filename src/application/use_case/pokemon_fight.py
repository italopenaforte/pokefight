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
            winner = self._select_winner(battle.pokemon_a, battle.pokemon_b)
            battle.winner = winner
            battle.fought = True
        return True

    def _select_winner(self, pokemon_a: Pokemon, pokemon_b: Pokemon):
        contestends = [pokemon_a, pokemon_b]
        winner = randint(0, len(contestends) - 1)
        return contestends[winner]
