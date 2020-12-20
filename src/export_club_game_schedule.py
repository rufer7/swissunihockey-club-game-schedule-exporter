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

script for exporting the game schedule of the selected club to a word document

input: data from swiss unihockey API v2
output: word document


"""
import docx

from docx_util import add_report_table
from swiss_unihockey_api_wrapper import GameRecord


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


def generate_game_schedule(document: docx.Document) -> None:
    """
    generate game schedule
    @param document:
    @return: nothing
    """
    games: list[GameRecord] = []
    insert_games(document, games)
    # TODO - insert paragraph
    # Alle aufgeführten Spiele finden in der Raiffeisen unihockeyARENA am Sportweg 3 in 3322 Urtenen-Schönbühl statt!
    # Wir freuen uns, Sie in unserer Halle als Zuschauer begrüssen zu dürfen.
    #
    # Hornets Regio Moosseedorf Worblental


def main() -> None:
    """
    main entry point
    """
    document = docx.Document("empty-game-schedule.docx")
    generate_game_schedule(document=document)
    document.save("game-schedule.docx")


if __name__ == "__main__":
    main()
