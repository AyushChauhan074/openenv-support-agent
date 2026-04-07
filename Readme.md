# 🚀 Advanced Customer Support OpenEnv

## 🧠 Overview

This project implements a **realistic reinforcement learning environment** simulating customer support workflows. Unlike traditional toy environments, this system introduces **dynamic tasks, multi-step dependencies, and behavioral reward shaping**, making it suitable for evaluating intelligent agents in real-world scenarios.

---

## 🎯 Key Features

### ✅ Dynamic Task Generation
- Generates **infinite realistic support tickets** via `env/generator.py`
- Includes noise, ambiguity, and varying difficulty
- Covers categories: Billing, Technical, Account, Delivery

### ✅ Multi-Step Decision Environment
Agents must follow a structured workflow:
1.  **Classify** the issue
2.  **Prioritize** urgency
3.  **Respond** appropriately
4.  **Resolve** the issue

Each step affects future rewards and system state (e.g., resolving before classifying is heavily penalized).

### ✅ Advanced Reward System
- Dense reward shaping (not binary)
- Penalizes incorrect sequencing and inefficiency
- Rewards correct reasoning, empathy in responses, and resolution quality.

### ✅ Hybrid Grader (Deterministic + Semantic)
- Deterministic scoring for fairness
- LLM-based semantic scoring (`gpt-4o-mini`) evaluates response quality
- Final score integrates accuracy, response quality, efficiency, and customer satisfaction.

### ✅ Realistic Customer Simulation
- Sentiment-aware (neutral, annoyed, angry)
- Satisfaction score evolves based on agent behavior
- Hidden complexity affects scoring difficulty

### ✅ Interactive UI (Gradio)
- Live environment interaction
- Step-by-step agent simulation
- Real-time scoring display

---

## 🏗️ Environment Design

### Observation
```json
{
  "ticket_id": "T1",
  "customer_query": "...",
  "history": [],
  "resolved": false,
  "satisfaction": 0.5
}
```

### Actions
- `classify`
- `prioritize`
- `respond`
- `resolve`

---

## 🧪 Evaluation Metrics

| Component        | Weight |
| ---------------- | ------ |
| Classification   | 20%    |
| Prioritization   | 20%    |
| Response Quality | 20%    |
| Resolution       | 20%    |
| Efficiency       | 10%    |
| Satisfaction     | 10%    |

## 📋 Task Descriptions & Difficulties

The environment ships with 4 carefully graded static tasks to evaluate agents:

1. **Easy (`easy`)**: User queries that a payment failed but amount was deducted.
   * **Difficulty:** Low complexity (0.8), neutral sentiment.
   * **Objective:** Correctly classify as "Billing", assign "medium" priority, and respond effectively.
2. **Medium (`medium`)**: User complains the app crashes while uploading files.
   * **Difficulty:** Higher complexity (1.0), annoyed sentiment.
   * **Objective:** Classify as "Technical", recognize "high" priority, and respond with empathy before resolving.
3. **Hard (`hard`)**: User states they were charged twice, app is broken, and demands an immediate fix.
   * **Difficulty:** Highest complexity (1.3), angry sentiment, overlapping categories.
   * **Objective:** Address "Billing" issues, escalate "high" priority, de-escalate the user's anger, and sequentially resolve.
4. **Expert (`expert`)**: User claims their account was hacked and unauthorized orders were placed.
   * **Difficulty:** Extreme complexity (1.6), angry sentiment, panic state.
   * **Objective:** Identify critical "Account" breach, flag "high" urgency, prioritize safety in the response over everything else, and resolve only when secure.

---

## 📈 Baseline Scores

Running the provided `inference.py` using standard LLM models reliably outputs the following baseline trajectory scores across the available tasks:
- **Easy Task:** `~0.85 - 0.95`
- **Medium Task:** `~0.80 - 0.90`
- **Hard Task:** `~0.75 - 0.85`
- **Expert Task:** `~0.65 - 0.75`

*(Scores naturally fluctuate based on the semantic variations in the LLM's dynamically generated responses).*

---

## 🚀 Run Locally

### 1. Set OpenAI API Key
```bash
export OPENAI_API_KEY="your_api_key_here"
```

### 2. Start API Server
```bash
python api/server.py
```

### 3. Start Gradio UI
```bash
python app.py
```

---

## 🐳 Deployment (Docker)

```bash
docker build -t scalorx-openenv .
docker run -p 7860:7860 -p 7861:7861 -e OPENAI_API_KEY=$OPENAI_API_KEY scalorx-openenv
```

---

## 💡 Why This Stands Out
- Not a toy environment → real-world simulation
- Not binary scoring → behavioral evaluation
- Not static → infinite dynamic tasks
- Not easy to exploit → multi-layer reward + penalties
"# openenv-support-agent" 
# openenv-support-agent
