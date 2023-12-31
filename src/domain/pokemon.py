from dataclasses import asdict, dataclass


@dataclass
class Pokemon:
    name: str
    base_experience: int

    dict = asdict
