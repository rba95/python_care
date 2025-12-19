# Documentation détaillée du TP2 : Analyseur de Logs SSH

Ce document explique le fonctionnement du script `panda.py`. L'objectif de ce programme est d'analyser un fichier de logs de sécurité (`auth.log`) pour détecter et visualiser les tentatives d'intrusion, notamment les attaques par force brute sur le service SSH[cite: 104, 111].

## Structure et Logique du Script

Le script suit une approche classique d'analyse de données : lecture, extraction, traitement et visualisation.

### 1. Initialisation et Regex

Le script commence par définir les outils nécessaires pour identifier les adresses IP.

* **L'Expression Régulière (Regex) :** Le code utilise le motif `r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'`.
    * Ce motif sert à reconnaître une adresse IPv4 standard (quatre groupes de chiffres séparés par des points). C'est le filtre qui permet de capturer l'IP de l'attaquant au milieu d'une ligne de texte complexe.
* **Les Variables :**
    * `ip_attempts` : Un dictionnaire vide `{}` qui servira à stocker chaque IP rencontrée et son nombre d'attaques.
    * `failed_logins` : Un compteur simple pour le nombre total d'échecs.

### 2. Lecture et Filtrage (La boucle principale)

Le script ouvre le fichier `auth.log` et le parcourt ligne par ligne.

* **Détection des échecs :** La condition `if 'Failed password' in line:` agit comme un premier filtre. Elle permet d'ignorer tout le trafic légitime ou non pertinent pour ne se concentrer que sur les erreurs d'authentification.
* **Extraction de l'IP :** Une fois une ligne suspecte trouvée, la fonction `re.search(pattern_ip, line)` est appelée pour "attraper" l'adresse IP précise dans cette ligne.
* **Comptage :** Si une IP est trouvée, le dictionnaire est mis à jour : `ip_attempts[ip] = ip_attempts.get(ip, 0) + 1`. Cette technique permet d'ajouter 1 au compteur de cette IP spécifique, ou de l'initialiser à 1 si c'est la première fois qu'on la voit.

### 3. Tri des Données

Une fois le fichier entièrement lu, il faut identifier les menaces principales.

* **Le Tri :** La ligne `sorted(ip_attempts.items(), key=lambda x: x[1], reverse=True)[:10]` est cruciale.
    * Elle transforme le dictionnaire en liste.
    * Elle trie cette liste en fonction du nombre d'attaques (la valeur `x[1]`).
    * `reverse=True` met les plus gros attaquants en premier.
    * `[:10]` ne garde que le "Top 10", éliminant le bruit de fond.

### 4. Visualisation Graphique

Pour rendre le résultat lisible, le script utilise la bibliothèque `matplotlib`.

* **Préparation des axes :** La commande `zip(*sorted_ips)` sépare les données en deux listes distinctes : une pour les IPs (axe X) et une pour le nombre d'essais (axe Y).
* **Création du graphique :** `plt.bar(ips, attempts)` génère un histogramme (diagramme à barres), ce qui est idéal pour comparer des quantités.
* **Mise en forme :** Des titres et labels sont ajoutés (`plt.title`, `plt.xlabel`), et `plt.xticks(rotation=45)` incline les adresses IP en bas du graphique pour qu'elles ne se chevauchent pas et restent lisibles.
