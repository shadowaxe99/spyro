```python
import datetime
from src.data.subscription_data import subscriptionData
from src.utils.helpers import calculate_percentage

class SubscriptionRetention:
    def __init__(self):
        self.subscription_data = subscriptionData

    def get_active_subscriptions(self):
        active_subscriptions = [sub for sub in self.subscription_data if sub['status'] == 'active']
        return active_subscriptions

    def get_cancelled_subscriptions(self):
        cancelled_subscriptions = [sub for sub in self.subscription_data if sub['status'] == 'cancelled']
        return cancelled_subscriptions

    def calculate_retention_rate(self):
        active_subscriptions = self.get_active_subscriptions()
        cancelled_subscriptions = self.get_cancelled_subscriptions()

        if len(active_subscriptions) == 0 and len(cancelled_subscriptions) == 0:
            return 0

        retention_rate = calculate_percentage(len(active_subscriptions), len(self.subscription_data))
        return retention_rate

    def track_subscription_retention(self):
        retention_rate = self.calculate_retention_rate()
        print(f"Subscription Retention Rate: {retention_rate}%")

if __name__ == "__main__":
    subscription_retention = SubscriptionRetention()
    subscription_retention.track_subscription_retention()
```