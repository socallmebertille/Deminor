<div align="center" class="text-center">
  <h1>Deminor</h1>

  <p><em>Démineur Python - Tkinter</em></p>
  <img alt="last-commit" src="https://img.shields.io/github/last-commit/socallmebertille/Deminor?style=flat&amp;logo=git&amp;logoColor=white&amp;color=0080ff" class="inline-block mx-1" style="margin: 0px 2px;">
  <img alt="repo-top-language" src="https://img.shields.io/github/languages/top/socallmebertille/Deminor?style=flat&amp;color=0080ff" class="inline-block mx-1" style="margin: 0px 2px;">
  <img alt="repo-language-count" src="https://img.shields.io/github/languages/count/socallmebertille/Deminor?style=flat&amp;color=0080ff" class="inline-block mx-1" style="margin: 0px 2px;">
  <p><em>Built with the tools and technologies:</em></p>
  <img alt="Python" src="https://img.shields.io/badge/Python-fdfd66.svg?style=flat&amp;logo=Python&amp;logoColor=Blue" class="inline-block mx-1" style="margin: 0px 2px;">
</div>

---

## 📋 Table des matières

- [VDescription](#-description)
- [Fonctionnalités](#-fonctionnalités)
- [Installation & lancement](#-installation-&-lancement)
- [Utilisation](#-utilisation)
- [Explications du code](#-explications-du-code)

## 🎮 Description

Ce projet est une version personnalisée du démineur, avec une grille configurable (nombre de lignes, colonnes et trésors).
Deux joueurs s’affrontent en alternance pour découvrir des trésors cachés dans la grille. Chaque case dévoilée donne un score selon la proximité des trésors.
- Interface graphique simple et intuitive avec Tkinter.
- Scores affichés en temps réel pour chaque joueur.
- La partie se termine quand tous les trésors sont trouvés.
- Affichage du gagnant ou égalité.

## ⚙️ Fonctionnalités

- Configuration du nombre de lignes, colonnes et trésors.
- Saisie des noms des deux joueurs.
- Affichage dynamique des scores et du joueur actif.
- Couleurs différentes selon la valeur des cases (proximité du trésor).
- Gestion des tours entre joueur A et joueur B.
- Message final indiquant le gagnant ou l'égalité.

## 🛠️ Installation & lancement

1- Assure-toi d'avoir Python installé (version 3.x). Tkinter est généralement inclus par défaut.
2- Télécharge ce script Python (demineur.py).
3- Lance le script avec la commande :

```
python3 deminor.py
```
4- Configure les paramètres dans la fenêtre d’accueil, puis clique sur START pour commencer.

## 📐 Utilisation

- Choisis les noms des joueurs.
- Définis le nombre de lignes, colonnes et trésors avec les curseurs.
- Clique sur START pour démarrer la partie.
- Clique sur une case pour découvrir ce qui s’y cache.
- Suis le score et le joueur actif en haut.
- Le jeu se termine quand tous les trésors ont été découverts, et affiche le gagnant.

## 📋 Explications du code

- `CreerGrille()` : crée la grille de jeu et place aléatoirement les trésors.
- `Jouer(x, y)` : gère la découverte d’une case, met à jour le score et le tour.
- `LancerJeu()` : ouvre la fenêtre de jeu avec la grille et les boutons.
- Interface principale pour configurer le jeu avant de lancer la partie.

