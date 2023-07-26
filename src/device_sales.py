```python
import datetime
from data.device_sales_data import DeviceSalesDataSchema

class DeviceSales:
    def __init__(self):
        self.device_sales_data = DeviceSalesDataSchema()

    def trackDeviceSales(self, device_id, user_id):
        sale_date = datetime.datetime.now()
        new_sale = {
            "device_id": device_id,
            "user_id": user_id,
            "sale_date": sale_date
        }
        self.device_sales_data.append(new_sale)

    def getDeviceSales(self):
        return self.device_sales_data

    def updateDeviceSales(self, message):
        if message == "updateDeviceSales":
            device_id = message.get("device_id")
            user_id = message.get("user_id")
            self.trackDeviceSales(device_id, user_id)

device_sales = DeviceSales()
```