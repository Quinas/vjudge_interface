from .resource import Resource


class ProblemData(Resource):
    def __init__(self, parsed_data, interface):
        super().__init__(parsed_data, interface)

        self.id = parsed_data["id"]
        self.is_favorite = parsed_data["is_favorite"]
        self.allow_submit = parsed_data["allow_submit"]
        self.status = parsed_data["status"]
        self.properties = parsed_data["properties"]


class ProblemListItem(Resource):
    def __init__(self, parsed_data, interface, problem_list):
        super().__init__(parsed_data, interface)

        self.problem_list = problem_list
        self.id = parsed_data["id"]
        self.title = parsed_data["title"]
        self.OJ = parsed_data["OJ"]
        self.origin_id = parsed_data["origin_id"]
        self.allow_submit = parsed_data["allow_submit"]
        self.update_time = parsed_data["update_time"]
        self.source = parsed_data["source"]
        self.source_href = parsed_data["source_href"]
        self.status = parsed_data["status"]
        self.href = "https://vjudge.net/problem/{}".format(self.id)
        self.origin_href = "https://vjudge.net/problem/{}/origin".format(self.id)

    def get_problem_data(self):
        return self.interface.get_problem_data(self.id)


class ProblemList(Resource):
    def __init__(self, parsed_data, interface):
        super().__init__(parsed_data, interface)

        self.problems = []
        for problem_data in parsed_data:
            self.problems.append(ProblemListItem(problem_data, interface, self))
