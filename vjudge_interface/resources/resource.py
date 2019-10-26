class Resource:
    def __init__(self, parsed_data, interface, vjudge_request, vjudge_parser, response):
        self.parsed_data = parsed_data
        self.interface = interface
        self.vjudge_request = vjudge_request
        self.vjudge_parser = vjudge_parser
        self.response = response
        self.is_error = False
