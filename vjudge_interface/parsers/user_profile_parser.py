import bs4
import re
import string

from .parser import Parser

SOLVED_TABLE_PARAMS = [
    "solved_last_24_hours",
    "solved_last_7_days",
    "solved_last_30_days",
    "overall_solved",
    "overall_attempted",
]

USER_INFO_PARAMS = {
    "registered": "Register:",
    "last_seen": "Last seen:",
    "school": "School:",
    "QQ": "QQ:",
    "email": "Email:",
}


class UserProfileParser(Parser):
    """
    {
        'username': 'Quinas',
        'user_id': 252602,
        'thumbnail': 'aaa',
        'solved_last_24_hours': 0,
        'solved_last_7_days': 0,
        'solved_last_30_days': 0,
        'overall_solved': 2,
        'overall_attempted': 5,
        'registered': '10 months ago',
        'last_seen': '3 months ago',
        'school': None,
        'QQ': None
    }
    """

    def parse(self, response):
        error = self.parse_error(response)
        if error is not None:
            return error

        self.data = {}
        self.soup = bs4.BeautifulSoup(response.text, "html.parser")
        self._username()
        self._user_id()
        self._thumbnail()
        self._solved_problems_table()
        self._user_info()
        return self.data

    def _username(self):
        self.data["username"] = self.soup.find(name="input", id="username")["value"]

    def _user_id(self):
        user_id = self.soup.find(name="span", text=re.compile("#")).string
        self.data["id"] = int(re.sub(r"\D", r"", user_id))

    def _thumbnail(self):
        self.data["thumbnail"] = self.soup.find(
            name="div", class_="container"
        ).div.div.a.img["src"]

    def _solved_problems_table(self):
        table = self.soup.find(name="table", class_="problem-solve").find_all("a")
        for idx, key in enumerate(SOLVED_TABLE_PARAMS):
            self.data[key] = int(table[idx].string)

    def _user_info(self):
        user_info = self.soup.find(name="dl", class_="user-info")

        for key, label in USER_INFO_PARAMS.items():
            value = None
            dt = user_info.find(name="dt", text=label)
            if dt is not None:
                value = dt.find_next_sibling("dd").next_element.strip()
            self.data[key] = value
