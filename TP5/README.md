# TP5 : Tableau de bord de surveillance système

Ce projet est un outil de monitoring en temps réel pour le terminal. Il utilise Python pour récupérer et afficher l'état des ressources de la machine (Processeur, RAM, Disques, Réseau) via une interface textuelle dynamique.

## Objectifs

L'objectif est de manipuler la bibliothèque système `psutil` pour extraire des métriques bas niveau et de présenter ces données de manière lisible pour un administrateur système.

## Analyse technique : La bibliothèque psutil

Le script s'appuie sur quatre fonctions clés de la bibliothèque pour auditer le système :

### 1. psutil.cpu_percent()
Cette fonction mesure la charge du processeur.
* **Fonctionnement :** Elle calcule le pourcentage d'utilisation du CPU sur un intervalle de temps donné.
* **Dans ce script :** Elle est utilisée pour afficher la charge globale, ainsi que la charge détaillée par cœur grâce à l'option `percpu=True`.

### 2. psutil.virtual_memory()
Elle fournit un état complet de la mémoire vive (RAM).
* **Données récupérées :** Le script exploite la mémoire totale, la mémoire utilisée et la mémoire disponible (cette dernière inclut le cache libérable, ce qui est plus précis que la mémoire libre).

### 3. psutil.disk_usage('/')
Cette fonction analyse l'espace de stockage sur un point de montage précis.
* **Fonctionnement :** Elle retourne l'espace total, utilisé et libre en octets. Le script parcourt toutes les partitions détectées pour afficher ces informations pour chaque disque.

### 4. psutil.net_io_counters()
Elle renvoie les statistiques de trafic réseau global depuis le démarrage de la machine.
* **Utilisation :** Le script affiche le cumul des octets envoyés et reçus pour donner une indication du volume de données échangées.

## Fonctionnement du code

Le script (`tp5.py`) intègre plusieurs mécanismes pour assurer un affichage fluide et interactif.

### Gestion de l'interface
* **Conversion d'unités :** Une fonction utilitaire convertit les octets bruts en unités lisibles (Ko, Mo, Go) pour faciliter la lecture.
* **Barres de progression :** Une fonction génère des barres visuelles en caractères ASCII pour représenter graphiquement les pourcentages d'utilisation.
* **Rafraîchissement :** L'écran est effacé à chaque cycle de mise à jour (toutes les 5 secondes) en utilisant la commande système appropriée (`cls` sur Windows, `clear` sur Linux/Mac).

### Programmation Asynchrone (Threading)
Une particularité importante de ce script est l'utilisation du multi-threading pour gérer l'arrêt du programme.
* **Problème :** La fonction `input()`, qui attend que l'utilisateur tape "quit", est bloquante. Si elle était placée dans la boucle principale, l'affichage ne se mettrait plus à jour.
* **Solution :** La surveillance du clavier est déplacée dans un thread séparé (`thread_clavier`). Cela permet au programme d'écouter les commandes de l'utilisateur en arrière-plan tout en continuant de mettre à jour le tableau de bord au premier plan.

## Installation et Exécution

Ce projet nécessite l'installation de la bibliothèque externe `psutil`.

1. **Installation des dépendances :**
   ```bash
   pip install psutil
