from .resource import Resource


class StatusData(Resource):
    def __init__(self, parsed_data, interface, vjudge_request, vjudge_parser, response):
        super().__init__(
            parsed_data, interface, vjudge_request, vjudge_parser, response
        )


class StatusListItem(Resource):
    def __init__(self, parsed_data, interface, vjudge_request, vjudge_parser, response):
        super().__init__(
            parsed_data, interface, vjudge_request, vjudge_parser, response
        )

        self.memory = parsed_data["memory"]
        self.access = parsed_data["access"]
        self.execution_time = parsed_data["execution_time"]
        self.language = parsed_data["language"]
        self.username = parsed_data["username"]
        self.user_id = parsed_data["user_id"]
        self.contest_id = parsed_data["contest_id"]
        self.contest_num = parsed_data["contest_num"]
        self.processing = parsed_data["processing"]
        self.run_id = parsed_data["run_id"]
        self.submission_time = parsed_data["submission_time"]
        self.OJ = parsed_data["OJ"]
        self.problem_id = parsed_data["problem_id"]
        self.source_length = parsed_data["source_length"]
        self.problem_number = parsed_data["problem_number"]
        self.status = parsed_data["status"]


class StatusList(Resource):
    def __init__(self, parsed_data, interface, vjudge_request, vjudge_parser, response):
        super().__init__(
            parsed_data, interface, vjudge_request, vjudge_parser, response
        )

        status = []
        for status_data in parsed_data:
            status.append(
                StatusListItem(
                    status_data, interface, vjudge_request, vjudge_parser, response
                )
            )
