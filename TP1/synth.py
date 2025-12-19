"""
TP : Génération de logs synthétiques (version texte)
---------------------------------------------------
Complétez ce script pour générer un fichier de logs "en clair"
contenant des événements simulés de différents serveurs et services.

Objectifs :
- Utiliser la bibliothèque random
- Générer des événements réalistes (host, process, niveau, message…)
- Produire un fichier de logs texte lisible
"""

import random
from datetime import datetime, timedelta
from pathlib import Path

# -----------------------------
# Configuration générale
# -----------------------------
N_EVENTS = 100   # Nombre de logs à générer
DAYS_RANGE = 1   # Étendue de temps (en jours)
OUT_FILE = "synthetic_system.log"

HOSTS = ["srv-web01", "srv-web02", "db-master", "db-replica", "fw1"]
PROCS = ["sshd", "nginx", "postgres", "systemd", "cron"]
LEVELS = ["INFO", "WARNING", "ERROR", "CRITICAL"]

MESSAGES = [
    "connexion acceptée depuis {ip}",
    "échec d'authentification utilisateur {user}",
    "latence élevée: {lat} ms",
    "erreur I/O sur disque {dev}",
    "redémarrage du service {proc}",
    "paquet dropped par firewall"
]

# -----------------------------
# Fonctions utilitaires
# -----------------------------

def random_ip():
    """Retourne une adresse IPv4 aléatoire."""
    # TODO : générer une adresse IP aléatoire
    for i in range (4):
        octet1 = random.randint(1, 254)
        octet2 = random.randint(1, 254)
        octet3 = random.randint(1, 254)
        octet4 = random.randint(1, 254)
        ip = f"{octet1}.{octet2}.{octet3}.{octet4}"
    return ip

    


def random_user():
    """Retourne un utilisateur choisi aléatoirement."""
    users = ["alice", "bob", "admin", "guest", "monitor"]
    # TODO : choisir un élément de la liste users avec random.choice
    user = random.choice(users)
    return user



def random_dev():
    """Retourne un périphérique disque aléatoire."""
    devices = ["/dev/sda1", "/dev/nvme0n1", "/dev/sdb"]
    # TODO : choisir un élément de la liste devices avec random.choice
    dev = random.choice(devices)
    return dev


# -----------------------------
# Boucle de génération
# -----------------------------
def main():
    # Point de départ temporel (aujourd'hui - DAYS_RANGE)
    start_time = datetime.now() - timedelta(days=DAYS_RANGE)
    events = []

    for i in range(N_EVENTS):
        # TODO : générer un delta aléatoire en secondes
        delta_seconds = random.randint(0,60)
        ts = start_time + timedelta(seconds=delta_seconds)
        ts_iso = ts.isoformat(sep=' ', timespec='seconds')

        # TODO : choisir un host, un process, et un niveau
        host = random.choice(HOSTS)
        proc = random.choice(PROCS)
        level = random.choice(LEVELS)

        # TODO : choisir un modèle de message et le compléter avec format()
        template = "" + random.choice(MESSAGES) + ""
        msg = template.format(
            ip=random_ip(),
            user=random_user(),
            lat=f"{random.uniform(10, 2000):.1f}",
            dev=random_dev(),
            proc=proc
        )

        # Format d’un log texte :
        # 2025-09-29 10:23:45 srv-web01 nginx[1234]: INFO connexion acceptée depuis 192.168.1.10
        line = f"{ts_iso} {host} {proc}[{random.randint(1000,9999)}]: {level} {msg}"

        events.append((ts, line))

    # Trier les événements par timestamp
    events.sort(key=lambda x: x[0])
    lines = [line for _, line in events]

    # Écrire dans un fichier texte
    with Path(OUT_FILE).open("w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")

    print(f"{len(lines)} événements générés dans {OUT_FILE}")


if __name__ == "__main__":
    main()
