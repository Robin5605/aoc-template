import requests

BASE_URL = "https://adventofcode.com"

def input_endpoint(*, year: int, day: int) -> str:
    return f"{BASE_URL}/{year}/day/{day}/input"

def get_input(*, year: int, day: int, session: str) -> str:
    url = input_endpoint(year=year, day=day)

    cookies = dict(session=session)
    res = requests.get(url, cookies=cookies)
    res.raise_for_status()

    return res.text