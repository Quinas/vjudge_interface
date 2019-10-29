import json
import bs4
from .parser import Parser


STATUS_DATA_PARAMS = {
    "author": "author",
    "author_id": "authorId",
    "additional_info": "additionalInfo",
    "code": "code",
    "contest_id": "contestId",
    "contest_num": "contestNum",
    "is_open": "isOpen",
    "language": "language",
    "language_canonical": "languageCanonical",
    "length": "length",
    "OJ": "oj",
    "prob_num": "probNum",
    "processing": "processing",
    "remote_run_id": "remoteRunId",
    "run_id": "runId",
    "share_code": "shareCode",
    "status": "status",
    "status_canonical": "statusCanonical",
    "status_type": "statusType",
    "submit_time": "submitTime",
}


class StatusDataParser(Parser):
    def __init__(self, status_id):
        self.status_id = status_id

    def parse(self, response):
        error = self.parse_error(response)
        if error is not None:
            return error

        json_data = json.loads(response.text)

        data = {"id": self.status_id}
        for key, field in STATUS_DATA_PARAMS.items():
            data[key] = json_data[field] if field in json_data else None

        return data
