import openai
import os
from src.utils import load_api_key

class AIAnalyzer:
    def __init__(self):
        self.api_key = load_api_key("OPENAI_API_KEY")
        openai.api_key = self.api_key

    def analyze_sentiment(self, text):
        """Uses GPT-3.5-turbo to determine sentiment of the text."""
        prompt = f"""
        Analyze the sentiment of the following text. 
        Return only a JSON object with keys: 'sentiment' (positive/negative/neutral), 'confidence' (0-1).
        
        Text: {text[:500]}  # Limiting context window for demo
        """
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=50,
            temperature=0.2
        )
        return response.choices[0].message.content.strip()

    def extract_entities(self, text):
        """Uses GPT-3.5-turbo to extract key entities (names, places, orgs)."""
        prompt = f"""
        Extract key entities (Person, Organization, Location) from the following text.
        Return a JSON list of objects with 'type' and 'value'.
        
        Text: {text[:500]}
        """
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100,
            temperature=0.2
        )
        return response.choices[0].message.content.strip()
