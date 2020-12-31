# swissunihockey-club-game-schedule-exporter
[![License](https://img.shields.io/badge/license-Apache%20License%202.0-blue.svg)](https://github.com/rufer7/swissunihockey-club-game-schedule-exporter/blob/main/LICENSE)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/rufer7/swissunihockey-club-game-schedule-exporter)
[![Python tests](https://github.com/rufer7/swissunihockey-club-game-schedule-exporter/workflows/Python%20tests/badge.svg)](https://github.com/rufer7/swissunihockey-club-game-schedule-exporter/actions?query=workflow%3A%22Python+tests%22)
[![CodeQL](https://github.com/rufer7/swissunihockey-club-game-schedule-exporter/workflows/CodeQL/badge.svg)](https://github.com/rufer7/swissunihockey-club-game-schedule-exporter/actions?query=workflow%3ACodeQL)

[![Twitter](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Fgithub.com%2Frufer7%2Fswissunihockey-club-game-schedule-exporter)](https://twitter.com/rufer_13)

A python application that allows to export the home game schedule of a club belonging to swiss unihockey to a Word document.


## Setup
1. create virtual environment

   `~/python39/python.exe -m venv venv`

1. activate virtual environment by executing the following command in PyCharms `Terminal`

    `venv/Scripts/activate`

1. install dependencies

    `pip install -r requirements.txt`

## Run
1. change to directory `src`
1. execute python app

    `python export_club_game_schedule.py`


## Execute tests
In PyCharm IDE:

1. set default test runner to `pytest`

    - Open settings in PyCharm: `File` > `Settings...`
    - Navigate to `Tools` > `Python Integrated Tools`
    - Under `Testing` select `pytest` as default test runner

1. open file tests/test_export_club_game_schedule.py

1. right click on tab in editor and execute `Run 'pytest in test_expor...'`

In `Terminal` of Pycharm IDE:
1. activate venv if not yet active
1. change to `tests` directory

    `cd src\tests`
1. execute `pytest`

    `pytest`

