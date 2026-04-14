# utils/session.py

import time


class SessionManager:
    def __init__(self, timeout=30):
        self.timeout = timeout  # seconds
        self.last_activity = time.time()

    def update_activity(self):
        self.last_activity = time.time()

    def is_session_active(self):
        return (time.time() - self.last_activity) < self.timeout