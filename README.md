# Codeur / Décodeur de Messages (Python)

Un projet simple en Python composé de deux scripts permettant de **chiffrer (encoder)** et **déchiffrer (décoder)** des messages textes à l'aide d'un algorithme de substitution de caractères personnalisé.

---

## 📋 Description

Ce projet propose un système d'encodage basique où chaque lettre et symbole est remplacé par un caractère spécifique. 

Le projet se compose de deux scripts principaux :
1. **`encodeur.py`** : Prend un texte lisible en entrée et le transforme en un message crypté.
2. **`decrypteur.py`** : Prend un message crypté et le traduit pour restituer le texte d'origine.

---

## 🛠️ Fonctionnement

L'algorithme utilise une substitution directe caractère par caractère.

### Table de correspondance (Exemples)
| Caractère original | Caractère encodé |
| :---: | :---: |
| `Espace` | `£` |
| `a` | `/` |
| `b` | `*` |
| `c` | `-` |
| `d` | `+` |
| `e` | `.` |
| `é` | `5` |
| `à` | `9` |

---

## 🚀 Utilisation

### Prérequis
- [Python 3.x](https://www.python.org/downloads/) installé sur votre machine.

### 1. Encoder un message
Exécutez le script d'encodage :
```bash
python encodeur.py
```
1. Saisissez le message que vous souhaitez encoder.
2. Attendez la fin de la temporisation (compte à rebours de 5 secondes).
3. Récupérez le message encodé affiché dans la console.

### 2. Décoder un message
Exécutez le script de décodage :
```bash
python decrypteur.py
```
1. Entrez ou collez le message encodé.
2. Attendez la fin de la temporisation.
3. Le message original décodé s'affichera à l'écran.

---

## 📁 Structure du projet

```text
.
├── encodeur.py      # Script de chiffrement du message
├── decrypteur.py    # Script de déchiffrement du message
└── README.md        # Documentation du projet
```

---
