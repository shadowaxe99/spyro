```python
import unittest
from src.subscription_services import manageSubscription
from src.data.subscription_data import subscriptionData

class TestSubscriptionRetention(unittest.TestCase):

    def setUp(self):
        self.subscriptionData = subscriptionData

    def test_subscription_retention(self):
        # Test if the subscription retention rate is being calculated correctly
        total_subscriptions = len(self.subscriptionData)
        retained_subscriptions = len([data for data in self.subscriptionData if data['status'] == 'active'])
        expected_retention_rate = retained_subscriptions / total_subscriptions

        actual_retention_rate = manageSubscription.calculate_retention_rate(self.subscriptionData)
        self.assertEqual(expected_retention_rate, actual_retention_rate)

if __name__ == '__main__':
    unittest.main()
```