from scapy.all import *

def pkt(pkt):
    print(pkt.summary())

sniff(prn=pkt, store=False)
