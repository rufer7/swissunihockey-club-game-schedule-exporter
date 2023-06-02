# -*- coding: utf-8 -*- #

"""

   Copyright 2020 Marc Rufer

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

wrapper for swiss unihockey API v2
API documentation: https://api-v2.swissunihockey.ch/api/doc


"""
import json
from dataclasses import dataclass
from typing import Dict

import requests

API_V2_BASE_URI = "https://api-v2.swissunihockey.ch/api/"
UNDEFINED_LOCATION = "???"


@dataclass
class GameRecord:  # pylint: disable=too-few-public-methods
    """
    game record
    """
    date: str = ""
    start_time: str = ""
    home_team_name: str = ""
    opponent: str = ""


def load_clubs(season: int) -> Dict[str, int]:
    """
    load clubs of specified season
    @param season: season (i.e. 2020 for season 2020/2021)
    @return: dictionary with names (keys) and ids (values) of clubs
    """
    clubs: Dict[str, int] = {}
    response = requests.get(API_V2_BASE_URI + "clubs?season=" + str(season))
    json_data = json.loads(response.text)
    for club in json_data["entries"]:
        clubs[club["text"]] = club["set_in_context"]["club_id"]
    return clubs


def load_home_games(club_id: int, season: int, home_arena: str) -> list[GameRecord]:
    """
    load games of specified club and season which take place in given home arena
    @param club_id: id of the club
    @param season: season (i.e. 2020 for season 2020/2021)
    @param home_arena: name of home arena
    @return: list of home games
    """
    home_games: list[GameRecord] = []
    response = requests.get(API_V2_BASE_URI
                            + "games?mode=club&games_per_page=1000&club_id="
                            + str(club_id)
                            + "&season="
                            + str(season))
    json_data = json.loads(response.text)
    title = json_data["data"]["title"]
    club_name = title[15:title.find(',')]
    game_data_rows = json_data["data"]["regions"][0]["rows"]
    for game_data_row in game_data_rows:
        cells = game_data_row["cells"]
        if home_arena == str.join(", ", cells[1]["text"]):
            if "Abgesagt" != cells[0][["text"][0]:
                game_record = GameRecord()
                game_record.date = cells[0]["text"][0]
                game_record.start_time = cells[0]["text"][1]
                home_team_name_prefix = get_home_team_name_prefix(cells[2]["text"][0])
                if cells[3]["text"][0].startswith("Hornets"):
                    home_team_name_suffix = cells[3]["text"][0].replace(club_name, "")
                    opponent = cells[4]["text"][0]
                else:
                    home_team_name_suffix = cells[4]["text"][0].replace(club_name, "")
                    opponent = cells[3]["text"][0]
                if home_team_name_suffix in ("", " ")\
                        and not home_team_name_prefix.startswith("Junioren U")\
                        and not home_team_name_prefix.startswith("Junioren/-innen U"):
                    home_team_name_suffix = " I"
                game_record.home_team_name = home_team_name_prefix + home_team_name_suffix
                game_record.opponent = opponent
                home_games.append(game_record)

    return home_games


def get_home_team_name_prefix(league: str) -> str:
    """
    get prefix for home team name
    @param league: league name
    """
    league = league.replace("Ligacup ", "")
    league = league.replace("Schweizer Cup ", "")
    league = league.replace(" Regional", "")

    if league.startswith("Herren"):
        return "Herren"
    if league.startswith("Damen"):
        return "Damen"
    return league


def load_arena_names(club_id: int, season: int) -> set:
    """
    load names of arenas the specified club plays at in the specified season
    @param club_id: id of the club
    @param season: season (i.e. 2020 for season 2020/2021)
    @return: set of names of arenas the club plays at in the given season
    """
    response = requests.get(API_V2_BASE_URI
                            + "games?mode=club&games_per_page=1000&club_id="
                            + str(club_id)
                            + "&season="
                            + str(season))
    json_data = json.loads(response.text)
    game_data_rows = json_data["data"]["regions"][0]["rows"]
    arena_names = set(str.join(", ", game_data_row["cells"][1]["text"]) for game_data_row in game_data_rows)
    if UNDEFINED_LOCATION in arena_names:
        arena_names.remove(UNDEFINED_LOCATION)
    return arena_names
