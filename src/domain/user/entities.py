from dataclasses import dataclass
from typing import List
from ..mixins import EntityMixin
from .enums import PostCategory
from .values import Birthday

@dataclass(frozen=True)
class Post(EntityMixin):
    title: str
    detail: str
    category: PostCategory

@dataclass(frozen=True)
class Company(EntityMixin):
    name: str

@dataclass(frozen=True)
class User(EntityMixin):
    name: str
    birthday: Birthday
    company: Company
    posts: List[Post]


