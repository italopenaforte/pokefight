from src.domain.pokemon import Pokemon

def pokemon_factory(name: str):
    return Pokemon(name=name, base_experience=60)