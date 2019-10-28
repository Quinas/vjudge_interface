from .resource import Resource


class ProblemData(Resource):
    def __init__(self, parsed_data, interface):
        super().__init__(parsed_data, interface)


class ProblemListItem(Resource):
    def __init__(self, parsed_data, interface):
        super().__init__(parsed_data, interface)

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


class ProblemList(Resource):
    def __init__(self, parsed_data, interface):
        super().__init__(parsed_data, interface)

        problems = []
        for problem_data in parsed_data:
            problems.append(ProblemListItem(problem_data, interface))
