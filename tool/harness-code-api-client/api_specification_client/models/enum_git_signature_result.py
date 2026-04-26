from enum import Enum


class EnumGitSignatureResult(str, Enum):
    BAD = "bad"
    GOOD = "good"
    INVALID = "invalid"
    KEY_EXPIRED = "key_expired"
    REVOKED = "revoked"
    UNSUPPORTED = "unsupported"
    UNVERIFIED = "unverified"

    def __str__(self) -> str:
        return str(self.value)
