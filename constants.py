# Packages
import re
from dataclasses import dataclass

# SINGLETON - import C
@dataclass(frozen=True)
class Constants:
    CONFIRMATIONS: tuple[str, ...] = ("y", "yes", "n", "no")
    FREQUENCIES: tuple[str, ...] = ("bi-monthly", "bi-weekly", "monthly", "weekly", "yearly")
    DISALLOWED_DANGEROUS_CHARACTERS: tuple[str, ...] = (";", "&&", "||", "|", "(", ")", "`", ">", ">>", "<", "*", "?", "~", "$", ",", "%")

    def get_disallowed_dangerous_characters_regex(self):
        return f"[{''.join(re.escape(c) for c in self.DISALLOWED_DANGEROUS_CHARACTERS)}]"

C = Constants()
