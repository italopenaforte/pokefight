from dataclasses import asdict, dataclass
from typing import Optional

from src.domain.pokemon import Pokemon


@dataclass
class Fight:
    pokemon_a: Pokemon
    pokemon_b: Pokemon
    fought: bool = False
    winner: Optional[Pokemon] = None

    dict = asdict
