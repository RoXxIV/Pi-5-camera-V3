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

        # slider
        self.slider_label = ctk.CTkLabel(self, text="lens")
        self.slider_label.pack(pady=5)

        self.slider = ctk.CTkSlider(self, from_=0.00, to=10.0, command=self.slider_event)
        self.slider.pack(pady=5)

        # Bouton arréter
        self.exit_button = ctk.CTkButton(self, text="éteindre", command=self.stop_app)
        self.exit_button.pack(pady=10)

    def slider_event(self, value):
        # mise a jour du lens
        self.camera.set_lens(value)
        print(f"Valeur du slider : {value}")

    def stop_app(self):
        # Arréte la cam et ferme l'appli.
        self.camera.stop()
        self.destroy()  # Ferme la fenétre
        print("Application arrétée.")
