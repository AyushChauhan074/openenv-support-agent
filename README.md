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
