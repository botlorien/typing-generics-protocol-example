from typing import Protocol, Any


class SupportLessThan(Protocol):
    def __lt__(self, other: Any) -> bool: ...
