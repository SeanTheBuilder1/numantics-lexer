from dataclasses import dataclass
from enum import Enum, auto


class LexerTokenTypeAcceptState(Enum):
    IN_PROGRESS = auto()
    ACCEPTED = auto()
    REJECTED = auto()


@dataclass
class LexerTokenTypeState:
    acceptance: LexerTokenTypeAcceptState
    end_at: int
    current_state: str = "q0"
