# Documentation détaillée du TP3 : Analyseur de Logs Apache

Ce document détaille le fonctionnement du script `TP3.py`. [cite_start]L'objectif de ce programme est d'auditer le trafic d'un serveur web en analysant le fichier `access.log`[cite: 59]. Il se concentre spécifiquement sur les erreurs "404 Not Found" pour identifier les liens morts, les erreurs de configuration ou les comportements automatisés (bots).

## Structure et Logique du Script

Le script utilise une approche orientée "Data Science" grâce à la bibliothèque `pandas`, ce qui permet de manipuler les logs comme un tableau structuré plutôt que comme du simple texte.

### 1. Parsing et Nettoyage des Données

La première étape consiste à transformer des lignes de texte brut en données exploitables.

* **L'Expression Régulière (Regex) :**
  Le script définit un motif complexe `LOG_PATTERN`. Ce motif agit comme un filtre qui découpe chaque ligne de log pour en extraire des champs précis : l'adresse IP, la date, la méthode HTTP (GET, POST), l'URL demandée, le code de statut et le "User Agent" (l'identité du navigateur).

* **Chargement en Mémoire :**
  Le script lit le fichier ligne par ligne. Si une ligne correspond au motif Regex, elle est stockée. Une fois la lecture terminée, toutes ces données sont converties en un **DataFrame Pandas** (`df`). C'est une structure de tableau très puissante qui permet de filtrer et trier des milliers de lignes instantanément.

### 2. Filtrage des Erreurs 404

Une fois les données dans le DataFrame, l'analyse commence.

* **Isolation des erreurs :**
  La commande `df[df['status'] == 404]` crée un sous-tableau ne contenant que les requêtes ayant échoué. Cela permet de travailler uniquement sur le trafic problématique sans être pollué par les connexions réussies.

* **Identification des responsables :**
  La méthode `.value_counts()` est appliquée sur la colonne des IPs. Elle compte automatiquement combien de fois chaque IP apparaît dans les erreurs et trie le résultat. On obtient ainsi immédiatement le "Top 5" des IPs générant le plus d'erreurs 404.

### 3. Détection des Bots (Robots d'indexation)

C'est une fonctionnalité avancée du script qui permet de qualifier le trafic.

* **Analyse du User Agent :**
  Le script inspecte la colonne `user_agent` à la recherche de mots-clés spécifiques comme "bot", "crawler" ou "spider".
* **Calcul d'impact :**
  Il sépare les erreurs causées par des humains de celles causées par des robots (comme Googlebot). Cela permet de relativiser la gravité des erreurs : une erreur 404 causée par un bot est souvent moins grave qu'une erreur rencontrée par un client réel.



### 4. Visualisation et Rapport

Le script termine par une représentation graphique des résultats.

* **Graphique en Barres :**
  Il utilise `matplotlib` pour générer un histogramme des 5 IPs les plus problématiques.
* **Mise en forme :**
  Le graphique est personnalisé avec un titre, des étiquettes d'axes claires, et une rotation des adresses IP sur l'axe X pour éviter qu'elles ne se chevauchent.
* **Rapport Textuel :**
  En plus du graphique, le script affiche un rapport détaillé dans la console, indiquant le pourcentage d'erreurs dues aux bots et la liste des IPs incriminées.
