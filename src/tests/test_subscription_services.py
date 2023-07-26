```python
import unittest
from src.subscription_services import manageSubscription

class TestSubscriptionServices(unittest.TestCase):

    def setUp(self):
        self.userProfile = {
            "name": "Test User",
            "subscriptionStatus": "active",
            "subscriptionType": "premium",
            "subscriptionStartDate": "2021-01-01",
            "subscriptionEndDate": "2022-01-01"
        }
        self.subscriptionData = {
            "subscriptionType": "premium",
            "subscriptionPrice": 19.99,
            "subscriptionFeatures": ["exclusive content", "games", "features"]
        }

    def test_manageSubscription(self):
        result = manageSubscription(self.userProfile, self.subscriptionData)
        self.assertEqual(result["subscriptionStatus"], "active")
        self.assertEqual(result["subscriptionType"], "premium")
        self.assertEqual(result["subscriptionPrice"], 19.99)
        self.assertIn("exclusive content", result["subscriptionFeatures"])
        self.assertIn("games", result["subscriptionFeatures"])
        self.assertIn("features", result["subscriptionFeatures"])

if __name__ == '__main__':
    unittest.main()
```