# Documentation détaillée du TP1 : Générateur de logs synthétiques

Ce document détaille le fonctionnement du script `synth.py`. L'objectif de ce programme est de générer artificiellement un fichier de logs nommé `synthetic_system.log`. Ce fichier simule l'activité d'un parc de serveurs pour fournir des données d'entraînement aux exercices d'analyse suivants.

## Structure et Logique du Script

Le script est organisé en plusieurs blocs distincts pour faciliter la lecture et la maintenance : la configuration, les outils de génération aléatoire, et la boucle principale.

### 1. La Configuration (Les Constantes)

Le début du script regroupe toutes les options modifiables. Ces variables sont écrites en majuscules pour indiquer qu'il s'agit de constantes globales.

* **N_EVENTS** : C'est le compteur qui détermine combien de lignes de logs seront créées au total.
* **HOSTS, PROCS, LEVELS** : Ces listes définissent le vocabulaire du système (noms des serveurs, noms des processus comme nginx ou sshd, et niveaux d'urgence comme ERROR ou INFO).
* **MESSAGES** : C'est une liste de phrases modèles (templates). Elles contiennent des balises spéciales entre accolades, comme `{user}` ou `{ip}`, qui servent de points d'insertion pour des données variables.

Cette séparation permet de modifier le scénario de simulation (par exemple, ajouter un nouveau serveur) sans avoir à toucher au code complexe plus bas.

### 2. Les Fonctions Utilitaires (L'aléatoire)

Pour que les logs aient l'air réels, le script utilise la bibliothèque `random` de Python à travers plusieurs fonctions spécifiques.

* **random_ip()** : Cette fonction génère une adresse IPv4. Elle tire au sort quatre nombres entiers entre 1 et 254 et les assemble avec des points.
* **random_user() et random_dev()** : Ces fonctions utilisent la commande `random.choice()`. Cette commande est essentielle : elle prend une liste en entrée (comme la liste des utilisateurs `users`) et renvoie un seul élément choisi au hasard. Cela permet de varier les acteurs dans les logs.

### 3. La Boucle Principale (Fonction main)

C'est ici que l'assemblage des données se fait.

**La gestion du temps**
Le script ne prend pas l'heure actuelle. Il définit une date de départ dans le passé, puis, à chaque tour de boucle, il ajoute un nombre aléatoire de secondes. Cela permet de simuler une activité continue sur une période donnée. La date est ensuite convertie en texte au format standard ISO (Année-Mois-Jour Heure:Minute:Seconde).

**Le remplissage des messages**
Le script sélectionne d'abord un modèle de message au hasard. Ensuite, il utilise la méthode `.format()` sur la chaîne de caractères. Cette méthode remplace les balises `{user}` ou `{ip}` définies plus haut par les valeurs concrètes générées par les fonctions utilitaires.

**L'assemblage final**
Une fois toutes les pièces disponibles (date, serveur, processus, message), elles sont assemblées en une seule ligne de texte grâce à une "f-string" (format string).

### 4. Tri Chronologique et Écriture

Pendant la génération, l'ajout aléatoire de secondes peut parfois créer un léger désordre temporel si on traitait plusieurs sources en parallèle, ou simplement par principe de rigueur.

Avant d'écrire dans le fichier final, le script stocke tous les événements dans une liste et applique la méthode `.sort()`. Cela garantit que le fichier de log final est strictement chronologique, du plus ancien au plus récent, comme le ferait un vrai système d'exploitation.

Le résultat est ensuite écrit ligne par ligne dans le fichier `synthetic_system.log`.
