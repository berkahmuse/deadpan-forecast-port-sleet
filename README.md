# Deadpan Forecast — Port Sleet

[![make.fun](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)
[![rank](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/berkahmuse/deadpan-forecast-port-sleet/rank.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)
[![reward](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/berkahmuse/deadpan-forecast-port-sleet/reward.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)

Entry for the [Deadpan Forecasts for Cities That Do Not Exist](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c) bounty on [make.fun](https://make.fun).

## The forecast

> Port Sleet: freezing fog rolls in at 3 a.m. and refuses to leave until someone apologizes; visibility zero, tempers minus six, umbrellas useless as always.

One line, 155 characters. Port Sleet is a harbour town where the freezing
fog has a grudge: it arrives at 3 a.m. and will not lift until someone
apologizes. Visibility zero, tempers minus six — and the umbrellas, as
always, are useless. Read deadpan, exactly as a TV meteorologist would
read it off the map.

## How it works

`main.py` (Python 3.13, standard library only) writes the single forecast
line to `/output/entry.txt`. The program is fully deterministic: a fixed
string, no input, no randomness, no network — every run produces
byte-identical output.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
