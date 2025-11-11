
# Write deployment script
#!/usr/bin/env python3
"""
Deployment script for Hugging Face Spaces
"""
import os
import shutil
from pathlib import Path
from huggingface_hub import HfApi, create_repo, upload_folder, upload_file
from huggingface_hub.utils import RepositoryNotFoundError

def deploy_to_huggingface():
    # Configuration
    HF_TOKEN = os.environ.get("HF_TOKEN")
    SPACE_NAME = os.environ.get("SPACE_NAME", "predictive-maintenance-app")
    MODEL_REPO = os.environ.get("MODEL_REPO", "predictive-maintenance-model")
    USERNAME = "dhanya-harish"  # Change to your HF username
    
    if not HF_TOKEN:
        raise ValueError("HF_TOKEN environment variable is required")
    
    # Initialize API
    api = HfApi(token=HF_TOKEN)
    
    full_space_id = f"{USERNAME}/{SPACE_NAME}"
    full_model_id = f"{USERNAME}/{MODEL_REPO}"
    
    print(f"Starting deployment to Hugging Face...")
    print(f"Space: {full_space_id}")
    print(f"Model: {full_model_id}")
    
    # Step 1: Upload model if exists
    model_path = Path("model/engine_model.joblib")
    if model_path.exists():
        print(f"Uploading model: {model_path}")
        try:
            create_repo(
                repo_id=full_model_id,
                repo_type="model",
                private=False,
                exist_ok=True,
                token=HF_TOKEN
            )
            
            upload_file(
                path_or_fileobj=str(model_path),
                path_in_repo=model_path.name,
                repo_id=full_model_id,
                repo_type="model",
                token=HF_TOKEN,
                commit_message="Auto-deploy model via GitHub Actions"
            )
            print(f" Model uploaded: https://huggingface.co/{full_model_id}")
        except Exception as e:
            print(f" Model upload failed: {e}")
    else:
        print("No model found to upload")
    
    # Step 2: Deploy Space
    print("Deploying Space...")
    
    # Create Space if doesn't exist
    try:
        api.repo_info(repo_id=full_space_id, repo_type="space")
        print(f"Space exists: {full_space_id}")
    except RepositoryNotFoundError:
        create_repo(
            repo_id=full_space_id,
            repo_type="space",
            private=False,
            exist_ok=True,
            token=HF_TOKEN,
            space_sdk="docker"  # or "streamlit", "gradio"
        )
        print(f"Space created: {full_space_id}")
    
    # Upload necessary files
    required_files = ["Dockerfile", "requirements.txt", "app.py", "README.md"]
    
    for file in required_files:
        if not Path(file).exists():
            print(f"Missing required file: {file}")
    
    # Upload files to Space
    upload_folder(
        folder_path=".",
        repo_id=full_space_id,
        repo_type="space",
        token=HF_TOKEN,
        commit_message="Auto-deploy via GitHub Actions CI/CD",
        ignore_patterns=[".git", ".github", "tests", "notebooks", "*.ipynb"]
    )
    
    print(f"Space deployed: https://huggingface.co/spaces/{full_space_id}")
    
    # Restart space to trigger rebuild
    try:
        api.restart_space(repo_id=full_space_id, token=HF_TOKEN)
        print("Space restart triggered")
    except Exception as e:
        print(f"Space restart not available: {e}")

if __name__ == "__main__":
    deploy_to_huggingface()
