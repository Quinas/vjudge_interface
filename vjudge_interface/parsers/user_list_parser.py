import json

USER_ITEM_PARAMS = {"username": 1, "nickname": 2, "school": 3, "solved": 4}


class UserListParser:
    """
    [
        {'username': 'user1', 'nickname': 'nick', 'school': 'myschool', 'solved': 0},
        {'username': 'user2', 'nickname': 'nick2', 'school': None, 'solved': 2},
        ...
    ]
    """

    def parse(self, response):
        json_data = json.loads(response.text)
        data = []
        for user in json_data["data"]:
            user_dict = {}
            for key, idx in USER_ITEM_PARAMS.items():
                user_dict[key] = user[idx]
            data.append(user_dict)

        return data
