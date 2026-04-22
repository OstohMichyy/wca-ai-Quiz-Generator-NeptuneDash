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
 ============================================================================
# PROMPT ENGINEER - Input & Prompt
# ============================================================================
user_input = input("Enter a topic OR paste a paragraph: ")
difficulty = input("Enter difficulty (easy/medium/hard): ")

print("\n🚀 kindly wait Generating quiz...\n")

# Detect if it's a paragraph or topic
if len(user_input.split()) > 20:
    prompt = f"""
You are a quiz generator.
Read the paragraph below and generate 5 {difficulty} multiple-choice questions.

Each question should have 4 options (A, B, C, D) and show the correct answer.

Paragraph:
{user_input}
"""
else:
    prompt = f"""
You are a quiz generator.
Generate 5 {difficulty} multiple-choice questions about the topic: "{user_input}"

Each question should have 4 options (A, B, C, D) and show the correct answer.
"""
