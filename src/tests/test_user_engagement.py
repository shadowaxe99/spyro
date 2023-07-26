```python
import unittest
from src.user_engagement import UserEngagement

class TestUserEngagement(unittest.TestCase):

    def setUp(self):
        self.user_engagement = UserEngagement()

    def test_track_user_interactions(self):
        interaction_count = self.user_engagement.track_interactions()
        self.assertIsInstance(interaction_count, int)
        self.assertGreaterEqual(interaction_count, 0)

    def test_track_time_spent(self):
        time_spent = self.user_engagement.track_time_spent()
        self.assertIsInstance(time_spent, float)
        self.assertGreaterEqual(time_spent, 0.0)

if __name__ == '__main__':
    unittest.main()
```