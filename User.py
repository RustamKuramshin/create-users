class User:
    name: str
    email: str
    role: str

    def __init__(self, name: str, email: str, role: str):
        self.name = name
        self.email = email
        self.role = role

    def __repr__(self):
        return f'User(name={self.name}, email={self.email}, role={self.role})'