```python
import json
from src.data.user_data import UserProfileSchema
from src.data.ai_services_data import AIServiceSchema
from src.data.smart_home_data import SmartHomeDeviceSchema
from src.data.subscription_data import SubscriptionDataSchema
from src.data.device_sales_data import DeviceSalesDataSchema

def load_json_data(file_path, schema):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return schema().load(data)

def save_json_data(file_path, data, schema):
    with open(file_path, 'w') as file:
        json.dump(schema().dump(data), file)

def update_user_profile(userProfile, new_data):
    userProfile.update(new_data)
    save_json_data('src/data/user_data.py', userProfile, UserProfileSchema)

def update_ai_services(aiServices, new_data):
    aiServices.update(new_data)
    save_json_data('src/data/ai_services_data.py', aiServices, AIServiceSchema)

def update_smart_home_devices(smartHomeDevices, new_data):
    smartHomeDevices.update(new_data)
    save_json_data('src/data/smart_home_data.py', smartHomeDevices, SmartHomeDeviceSchema)

def update_subscription_data(subscriptionData, new_data):
    subscriptionData.update(new_data)
    save_json_data('src/data/subscription_data.py', subscriptionData, SubscriptionDataSchema)

def update_device_sales_data(deviceSalesData, new_data):
    deviceSalesData.update(new_data)
    save_json_data('src/data/device_sales_data.py', deviceSalesData, DeviceSalesDataSchema)
```