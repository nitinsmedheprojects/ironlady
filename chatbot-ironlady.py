# chatbot.py
from fuzzywuzzy import process

# FAQs with synonyms
faq_data = {
    "programs": {
        "questions": ["what programs does iron lady offer", "programs", "courses", "training", "options"],
        "answer": "Iron Lady offers leadership programs focused on confidence, communication, and growth for women professionals."
    },
    "duration": {
        "questions": ["what is the program duration", "duration", "how long", "time", "length"],
        "answer": "The program duration varies, but most programs run for 8 to 12 weeks."
    },
    "mode": {
        "questions": ["is the program online or offline", "mode", "online", "offline", "class type"],
        "answer": "The programs are primarily conducted online for flexibility, with occasional offline workshops."
    },
    "certificate": {
        "questions": ["are certificates provided", "certificate", "completion proof", "certification"],
        "answer": "Yes, certificates are provided upon successful completion of the program."
    },
    "mentors": {
        "questions": ["who are the mentors", "coaches", "mentors", "trainers", "teachers"],
        "answer": "Our mentors are experienced leaders, industry professionals, and certified coaches."
    }
}

faq_menu = """
Here are some popular questions you can ask:
1. What programs does Iron Lady offer?
2. What is the program duration?
3. Is the program online or offline?
4. Are certificates provided?
5. Who are the mentors/coaches?
"""

# Flatten questions for fuzzy matching
all_questions = []
q_to_key = {}
for key, value in faq_data.items():
    for q in value["questions"]:
        all_questions.append(q)
        q_to_key[q] = key

def chatbot():
    print("🤖 Iron Lady Chatbot: Hello! Welcome to Iron Lady’s Leadership Program assistant.")
    name = input("🤖 Chatbot: May I know your name? \nYou: ").strip().title()
    if not name:
        name = "Friend"
    print(f"🤖 Chatbot: Nice to meet you, {name}! 🌸")
    print("🤖 Chatbot: You can ask me about Iron Lady’s programs. Type 'exit' anytime to end.")
    print(faq_menu)

    last_topic = None  # to remember context

    while True:
        user_input = input(f"\n{name}: ").lower().strip()

        if user_input in ["exit", "quit", "bye"]:
            print(f"🤖 Chatbot: Thank you, {name}, for your interest in Iron Lady. Have a wonderful day! 🌟")
            break

        # If user types a number, map it
        if user_input.isdigit() and int(user_input) in range(1, 6):
            mapping = {
                "1": "programs",
                "2": "duration",
                "3": "mode",
                "4": "certificate",
                "5": "mentors"
            }
            key = mapping[user_input]
            print(f"🤖 Chatbot: {faq_data[key]['answer']}")
            last_topic = key
            continue

        # Context awareness (follow-up questions like "how long?")
        if last_topic and user_input in ["how long", "duration", "time"]:
            print(f"🤖 Chatbot: {faq_data['duration']['answer']}")
            continue

        # Fuzzy match with synonyms
        best_match, score = process.extractOne(user_input, all_questions)
        if score >= 70:  # good match
            key = q_to_key[best_match]
            print(f"🤖 Chatbot: {faq_data[key]['answer']}")
            last_topic = key
        else:
            print(f"🤖 Chatbot: I didn’t quite get that, {name}. Here are some things you can ask me:")
            print(faq_menu)

if __name__ == "__main__":
    chatbot()
