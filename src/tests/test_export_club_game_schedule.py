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
from unittest import mock
from unittest.mock import patch

import docx
import pytest

import export_club_game_schedule


@pytest.fixture(scope="session", autouse=True)
def before_all():
    """
    code to be executed before all tests
    """
    print()
    print("START before_all ...")
    # change working directory to src so that files like empty-game-schedule.docx, game-schedule.docx could be found
    os.chdir(os.path.relpath('..'))

    with mock.patch('export_club_game_schedule.select_season_club_and_home_arena') as MockClass:  # pylint: disable=invalid-name
        MockClass.return_value = (
            2020,
            "Hornets R.Moosseedorf Worblental",
            "RAIFFEISEN unihockeyARENA, Urtenen Schönbühl")
        # generate game schedule
        export_club_game_schedule.main()
    # load game-schedule.docx
    TestExportedGameSchedule.document = docx.Document("game-schedule.docx")
    print("END before_all SUCCEEDED")


class TestInsertion:  # pylint: disable=too-few-public-methods
    """
    class for test grouping purposes
    """
    @patch("docx.Document")
    def test_insert_paragraphs_from_file(self, mocked_document):  # pylint: disable=no-self-use
        """

        @param self:
        @return: nothing
        """
        # arrange
        # act
        export_club_game_schedule.insert_paragraphs_from_file(mocked_document, "after-table-text.txt")
        # assert
        mocked_document.add_paragraph.assert_called_with('Hornets Regio Moosseedorf Worblental')


class TestExportedGameSchedule:  # pylint: disable=too-few-public-methods
    """
    class for test grouping purposes
    """
    document = None

    def test_table_headers_in_document(self):
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

    def test_amount_of_rows_in_document(self):
        """

        @param self:
        @return: nothing
        """
        # arrange
        assert self.document
        tables = self.document.tables
        table = tables[0]
        # assert
        assert len(table.rows) - 1 == 14
