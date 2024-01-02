class PokemonNotFound(Exception):
    def __init__(
        self,
    ):
        self.super("Pokemon Not Found")
