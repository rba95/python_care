import psutil
import time
import os
import threading

program_running = True

def effacer_ecran():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def convertir_octets(taille_en_octets):
    for unite in ["o", "Ko", "Mo", "Go", "To"]:
        if taille_en_octets < 1024:
            return f"{taille_en_octets:.2f} {unite}"
        taille_en_octets /= 1024
    return f"{taille_en_octets:.2f} Po"

def dessiner_barre(pourcentage):
    longueur_barre = 20
    nb_rempli = int(longueur_barre * pourcentage / 100)
    barre = '█' * nb_rempli + '-' * (longueur_barre - nb_rempli)
    return f"[{barre}] {pourcentage:.1f}%"

def attendre_commande_quitter():
    global program_running
    print("Astuce : Écrivez 'quit' et appuyez sur Entrée pour arrêter.")
    while program_running:
        texte = input() 
        if texte.strip().lower() == 'quit':
            print("Arrêt en cours...")
            program_running = False
            break

def afficher_tableau_de_bord():
    while program_running:
        effacer_ecran()
        
        print("--- MON TABLEAU DE BORD SYSTÈME ---")
        print(" (Mise à jour toutes les 5 secondes)")
        print("-----------------------------------")

        print("\n[PROCESSEUR / CPU]")
        cpu_total = psutil.cpu_percent()
        print(f"Utilisation globale : {dessiner_barre(cpu_total)}")
        
        print("Détail par cœur :")
        liste_cpu = psutil.cpu_percent(percpu=True)
        for i, usage in enumerate(liste_cpu):
            print(f"  - Cœur {i} : {dessiner_barre(usage)}")

        print("\n[MÉMOIRE RAM]")
        memoire = psutil.virtual_memory()
        print(f"  Totale    : {convertir_octets(memoire.total)}")
        print(f"  Utilisée  : {convertir_octets(memoire.used)} {dessiner_barre(memoire.percent)}")
        print(f"  Disponible: {convertir_octets(memoire.available)}")

        print("\n[DISQUE DUR]")
        try:
            partitions = psutil.disk_partitions()
            for partition in partitions:
                info_disque = psutil.disk_usage(partition.mountpoint)
                print(f"  Lecteur {partition.device} : {dessiner_barre(info_disque.percent)}")
                print(f"    Libre : {convertir_octets(info_disque.free)} / Total : {convertir_octets(info_disque.total)}")
        except Exception as e:
            print(f"  Impossible de lire les infos disque : {e}")

        print("\n[RÉSEAU]")
        reseau = psutil.net_io_counters()
        print(f"  Données envoyées : {convertir_octets(reseau.bytes_sent)}")
        print(f"  Données reçues   : {convertir_octets(reseau.bytes_recv)}")

        print("\n-----------------------------------")
        
        for _ in range(50):
            if not program_running:
                break
            time.sleep(0.1)

if __name__ == "__main__":
    thread_clavier = threading.Thread(target=attendre_commande_quitter)
    thread_clavier.start()

    try:
        afficher_tableau_de_bord()
    except KeyboardInterrupt:
        program_running = False

    thread_clavier.join()
    print("Au revoir !")
