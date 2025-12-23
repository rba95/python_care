# TP5 : Tableau de bord de surveillance système

Ce projet consiste en la création d'un outil de monitoring en temps réel écrit en Python. Il permet de visualiser l'état des ressources de la machine (Processeur, RAM, Disques, Réseau) directement dans le terminal.

## Objectifs du TP

[cite_start]L'objectif principal est d'apprendre à interagir avec les données bas niveau du système d'exploitation via la bibliothèque `psutil`[cite: 136]. [cite_start]Le script doit être capable d'extraire des métriques, de les formater de manière lisible pour l'humain et de les actualiser dynamiquement[cite: 141, 142].

## Analyse des fonctions techniques (psutil)

[cite_start]Conformément aux consignes du TP, voici l'explication technique des fonctions clés de la bibliothèque `psutil` utilisées pour récupérer les métriques brutes[cite: 149].

### 1. psutil.cpu_percent()
Cette fonction retourne un nombre flottant représentant l'utilisation actuelle du processeur en pourcentage.
* **Fonctionnement :** Elle compare les temps d'activité du système entre deux intervalles.
* [cite_start]**Utilisation dans le script :** Nous l'utilisons en mode non-bloquant pour obtenir la charge globale, ainsi qu'avec l'argument `percpu=True` pour obtenir le détail cœur par cœur[cite: 150].

### 2. psutil.virtual_memory()
Elle renvoie un objet complexe (named tuple) contenant les statistiques sur la mémoire vive (RAM).
* [cite_start]**Données clés :** Elle fournit la mémoire totale (`total`), la mémoire utilisée (`used`) et surtout la mémoire disponible (`available`), qui est plus pertinente que la mémoire libre car elle inclut les caches libérables[cite: 151].

### 3. psutil.disk_usage('/')
Cette fonction analyse l'utilisation de l'espace disque pour une partition donnée (ici la racine `/` ou le disque principal).
* [cite_start]**Retour :** Elle fournit l'espace total, l'espace utilisé et l'espace libre en octets, ainsi que le pourcentage d'occupation[cite: 152].

### 4. psutil.net_io_counters()
Elle récupère les statistiques globales des interfaces réseau depuis le démarrage du système.
* [cite_start]**Données clés :** Nous exploitons principalement `bytes_sent` (octets envoyés/upload) et `bytes_recv` (octets reçus/download) pour afficher le volume de données échangées[cite: 153].

## Fonctionnement du Script (`monitor.py`)

Le script proposé va plus loin qu'un simple affichage en implémentant plusieurs fonctionnalités avancées pour améliorer l'expérience utilisateur.

### Gestion de l'affichage et du formatage
Les données brutes fournies par le système sont souvent peu lisibles (des octets ou des flottants précis).
* **Conversion d'unités :** La fonction `convertir_octets` transforme automatiquement les grands nombres en unités lisibles (Ko, Mo, Go, To) en divisant successivement par 1024.
* **Visualisation graphique :** La fonction `dessiner_barre` génère une barre de progression en caractères ASCII (ex: `[██████----] 60%`). Cela permet de visualiser la charge d'un coup d'œil sans lire les chiffres.

### Gestion de la concurrence (Threading)
Une particularité de ce script est l'utilisation du module `threading`.
* **Problème :** La fonction `input()` qui attend que l'utilisateur tape "quit" est bloquante. Si on la mettait dans la boucle principale, le tableau de bord ne se mettrait plus à jour tant que l'utilisateur n'appuie pas sur Entrée.
* **Solution :** La fonction `attendre_commande_quitter` est lancée dans un fil d'exécution séparé (thread). [cite_start]Elle surveille le clavier en arrière-plan sans empêcher la boucle d'affichage `afficher_tableau_de_bord` de tourner toutes les 5 secondes[cite: 165].

### Rafraîchissement fluide
[cite_start]Pour effacer l'écran proprement, le script détecte le système d'exploitation (`os.name`) et exécute la commande appropriée (`cls` pour Windows, `clear` pour Linux/Mac)[cite: 170].
De plus, la pause de 5 secondes est découpée en 50 petites pauses de 0.1 seconde. Cela permet au programme de réagir presque instantanément si l'utilisateur demande l'arrêt, au lieu d'attendre la fin des 5 secondes.

## Prérequis et Installation

Ce projet nécessite l'installation de la bibliothèque externe `psutil`.

Installation :
```bash
pip install psutil
