import bs4
import json

from .parser import Parser


class GroupDataParser(Parser):
    def parse(self, response):
        error = self.parse_error(response)
        if error is not None:
            return error

        self.data = {}
        self.soup = bs4.BeautifulSoup(response.text, "html.parser")
        self.json_data = json.loads(
            self.soup.find("textarea", {"name": "dataJson"}).text
        )
        self._name()
        self._logo()
        self._brief()
        self._visibility()
        self._join_policy()
        self._members_number()
        self._create_time()
        self._intro()
        self._contests()
        self._members()
        return self.data

    def _name(self):
        self.data["name"] = self.json_data["name"]

    def _logo(self):
        self.data["logo"] = self.soup.find(name="img", class_="card-img-top")["src"]

    def _brief(self):
        self.data["brief"] = self.json_data["brief"]

    def _visibility(self):
        li = self.soup.find_all(name="li", class_="list-group-item")[0]
        self.data["visibility"] = li.span.text

    def _join_policy(self):
        li = self.soup.find_all(name="li", class_="list-group-item")[1]
        self.data["join_policy"] = li.span.text

    def _members_number(self):
        li = self.soup.find_all(name="li", class_="list-group-item")[4]
        self.data["members_number"] = li.a.text

    def _create_time(self):
        li = self.soup.find_all(name="li", class_="list-group-item")[6]
        self.data["create_time"] = li.text.strip().split(" ")[-1]

    def _intro(self):
        self.data["intro"] = self.json_data["intro"]

    def _contests(self):
        self.data["contests"] = []

        for contest in self.json_data["contests"]:
            self.data["contests"].append(
                {
                    "contest_id": contest[0],
                    "title": contest[1],
                    "contestants": contest[2],
                    "begin_time": contest[3],
                    "length": contest[4] - contest[3],
                    "openness": contest[5],
                }
            )

    def _members(self):
        self.data["members"] = []

        for member in self.json_data["memberBriefs"]:
            self.data["members"].append(
                {
                    "user_id": member["id"],
                    "username": member["username"],
                    "nickname": member["nickName"],
                    "join_time": member["joinTime"],
                    "last_seen": member["lastSeenTime"],
                    "role": member["role"],
                }
            )

