```python
import unittest
from src.monetization import manageSubscription, trackDeviceSales
from src.data.subscription_data import subscriptionData
from src.data.device_sales_data import deviceSalesData

class TestMonetization(unittest.TestCase):

    def setUp(self):
        self.subscriptionData = subscriptionData
        self.deviceSalesData = deviceSalesData

    def test_manageSubscription(self):
        result = manageSubscription(self.subscriptionData)
        self.assertIsNotNone(result)
        self.assertEqual(result['status'], 'success')

    def test_trackDeviceSales(self):
        result = trackDeviceSales(self.deviceSalesData)
        self.assertIsNotNone(result)
        self.assertEqual(result['status'], 'success')

if __name__ == '__main__':
    unittest.main()
```