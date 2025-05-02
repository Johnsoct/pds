# Packages
from dataclasses import dataclass

@dataclass(frozen=True)
class Constants:
    FREQUENCIES: tuple[str, ...] = ("bi-monthly", "bi-weekly", "monthly", "weekly", "yearly")
    NUMERICAL_CHARACTERS: tuple[str, ...] = ("$", ",")
