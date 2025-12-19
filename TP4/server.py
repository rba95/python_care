import socket

# Création du socket serveur (IPv4, TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Adresse et port du serveur
server_address = ('localhost', 1024)

try:
    # Liaison du socket à l'adresse et au port
    server_socket.bind(server_address)
    
    # Le serveur écoute les connexions entrantes (1 connexion max en file d'attente)
    server_socket.listen(1)
    print(f"Le serveur écoute sur {server_address}...")

    # Attente d'une connexion (bloquant)
    connection, client_address = server_socket.accept()
    
    try:
        print(f"Connexion reçue de : {client_address}")

        # Réception des données (buffer de 1024 octets)
        data = connection.recv(1024)
        if data:
            print(f"Données reçues : {data.decode('utf-8')}")
        else:
            print("Aucune donnée reçue.")
            
    finally:
        # Fermeture de la connexion client
        connection.close()
        print("Connexion client fermée.")

except Exception as e:
    print(f"Erreur serveur : {e}")
finally:
    # Fermeture du socket serveur
    server_socket.close()
    print("Serveur arrêté.")
