import toml
from dataclasses import dataclass

@dataclass
class Config:
    year: int
    session: str

class ConfigException(Exception):
    pass

with open("config.toml") as f:
    data = toml.load(f)

def get_year() -> int | None:
    return data.get("year")

def get_session_token() -> str | None:
    return data.get("session")

def parse_config() -> Config:
    year = get_year()
    if year is None:
        raise ConfigException("Unable to parse year from configuration file.")

    session = get_session_token()
    if session is None:
        raise ConfigException("Unable to parse year from configuration file")

    return Config(year=year, session=session)