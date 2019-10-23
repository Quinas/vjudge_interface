import vjudge_interface.client as client

import vjudge_interface.requests as vjudge_requests
import vjudge_interface.parsers as vjudge_parsers
import vjudge_interface.resources as vjudge_resources


class VjudgeInterface:
    def __init__(self, username: str = None, password: str = None):
        self.client = client.ApiClient("https://vjudge.net/", username, password)

    def login(self, username: str, password: str):
        self.client.login(username, password)

    def get_user_profile(self, username: str):
        return self.obtain_resource(
            locals(),
            vjudge_requests.GetUserProfile,
            vjudge_parsers.UserProfileParser(),
            vjudge_resources.UserProfile,
        )

    def get_my_user_profile(self):
        return self.get_user_profile(self.client.username)

    def get_user_list(
        self,
        start: int = None,
        length: int = None,
        username: str = None,
        nickname: str = None,
        school: str = None,
        time_range: vjudge_requests.constants.TimeRange = None,
    ):
        return self.obtain_resource(
            locals(),
            vjudge_requests.GetUserList,
            vjudge_parsers.UserListParser(),
            vjudge_resources.UserList,
        )

    def get_contest_list(
        self,
        start: int = None,
        length: int = None,
        title: str = None,
        owner: str = None,
        category: vjudge_requests.constants.ContestListCategory = None,
        running: vjudge_requests.constants.Running = None,
    ):
        return self.obtain_resource(
            locals(),
            vjudge_requests.GetContestList,
            vjudge_parsers.ContestListParser(),
            vjudge_resources.ContestList,
        )

    def get_contest_data(self, contest_id: int):
        return self.obtain_resource(
            locals(),
            vjudge_requests.GetContestData,
            vjudge_parsers.ContestDataParser(),
            vjudge_resources.ContestData,
        )

    def get_status_list(
        self,
        start: int = None,
        length: int = None,
        username: str = None,
        OJ: vjudge_requests.constants.OnlineJudge = None,
        problem: str = None,
        result: vjudge_requests.constants.Result = None,
        language: vjudge_requests.constants.Language = None,
        only_followed: bool = None,
    ):
        return self.obtain_resource(
            locals(),
            vjudge_requests.GetStatusList,
            vjudge_parsers.StatusListParser(),
            vjudge_resources.StatusList,
        )

    def get_group_data(self, short_name: str):
        return vjudge_parsers.GroupDataParser().parse(
            self.client.send_request(vjudge_requests.GetGroupData(short_name))
        )

    def get_problem_list(
        self,
        start: int = None,
        length: int = None,
        OJ: vjudge_requests.constants.OnlineJudge = None,
        problem_number: str = None,
        title: str = None,
        origin: str = None,
        category: vjudge_requests.constants.ProblemListCategory = None,
        order_direction: vjudge_requests.constants.OrderDirection = None,
        order_by: vjudge_requests.constants.ProblemListOrderBy = None,
    ):
        return self.obtain_resource(
            locals(),
            vjudge_requests.GetProblemList,
            vjudge_parsers.ProblemListParser(),
            vjudge_resources.ProblemList,
        )

    def obtain_resource(self, args, request, parser, resource):
        filtered_args = {
            key: val for key, val in args.items() if val is not None and key != "self"
        }
        return resource(
            parser.parse(self.client.send_request(request(**filtered_args)))
        )
