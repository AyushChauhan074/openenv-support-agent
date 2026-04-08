import os
from huggingface_hub import HfApi

def deploy():
    token = os.getenv("HF_TOKEN")
    if not token:
        print("HF_TOKEN missing!")
        return

    api = HfApi(token=token)
    repo_id = "ayushChauahan/support-agent-env"
    
    print(f"Creating or locating Space: {repo_id}...")
    try:
        api.create_repo(
            repo_id=repo_id,
            repo_type="space",
            space_sdk="docker",
            exist_ok=True,
            private=False
        )
    except Exception as e:
        print(f"Notice: {e}")

    print("Uploading project files to Hugging Face Spaces...")
    api.upload_folder(
        folder_path=".",
        repo_id=repo_id,
        repo_type="space",
        ignore_patterns=["venv/*", "__pycache__/*", ".git/*", ".env", "*.pyc", "output.txt"]
    )
    print(f"Successfully Deployed! Space URL: https://huggingface.co/spaces/{repo_id}")

if __name__ == "__main__":
    deploy()
