# Travaux Pratiques Python

## Description des TP

### 1. Génération de logs synthétiques (TP1)
**Fichier :** `synth.py`

Ce script a pour objectif de simuler l'activité d'un système en générant des fichiers de logs réalistes. Il est utilisé pour produire des données de test pour les exercices de supervision.

* **Fonctionnalités :** Utilisation de la bibliothèque `random` pour générer des adresses IP, des utilisateurs et des niveaux de gravité (INFO, WARNING, CRITICAL).
* **Sortie :** Produit le fichier `synthetic_system.log` contenant des événements horodatés.

### 2. Analyse de logs SSH (TP2)
**Fichier :** `panda.py`

Cet outil analyse le fichier `auth.log` pour détecter des tentatives d'intrusion, spécifiquement des attaques par force brute sur le service SSH.

* **Fonctionnalités :** Parsing de texte via expressions régulières pour isoler les lignes contenant "Failed password".
* **Visualisation :** Génération d'un histogramme des adresses IP suspectes avec `matplotlib`.

### 3. Analyse de logs Apache (TP3)
**Fichier :** `TP3.py`

Ce script traite les logs d'un serveur web (`access.log`) pour identifier les liens morts et l'activité des bots.

* **Fonctionnalités :** Utilisation de `pandas` pour structurer les données et filtrer les codes de statut 404.
* **Analyse :** Identification des "User Agents" de type bot (Googlebot, Bingbot) et calcul de leur impact sur les erreurs.

### 4. Scanner de ports TCP (TP4)
**État :** En cours de développement

Un outil en ligne de commande pour scanner une adresse IP et lister les ports ouverts.

* **Technique :** Utilisation du module `socket` pour tester les connexions.
* **Interface :** Gestion des arguments (IP, plage de ports) via `argparse`.

## Prérequis et Installation

Les scripts nécessitent Python 3 ainsi que certaines bibliothèques externes pour l'analyse de données et la visualisation.

Installation des dépendances :

```bash
pip install pandas matplotlib
