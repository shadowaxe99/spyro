```python
class UserProfile:
    def __init__(self, user_id, name, preferences, interaction_history):
        self.user_id = user_id
        self.name = name
        self.preferences = preferences
        self.interaction_history = interaction_history

userProfile = []

def add_user(user_id, name, preferences, interaction_history):
    new_user = UserProfile(user_id, name, preferences, interaction_history)
    userProfile.append(new_user)

def get_user(user_id):
    for user in userProfile:
        if user.user_id == user_id:
            return user
    return None

def update_user(user_id, name=None, preferences=None, interaction_history=None):
    user = get_user(user_id)
    if user:
        if name:
            user.name = name
        if preferences:
            user.preferences = preferences
        if interaction_history:
            user.interaction_history = interaction_history

def delete_user(user_id):
    user = get_user(user_id)
    if user:
        userProfile.remove(user)
```