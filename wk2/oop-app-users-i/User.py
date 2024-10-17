class User:
    all_posts = []

    def __init__(self, name, email, drivers_license=None):
        self.name = name
        self.email = email
        self.drivers_license = drivers_license