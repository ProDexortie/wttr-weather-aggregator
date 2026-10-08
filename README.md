# Wttr Weather Aggregator

Консольный скрипт для получения текущей погоды по списку городов через сервис [wttr.in](https://wttr.in) и подсчёта сводной статистики по странам.

## Требования

- Python 3.7+

## Запуск

Список городов задаётся в файле `Cities.txt` (по одному городу на строку).

Запуск скрипта:

```bash
python main.py
```

## Пример вывода

```text
Moscow, Russia +14 °C
Khabarovsk, Russia +3 °C
Saint-Petersburg, Russia +12 °C
Vienna, Austria +18 °C
Izhevsk, Russia +11 °C
Perm, Russia +9 °C
NhaTrang, Vietnam +27 °C
Villach, Austria +18 °C

Russia — 5 cities, avg: +10 °C, min: +3 °C, max: +14 °C
Austria — 2 cities, avg: +18 °C, min: +18 °C, max: +18 °C
Vietnam — 1 city, avg: +27 °C, min: +27 °C, max: +27 °C
```
