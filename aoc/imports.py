from day01.solution import Solution1
from day02.solution import Solution2
from day03.solution import Solution3
from day04.solution import Solution4
from day05.solution import Solution5
from day06.solution import Solution6
from day07.solution import Solution7
from day08.solution import Solution8
from day09.solution import Solution9
from day10.solution import Solution10
from day11.solution import Solution11
from day12.solution import Solution12
from day13.solution import Solution13
from day14.solution import Solution14
from day15.solution import Solution15
from day16.solution import Solution16
from day17.solution import Solution17
from day18.solution import Solution18
from day19.solution import Solution19
from day20.solution import Solution20
from day21.solution import Solution21
from day22.solution import Solution22
from day23.solution import Solution23
from day24.solution import Solution24
from day25.solution import Solution25

solution_classes = (
    Solution1,
    Solution2,
    Solution3,
    Solution4,
    Solution5,
    Solution6,
    Solution7,
    Solution8,
    Solution8,
    Solution9,
    Solution10,
    Solution11,
    Solution12,
    Solution13,
    Solution14,
    Solution15,
    Solution16,
    Solution17,
    Solution18,
    Solution19,
    Solution20,
    Solution21,
    Solution22,
    Solution23,
    Solution24,
    Solution25,
)

def get_solution_class(*, day: int):
    if day < 1 and day > 25:
        raise Exception("Invalid day. Day must be between 1 and 25 inclusive.")

    return solution_classes[day]