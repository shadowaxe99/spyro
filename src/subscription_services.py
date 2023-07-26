```python
import json
from src.data.subscription_data import subscriptionData
from src.utils.constants import SubscriptionDataSchema

class SubscriptionService:
    def __init__(self):
        self.subscription_data = subscriptionData

    def manage_subscription(self, user_id, action, subscription_type=None):
        user_subscription = self.get_user_subscription(user_id)
        if action == 'subscribe':
            return self.subscribe(user_subscription, subscription_type)
        elif action == 'unsubscribe':
            return self.unsubscribe(user_subscription)
        else:
            return {"error": "Invalid action"}

    def get_user_subscription(self, user_id):
        for data in self.subscription_data:
            if data['user_id'] == user_id:
                return data
        return None

    def subscribe(self, user_subscription, subscription_type):
        if user_subscription:
            user_subscription['subscription_type'] = subscription_type
            user_subscription['status'] = 'active'
            return user_subscription
        else:
            return {"error": "User not found"}

    def unsubscribe(self, user_subscription):
        if user_subscription:
            user_subscription['status'] = 'inactive'
            return user_subscription
        else:
            return {"error": "User not found"}

    def update_subscription_data(self):
        with open('src/data/subscription_data.py', 'w') as file:
            file.write(json.dumps(self.subscription_data, indent=4))

    def validate_subscription_data(self, data):
        schema = SubscriptionDataSchema()
        errors = schema.validate(data)
        if errors:
            return False
        return True
```