
from memory import add_memory, get_memory, clear_memory
from llm import get_response

def build_prompt(user_input):
    context = ""

    for m in get_memory():
        context += f"User: {m['user']}\nAI: {m['ai']}\n"

    context += f"User: {user_input}\nAI:"
    return context

def chat():
    print("\nAI Assistant (exit / memory / clear)\n")

    while True:
        user = input("You: ")

        if user == "exit":
            break

        if user == "memory":
            print(get_memory())
            continue

        if user == "clear":
            clear_memory()
            print("Memory cleared.")
            continue

        prompt = build_prompt(user)
        response = get_response(prompt)

        print("AI:", response, "\n")

        add_memory(user, response)


if __name__ == "__main__":
    chat()

