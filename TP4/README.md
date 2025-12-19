T# Documentation détaillée du TP4 : Scanner de Ports TCP

Ce document décrit le fonctionnement du script de scan de ports. Contrairement aux scripts précédents qui analysaient des fichiers existants, ce programme est un outil actif qui interagit directement avec le réseau. Son objectif est de vérifier quels services sont accessibles sur une machine donnée (serveur web, SSH, base de données) en testant une plage de ports définie.

## Spécificité d'Exécution : Interface en Ligne de Commande

Ce script ne s'exécute pas simplement en cliquant dessus ou en lançant `python scan.py` sans rien d'autre. Il a été conçu pour être flexible et pilotable directement depuis le terminal, comme un véritable outil d'administration système.

Pour fonctionner, il attend des **arguments** spécifiques. [cite_start]Cela est rendu possible grâce à l'utilisation de la bibliothèque `argparse`[cite: 7].

Exemple de commande pour l'exécuter :
`python scan.py --ip 192.168.1.1 --start-port 1 --end-port 1024`

* [cite_start]**--ip** : Définit l'adresse de la machine cible[cite: 8].
* [cite_start]**--start-port** et **--end-port** : Délimitent la plage de recherche[cite: 9, 11].

Cette méthode permet de scanner différentes cibles sans jamais avoir à modifier le code source du script.

## Structure et Logique du Code

[cite_start]Le script repose sur le module standard `socket`, qui est la brique de base pour toute communication réseau en Python[cite: 6].

### 1. La Connexion Socket
Le cœur du scanner est une boucle qui parcourt chaque port demandé. Pour chaque port, le script tente d'établir une connexion TCP :

* **Création du socket :** On initialise un point de connexion Internet (IPv4) en mode TCP.
* **La tentative (Connect) :** Le script utilise la méthode `connect_ex()`. Contrairement à un `connect()` classique qui plante le programme en cas d'échec, `connect_ex()` renvoie simplement un code d'erreur.
* **L'analyse du résultat :** Si la méthode renvoie `0`, cela signifie que la connexion a réussi : le port est donc **OUVERT**. Sinon, il est fermé ou filtré.

### 2. Gestion des Erreurs et Timeouts
Scanner un réseau peut être lent si la machine cible ne répond pas. [cite_start]Une partie essentielle du code consiste à gérer le "Timeout" (temps limite)[cite: 13].
Si on ne définit pas de limite, le script pourrait attendre indéfiniment sur un port protégé par un pare-feu. Le code impose donc un délai court (par exemple 0.5 seconde) pour passer rapidement au port suivant si aucune réponse n'est reçue.

### 3. Environnement de Test

Pour vérifier le bon fonctionnement de ce scanner sans attaquer de vraies machines (ce qui est illégal sans autorisation), un environnement de test est nécessaire.

**Code du cours fourni pour les tests :**
Un script annexe (serveur factice) est mis à votre disposition. Ce code doit être lancé dans un terminal séparé avant de démarrer votre scanner. Il va "écouter" sur plusieurs ports spécifiques pour simuler des services ouverts. Cela vous permettra de valider que votre scanner détecte correctement les ports ouverts et ignore les fermés.
