# pylint: disable=redefined-outer-name
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


test cases for export_club_game_schedule.py

"""
import os

import docx
import pytest

from src import export_club_game_schedule


@pytest.fixture(scope="session", autouse=True)
def before_all():
    """
    code to be executed before all tests
    """
    print()
    print("START before_all ...")
    # change working directory to src so that files like empty-game-schedule.docx, game-schedule.docx could be found
    os.chdir(os.path.relpath('..'))
    # generate game schedule
    export_club_game_schedule.main()
    # load game-schedule.docx
    TestExportedGameSchedule.document = docx.Document("game-schedule.docx")
    print("END before_all SUCCEEDED")


class TestExportedGameSchedule:
    """
    class for test grouping purposes
    """
    document = None

    def test_table_headers_in_game_schedule(self):
        """

        @param self:
        @return: nothing
        """
        # arrange
        assert self.document
        tables = self.document.tables
        table = tables[0]
        row_iterator = iter(table.rows)
        header_row = next(row_iterator)
        # assert
        assert header_row.cells[0].text == "Datum"
        assert header_row.cells[1].text == "Anpfiff"
        assert header_row.cells[2].text == "Hornets-Team"
        assert header_row.cells[3].text == "Gegner"
