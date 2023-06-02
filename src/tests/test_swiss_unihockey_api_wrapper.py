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


test cases for swiss_unihockey_api_wrapper.py

"""
import swiss_unihockey_api_wrapper


SEASON = 2020


class TestClubsLoading:  # pylint: disable=too-few-public-methods
    """
    class for test grouping purposes
    """
    def test_load_clubs(self):  # pylint: disable=no-self-use
        """

        @param self:
        @return: nothing
        """
        # arrange
        # act
        clubs = swiss_unihockey_api_wrapper.load_clubs(SEASON)
        # assert
        assert len(clubs) == 377
        assert clubs["Hornets R.Moosseedorf Worblental"]


class TestGamesLoading:
    """
    class for test grouping purposes
    """
    HORNETS_CLUB_ID = 441388
    HORNETS_HOME_ARENA = "RAIFFEISEN unihockeyARENA, Urtenen Schönbühl"

    def test_load_home_games(self):
        """

        @param self:
        @return: nothing
        """
        # arrange
        # act
        hornets_home_games = swiss_unihockey_api_wrapper.load_home_games(self.HORNETS_CLUB_ID,
                                                                         SEASON,
                                                                         self.HORNETS_HOME_ARENA)
        # assert
        assert len(hornets_home_games) == 14
        first = hornets_home_games[0]
        assert first.date == "16.08.2020"
        assert first.start_time == "19:30"
        assert first.home_team_name == "Herren IV"
        assert first.opponent == "Team Flamingo"

    def test_load_arena_names(self):
        """

        @param self:
        @return: nothing
        """
        # arrange
        # act
        arena_names = swiss_unihockey_api_wrapper.load_arena_names(self.HORNETS_CLUB_ID, SEASON)
        # assert
        assert len(arena_names) == 48
        assert self.HORNETS_HOME_ARENA in arena_names
        assert "BFO Visp, Visp" in arena_names
        assert "???" not in arena_names
