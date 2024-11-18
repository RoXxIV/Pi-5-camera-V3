
# Projet Webcam avec Raspberry Pi

Ce projet permet de contr�ler une cam�ra module v3 connect�e � un Raspberry Pi 5 via une interface graphique d�velopp�e avec **CustomTkinter**. Il inclut �galement la gestion d'un bouton GPIO pour capturer des photos.

---

## Fonctionnalit�s

- **Capture de photos :**
  - Depuis l'interface graphique.
  - En appuyant sur un bouton physique connect� au GPIO.
- **Pr�visualisation en direct :**
  - Une fen�tre s�par�e affiche le flux vid�o en direct.
- **Enregistrement des photos :**
  - Les photos captur�es sont automatiquement enregistr�es dans un dossier d�di�.

---
projet_webcam/ 
+-- main.py # Point d'entr�e principal 
+-- camera.py # Gestion de la cam�ra (capture, preview, arr�t) 
+-- gpio_handler.py # Gestion du bouton GPIO 
+-- gui.py # Interface graphique avec CustomTkinter 
+-- open_app.sh # Script de lancement automatis� 
+-- photos/ # Dossier pour les photos captur�es 
+-- app.log # Fichier de logs pour d�bogage (cr�� automatiquement) 
+-- README.md # Documentation du projet


---

## Pr�requis

1. **Mat�riel :**
   - Raspberry Pi avec une cam�ra compatible (e.g., cam�ra officielle Raspberry Pi).
   - Un bouton connect� au GPIO 24 et au GND.

2. **Logiciels :**
   - Raspberry Pi OS
   - Python 3.7 ou plus r�cent.

3. **Biblioth�ques Python :**
   - `customtkinter`
   - `gpiozero`
   - `picamera2`

---

## Installation

1. **Cloner le projet :**
   ```bash
   git clone https://github.com/votre-utilisateur/projet_webcam.git
   cd projet_webcam
   
2. **Rendre le script ex�cutable :**
	```bash
	 chmod +x open_app.sh
3. **Rendre le script ex�cutable :** 
	```bash
	./open_app.sh
## Utilisation
-   **D�marrer l'application :**
    
    -   Lancez le script `open_app.sh`.
-   **Fonctionnalit�s disponibles :**
    
    -   **Bouton dans l'interface :** Cliquez sur "Prendre une photo" pour capturer une photo.
    -   **Bouton physique :** Appuyez sur le bouton connect� au GPIO 24 pour capturer une photo.
    -   Les photos seront enregistr�es dans le dossier `photos/`.
    
    ## D�bogage
-   Les logs d'ex�cution sont disponibles dans le fichier `app.log`.
-   Si le script se ferme imm�diatement, lancez-le sans redirection pour voir les erreurs :
```bash
./open_app.sh
```



