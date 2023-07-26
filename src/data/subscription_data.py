```python
from datetime import datetime
from marshmallow import Schema, fields

class SubscriptionData:
    def __init__(self, user_id, subscription_status, subscription_type, start_date, end_date):
        self.user_id = user_id
        self.subscription_status = subscription_status
        self.subscription_type = subscription_type
        self.start_date = start_date
        self.end_date = end_date

class SubscriptionDataSchema(Schema):
    user_id = fields.Str(required=True)
    subscription_status = fields.Str(required=True)
    subscription_type = fields.Str(required=True)
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)

subscriptionData = [
    SubscriptionData("user1", "active", "premium", datetime(2022, 1, 1), datetime(2023, 1, 1)),
    SubscriptionData("user2", "inactive", "basic", datetime(2022, 2, 1), datetime(2023, 2, 1)),
    SubscriptionData("user3", "active", "premium", datetime(2022, 3, 1), datetime(2023, 3, 1)),
]
```