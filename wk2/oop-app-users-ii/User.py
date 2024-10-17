class User:
    


    def __init__(self, name, email, drivers_liscence):
        self.name = name
        self.email = email
        self.drivers_liscence = drivers_liscence
        self.posts = []

    
    def create_a_post(self, post):
        self.post = post