import json
import os

def load_config():
    """Load configuration from config.json"""
    config_path = os.path.join(os.path.dirname(__.__file__), '..', 'config.json')
    with open(config_path, 'r') as f:
        return json.load(f)

def print_banner():
    banner = """
    ███╗   ██╗███████╗██╗  ██╗██╗   ██╗███████╗
    ████╗  ██║██╔════╝╚██╗██╔╝██║   ██║██╔════╝
    ██╔██╗ ██║█████╗   ╚███╔╝ ██║   ██║███████╗
    ██║╚██╗██║██╔══╝   ██╔██╗ ██║   ██║╚════██║
    ██║ ╚████║███████╗██╔╝ ██╗╚██████╔╝███████║
    ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝
    """
    print(banner)

def get_ip_from_dns(domain):
    import socket
    try:
        return socket.gethostbyname(domain)
    except socket.gaierror:
        return None
