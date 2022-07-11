from dataclasses import dataclass
from typing import List, Optional
from src.domain.mixins import EntityMixin

@dataclass(frozen=True)
class User(EntityMixin):
    name: str


