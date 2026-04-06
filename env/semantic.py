import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def semantic_similarity(expected, response):
    prompt = f"""
Score semantic similarity between:
Expected: {expected}
Response: {response}

Return ONLY a number between 0 and 1.
"""

    try:
        res = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
        score = float(res.choices[0].message.content.strip())
        return max(0, min(1, score))
    except:
        return 0.5  # fallback
