import json
import bs4
from .parser import Parser

CONTEST_DATA_PARAMS = {
    "id": "id",
    "title": "title",
    "type": "type",
    "announcement": "announcement",
    "auth_status": "authStatus",
    "begin_time": "begin",
    "end_time": "end",
    "creation_time": "createTime",
    "description": "description",
    "ended": "ended",
    "favorite": "fav",
    "manager_id": "managerId",
    "manager_name": "managerName",
    "openness": "openness",
    "partial_score": "partialScore",
    "penalty": "penalty",
    "problems_hash": "problemsHash",
    "started": "started",
    "problems": "problems",
}

CONTEST_RANK_PARAMS = {
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

        self.data = {}
        self.soup = bs4.BeautifulSoup(response.text, "html.parser")

        password_input = self.soup.find("input", id="contest-login-password")
        if password_input is not None:
            return {"_error": "You don't have access to view the contest."}

        self.json_data = json.loads(
            self.soup.find("textarea", {"name": "dataJson"}).text
        )

        self._json_data()

        return self.data

    def _json_data(self):
        for key, idx in CONTEST_DATA_PARAMS.items():
            self.data[key] = self.json_data[idx]


class ContestRankParser(Parser):
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
        for key, field in CONTEST_RANK_PARAMS.items():
            data[key] = json_data[field] if field in json_data else None
        return data
