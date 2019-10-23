from .resource import Resource


class Group(Resource):
    def __init__(self, parsed_data, interface, vjudge_request, vjudge_parser, response):
        super().__init__(
            parsed_data, interface, vjudge_request, vjudge_parser, response
        )

