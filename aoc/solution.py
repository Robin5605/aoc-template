from abc import ABC

class SolutionABC(ABC):
    def __init__(self, content: str) -> None:
        ...

    def part_one(self) -> str | int:
        ...

    def part_two(self) -> str | int:
        ...