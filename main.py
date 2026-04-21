import requests
import json

print("Yoo! welcome to Quiz Generator ")

# ============================================================================
#  API LEAD - API Configuration
# ============================================================================
api_key = "your-openai-api-key"

def get_headers():
    return {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
