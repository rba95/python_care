import socket
import threading
import argparse


fichier = "logscan.txt"

parser = argparse.ArgumentParser()
parser.add_argument("--ip", type=str, required=True, help="IP address")
parser.add_argument("--start-port", type=int, required=True, help="Port de début")
parser.add_argument("--end-port", type=int, required=True, help="Port de fin")
parser.add_argument("--verbose", type=bool, default=False, help="Verbose port fermé")


args = parser.parse_args()
ip = args.ip
start_port = args.start_port
end_port = args.end_port

if start_port < 0 or end_port > 65535:
    print("Les ports doivent être compris entre 0 et 65535")
    exit()

def scan_port(port):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.settimeout(5)
        print("Scanning port", port)
        result = client_socket.connect_ex((ip, port))

        f = open(fichier, 'a', encoding='utf-8')


        if result == 0:
            
            contenu = f.write(f"Port {port} est ouvert\n")

            print("Port", port, "est ouvert")
        elif args.verbose == True:
           
           contenu = f.write(f"Port {port} est fermé\n")
        f.close()

    except socket.error as e:
        print(f"Erreur lors de la connexion au port {port}: {e}")
        return
    
    except socket.timeout:
        print(f"Timeout lors de la connexion au port {port}")
        return
    
    except socket.gaierror:
        print(f"Erreur dans l'adresse {ip}")
        return

    except FileNotFoundError:
        print(f"Erreur : Le fichier '{fichier}' n'a pas été trouvé.")

    except UnicodeDecodeError:
        print("Erreur : L'encodage 'utf-8' spécifié n'a pas pu décoder les octets du fichier.")
    
    client_socket.close()

for i in range(args.start_port, args.end_port + 1):
    thread = threading.Thread(target=scan_port, args=(i,))
    thread.start()

thread.join()

