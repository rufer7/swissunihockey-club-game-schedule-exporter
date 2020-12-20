# swissunihockey-club-game-schedule-exporter
[![License](https://img.shields.io/badge/license-Apache%20License%202.0-blue.svg)](https://github.com/rufer7/swissunihockey-club-game-schedule-exporter/blob/main/LICENSE)

A python application that allows to export the game schedule of a club belonging to swiss unihockey to a word document


## Setup
1. install dependencies

    `pip install -r requirements.txt`

## Run
`python export_club_game_schedule.py`


## Execute tests
IDE: PyCharm

1. set default test runner to `pytest`

    - Open settings in PyCharm: `File` > `Settings...`
    - Navigate to `Tools` > `Python Integrated Tools`
    - Under `Testing` select `pytest` as default test runner

1. open file tests/test_export_club_game_schedule.py

1. right click on tab in editor and execute `Run 'pytest in test_gener...'`
