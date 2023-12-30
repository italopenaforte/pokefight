import requests

from src.pokemon.pokemon import Pokemon


def factory_pokemon(name: str) -> Pokemon:
    response = requests.get(url=f"https://pokeapi.co/api/v2/pokemon/{name}", timeout=1)
    if response.ok:
        payload_pokemon = response.json()
        return Pokemon(
            name=name, base_experience=payload_pokemon.get("base_experience")
        )
