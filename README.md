# Advent of Code Template
A GitHub Python template for Advent of Code, with a fully featured CLI.

## Set up
Here's how to start using this template:

1. Create your own repository from this template

2. Clone your own repository locally
    ```bash
    git clone https://github.com/<USERNAME>/aoc-template
    ```
    Where `<USERNAME>` is your username

3. Change directory into the repository
    ```bash
    cd aoc-template
    ```

4. Install the required dependencies by running this command:
    ```bash
    poetry install
    ```
    Note that poetry needs to be installed beforehand. See [here](https://python-poetry.org/docs/#installation) for an installation guide on installing Poetry.

## Configuration
This project comes with a simple configuration file that needs to be configured. It's named `config.toml`, in the root project directory. An example configuration file is provided below:
```
year=2022
session="session token"
```
If you're not sure how to obtain your session token, see the "[Obtaining Session Token](#obtaining-session-token)" section

## Usage guide
This template comes with a CLI, powered by [Typer](https://typer.tiangolo.com/).

The project will come with 26 folders: an `aoc` folder and 25 folders for each day of Advent of Code. 

Each folder contains one file: `solution.py`. This is where you will be typing up your actual solution. Other required files may be created within this directory as needed to allow for extensibility.

Each `solution.py` file will contain a class with 3 methods:
- `__init__(self, content: str) -> None`
    - The class's initializer method. `content: str` is the input data for the particular day, as a string. 
    - You may want to bind `content` to the class instance, by using `self.content = content`. This way, you can access the raw data from anywhere within the class.
    - You may also want to bind a parsed set of data to `self`, similar to how it was done before. Any other needed variables can be bound as well.
- `part_one(self) -> str | int`
    - This method should return your solution for part one of that day's Advent of Code puzzle.
    - The return type can either be a string or an integer, however historically Advent of Code's solution data types have been integers. It will be stringified under to hood to abstract this away from you.
- `part_two(self) -> str | int`
    - Similar to the function for `part_one`, except this function should return your solution for part two.
    
The syntax to run your solution is as below:
```bash
python -m aoc --day DAY --part PART
```
Where
- `--day` is a required argument consisting of the day you want solutions for, an integer between 1-25.
- `--part` is an optional argument indicating the specific part you want solutions for. Either `1` or `2`. If omitted, both parts will be shown.

## Obtaining session token
This project requires your session token to be able to fetch input data, as this Advent of Code gives different users different input data. You can get your Advent of Code session token by going to the [Advent of Code](https://adventofcode.com/) homepage, and logging in.
Once you're logged in, open up your browser's developer console, and find the cookies. Copy the "value" and paste it into the `session` key of `config.toml`.