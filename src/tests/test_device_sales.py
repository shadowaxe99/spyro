```python
import unittest
from src.device_sales import trackDeviceSales
from src.data.device_sales_data import DeviceSalesDataSchema

class TestDeviceSales(unittest.TestCase):

    def setUp(self):
        self.device_sales_data = {
            "total_sales": 1000,
            "monthly_sales": 100,
            "daily_sales": 5
        }
        self.device_sales_schema = DeviceSalesDataSchema()

    def test_track_device_sales(self):
        result = trackDeviceSales(self.device_sales_data)
        self.assertIsNotNone(result)
        self.assertTrue(self.device_sales_schema.validate(result))

    def test_track_device_sales_no_data(self):
        with self.assertRaises(ValueError):
            trackDeviceSales(None)

    def test_track_device_sales_invalid_data(self):
        invalid_data = {
            "total_sales": "1000",
            "monthly_sales": "100",
            "daily_sales": "5"
        }
        with self.assertRaises(ValueError):
            trackDeviceSales(invalid_data)

if __name__ == '__main__':
    unittest.main()
```