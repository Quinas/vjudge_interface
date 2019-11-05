from .resource import Resource


class StatusData(Resource):
    def __init__(self, parsed_data, interface):
        super().__init__(parsed_data, interface)

        self.id = parsed_data["id"]
        self.author = parsed_data["author"]
        self.author_id = parsed_data["author_id"]
        self.additional_info = parsed_data["additional_info"]
        self.code = parsed_data["code"]
        self.contest_id = parsed_data["contest_id"]
        self.contest_num = parsed_data["contest_num"]
        self.is_open = parsed_data["is_open"]
        self.language = parsed_data["language"]
        self.language_canonical = parsed_data["language_canonical"]
        self.length = parsed_data["length"]
        self.OJ = parsed_data["OJ"]
        self.prob_num = parsed_data["prob_num"]
        self.processing = parsed_data["processing"]
        self.remote_run_id = parsed_data["remote_run_id"]
        self.run_id = parsed_data["run_id"]
        self.share_code = parsed_data["share_code"]
        self.status = parsed_data["status"]
        self.status_canonical = parsed_data["status_canonical"]
        self.status_type = parsed_data["status_type"]
        self.submission_time = parsed_data["submit_time"]


class StatusListItem(Resource):
    def __init__(self, parsed_data, interface, status_list):
        super().__init__(parsed_data, interface)

        self.status_list = status_list
        self.memory = parsed_data["memory"]
        self.access = parsed_data["access"]
        self.execution_time = parsed_data["execution_time"]
        self.language = parsed_data["language"]
        self.username = parsed_data["username"]
        self.user_id = parsed_data["user_id"]
        self.contest_id = parsed_data["contest_id"]
        self.contest_num = parsed_data["contest_num"]
        self.processing = parsed_data["processing"]
        self.status_id = parsed_data["run_id"]
        self.submission_time = parsed_data["submission_time"]
        self.OJ = parsed_data["OJ"]
        self.problem_id = parsed_data["problem_id"]
        self.source_length = parsed_data["source_length"]
        self.problem_number = parsed_data["problem_number"]
        self.status = parsed_data["status"]
        self.status_canonical = parsed_data["status_canonical"]

    def get_status_data(self):
        return self.interface.get_status_data(self.status_id)


class StatusList(Resource):
    def __init__(self, parsed_data, interface):
        super().__init__(parsed_data, interface)

        self.status = []
        for status_data in parsed_data:
            self.status.append(StatusListItem(status_data, interface, self))
