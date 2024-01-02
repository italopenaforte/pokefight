class PokemonNotFound(Exception):
    def __init__(
        self,
    ):
        super().__init__("Pokemon Not Found")
