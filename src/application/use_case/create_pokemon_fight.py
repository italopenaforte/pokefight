from dataclasses import dataclass

from src.application.factory.pokemon_factory import pokemon_factory
from src.application.repository.fight_repository.fight_repository import \
    FightRepository
from src.domain.fight import Fight


@dataclass
class Input:
    pokemon_a: str
    pokemon_b: str


class CreatePokemonFight:
    def __init__(self, fight_repository: FightRepository):
        self._fight_repository = fight_repository

    def execute(self, first, second):
        pokemon_a = pokemon_factory(first)
        pokemon_b = pokemon_factory(second)
        fight = {"first": pokemon_a, "second": pokemon_b}
        return self._fight_repository.create(fight)
