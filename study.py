import random

# Predefined responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
    "how are you": ["I'm a bot, so always good!", "Doing great, thanks!", "Ready to assist you."],
    "help": [
        "I can answer questions about your study schedule, give tips, or just chat!", 
        "Try asking me about deadlines or how to stay focused."
    ],
    "bye": ["Goodbye!", "See you later!", "Have a great day!"],
    "joke": [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why did the computer get cold? Because it forgot to close Windows!"
    ],
    "default": [
        "Sorry, I didn't get that. Can you try asking something else?", 
        "I'm not sure about that. Try asking in a different way."
    ]
}

def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])

def main():
    print("Welcome to StudyBot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if "bye" in user_input.lower():
            print("StudyBot: " + random.choice(responses["bye"]))
            break
        response = get_response(user_input)
        print("StudyBot: " + response)

if __name__ == "__main__":
    main()