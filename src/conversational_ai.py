```python
import nltk
from nltk.chat.util import Chat, reflections
from src.data.user_data import userProfile

class ConversationalAI:
    def __init__(self):
        self.reflections = reflections
        self.sets = [
            [r'my name is (.*)', ['Hello %1, How are you today ?',]],
            [r'hi|hey|hello', ['Hello', 'Hey there',]],
            [r'quit', ['Bye bye. It was nice talking to you.!!', 'It was nice talking to you. See you soon :)']],
            [r'(.*) (happy|funny|good) ?', ['%1 %2']],
            [r'(.*) (sad|bad) ?', ['%1 %2']],
            [r'i need (.*)', ['Why do you need %1 ?',]],
            [r'i am (.*)', ['How does being %1 make you feel ?',]],
            [r'(.*) age?', ['I am a computer program, so I don\'t have an age',]],
            [r'(.*) (location|city) ?', 'I am a computer program, I don\'t have a location'],
            [r'how is weather in (.*)?', ['I do not have access to weather data. But I can find that information for you from the web.',]],
            [r'(.*)', ['I didn\'t understand that. Can you please rephrase your question or statement?',]],
        ]

    def initiateConversation(self, user_input):
        chat = Chat(self.sets, self.reflections)
        chat.converse(user_input)

    def personalizeExperience(self):
        user_name = userProfile.get('name', 'User')
        self.sets.append([r'my name is (.*)', [f'Hello {user_name}, How are you today ?',]])

conversational_ai = ConversationalAI()

def startConversation(user_input):
    conversational_ai.initiateConversation(user_input)

def updatePersonalization():
    conversational_ai.personalizeExperience()
```