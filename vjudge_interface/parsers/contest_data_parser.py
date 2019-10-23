import json

CONTEST_DATA_PARAMS = {
    "id": "id",
    "title": "title",
    "begin_time": "begin",
    "length": "length",
    "is_replay": "isReplay",
    "participants": "participants",
    "submissions": "submissions",
}


class ContestDataParser:
    def parse(self, response):
        json_data = json.loads(response.text)
        data = {}
        for key, field in CONTEST_DATA_PARAMS.items():
            data[key] = json_data[field]
        return data
