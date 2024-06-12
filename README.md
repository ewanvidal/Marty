# Projet de robotique : Navigation de Marty dans un labyrinthe

## Table des matières

* [Introduction](#Introduction)
* [Objectifs](#Objectifs)
* [Ressources](#Ressources)
* [Utilisation](#Utilisation)
* [Contributeurs](#Contributeurs)
* [Structure](#Structure)
* [Liens](#Liens)

### **Introduction**

Dans le cadre du module de robotique de la 3ème année à Polytech Dijon, nous devons programmer le robot Marty pour qu'il réalise un labyrinthe. L'objectif principal de ce projet est de concevoir un programme en Python capable de piloter deux robots Marty de manière coordonnée à travers un labyrinthe. Nous aborderons les différentes étapes nécessaires pour configurer les robots, établir une communication efficace avec eux, et élaborer des algorithmes de navigation et de coordination. 

### **Objectifs**

 Apprendre à programmer le robot Marty en Python.
 Développer des compétences en robotique et en navigation autonome.

### **Ressources**

 Robot Marty
 Logiciel de programmation Python
 Base de données de marty avec les fonctions de référence

 ### **Utilisation**

Il suffit de lancer l'interface afin de commencer. La connexion et la callibration seront disponibles via cette interface. 
 ```python interface.py```
 Le widget control permet de faire plusieurs emotes que nous vous laissons découvrir (via les touches des numéros).
 Le labyrinthe se lance avec la touche L du clavier.

### **Structure du projet**

 Se repérer dans tous les fichiers peut s'avérer compliqué, voici donc les points imoortants à noter quant à ce projet : 
 La gestion de l'interface avec pyQt6 se situe sur le fichier ```interface.py```.
 La logique de codage et tous le reste du code se trouve dans les fichiers à l'intérieur du dossier ```src/interface/application```.
 Plusieurs images et sons sont disponibles dans les dossiers ```src/sound```et```src/img```.

### **Remarques**

 Ce projet est un point de départ pour apprendre à programmer le robot Marty et à le faire naviguer dans un labyrinthe/trajet.
 La callibration de chaque robot est nécessaire afin d'avoir les bonnes couleurs, celle-ci est cruciale car la luminosité de la pièce joue un rôle et chaque capteur de couleur est différent.
 Quelques règles doivent être énoncées avant : Chaque robot sera donné un parcours à faire, celui-ci comportaera des cases noires. Le 2ème robot fera de même les caes noires seront positionnées sur d'autres cases.
 Ensuite, les robots devront partageer leurs parcours afin d'obtenir le parcours final qui aura toutes les cases. 
 Enfin, un robot devra parcourir ce trajet final suivant les couleurs que nous avions découvertes.
 Par la suite, l'utilisation de la caméra embarquée du robot peut-être utile afin de développer d'autres fonctionnalités.

### **Contributeurs**

- Guillot Natthan
- Druhet Joachim
- Vidal Ewan

### **Liens utiles**

 - Site web Marty: https://marty-webapp.web.app/
 - GitHub Marty (documentation): https://github.com/robotical/martypy/blob/b2567d66fb2742c0a62e47c3aa2111bc6c6f5218/martypy/Marty.py#L2
