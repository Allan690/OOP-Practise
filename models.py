all_questions = []
all_answers = []


class User(object):
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password
        self.users = {}

    def login(self):
        pass

    def post_questions(self):
        pass

    def ans_questions(self):
        pass

    def view_answers(self):
        pass

    def accept_answers(self):
        pass

    def get_username(self):
        pass


class Question(object):
    def __init__(self, quiz_id, description, date_created, date_modified):
        self.quiz_id = quiz_id
        self.description = description
        self.date_created = date_created
        self.date_modified = date_modified


class Answer(object):
    def __init__(self, ans_id, title, description, date_created, date_modified):
        self.ans_id = ans_id
        self.title = title
        self.description = description
        self.date_created = date_created
        self.date_modified = date_modified


class Admin(User):
    def __init__(self, username, password):
        super(Admin, self).__init__(username, password)


if __name__ == "main":
    user = User("Allan Mogusu", "Allan")
    admin = Admin("Allan Nyagwachi", "Mogusu")



