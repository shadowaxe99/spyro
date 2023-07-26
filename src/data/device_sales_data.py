```python
from datetime import datetime
from typing import List, Dict

class DeviceSalesData:
    def __init__(self):
        self.sales_data = []

    def add_sale(self, device_id: str, user_id: str, sale_date: datetime):
        sale = {
            "device_id": device_id,
            "user_id": user_id,
            "sale_date": sale_date
        }
        self.sales_data.append(sale)

    def get_sales(self) -> List[Dict]:
        return self.sales_data

    def get_sales_count(self) -> int:
        return len(self.sales_data)

deviceSalesData = DeviceSalesData()
```