from enum import Enum


class ContestListOrderBy(Enum):
    ID = 0
    TITLE = 2
    PARTICIPANTS = 3
    BEGIN_TIME = 4


class ProblemListOrderBy(Enum):
    FAVORITE_TIME = 1
    PROBLEM_NUMBER = 3
    TITLE = 4
    UPDATE_TIME = 5


class ContestListCategory(Enum):
    ALL = "all"
    MY_CONTESTS = "mine"
    MY_PARTICIPATION = "participation"
    MY_ARRANGEMENT = "arrangement"
    MY_GROUP = "mygroup"
    MY_FAVORITES = "favorites"
    MY_FOLLOW = "follow"
    CLASSICAL = "classical"
    GROUP = "group"
    REPLAY = "replay"


class ProblemListCategory(Enum):
    ALL = "all"
    SOLVED = "solved"
    ATTEMPTED = "attempted"
    FAVORITES = "favorites"


class Running(Enum):
    ALL = 0
    SCHEDULED = 1
    RUNNING = 2
    ENDED = 3


class OrderDirection(Enum):
    ASCENDING = "asc"
    DESCENDING = "desc"


class Result(Enum):
    ALL = 0
    ACCEPTED = 1
    PRESENTATION_ERROR = 2
    WRONG_ANSWER = 3
    TIME_LIMIT_EXCEEDED = 4
    MEMORY_LIMIT_EXCEEDED = 5
    OUTPUT_LIMIT_EXCEEDED = 6
    RUNTIME_ERROR = 7
    COMPILE_ERROR = 8
    UNKNOWN_ERROR = 9
    SUBMIT_ERROR = 10
    QUEUING_AND_JUDGING = 11


class OnlineJudge(Enum):
    ALL = "All"
    _51NOD = "51Nod"
    ACDREAM = "ACdream"
    AIZU = "Aizu"
    ATCODER = "AtCoder"
    CODECHEF = "CodeChef"
    CODEFORCES = "CodeForces"
    CSU = "CSU"
    EIJUDGE = "EIJudge"
    EOLYMP = "EOlymp"
    FZU = "FZU"
    GYM = "Gym"
    HACKERRANK = "HackerRank"
    HDU = "HDU"
    HIHOCODER = "HihoCoder"
    HIT = "HIT"
    HUST = "HUST"
    HYSBZ = "HYSBZ"
    KATTIS = "Kattis"
    LIGHTOJ = "LightOJ"
    MINIEYE = "MiniEye"
    NBUT = "NBUT"
    OPENJ_BAILIAN = "OpenJ_Bailian"
    OPENJ_POJ = "OpenJ_POJ"
    POJ = "POJ"
    SCU = "SCU"
    SGU = "SGU"
    SPOJ = "SPOJ"
    TOPCODER = "TopCoder"
    UESTC = "UESTC"
    UESTC_OLD = "UESTC_old"
    URAL = "URAL"
    UVA = "UVA"
    UVALIVE = "UVALive"
    Z_TRENING = "Z_trening"
    ZOJ = "ZOJ"


class Language(Enum):
    ALL = ""
    CPP = "CPP"
    C = "C"
    JAVA = "JAVA"
    PASCAL = "PASCAL"
    PYTHON = "PYTHON"
    CSHARP = "CSHARP"
    RUBY = "RUBY"
    OTHER = "OTHER"


class TimeRange(Enum):
    TIME_24HOURS = 0
    TIME_7DAYS = 1
    TIME_30DAYS = 2
    OVERALL = 3
