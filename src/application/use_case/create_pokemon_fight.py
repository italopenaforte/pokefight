from src.application.factory.pokemon_factory import pokemon_factory


class CreatePokemonFight:

    def execute(self, pokemon_a: str, pokemon_b: str):
        pokemon_a = pokemon_factory(pokemon_a)
        pokemon_b = pokemon_factory(pokemon_b)

        return True