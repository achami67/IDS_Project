#Importer la fonction sniff de Scapy, qui permet de capturer des paquets réseau
from scapy.all import sniff


# Cette fonction sera appelé chaque fois qu'un paquet réseau est capturé
def packet_callback(packet):
	# Affiche un résumé simple du paquet capture
	print(packet.sumary())
