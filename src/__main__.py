from pprint import pprint

from src.application.repository.fight_repository.fight_repository import \
    FightRepository
from src.application.use_case.create_pokemon_fight import (CreatePokemonFight,
                                                           Input)
from src.application.use_case.pokemon_fight import PokemonFight

if __name__ == "__main__":
    fight_repository = FightRepository()

    create_pokemon_fight_use_case = CreatePokemonFight(fight_repository)
    pokemon_fight_use_case = PokemonFight(fight_repository)

    pprint(create_pokemon_fight_use_case.execute(input=Input("ditto", "pikachu")))
    pprint(create_pokemon_fight_use_case.execute(input=Input("ditto", "pikachu")))

    pprint(pokemon_fight_use_case.execute())
