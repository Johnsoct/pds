# Packages
from dataclasses import dataclass

@dataclass(frozen=True)
class Constants:
    FREQUENCIES: tuple[str, ...] = ("bi-monthly", "bi-weekly", "monthly", "weekly", "yearly")
    DISALLOWED_DANGEROUS_CHARACTERS: tuple[str, ...] = (";", "&&", "||", "|", "(", ")", "`", ">", ">>", "<", "*", "?", "~", "$", ",", "%")
