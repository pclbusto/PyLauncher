import pygame
import os
import  math

_image_library = {}


class Titulo:
    def __init__(self, imagen, pos):
        self.image_titulo = imagen
        self.pos = pos


class Wheel:

    def __init__(self):
        # calculamos los valores de una circunferencia y guardamos los pares X,Y
        self.lista_valores = []
        self.radio = 100
        for index in range(0, 1000, 1):
            x = 10*(index / 1000)
            y = math.sqrt(self.radio - math.pow(x, 2))*15
            self.lista_valores.append((x,y))
        print(self.lista_valores)

        #cargamos todas las imagenes del directorio
        self.path_titulos = "plataforma\\snes\\titles"
        self.lista_nombre_imagenes_titulos = os.listdir(self.path_titulos)
        self.lista_titulos = []
        #index = 0
        for i,nombre_imagen in enumerate(self.lista_nombre_imagenes_titulos):
            imagen_titulo = self.get_image(os.path.join(self.path_titulos, nombre_imagen))
            self.lista_titulos.append(Titulo(imagen_titulo, self.lista_valores[i]))
            #index+=200

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
    #os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 0)11
    pygame.init()
    screen = pygame.display.set_mode( (800, 600),pygame.DOUBLEBUF)
    done = False
    clock = pygame.time.Clock()
    angle = 0
    y = 0
    x = 0
    i = 0
    while not done:
        i=i+1
        i=i%(500-len(w.lista_titulos))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill((0, 0, 0))
        # angle -= 0.01
        # scale +=0.001
        # ensure angle does not increase indefinitely
        # angle %= 360
        # create a new, rotated Surface

        for index,imagen_titulo in enumerate(w.lista_titulos):
            imagen_titulo.pos = (200, w.lista_valores[i+index][1])
            old_size = imagen_titulo.image_titulo.get_size()
            new_size = (int(old_size[0]*w.lista_valores[i+index][0]),int(old_size[1]*w.lista_valores[i+index][0]))
            print("viejo tama {}".format(old_size))
            print("Nuevo tama {}".format(new_size))
            print(i)
            image_res = pygame.transform.scale(imagen_titulo.image_titulo,new_size)
            screen.blit(image_res, imagen_titulo.pos)

        pygame.display.flip()
        clock.tick(60)
