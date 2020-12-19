# swissunihockey-club-game-schedule-exporter
A python application that allows to export the game schedule of a club belonging to swiss unihockey to a word document


## Setup
1. install dependencies

    `pip install -r requirements.txt`

## Run
`python export_club_game_schedule.py`


## Execute tests
IDE: PyCharm

1. install pytest

    Execute `pip install pytest` in PyCharms `Terminal`

2. Set default test runner to `pytest`

    - Open settings in PyCharm: File > Settings...
    - Navigate to `Tools` > `Python Integrated Tools`
    - Under `Testing` select `pytest` as default test runner

3. open file tests/test_export_club_game_schedule.py

4. right click on tab in editor and execute `Run 'pytest in test_gener...'`
