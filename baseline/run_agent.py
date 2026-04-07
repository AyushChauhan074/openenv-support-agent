import requests

BASE = "http://localhost:7860"

def run(task):
    requests.post(f"{BASE}/reset", params={"task_name": task})

    actions = [
        {"action_type": "classify", "content": "Billing"},
        {"action_type": "prioritize", "content": "high"},
        {"action_type": "respond", "content": "Sorry for the issue. We are fixing it."},
        {"action_type": "resolve", "content": "Billing issue resolved"}
    ]

    for a in actions:
        requests.post(f"{BASE}/step", json=a)

    score = requests.post(f"{BASE}/grader").json()
    return score

if __name__ == "__main__":
    for t in ["easy", "medium", "hard"]:
        print(t, run(t))