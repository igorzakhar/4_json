# Prettify JSON

This script provides a capability to ["pretty-print"](https://en.wikipedia.org/wiki/Prettyprint) output on console from file, that contains JSON data.

# Quickstart

pprint_json.py single-file program with no external dependencies.
Example of script launch on Linux, Python 3.5:

```#!bash
$ python pprint_json.py <path to file>
```
Console output example:
```#!bash
[
    {
        "Cells": {
            "Address": "улица Академика Павлова, дом 10",
            "AdmArea": "Западный административный округ",
            "ClarificationOfWorkingHours": null,
            "District": "район Кунцево",
            "IsNetObject": "да",
            "Name": "Ароматный Мир",
            "OperatingCompany": "Ароматный Мир",
            "PublicPhone": [
                {
                    "PublicPhone": "(495) 777-51-95"
                }
            ],
            "TypeService": "реализация продовольственных товаров",
            "WorkingHours": [
                {
                    "DayOfWeek": "понедельник",
                    "Hours": "09:30-22:30"
                },
...
```

# Project Goals

The code is written for educational purposes. Training course for web-de
