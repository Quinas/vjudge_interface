from .resource import Resource


class ContestData(Resource):
    def __init__(self, parsed_data, interface, vjudge_request, vjudge_parser, response):
        super().__init__(
            parsed_data, interface, vjudge_request, vjudge_parser, response
        )

        self.id = parsed_data["id"]
        self.title = parsed_data["title"]
        self.begin_time = parsed_data["begin_time"]
        self.length = parsed_data["length"]
        self.is_replay = parsed_data["is_replay"]
        self.participants = parsed_data["participants"]
        self.submissions = parsed_data["submissions"]


class ContestListItem(Resource):
    def __init__(self, parsed_data, interface, vjudge_request, vjudge_parser, response):
        super().__init__(
            parsed_data, interface, vjudge_request, vjudge_parser, response
        )

        self.id = parsed_data["id"]
        self.title = parsed_data["title"]
        self.begin_time = parsed_data["begin_time"]
        self.end_time = parsed_data["end_time"]
        self.opennes = parsed_data["openness"]
        self.owner = parsed_data["owner"]
        self.owner_id = parsed_data["owner_id"]
        self.group_name = parsed_data["group_name"]
        self.group_shortname = parsed_data["group_shortname"]
        self.type = parsed_data["type"]
        self.is_favorite = parsed_data["is_favorite"]
        self.is_group_manager = parsed_data["is_group_manager"]
        self.is_contest_manager = parsed_data["is_contest_manager"]
        self.contestants_number = parsed_data["contestants_number"]


class ContestList(Resource):
    def __init__(self, parsed_data, interface, vjudge_request, vjudge_parser, response):
        super().__init__(
            parsed_data, interface, vjudge_request, vjudge_parser, response
        )

        contests = []
        for contest_data in parsed_data:
            contests.append(
                ContestListItem(
                    contest_data, interface, vjudge_request, vjudge_parser, response
                )
            )
