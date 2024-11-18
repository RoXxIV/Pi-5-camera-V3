#!/bin/bash

# Chemin vers le dossier du projet
PROJECT_DIR="/home/roxx/Desktop/projet_webcam"

# Chemin vers l'environnement virtuel
VENV_PATH="$PROJECT_DIR/venv"

# Activer le venv ou le creer s'il n'existe pas
if [ -d "$VENV_PATH" ]; then
    source "$VENV_PATH/bin/activate"
else
    echo "L'environnement virtuel n'existe pas. Cr�ation d'un venv..."
    python3 -m venv "$VENV_PATH"
    source "$VENV_PATH/bin/activate"
fi

# Mettre a jour pip et installer les dependances
pip install --upgrade pip
pip install customtkinter gpiozero picamera2

# Lancer le script principal sans redirection
python3 "$PROJECT_DIR/main.py"

# Empecher la fermeture immediate
echo "Appuyez sur une touche pour quitter..."
read -n 1
