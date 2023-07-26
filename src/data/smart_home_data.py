```python
from src.utils.constants import SmartHomeDeviceSchema

# Mock data for smart home devices
smartHomeDevices = [
    {
        "device_id": "device_1",
        "device_name": "Living Room Lights",
        "device_type": "lights",
        "status": "off",
        "compatible_with": ["voice_commands"]
    },
    {
        "device_id": "device_2",
        "device_name": "Kitchen Thermostat",
        "device_type": "thermostat",
        "status": "on",
        "temperature": 22,
        "compatible_with": ["voice_commands", "temperature_control"]
    },
    {
        "device_id": "device_3",
        "device_name": "Bedroom TV",
        "device_type": "tv",
        "status": "off",
        "compatible_with": ["voice_commands", "channel_control", "volume_control"]
    }
]

def validate_smart_home_data():
    for device in smartHomeDevices:
        SmartHomeDeviceSchema().load(device)
```