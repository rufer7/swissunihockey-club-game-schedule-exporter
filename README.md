# swissunihockey-club-game-schedule-exporter
[![License](https://img.shields.io/badge/license-Apache%20License%202.0-blue.svg)](https://github.com/rufer7/swissunihockey-club-game-schedule-exporter/blob/main/LICENSE)
[![Python tests](https://github.com/rufer7/swissunihockey-club-game-schedule-exporter/workflows/Python%20tests/badge.svg)](https://github.com/rufer7/swissunihockey-club-game-schedule-exporter/actions?query=workflow%3A%22Python+tests%22)
[![CodeQL](https://github.com/rufer7/swissunihockey-club-game-schedule-exporter/workflows/CodeQL/badge.svg)](https://github.com/rufer7/swissunihockey-club-game-schedule-exporter/actions?query=workflow%3ACodeQL)

A python application that allows to export the game schedule of a club belonging to swiss unihockey to a Word document


## Setup
1. create virtual environment in PyCharm
1. activate virtual environment by executing the following command in PyCharms `Terminal`

    `venv/Scripts/activate`

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

1. right click on tab in editor and execute `Run 'pytest in test_expor...'`
