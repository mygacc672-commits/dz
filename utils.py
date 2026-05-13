import os

def load_api_key(env_var_name):
    """Loads an API key from environment variables."""
    api_key = os.getenv(env_var_name)
    if not api_key:
        raise ValueError(f"Environment variable {env_var_name} not set.")
    return api_key
