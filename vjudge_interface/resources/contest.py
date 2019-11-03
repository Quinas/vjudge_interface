from .resource import Resource

import vjudge_interface.requests as vjudge_requests


class ContestData(Resource):
    def __init__(self, parsed_data, interface):
        super().__init__(parsed_data, interface)

        self.id = parsed_data["data"]["id"]
        self.title = parsed_data["data"]["title"]
        self.type = parsed_data["data"]["type"]
        self.announcement = parsed_data["data"]["announcement"]
        self.auth_status = parsed_data["data"]["auth_status"]
        self.begin_time = parsed_data["data"]["begin_time"]
        self.end_time = parsed_data["data"]["end_time"]
        self.length = self.end_time - self.begin_time
        self.creation_time = parsed_data["data"]["creation_time"]
        self.description = parsed_data["data"]["description"]
        self.ended = parsed_data["data"]["ended"]
        self.favorite = parsed_data["data"]["favorite"]
        self.manager_id = parsed_data["data"]["manager_id"]
        self.manager_name = parsed_data["data"]["manager_name"]
        self.openness = parsed_data["data"]["openness"]
        self.partial_score = parsed_data["data"]["partial_score"]
        self.penalty = parsed_data["data"]["penalty"]
        self.problems_hash = parsed_data["data"]["problems_hash"]
        self.started = parsed_data["data"]["started"]
        self.problems = []
        for problem in parsed_data["data"]["problems"]:
            self.problems.append(ContestProblem(problem, interface, self))

        self.is_replay = parsed_data["rank"]["is_replay"]
        self.submissions = []
        for submission in parsed_data["rank"]["submissions"]:
            self.submissions.append(ContestRankSubmission(submission, interface, self))

        self.participants = []
        for user_id in parsed_data["rank"]["participants"]:
            user_data = {
                "user_id": int(user_id),
                "username": parsed_data["rank"]["participants"][user_id][0],
                "nickname": parsed_data["rank"]["participants"][user_id][1],
            }
            self.participants.append(
                ContestUser(
                    user_data,
                    interface,
                    self,
                    [s for s in self.submissions if s.user_id == int(user_id)],
                )
            )

    def get_contest_status(
        self,
        start: int = 0,
        length: int = 10000,
        username: str = None,
        OJ: vjudge_requests.constants.OnlineJudge = None,
        problem: str = None,
        result: vjudge_requests.constants.Result = None,
        language: vjudge_requests.constants.Language = None,
    ):
        return self.interface.get_status_list(
            start=start,
            length=length,
            username=username,
            contest_id=self.id,
            OJ=OJ,
            problem=problem,
            result=result,
            language=language,
            in_contest=True,
        )


class ContestProblem(Resource):
    def __init__(self, parsed_data, interface, contest):
        super().__init__(parsed_data, interface)

        self.contest = contest
        self.contest_id = contest.id
        self.id = parsed_data["pid"]
        self.title = parsed_data["title"]
        self.OJ = parsed_data["oj"]
        self.origin_number = parsed_data.get("probNum")
        self.letter = parsed_data["num"]
        self.public_description_id = parsed_data["publicDescId"]
        self.public_description_version = parsed_data["publicDescVersion"]
        self.descriptions = []
        if "allDescBriefs" in parsed_data:
            for description in parsed_data["allDescBriefs"]:
                self.descriptions.append(
                    ContestProblemDescription(description, interface, contest, self)
                )

        self.properties = parsed_data["properties"]
        self.weight = parsed_data["weight"]
        self.origin_href = "https://vjudge.net/problem/{}/origin".format(self.id)


class ContestProblemDescription(Resource):
    def __init__(self, parsed_data, interface, contest, problem):
        super().__init__(parsed_data, interface)

        self.contest = contest
        self.contest_id = contest.id
        self.problem = problem
        self.problem_id = problem.id
        self.id = parsed_data["id"]
        self.update_date = parsed_data["updateDate"]
        self.version = parsed_data["version"]
        self.author = parsed_data["author"]
        self.remarks = parsed_data["remarks"]
        self.href = "https://vjudge.net/problem/description/{}?{}".format(
            self.id, self.version
        )


class ContestUser(Resource):
    def __init__(self, parsed_data, interface, contest, submissions):
        super().__init__(parsed_data, interface)

        self.contest = contest
        self.contest_id = contest.id
        self.user_id = parsed_data["user_id"]
        self.username = parsed_data["username"]
        self.nickanme = parsed_data["nickname"]
        self.submissions = submissions
        self.accepted = sum(s.status == 1 for s in self.submissions)
        self.failed = sum(s.status == 0 for s in self.submissions)
        self.pending = sum(s.status == 2 for s in self.submissions)
        self.penalty = self._calculate_penalty()
        self.rank = 0

        for submission in self.submissions:
            submission.user = self

    def get_user_profile(self):
        return self.interface.get_user_profile(self.username)

    def _calculate_penalty(self):
        return 0


class ContestRankSubmission(Resource):
    def __init__(self, parsed_data, interface, contest):
        super().__init__(parsed_data, interface)

        self.contest = contest
        self.contest_id = contest.id
        self.user_id = parsed_data[0]
        self.problem_index = parsed_data[1]
        self.status = parsed_data[2]
        self.time = parsed_data[3]
        self.accepted = None if len(parsed_data) <= 4 else parsed_data[4]
        self.total = None if len(parsed_data) <= 5 else parsed_data[5]
        self.problem = contest.problems[self.problem_index]
        self.user = None


class ContestListItem(Resource):
    def __init__(self, parsed_data, interface, contest_list):
        super().__init__(parsed_data, interface)

        self.contest_list = contest_list
        self.id = parsed_data["id"]
        self.title = parsed_data["title"]
        self.begin_time = parsed_data["begin_time"]
        self.end_time = parsed_data["end_time"]
        self.openness = parsed_data["openness"]
        self.owner = parsed_data["owner"]
        self.owner_id = parsed_data["owner_id"]
        self.group_name = parsed_data["group_name"]
        self.group_shortname = parsed_data["group_shortname"]
        self.type = parsed_data["type"]
        self.is_favorite = parsed_data["is_favorite"]
        self.is_group_manager = parsed_data["is_group_manager"]
        self.is_contest_manager = parsed_data["is_contest_manager"]
        self.contestants_number = parsed_data["contestants_number"]

    def get_contest_data(self, password=None):
        return self.interface.get_contest_data(self.id, password)


class ContestList(Resource):
    def __init__(self, parsed_data, interface):
        super().__init__(parsed_data, interface)

        self.contests = []
        for contest_data in parsed_data:
            self.contests.append(ContestListItem(contest_data, interface, self))
