import nltk
from nltk.chat.util import Chat, reflections

# Pairs is a list of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?"]
    ],
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you?"]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by Python.", "You can call me PyBot!"]
    ],
    [
        r"how are you?",
        ["I'm doing well, thank you!", "I'm great! How can I assist you?"]
    ],
    [
        r"sorry (.*)",
        ["It's okay!", "No worries!", "Don't worry about it."]
    ],
    [
        r"quit",
        ["Bye! Take care.", "It was nice talking to you. Goodbye!"]
    ],
    [
        r"(.*)",
        ["I didn’t understand that. Can you say it another way?"]
    ],
]

# Create chatbot instance
def chatbot():
    print("Hi! I'm PyBot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

# Run chatbot
if __name__ == "__main__":
    nltk.download('punkt')  # Required for nltk.chat
    chatbot()
