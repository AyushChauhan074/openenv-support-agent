import random

TASKS = {
    "easy": {
        "query": "Payment failed but amount deducted",
        "category": "Billing",
        "urgency": "medium",
        "complexity": 0.8,
        "sentiment": "neutral"
    },
    "medium": {
        "query": "App crashes while uploading files",
        "category": "Technical",
        "urgency": "high",
        "complexity": 1.0,
        "sentiment": "annoyed"
    },
    "hard": {
        "query": "Charged twice and app not working fix immediately",
        "category": "Billing",
        "urgency": "high",
        "complexity": 1.3,
        "sentiment": "angry"
    }
}

def inject_noise(query):
    noise = [
        "pls help asap",
        "idk what's happening",
        "wtf app broken",
        "?? urgent"
    ]
    return query + " " + random.choice(noise)
