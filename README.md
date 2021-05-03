# Getting hourly data from a weather API

This is to answer a theory that someone posed to me - in Britain it's always sunnier in the morning than later in the day. So to get the truth, let's collect weather and sunrise data at 7, 8 and 9am, as well as 12 and 19 - once we have enough data we can have a look at the data near sunrise, and find out the answer. Tune in later to see what happens.

I know I could just purchase historical data, and I know it's not very interesting, but hey its a weekend project and a lovely piece of conversation.

To get the data I'm gonna use crontab on a raspberry pi, using the free API from [Open Weather Map](https://openweathermap.org/).

## Installation
Create a venv - its just a good thing to do isn't it. Choose a directory you like, and give it a name, I call it sunny-morning.
```bash
~$mkdir sunny-morning & python3 -m venv sunny-morning & source sunny-morning/bin/activate
~$python3 pip install -r /path/to/sunny-morning/requirements.txt
```

You'll need to make a yaml file **api_key.yaml** in the sunny-morning directory which looks like:
```yaml
api_key: OpenWeatherMapAPIKEY
city_ids:
  - city_ids  # open weather map city ids
```

Now I'm using crontab:

```bash
~$crontab -e
```
Add these lines:
```crontab
0 7 * * * source path/to/your/venv/bin/activate & python3 path/to/sunny-morning/get_data.py
0 8 * * * source path/to/your/venv/bin/activate & python3 path/to/sunny-morning/get_data.py
0 9 * * * source path/to/your/venv/bin/activate & python3 path/to/sunny-morning/get_data.py

0 12 * * * source path/to/your/venv/bin/activate & python3 path/to/sunny-morning/get_data.py
0 19 * * * source path/to/your/venv/bin/activate & python3 path/to/sunny-morning/get_data.py
```