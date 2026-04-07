import gradio as gr
import requests
import os

BASE = "http://localhost:7860"

def reset_env():
    try:
        res = requests.post(f"{BASE}/reset")
        return res.json()
    except Exception as e:
        return {"error": str(e)}

def step_env(action_type, content):
    try:
        res = requests.post(
            f"{BASE}/step",
            json={"action_type": action_type, "content": content}
        )
        return res.json()
    except Exception as e:
        return {"error": str(e)}

def get_score():
    try:
        res = requests.post(f"{BASE}/grader")
        return res.json()
    except Exception as e:
        return {"error": str(e)}

with gr.Blocks(title="Support Agent OpenEnv") as app:
    gr.Markdown("# Support Agent Environment — ScalorX")
    gr.Markdown("Interact with the RL environment directly through this dashboard.")

    with gr.Row():
        with gr.Column():
            reset_btn = gr.Button("Reset Environment")
            action_type = gr.Dropdown(
                ["classify", "prioritize", "respond", "resolve"], 
                label="Action Type"
            )
            content = gr.Textbox(label="Content (Value / Text)")
            step_btn = gr.Button("Send Action")
            score_btn = gr.Button("Final Score")

        with gr.Column():
            gr.Markdown("### Current Observation / State")
            output = gr.JSON()

    reset_btn.click(reset_env, outputs=output)
    step_btn.click(step_env, inputs=[action_type, content], outputs=output)
    score_btn.click(get_score, outputs=output)

if __name__ == "__main__":
    app.launch(server_name="localhost", server_port=7861)
