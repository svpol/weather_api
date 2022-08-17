import requests
import json


# Enter a valid API key below.
# APP_ID = '...'


def get_current_weather(lat: str, long: str) -> dict:
    """
    Returns current weather by geographic coordinates.
    :param lat: latitude, string,
    :param long: longitude, string.
    :return: dict with weather data
    """
    url = "https://api.openweathermap.org/data/2.5/weather?lat=" + lat + "&lon=" + \
                      long + "&units=metric&appid=" + APP_ID
    return requests.get(url).json()


def get_5day_forecast(lat: str, long: str) -> dict:
    """
    Returns weather forecast for 5 days with data every 3 hours by geographic coordinates.
    :param lat: latitude, string,
    :param long: longitude, string.
    :return: dict with weather data
    """
    url = "https://api.openweathermap.org/data/2.5/forecast?lat=" + lat + "&lon=" + \
          long + "&units=metric&appid=" + APP_ID
    return requests.get(url).json()


def dump_to_json(data: dict, filepath: str) -> None:
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)


if __name__ == "__main__":

    # The result of these function calls with a valid API key is presented in result_examples directory.
    # The API key must not be published anywhere.
    dump_to_json(get_current_weather('33.753746', '-84.386330'), 'result_examples/atlanta_current_weather.json')
    dump_to_json(get_5day_forecast('33.753746', '-84.386330'), 'result_examples/atlanta_forecast.json')
