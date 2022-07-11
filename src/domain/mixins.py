from dataclasses import dataclass
from typing_extensions import Self

@dataclass(frozen=True)
class EntityMixin:
    id: str
    created_at: int
    updated_at: int

    def __eq__(self, o: object) -> bool:
        if isinstance(o, self.__class__):
            return self.id == o.id

        return False

