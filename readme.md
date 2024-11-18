
# Projet Webcam avec Raspberry Pi

Ce projet permet de controler une caméra module v3 connectée a un Raspberry Pi 5 via une interface graphique développée avec **CustomTkinter**. Il inclut également la gestion d'un bouton GPIO pour capturer des photos.

---

## Fonctionnalités

- **Capture de photos :**
  - Depuis l'interface graphique.
  - En appuyant sur un bouton physique connecté au GPIO.
- **Prévisualisation en direct :**
  - Une fenétre séparée affiche le flux vidéo en direct.
- **Enregistrement des photos :**
  - Les photos capturées sont automatiquement enregistrées dans un dossier dédié.

---
projet_webcam/ 
+-- main.py # Point d'entrée principal 
+-- camera.py # Gestion de la caméra (capture, preview, arrét) 
+-- gpio_handler.py # Gestion du bouton GPIO 
+-- gui.py # Interface graphique avec CustomTkinter 
+-- open_app.sh # Script de lancement automatisé 
+-- photos/ # Dossier pour les photos capturées 
+-- app.log # Fichier de logs pour débogage (créé automatiquement) 
+-- README.md # Documentation du projet


---

## Prérequis

1. **Matériel :**
   - Raspberry Pi avec une caméra compatible (e.g., caméra officielle Raspberry Pi).
   - Un bouton connecté au GPIO 24 et au GND.

2. **Logiciels :**
   - Raspberry Pi OS
   - Python 3.7 ou plus récent.

3. **Bibliothèques Python :**
   - `customtkinter`
   - `gpiozero`
   - `picamera2`

---

## Installation

1. **Cloner le projet :**
   ```bash
   git clone https://github.com/votre-utilisateur/projet_webcam.git
   cd projet_webcam
   
2. **Rendre le script exécutable :**
	```bash
	 chmod +x open_app.sh
3. **Rendre le script exécutable :** 
	```bash
	./open_app.sh
## Utilisation
-   **Démarrer l'application :**
    
    -   Lancez le script `open_app.sh`.
-   **Fonctionnalités disponibles :**
    
    -   **Bouton dans l'interface :** Cliquez sur "Prendre une photo" pour capturer une photo.
    -   **Bouton physique :** Appuyez sur le bouton connecté au GPIO 24 pour capturer une photo.
    -   Les photos seront enregistrées dans le dossier `photos/`.
    
    ## Débogage
-   Les logs d'exécution sont disponibles dans le fichier `app.log`.
-   Si le script se ferme immédiatement, lancez-le sans redirection pour voir les erreurs :
```bash
./open_app.sh
```



