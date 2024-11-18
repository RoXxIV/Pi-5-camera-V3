import customtkinter as ctk


class CameraApp(ctk.CTk):
    def __init__(self, camera):
        super().__init__()
        self.camera = camera  # Instance de la caméra

        # Configuration de la fenétre principale
        self.title("PiCam Interface")
        self.geometry("500x250")
        self.resizable(False, False)

        # Titre
        self.label = ctk.CTkLabel(self, text="Custom webcam", font=("Arial", 20))
        self.label.pack(pady=15)

        # Bouton prendre une photo
        self.photo_button = ctk.CTkButton(self, text="Prendre une photo", command=self.camera.take_photo)
        self.photo_button.pack(pady=10)

        # Bouton arréter
        self.exit_button = ctk.CTkButton(self, text="éteindre", command=self.stop_app)
        self.exit_button.pack(pady=10)

    def stop_app(self):
        # Arréte la cam et ferme l'appli.
        self.camera.stop()
        self.destroy()  # Ferme la fenétre
        print("Application arrétée.")