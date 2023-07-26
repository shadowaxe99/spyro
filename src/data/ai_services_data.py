```python
# src/data/ai_services_data.py

from src.utils.constants import AIServiceSchema

# List of AI services available from Eleven Labs
aiServices = [
    {
        "id": "service1",
        "name": "Virtual Assistant",
        "description": "AI-powered virtual assistant for managing your tasks and schedule.",
        "access": "Free"
    },
    {
        "id": "service2",
        "name": "Educational Tool",
        "description": "Interactive learning tools powered by AI for a personalized learning experience.",
        "access": "Subscription"
    },
    {
        "id": "service3",
        "name": "Entertainment",
        "description": "AI-powered games and entertainment content.",
        "access": "Subscription"
    },
    {
        "id": "service4",
        "name": "Personalized Recommendations",
        "description": "AI-powered personalized content and service recommendations based on your preferences and usage.",
        "access": "Free"
    }
]

# Validate the data against the schema
for service in aiServices:
    assert AIServiceSchema.validate(service), f"Invalid data format for {service['name']}"
```