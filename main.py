from camera import Camera
from gpio_handler import GPIOHandler
from gui import CameraApp

if __name__ == "__main__":
    try:
        # Initialisation de la cam
        camera = Camera()
        camera.start()

        # Init du gestionnaire GPIO
        gpio_handler = GPIOHandler(gpio_pin=24, camera=camera)

        # Lancer l'UI
        app = CameraApp(camera=camera)
        app.mainloop()

    except KeyboardInterrupt:
        print("Arrét manuel.")

    finally:
        camera.stop()
        print("Cam arrétée.")
