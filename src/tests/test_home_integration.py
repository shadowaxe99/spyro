```python
import unittest
from src.home_integration import integrateHomeDevice
from src.data.smart_home_data import smartHomeDevices

class TestHomeIntegration(unittest.TestCase):

    def setUp(self):
        self.device1 = {
            "deviceName": "Smart Light",
            "deviceType": "light",
            "status": "off"
        }
        self.device2 = {
            "deviceName": "Smart Thermostat",
            "deviceType": "thermostat",
            "status": "off"
        }
        smartHomeDevices.append(self.device1)
        smartHomeDevices.append(self.device2)

    def test_integrateHomeDevice(self):
        integrateHomeDevice("Smart Light", "on")
        self.assertEqual(smartHomeDevices[0]["status"], "on")
        integrateHomeDevice("Smart Thermostat", "on")
        self.assertEqual(smartHomeDevices[1]["status"], "on")

    def tearDown(self):
        smartHomeDevices.remove(self.device1)
        smartHomeDevices.remove(self.device2)

if __name__ == '__main__':
    unittest.main()
```