#!/usr/bin/env python3
"""
Fixed deployment script for Hugging Face Spaces
"""
import os
from pathlib import Path
from huggingface_hub import HfApi, create_repo
from huggingface_hub.utils import RepositoryNotFoundError

def deploy_to_huggingface():
    # Configuration
    HF_TOKEN = os.environ.get("HF_TOKEN")
    SPACE_NAME = "predictive-maintenance-app"
    USERNAME = "dhanya-harish"
    
    if not HF_TOKEN:
        raise ValueError("HF_TOKEN environment variable is required")
    
    # Initialize API
    api = HfApi(token=HF_TOKEN)
    
    full_space_id = f"{USERNAME}/{SPACE_NAME}"
    
    print(f"Starting deployment to Hugging Face...")
    print(f"Space: {full_space_id}")
    
    # Step 1: Create Space if it doesn't exist
    try:
        api.repo_info(repo_id=full_space_id, repo_type="space")
        print(f"✅ Space exists: {full_space_id}")
    except RepositoryNotFoundError:
        print(f"📝 Creating new Space: {full_space_id}")
        create_repo(
            repo_id=full_space_id,
            repo_type="space",
            private=False,
            exist_ok=True,
            token=HF_TOKEN,
            space_sdk="streamlit"  # Changed from docker to streamlit for simplicity
        )
        print(f"Space created: {full_space_id}")
    
    # Step 2: Upload files to Space
    print("Uploading files to Space...")
    
    # Upload individual files to avoid LFS issues
    files_to_upload = ["app.py", "requirements.txt", "README.md"]
    
    for file in files_to_upload:
        if Path(file).exists():
            api.upload_file(
                path_or_fileobj=file,
                path_in_repo=file,
                repo_id=full_space_id,
                repo_type="space",
                commit_message=f"Add {file} via GitHub Actions",
                token=HF_TOKEN
            )
            print(f"Uploaded: {file}")
        else:
            print(f" Missing: {file}")
    
    # Upload model if exists
    model_path = Path("model/engine_model.joblib")
    if model_path.exists():
        api.upload_file(
            path_or_fileobj=str(model_path),
            path_in_repo="model/engine_model.joblib",
            repo_id=full_space_id,
            repo_type="space",
            commit_message="Add model file",
            token=HF_TOKEN
        )
        print(f"Uploaded model: {model_path}")
    
    print(f"Deployment completed!")
    print(f"Your Space is live at: https://huggingface.co/spaces/{full_space_id}")

if __name__ == "__main__":
    deploy_to_huggingface()
