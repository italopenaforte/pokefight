from src.use_cases.create_pokemon_battle import CreatePokemonBattle

if __name__ == "__main__":
    use_case = CreatePokemonBattle()
    use_case.execute(pokemon_a="ditto", pokemon_b="pikachu")
