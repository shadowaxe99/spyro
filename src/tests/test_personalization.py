```python
import unittest
from src.personalization import personalizeExperience
from src.data.user_data import userProfile
from src.utils.helpers import updateProfile

class TestPersonalization(unittest.TestCase):

    def setUp(self):
        self.userProfile = userProfile
        self.personalizedExperience = personalizeExperience(self.userProfile)

    def test_personalizeExperience(self):
        self.assertIsNotNone(self.personalizedExperience, "Failed to generate personalized experience")

    def test_updateProfile(self):
        updatedProfile = updateProfile(self.userProfile, {"favorite_game": "Spyro The Dragon"})
        self.assertEqual(updatedProfile["favorite_game"], "Spyro The Dragon", "Failed to update user profile")

if __name__ == '__main__':
    unittest.main()
```