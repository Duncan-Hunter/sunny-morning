import os
import requests
import yaml
from datetime import datetime

def main():
    directory = os.path.dirname(os.path.realpath(__file__))
    with open(f"{directory}/api_key.yaml", "r") as yaml_file:
        yaml_data = yaml.load(yaml_file)
    api_key = yaml_data["api_key"]
    cities = yaml_data["city_ids"]
    for city_id in cities:
        url = f"http://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={api_key}"
        data = requests.get(url)
        print(data.json())
        data = data.json()
        now = datetime.now()
        write_data = dict()
        save_format = "%Y-%m-%d-%H:%M"
        save_now = f"{city_id}_" + now.strftime(save_format)
        write_data["save_now"] = save_now
        write_data["weather"] = data["weather"][0]["main"]
        write_data["weather_desc"] = data["weather"][0]["description"]
        write_data["weather_id"] = data["weather"][0]["id"]
        sunrise = datetime.fromtimestamp(data["sys"]['sunrise'])
        write_data["sunrise"] = sunrise.strftime(save_format)
        with open(f"{directory}/data/{save_now}.yaml", 'w') as file:
            yaml.dump(write_data, file)

if __name__ == "__main__":
    main()
