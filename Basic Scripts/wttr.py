"""
::@name Get Weather for a city and display it in the console

::@description
    Takes input for city. Gives output of weather for a city in a text format.
    Command arg -c City
::@/description

"""
import argparse
import requests


PARSER = argparse.ArgumentParser()

PARSER.add_argument(
    "-c",
    "--city",
    dest="city",
    default="Christchurch",
    help="Name of the City to display weather info from wttr.in",
)


ARGS = PARSER.parse_args()

CITY = ARGS.city


def get_weather():
    """Display Weather for city in console"""
    url = f"https://wttr.in/{CITY}"
    response = requests.get(url=url, timeout=None)
    print(response.text)


if __name__ == "__main__":
    get_weather()
