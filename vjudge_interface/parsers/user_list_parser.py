import json

from .parser import Parser

USER_ITEM_PARAMS = {"username": 1, "nickname": 2, "school": 3, "solved": 4}


class UserListParser(Parser):
    """
    [
        {'username': 'user1', 'nickname': 'nick', 'school': 'myschool', 'solved': 0},
        {'username': 'user2', 'nickname': 'nick2', 'school': None, 'solved': 2},
        ...
    ]
    """

    def parse(self, response):
        self.parse_error(response)

        json_data = json.loads(response.text)
        data = []
        for user in json_data["data"]:
            user_dict = {}
            for key, idx in USER_ITEM_PARAMS.items():
                user_dict[key] = user[idx]
            data.append(user_dict)

        return data
