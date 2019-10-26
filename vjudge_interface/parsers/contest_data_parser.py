import json
from .parser import Parser

CONTEST_DATA_PARAMS = {
    "id": "id",
    "title": "title",
    "begin_time": "begin",
    "length": "length",
    "is_replay": "isReplay",
    "participants": "participants",
    "submissions": "submissions",
}


class ContestDataParser(Parser):
    def parse(self, response):
        error = self.parse_error(response)
        if error is not None:
            return error

        try:
            json_data = json.loads(response.text)
        except ValueError:
            return {
                "_error": "Invalid response (do you have access to view this contest?)"
            }

        data = {}
        for key, field in CONTEST_DATA_PARAMS.items():
            data[key] = json_data[field] if field in json_data else None
        return data
