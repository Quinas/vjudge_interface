import vjudge_interface.client as client

import vjudge_interface.requests as vrequests
import vjudge_interface.parsers as vparsers
import vjudge_interface.resources as vresources


class VjudgeInterface:
    def __init__(self, username: str = None, password: str = None):
        self.client = client.ApiClient("https://vjudge.net/", username, password)

    def login(self, username: str, password: str):
        self.client.login(username, password)

    def get_user_profile(self, username: str):
        parsed_data = self.request_and_parse(
            locals(), vrequests.GetUserProfile, vparsers.UserProfileParser()
        )
        return self.initialize_resource(parsed_data, vresources.UserProfile)

    def get_my_user_profile(self):
        return self.get_user_profile(self.client.username)

    def get_user_list(
        self,
        start: int = None,
        length: int = None,
        username: str = None,
        nickname: str = None,
        school: str = None,
        time_range: vrequests.constants.TimeRange = None,
    ):
        parsed_data = self.request_and_parse(
            locals(), vrequests.GetUserList, vparsers.UserListParser()
        )
        return self.initialize_resource(parsed_data, vresources.UserList)

    def get_contest_list(
        self,
        start: int = None,
        length: int = None,
        title: str = None,
        owner: str = None,
        category: vrequests.constants.ContestListCategory = None,
        running: vrequests.constants.Running = None,
    ):
        parsed_data = self.request_and_parse(
            locals(), vrequests.GetContestList, vparsers.ContestListParser()
        )
        return self.initialize_resource(parsed_data, vresources.ContestList)

    def get_contest_data(self, contest_id: int, password: str = None):
        if password is not None:
            self.client.send_request(vrequests.LoginContest(contest_id, password))

        data = vparsers.ContestDataParser().parse(
            self.client.send_request(vrequests.GetContestData(contest_id))
        )

        rank = vparsers.ContestRankParser().parse(
            self.client.send_request(vrequests.GetContestRank(contest_id))
        )

        parsed_data = {"data": data, "rank": rank}
        if "_error" in data:
            parsed_data["_error"] = data["_error"]
        elif "_error" in rank:
            parsed_data["_error"] = rank["_error"]

        return self.initialize_resource(parsed_data, vresources.ContestData)

    def get_status_list(
        self,
        start: int = None,
        length: int = None,
        username: str = None,
        contest_id: int = None,
        OJ: vrequests.constants.OnlineJudge = None,
        problem: str = None,
        result: vrequests.constants.Result = None,
        language: vrequests.constants.Language = None,
        only_followed: bool = None,
        in_contest: bool = None,
    ):
        parsed_data = self.request_and_parse(
            locals(), vrequests.GetStatusList, vparsers.StatusListParser()
        )
        return self.initialize_resource(parsed_data, vresources.StatusList)

    def get_group_data(self, short_name: str):
        return vparsers.GroupDataParser().parse(
            self.client.send_request(vrequests.GetGroupData(short_name))
        )

    def get_problem_list(
        self,
        start: int = None,
        length: int = None,
        OJ: vrequests.constants.OnlineJudge = None,
        problem_number: str = None,
        title: str = None,
        origin: str = None,
        category: vrequests.constants.ProblemListCategory = None,
        order_direction: vrequests.constants.OrderDirection = None,
        order_by: vrequests.constants.ProblemListOrderBy = None,
    ):
        parsed_data = self.request_and_parse(
            locals(), vrequests.GetProblemList, vparsers.ProblemListParser()
        )
        return self.initialize_resource(parsed_data, vresources.ProblemList)

    def get_status_data(self, status_data_id: int):
        parsed_data = self.request_and_parse(
            locals(), vrequests.GetStatusData, vparsers.StatusDataParser(status_data_id)
        )
        return self.initialize_resource(parsed_data, vresources.StatusData)

    def request_and_parse(self, args, request, parser):
        filtered_args = {
            key: val for key, val in args.items() if val is not None and key != "self"
        }

        response = self.client.send_request(request(**filtered_args))
        parsed_data = parser.parse(response)

        return parsed_data

    def initialize_resource(self, parsed_data, resource):
        if "_error" in parsed_data:
            return vresources.Error(parsed_data, self)

        return resource(parsed_data, self)
