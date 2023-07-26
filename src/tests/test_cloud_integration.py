```python
import unittest
from unittest.mock import patch
from src.cloud_integration import connectToAIService

class TestCloudIntegration(unittest.TestCase):

    @patch('src.cloud_integration.requests.get')
    def test_connectToAIService(self, mock_get):
        # Mocking the response from the AI service
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'service_name': 'AI Service 1',
            'status': 'connected'
        }

        # Test successful connection
        response = connectToAIService('AI Service 1')
        self.assertEqual(response['service_name'], 'AI Service 1')
        self.assertEqual(response['status'], 'connected')

        # Test unsuccessful connection
        mock_get.return_value.status_code = 404
        response = connectToAIService('AI Service 2')
        self.assertEqual(response, 'Unable to connect to AI Service 2')

if __name__ == '__main__':
    unittest.main()
```