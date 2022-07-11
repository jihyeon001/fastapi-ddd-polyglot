import re
from dataclasses import dataclass

regex = r"\d{4}-\d{2}-\d{2}"
pattern = re.compile(regex)

@dataclass(init=False, eq=True, frozen=True)
class Birthday:

    year: int
    month: int
    day: int

    def __init__(self, birthday: str):
        if pattern.match(birthday) is None:
            raise ValueError("birthday should be a valid format.")
        self.year, self.month, self.day = birthday.split('-')
    
    def __str__(self) -> str:
        return f"{self.year}-{self.month}-{self.day}"