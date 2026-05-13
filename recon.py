import requests
from bs4 import BeautifulSoup
import whois
import argparse
from tools.utils import print_banner, get_ip_from_dns

def get_whois(domain):
    """Get WHOIS information"""
    try:
        w = whois.whois(domain)
        print("\n[+] WHOIS Information:")
        print(f"Registrar: {w.registrar}")
        print(f"Creation Date: {w.creation_date}")
        print(f"Expiry Date: {w.expiry_date}")
    except Exception as e:
        print(f"[!] Error: {e}")

def simple_subdomain_enum(domain):
    """Basic subdomain enumeration using Google Search API (simplified)"""
    url = f"https://www.google.com/search?q=site:{domain}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract titles (simplified approach)
    titles = soup.find_all('h3')
    print(f"\n[+] Possible Subdomains for {domain}:")
    for title in titles[:5]:  # Show first 5
        print(f"- {title.get_text()}")

def main():
    print_banner()
    parser = argparse.ArgumentParser(description="Recon Module")
    parser.add_argument("-d", "--domain", required=True, help="Target Domain")
    args = parser.parse_args()

    ip = get_ip_from_dns(args.domain)
    if ip:
        print(f"[+] IP Address: {ip}")
    
    get_whois(args.domain)
    simple_subdomain_enum(args.domain)

if __name__ == "__main__":
    main()
