class user:
    user_list = []
    def __init__(self,first_name,last_name,phone_number,email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def save_user(self):
        user.user_list.append(self)
