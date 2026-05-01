

history = []

def add_memory(user, ai):
    history.append({"user": user, "ai": ai})


def get_memory(n=5):
    return history[-n:]


def clear_memory():
    history.clear()

