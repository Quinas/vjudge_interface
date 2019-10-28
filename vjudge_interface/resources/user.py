from .resource import Resource


class UserProfile(Resource):
    def __init__(self, parsed_data, interface):
        super().__init__(parsed_data, interface)

        self.username = parsed_data["username"]
        self.id = parsed_data["id"]
        self.solve_last_24_hours = parsed_data["solved_last_24_hours"]
        self.solved_last_30_days = parsed_data["solved_last_30_days"]
        self.overall_solved = parsed_data["overall_solved"]
        self.registered = parsed_data["registered"]
        self.school = parsed_data["school"]
        self.QQ = parsed_data["QQ"]


class UserListItem(Resource):
    def __init__(self, parsed_data, interface):
        super().__init__(parsed_data, interface)

        self.username = parsed_data["username"]
        self.nickname = parsed_data["nickname"]
        self.school = parsed_data["school"]
        self.solved = parsed_data["solved"]


class UserList(Resource):
    def __init__(self, parsed_data, interface):
        super().__init__(parsed_data, interface)

        self.users = []
        for user_data in parsed_data:
            self.users.append(UserListItem(user_data, interface))
