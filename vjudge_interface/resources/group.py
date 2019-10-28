from .resource import Resource


class Group(Resource):
    def __init__(self, parsed_data, interface):
        super().__init__(parsed_data, interface)

