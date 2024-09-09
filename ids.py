#Importer la fonction sniff de Scapy, qui permet de capturer des paquets réseau
from scapy.all import sniff


# Cette fonction sera appelé chaque fois qu'un paquet réseau est capturé
def packet_callback(packet):
	# Affiche un résumé simple du paquet capture
	print(packet.summary())

# Fonction principale qui démarre le processus
def main():
	# Message d'information indiquant que le système IDS (Intrusion Detection System) est en cours de démarrage
	print("Démarrage de l'IDS...")
	
	#Capture 10 paquets réseau et appelle packet_callback pour chaque paquet capturé
	sniff(prn=packet_callback, count=30)

#Vérifie si le script est exécuté directement (et non importé dans un autre module)
if __name__ == '__main__':
	# Appelle la fonction principale
	main()
