from pprint import pprint

from fastapi import FastAPI
from pydantic import BaseModel

from src.application.repository.fight_repository.fight_repository import (
    FightCreated, FightRepository)
from src.application.use_case.create_pokemon_fight import (CreatePokemonFight,
                                                           Input)
from src.application.use_case.pokemon_fight import PokemonFight

app = FastAPI()


class Fight(BaseModel):
    pokemon_a: str
    pokemon_b: str


fight_repository = FightRepository()


@app.post("/pokemon/fight")
def create_pokemon_fight(fight: Fight):
    create_pokemon_fight_use_case = CreatePokemonFight(fight_repository)
    return create_pokemon_fight_use_case.execute(
        input=Input(fight.pokemon_a, fight.pokemon_b)
    )


@app.get("/pokemon/fight")
def pokemon_fight():
    pokemon_fight_use_case = PokemonFight(fight_repository)
    return pokemon_fight_use_case.execute()
