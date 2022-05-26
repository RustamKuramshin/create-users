class User:
    user_name: str
    user_surname: str
    user_patronymic: str
    user_phone: str
    email: str
    role_id: int
    realm_id: int
    user_id: int
    password_hash: str

    def __init__(self,
                 user_name: str,
                 user_surname: str,
                 user_patronymic: str,
                 user_phone: str,
                 email: str,
                 role_id: int,
                 realm_id: int,
                 user_id: int,
                 password_hash: str):

        self.user_name = user_name
        self.user_surname = user_surname
        self.user_patronymic = user_patronymic
        self.user_phone = user_phone
        self.email = email
        self.role_id = role_id
        self.realm_id = realm_id
        self.user_id = user_id
        self.password_hash = password_hash

    def __repr__(self):
        return f'User(user_name={self.user_name}, user_surname={self.user_surname}, user_id={self.user_id})'
