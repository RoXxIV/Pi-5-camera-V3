from picamera2 import Picamera2, Preview
from datetime import datetime
import os


class Camera:
    def __init__(self):
        # Init de la caméra Picamera2
        self.picam2 = Picamera2()
        camera_config = self.picam2.create_preview_configuration()
        self.picam2.configure(camera_config)

        # Dossier pour enregistrer les photos
        self.photos_path = "/home/roxx/Desktop/projet_webcam/photos"
        os.makedirs(self.photos_path, exist_ok=True)

    def start(self):
        # Démarre la cam avec le preview.
        self.picam2.start_preview(Preview.QTGL)
        self.picam2.start()
        print("Caméra démarrée avec prévisualisation.")

    def stop(self):
        # Arréte la cam
        try:
            self.picam2.stop_preview()
        except RuntimeError as e:
            print(f"Avertissement : {e}")
        finally:
            self.picam2.close()
            print("Caméra arrétée.")

    def take_photo(self):
        # Prend une photo et l'enregistre avec un horodatage.
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_path = os.path.join(self.photos_path, f"pic_{timestamp}.jpg")
            self.picam2.capture_file(file_path)
            print(f"Photo capturée et sauvegardée : {file_path}")
            return file_path
        except Exception as e:
            print(f"Erreur lors de la capture : {e}")
