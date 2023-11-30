import random

# Pre-defined responses
responses = {
    "hello": ["Hi there! How can I help you today?", "Hello!", "Hey, what can I do for you?"],
    "traffic update": "I'm sorry, I don't have access to real-time map information.",
    "joke": ["Why don't scientists trust atoms? Because they make up everything!", "What do you call a fish with no eyes? Fsh!", "Why did the scarecrow win an award? Because he was outstanding in his field!"],
    "story": ["Once upon a time, in a faraway land, there lived a wise old turtle...", "In a magical forest, a mischievous squirrel named Sam loved to play pranks on the other animals..."]
}

# Chatbot function
def chatbot_response(user_input):
    for keyword, response in responses.items():
        if keyword in user_input.lower():
            if isinstance(response, list):
                return random.choice(response)
            else:
                return response
    return "I'm not sure how to respond to that. Please ask something else."

# Main loop
while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)
