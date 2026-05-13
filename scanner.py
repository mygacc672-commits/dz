import nmap
import argparse
from tools.utils import load_config, print_banner

def scan_ports(ip, ports=1024):
    """Scan common ports on target IP"""
    nm = nmap.PortScanner()
    nm.scan(ip, str(ports))
    
    print(f"\n[+] Scanning {ip}...")
    for host in nm.all_hosts():
        print(f"Host: {host}")
        for proto in nm[host].all_protocols():
            lport = nm[host][proto].keys()
            for port in sorted(lport):
                state = nm[host][proto][port]['state']
                print(f"Port: {port}\tState: {state}")

def main():
    print_banner()
    parser = argparse.ArgumentParser(description="Simple Port Scanner")
    parser.add_argument("-t", "--target", required=True, help="Target IP or Domain")
    args = parser.parse_args()

    # Resolve domain to IP if needed
    import socket
    try:
        ip = socket.gethostbyname(args.target)
    except socket.gaierror:
        ip = args.target  # Assume it's an IP

    config = load_config()
    scan_ports(ip, config['max_ports'])

if __name__ == "__main__":
    main()
