import requests

from src.application.factory.erros import PokemonNotFound


def pokemon_factory(name: str):
    response = requests.get(url=f"https://pokeapi.co/api/v2/pokemon/{name}", timeout=3)

    if response.status_code == 200:
        payload = response.json()
        return {"name": name, "base_experience": payload.get("base_experience")}
    raise PokemonNotFound()
