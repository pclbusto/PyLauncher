import pygame
import os

_image_library = {}


class Titulo:
    def __init__(self, imagen, pos,z):
        self.image_titulo = imagen
        self.pos = pos
        self.z = z

class Wheel:

    def __init__(self):
        #cargamos todas las imagenes del directorio
        self.path_titulos = "plataforma/snes/titles"
        self.lista_nombre_imagenes_titulos = os.listdir(self.path_titulos)
        self.lista_titulos = []
        index = 0;
        delta_z = 1/len(self.lista_nombre_imagenes_titulos);
        z = delta_z;
        for nombre_imagen in self.lista_nombre_imagenes_titulos:
            imagen_titulo = self.get_image(os.path.join(self.path_titulos, nombre_imagen))
            # imagen_titulo = imagen_titulo.convert()
            self.lista_titulos.append(Titulo(imagen_titulo, (600, index)), z)
            z += delta_z
            index += imagen_titulo.get_height()

    def get_image(self, path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
            canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
            image = pygame.image.load(path)
            _image_library[path] = image
        return image


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((int (pygame.display.Info().current_w/2), int(pygame.display.Info().current_h/2)))

    w = Wheel()
    done = False
    clock = pygame.time.Clock()
    angle = 0
    y = 0
    x = 0
    imagen_titulo = w.lista_titulos[3].image_titulo
    center = imagen_titulo.get_rect().center
    center = (center[0],center[1])
    scale=1
    print(center)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill((0, 255, 255))
        angle -= 5%360
        scale -=0.01
        # ensure angle does not increase indefinitely
        # angle %= 360
        # create a new, rotated Surface

        for imagen_titulo in w.lista_titulos:
            pos = (imagen_titulo.pos[0], imagen_titulo.pos[1]+300)
            screen.blit(imagen_titulo.image_titulo, pos)

        events = pygame.event.get()
        for event in events:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                print("Arriba")
            if keys[pygame.K_DOWN]:
                print("Abajo")

        pygame.display.flip()
        clock.tick(60)

