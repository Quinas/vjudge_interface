import json

from .parser import Parser

CONTEST_ITEM_PARAMS = {
    "id": 0,
    "title": 1,
    "begin_time": 2,
    "end_time": 3,
    "openness": 4,
    "owner": 5,
    "owner_id": 6,
    "group_name": 7,
    "group_shortname": 8,
    "type": 9,
    "is_favorite": 10,
    "is_group_manager": 11,
    "is_contest_manager": 12,
    "contestants_number": 13,
}


class ContestListParser(Parser):
    """
    [
        {'username': 'user1', 'nickname': 'nick', 'school': 'myschool', 'solved': 0},
        {'username': 'user2', 'nickname': 'nick2', 'school': None, 'solved': 2},
        ...
    ]
    """

    def parse(self, response):
        error = self.parse_error(response)
        if error is not None:
            return error

        json_data = json.loads(response.text)
        data = []
        for contest in json_data["data"]:
            contest_dict = {}
            for key, idx in CONTEST_ITEM_PARAMS.items():
                contest_dict[key] = contest[idx]
            data.append(contest_dict)

        return data

