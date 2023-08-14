#TODO: Nothing -:

class User:
    def __init__(self, username: str, fullname: str, role: str, logged_in: bool) -> None:
        self.username = username
        self.fullname = fullname
        self.role = role
        self.logged_in = logged_in