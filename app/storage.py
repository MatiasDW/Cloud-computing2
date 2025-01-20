# app/storage.py
class Storage:
    """
    Centralized storage for in-memory databases.
    """
    def __init__(self):
        self.users_db = {}  # In-memory storage for user data
        self.sessions_db = {}  # In-memory storage for session data


# Instantiate a global storage object
storage = Storage()
