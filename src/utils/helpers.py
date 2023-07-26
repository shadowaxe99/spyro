```python
import json
from src.data.user_data import UserProfileSchema
from src.data.ai_services_data import AIServiceSchema
from src.data.smart_home_data import SmartHomeDeviceSchema
from src.data.subscription_data import SubscriptionDataSchema
from src.data.device_sales_data import DeviceSalesDataSchema

def validate_data(data, schema):
    try:
        json.loads(data)
        schema.load(data)
        return True
    except Exception as e:
        print(f"Data validation error: {str(e)}")
        return False

def update_user_profile(userProfile, new_data):
    if validate_data(new_data, UserProfileSchema):
        userProfile.update(new_data)
        return True
    return False

def update_ai_services(aiServices, new_data):
    if validate_data(new_data, AIServiceSchema):
        aiServices.update(new_data)
        return True
    return False

def update_smart_home_devices(smartHomeDevices, new_data):
    if validate_data(new_data, SmartHomeDeviceSchema):
        smartHomeDevices.update(new_data)
        return True
    return False

def update_subscription_data(subscriptionData, new_data):
    if validate_data(new_data, SubscriptionDataSchema):
        subscriptionData.update(new_data)
        return True
    return False

def update_device_sales_data(deviceSalesData, new_data):
    if validate_data(new_data, DeviceSalesDataSchema):
        deviceSalesData.update(new_data)
        return True
    return False
```