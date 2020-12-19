# -*- coding: utf-8 -*- #

"""

wrapper for swiss unihockey API v2


"""
from dataclasses import dataclass
from datetime import date


@dataclass
class GameRecord:  # pylint: disable=too-few-public-methods
    """
    game record
    """
    date: date = None
    start_time: str = ""
    team_name: str = ""
    opponent: str = ""
