```python
import time
from src.data.user_data import userProfile

class UserEngagement:
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.total_time = 0
        self.interactions = 0

    def start_interaction(self):
        self.start_time = time.time()

    def end_interaction(self):
        self.end_time = time.time()
        self.total_time += self.end_time - self.start_time
        self.interactions += 1

    def get_average_interaction_time(self):
        if self.interactions == 0:
            return 0
        return self.total_time / self.interactions

    def get_total_interaction_time(self):
        return self.total_time

    def get_total_interactions(self):
        return self.interactions

    def update_user_profile(self):
        userProfile['average_interaction_time'] = self.get_average_interaction_time()
        userProfile['total_interaction_time'] = self.get_total_interaction_time()
        userProfile['total_interactions'] = self.get_total_interactions()

userEngagement = UserEngagement()
```