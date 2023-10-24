responses = {
    "hello": "Hello! How can I assist you today?",
    "hi": "Hi! How can I help you!",
    "who are you": "I am a chat bot.",
    "how are you": "I don't have feelings, but thanks for asking.",
    "default": "I'm sorry, I don't understand. Please ask me something else."
}

while True:
    user_input = input("You: ").lower()  

    if user_input in responses:
        print("Chatbot:", responses[user_input])
    elif "thank you" in user_input:
        print("Chatbot: You're welcome!")
    elif "help" in user_input:
        print("Chatbot: I'm here to answer your questions. Just ask away!")
    elif "bye" in user_input:
        print("Chatbot: Goodbye! Have a nice day.")
        break
    else:
        print("Chatbot:", responses["default"])
