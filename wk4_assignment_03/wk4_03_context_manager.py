import json
import os

def load_business_context():
    """Loads the identity data for Digital Prosperity Hub."""
    file_path = "wk4_03_business_context.json"
    
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)
    else:
        # Fallback if the file is missing
        return {
            "user_profile": {"name": "Karthik", "company": "Digital Prosperity Hub"},
            "business_details": {}
        }

def get_signature():
    context = load_business_context()
    return context.get("user_profile", {}).get("signature", "")