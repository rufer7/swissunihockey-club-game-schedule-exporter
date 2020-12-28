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

script for exporting the home game schedule of the selected club and season to a word document

input: data from swiss unihockey API v2
output: word document


"""
import tkinter
from datetime import datetime
from tkinter import Tk, StringVar, OptionMenu
from typing import Tuple, List

import docx

from docx_util import add_report_table
from swiss_unihockey_api_wrapper import GameRecord


def select_season_club_and_home_arena() -> Tuple[int, str, str]:
    """
    show UI for selection of season, club and home arena
    @return:
    """
    seasons: List[int] = [
        datetime.now().year - 1,
        datetime.now().year,
        datetime.now().year + 1
    ]

    root = Tk()
    root.title("Select season, club and home arena")
    root.geometry("375x120")
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)

    season_variable = StringVar(root)
    club_variable = StringVar(root)
    home_arena_variable = StringVar(root)

    season_label = tkinter.Label(root, text="Season:")
    season_label.grid(row=1, column=0, sticky="w")

    season_option_menu = OptionMenu(root, season_variable, *seasons)
    season_option_menu.grid(row=1, column=1, sticky="nsew")

    def on_select_season(*args):
        selected_season = season_variable.get()
        clubs = {"tralala": 1, "tralala2": 2}

        club_label = tkinter.Label(root, text="Club:")
        club_label.grid(row=2, column=0, sticky="w")
        club_option_menu = OptionMenu(root, club_variable, *clubs)
        club_option_menu.grid(row=2, column=1, sticky="nsew")

    season_variable.trace('w', on_select_season)

    def on_select_club(*args):
        home_arenas = ["arena", "arena2"]

        home_arena_label = tkinter.Label(root, text="Home arena:")
        home_arena_label.grid(row=3, column=0, sticky="w")
        home_arena_option_menu = OptionMenu(root, home_arena_variable, *home_arenas)
        home_arena_option_menu.grid(row=3, column=1, sticky="nsew")

    club_variable.trace('w', on_select_club)

    def on_select_home_arena(*args):
        root.quit()

    home_arena_variable.trace('w', on_select_home_arena)

    root.mainloop()

    return season_variable.get(), club_variable.get(), home_arena_variable.get()


def insert_games(document: docx.Document, games: list[GameRecord]) -> None:
    """
    insert table containing games into document
    @param document:
    @param games:
    @return: nothing
    """
    table = add_report_table(document, ('Datum', 'Anpfiff', 'Hornets-Team', 'Gegner'), len(games) + 1)
    for i, game in enumerate(games):
        row = i + 1
        table.cell(row, 0).text = game.date
        table.cell(row, 1).text = game.start_time
        table.cell(row, 2).text = game.team_name
        table.cell(row, 3).text = game.opponent


def insert_paragraphs_from_file(document: docx.Document, path_to_file: str) -> None:
    """
    insert paragraphs from file into document
    @param document:
    @param path_to_file:
    @return: nothing
    """
    with open(path_to_file, encoding="utf-8") as stream:
        line = stream.readline()
        count = 1
        while line:
            document.add_paragraph(line.strip())
            line = stream.readline()
            count += 1


def generate_game_schedule(document: docx.Document) -> None:
    """
    generate game schedule
    @param document:
    @return: nothing
    """
    season, club_name, home_arena = select_season_club_and_home_arena()
    games: list[GameRecord] = []
    insert_games(document, games)
    insert_paragraphs_from_file(document, "after-table-text.txt")


def main() -> None:
    """
    main entry point
    """
    document = docx.Document("empty-game-schedule.docx")
    generate_game_schedule(document=document)
    document.save("game-schedule.docx")


if __name__ == "__main__":
    main()
