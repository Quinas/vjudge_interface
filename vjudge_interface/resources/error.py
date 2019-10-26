from .resource import Resource


class Error(Resource):
    def __init__(self, parsed_data, interface, vjudge_request, vjudge_parser, response):
        super().__init__(
            parsed_data, interface, vjudge_request, vjudge_parser, response
        )

        self.error = parsed_data["_error"]
        self.is_error = True
