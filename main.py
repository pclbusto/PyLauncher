import pygame
import os

_image_library = {}


class Titulo:
    def __init__(self, imagen, pos):
        self.image_titulo = imagen
        self.pos = pos


class Wheel:

    def __init__(self):
        #cargamos todas las imagenes del directorio
        self.path_titulos = "plataforma/snes/titles"
        self.lista_nombre_imagenes_titulos = os.listdir(self.path_titulos)
        self.lista_titulos = []
        index = 0;
        for nombre_imagen in self.lista_nombre_imagenes_titulos:
            imagen_titulo = self.get_image(os.path.join(self.path_titulos, nombre_imagen))
            self.lista_titulos.append(Titulo(imagen_titulo, (index,800)))
            index+=200

    def get_image(self, path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
            canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
            image = pygame.image.load(path)
            _image_library[path] = image
        return image


if __name__ == "__main__":
    w = Wheel()
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    done = False
    clock = pygame.time.Clock()
    angle = 0
    y = 0
    x = 0
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill((0, 255, 255))
        angle -= 0.01
        # scale +=0.001
        # ensure angle does not increase indefinitely
        # angle %= 360
        # create a new, rotated Surface

        for imagen_titulo in w.lista_titulos:
            imagen_titulo.pos = (imagen_titulo.pos[0]+2, imagen_titulo.pos[1])
            screen.blit(imagen_titulo.image_titulo, imagen_titulo.pos)

        pygame.display.flip()
        clock.tick(120)

