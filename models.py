all_questions = []
all_answers = []
all_users=[]

class User(object):
    def __init__(self, email, password):
        self.email = email
        self.password = password
        all_users.append(self)

    def login(self):
        pass

    def post_question(self, quiz_id, title, description, date_created, date_modified):
        question = Question(quiz_id,title, description, date_created, date_modified)
        all_questions.append(question)
        # print("I am here")
        # print(all_questions)

    def ans_question(self, ans_id, title, description, date_created, date_modified):
        answer = Answer(ans_id, title, description, date_created, date_modified)
        all_answers.append(answer)

    def view_questions(self):
        print(all_questions)

    def view_answers(self):
        print(all_answers)

    def accept_answers(self):
        pass

    def get_username(self):
        pass


class Question(object):
    def __init__(self, quiz_id, title, description, date_created, date_modified):
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


if __name__ == "__main__":
    user = User("Allan Mogusu", "Allan")
    # admin = Admin("Allan Nyagwachi", "Mogusu")
    user.post_question('1','Python', 'How to install python3','12.3.2018','27.4.2018')
    user.view_questions()



