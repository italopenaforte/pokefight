from random import randint

from src.pokemon.pokemon import Pokemon


def lets_fight(pokemon_a: Pokemon, pokemon_b: Pokemon):
    contestants = [pokemon_a, pokemon_b]
    winner = randint(0, len(contestants) - 1)
    return contestants[winner]
