```python
import requests
from src.utils.constants import ELEVEN_LABS_API_URL
from src.data.ai_services_data import aiServices

def connectToAIService(service_name):
    """
    Function to connect to a specific AI service from Eleven Labs.
    """
    try:
        # Check if the service is available
        if service_name not in aiServices:
            raise ValueError(f"Service {service_name} not found in Eleven Labs services.")

        # Connect to the service
        response = requests.get(f"{ELEVEN_LABS_API_URL}/{service_name}")

        # Check the response status
        if response.status_code != 200:
            raise ConnectionError(f"Failed to connect to {service_name} service.")

        return response.json()

    except Exception as e:
        print(f"Error: {str(e)}")
        return None

def updateAIServices():
    """
    Function to update the list of AI services from Eleven Labs.
    """
    try:
        # Connect to the Eleven Labs API
        response = requests.get(ELEVEN_LABS_API_URL)

        # Check the response status
        if response.status_code != 200:
            raise ConnectionError("Failed to connect to Eleven Labs API.")

        # Update the list of AI services
        aiServices = response.json()

    except Exception as e:
        print(f"Error: {str(e)}")
```