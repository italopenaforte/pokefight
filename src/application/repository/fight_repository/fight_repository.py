from dataclasses import dataclass

from src.domain.fight import Fight


@dataclass(kw_only=True)
class FightCreated(Fight):
    id: int


class FightRepository:
    def __init__(self):
        self.__database: [dict] = []

    def create(self, fight: Fight):
        fight = FightCreated(
            winner=fight.winner,
            fought=fight.fought,
            pokemon_a=fight.pokemon_a,
            pokemon_b=fight.pokemon_b,
            id=self._calculate_id(),
        )
        self.__database.append(fight)
        return fight

    def search_battle_not_started(self):
        return [battle for battle in self.__database if battle.fought is False]

    def _calculate_id(self):
        total_itens = len(self.__database)
        if total_itens != 0:
            last_item = self.__database[-1]
            return last_item.id + 1
        return 1
