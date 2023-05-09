class User:
    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
    
    def getUserName(self):
        return self.name

    def getUserEmail(self):
        return self.email
    
    def getUserPassword(self):
        return self.password
    
