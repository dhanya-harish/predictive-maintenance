
from huggingface_hub import hf_hub_download
from joblib import load
import os

def load_hf_model(repo_id: str, filename: str = "best_model.joblib"):
    \"\"\"Download and load the model from Hugging Face Hub.\"\"\"
    model_path = hf_hub_download(repo_id=repo_id, filename=filename)
    model = load(model_path)
    print(f"Model loaded from Hugging Face Hub: {model_path}")
    return model

# You might want to add a function here to load the preprocessor and feature names as well
# For example:
# def load_hf_artifacts(repo_id: str, model_filename: str = "best_model.joblib", preprocessor_filename: str = "preprocessor.joblib", features_filename: str = "feature_cols.json"):
#     model = load_hf_model(repo_id, model_filename)
#     preprocessor = None
#     features = None
#     try:
#         preprocessor_path = hf_hub_download(repo_id=repo_id, filename=preprocessor_filename)
#         preprocessor = load(preprocessor_path)
#     except Exception:
#         print(f"Warning: Preprocessor file not found at {preprocessor_filename}")
#         pass # Preprocessor is optional
#     try:
#         features_path = hf_hub_download(repo_id=repo_id, filename=features_filename)
#         with open(features_path, 'r') as f:
#             features = json.load(f)
#     except Exception:
#         print(f"Warning: Feature names file not found at {features_filename}")
#         pass # Feature names are optional
#     return model, preprocessor, features

