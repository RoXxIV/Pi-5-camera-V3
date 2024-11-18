from gpiozero import Button
from threading import Event
import time


class GPIOHandler:
    def __init__(self, gpio_pin, camera):
        self.button = Button(gpio_pin)
        self.camera = camera  # Instance de la caméra
        self.photo_event = Event()  # Pour éviter les captures multiples
        self.button.when_pressed = self.handle_button_press 
    def handle_button_press(self):
        # Gestion de l'appui sur le bouton.
        if not self.photo_event.is_set():  # éviter les rebonds
            self.photo_event.set()
            try:
                self.camera.take_photo()  # Prend une photo
            finally:
                time.sleep(0.3)  # Break pour éviter les rebonds
                self.photo_event.clear()
