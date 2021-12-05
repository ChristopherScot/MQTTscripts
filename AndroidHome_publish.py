from scapy.all import *
import os
import paho.mqtt.client as mqtt

def arp_display(pkt):
  if ARP not in pkt:
    return pkt.summary()
    if pkt[ARP].op == 1: #who-has (request)
        client = mqtt.Client()
        client.connect("c2smart.asuscomm.com", 1883, 60)

        if pkt[ARP].hwsrc == "64:bc:0c:65:d3:76": # ARP Probe
             print "Arp probe from Android Phone " + pkt[ARP].psrc
             mqttc.publish("AmHome/Chris", 1, qos=2, retain=True)	
        
print sniff(prn=arp_display, filter="arp", store=0, count=0)
