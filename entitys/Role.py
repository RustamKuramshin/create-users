from typing import Dict


class Role:
    role_name_to_id: Dict[str, int] = {}

    def __init__(self,
                 role_id: int,
                 name: str,
                 realm_id: int):
        self.role_id = role_id
        self.name = name
        self.realm_id = realm_id

    def __repr__(self):
        return f'Role(role_id={self.role_id}, name={self.name}, realm_id={self.realm_id})'
