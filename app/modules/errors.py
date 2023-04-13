class InvalidUserId(Exception):
    def __init__(self, user_id: str):
        self.user_id: str = user_id
