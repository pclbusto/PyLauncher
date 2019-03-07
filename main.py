import pygame
import os
import numpy as np

_image_library = {}


class Titulo:
    def __init__(self, imagen, pos, z):
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
        delta_z = 360/len(self.lista_nombre_imagenes_titulos);
        z = delta_z
        print(len(self.lista_nombre_imagenes_titulos))
        for nombre_imagen in self.lista_nombre_imagenes_titulos:
            imagen_titulo = self.get_image(os.path.join(self.path_titulos, nombre_imagen))
            # imagen_titulo = imagen_titulo.convert()
            self.lista_titulos.append(Titulo(imagen_titulo, (500, index), z))
            z += delta_z
            index += int(imagen_titulo.get_height())

    def get_image(self, path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
            canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
            image = pygame.image.load(path)
            _image_library[path] = image
        return image

    def get_points(self, radius, number_of_points):
        radians_between_each_point = 2 * np.pi / number_of_points
        list_of_points = []
        for p in range(0, number_of_points):
            list_of_points.append(
                (radius * np.cos(p * radians_between_each_point), radius * np.sin(p * radians_between_each_point)))
        return list_of_points

if __name__ == "__main__":
    pygame.init()
    # screen = pygame.display.set_mode((int (pygame.display.Info().current_w/2), int(pygame.display.Info().current_h/2)))
    screen = pygame.display.set_mode((int (pygame.display.Info().current_w), int(pygame.display.Info().current_h)))

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
    lista_puntos = w.get_points(400, len(w.lista_titulos))
    lst_points = []
    for punto in lista_puntos:
        point = (punto[0]+400, punto[1]+400)
        lst_points.append(point)

    print("LISTA")
    print(lst_points)
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

        for index, imagen_titulo in  enumerate(w.lista_titulos):
            pos = (imagen_titulo.pos[0], imagen_titulo.pos[1])
            # rect = imagen_titulo.image_titulo.get_rect(center=(500, imagen_titulo.pos[1]+200))
            rect = imagen_titulo.image_titulo.get_rect(center=(500, 200))

            # print(rect.center)
            imagen = pygame.transform.scale(imagen_titulo.image_titulo, (int(imagen_titulo.image_titulo.get_width()/2),int( imagen_titulo.image_titulo.get_height()/2)))

            rect = imagen.get_rect(center=(lst_points[index][0], lst_points[index][1]))

        # imagen = imagen_titulo
        # rect = imagen.get_rect(center=(900, 500))
            screen.blit(imagen, rect)
        # print("---------------------------------------")
        events = pygame.event.get()
        for event in events:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                print("Arriba")
            if keys[pygame.K_DOWN]:
                print("Abajo")

        pygame.display.flip()
        clock.tick(60)

