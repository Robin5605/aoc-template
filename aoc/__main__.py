import typer
from importlib import import_module
from rich import print
from rich.table import Table
from rich.console import Console
from aoc.solution import SolutionABC
from aoc.get_input import get_input
from requests import HTTPError
from aoc.config import parse_config
from aoc.imports import get_solution_class

def main(
        day: int = typer.Option(None, min=1, max=25), 
        part: int = typer.Option(None, min=1, max=2)
    ):

        config = parse_config()

        table = Table(title=f"Day {day} Solutions")
        table.add_column("Part", justify="center", style="cyan")
        table.add_column("Solution", justify="left", style="magenta")
        
        cls: type[SolutionABC] = get_solution_class(day=day)

        try:
            content = get_input(year=config.year, day=day, session=config.session)
        except HTTPError:
            print(f"Failed fetching input data for day {day}.")
            raise typer.Exit(code=1)

        solution = cls(content)
        part_one, part_two = solution.part_one(), solution.part_two()

        if part is None:
            table.add_row("1", str(part_one))
            table.add_row("2", str(part_two))
        else:
            if part == 1:
                result = solution.part_one()
            if part == 2:
                result = solution.part_two()

            table.add_row(str(part), str(result))

        c = Console()
        c.print(table)

if __name__ == "__main__":
    typer.run(main)