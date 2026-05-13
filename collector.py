import requests
from bs4 import BeautifulSoup
import yaml
import logging

class OSINTCollector:
    def __init__(self, config_path="config/settings.yaml"):
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)
        self.headers = {
            "User-Agent": self.config.get("user_agent", "Mozilla/5.0")
        }

    def fetch_web_page(self, url):
        """Fetches HTML content from a given URL."""
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            return BeautifulSoup(response.text, 'html.parser')
        except Exception as e:
            logging.error(f"Error fetching {url}: {e}")
            return None

    def extract_text(self, soup):
        """Extracts all text from a BeautifulSoup object."""
        if not soup:
            return ""
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.extract()
        return soup.get_text(separator=' ', strip=True)

    def run(self, target_url):
        """Main execution method."""
        logging.info(f"Starting collection for {target_url}")
        soup = self.fetch_web_page(target_url)
        if soup:
            text_content = self.extract_text(soup)
            print(f"Collected Text Length: {len(text_content)} chars")
            return text_content
        else:
            return None
