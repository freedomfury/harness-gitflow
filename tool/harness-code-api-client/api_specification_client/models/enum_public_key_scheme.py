from enum import Enum


class EnumPublicKeyScheme(str, Enum):
    PGP = "pgp"
    SSH = "ssh"

    def __str__(self) -> str:
        return str(self.value)
