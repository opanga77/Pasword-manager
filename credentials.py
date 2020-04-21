class Info:
    info_list = []

    def __init__(self,face_bookp,email_p):
        self.face_bookp =face_bookp
        self.email_p = email_p

#the function below saves credentias
    def save_info(self):
        Info.info_list.append(self)

#the function below deletes credentials
    def delete_info(self):
        Info.info_list.remove(self)

#below here class mothod used to involve the whole class and displays it
    @classmethod
    def display_info(cls):
        return cls.info_list