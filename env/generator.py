import random

CATEGORIES = ["Billing", "Technical", "Account", "Delivery"]
URGENCY = ["low", "medium", "high"]

TEMPLATES = [
    "I was charged twice for my order",
    "App crashes when I try to upload files",
    "Cannot login to my account",
    "My delivery is delayed and no update"
]

NOISE = [
    "pls fix asap",
    "??",
    "wtf",
    "idk what's happening"
]

def generate_ticket():
    base = random.choice(TEMPLATES)
    category = (
        "Billing" if "charged" in base else
        "Technical" if "crashes" in base else
        "Account" if "login" in base else
        "Delivery"
    )

    urgency = random.choice(URGENCY)

    noisy_query = base + " " + random.choice(NOISE)

    return {
        "query": noisy_query,
        "category": category,
        "urgency": urgency,
        "complexity": round(random.uniform(0.7, 1.5), 2),
        "sentiment": random.choice(["neutral", "annoyed", "angry"])
    }
