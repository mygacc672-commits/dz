from scapy.all import sniff, wrpcap, ARP
import time

def packet_callback(packet):
    """Callback for each captured packet"""
    if packet.haslayer(ARP):
        arp_layer = packet.getlayer(ARP)
        if arp_layer.op == 1:  # Who has?
            print(f"[+] ARP Request: {arp_layer.psrc} is at {arp_layer.hwsrc}")

def monitor_wifi(interface='wlan0', count=10):
    """Monitor Wi-Fi for ARP packets"""
    print(f"[+] Starting capture on {interface}...")
    sniff(iface=interface, prn=packet_callback, count=count)
    print("[+] Capture complete.")

if __name__ == "__main__":
    monitor_wifi()
