import random
import pygame


class cubito(object):
    rows = 10
    width_c = 500

    def __init__(self, start, dirx=1, diry=0, color=(0, 0, 255)):  # Define la posición del cubo inicial y su color
        self.position = start
        self.dirx = 1
        self.diry = 0
        self.color = color

    def move(self, dirx, diry):  # Define el movimiento mediante cuadrantes
        self.dirx = dirx
        self.diry = diry
        self.position = (self.position[0] + self.dirx, self.position[1] + self.diry)

    def draw(self, surface):  # Dibujando el cubito
        dis = self.width_c // self.rows
        i = self.position[0]
        j = self.position[1]

        pygame.draw.rect(surface, self.color, (i * dis + 1, j * dis + 1, dis - 2, dis - 2))


class snake(object):
    body = []
    turns = {}

    def __init__(self, color, position):  # Definiendo la posición inicial y como obtiene su cuerpo y color
        self.color = color
        self.head = cubito(position)
        self.body.append(self.head)
        self.dirx = 0
        self.diry = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for key in keys:  # Asegurandonos que las teclas que se presionen tengan la dirección correcta
                if keys[pygame.K_LEFT]:
                    self.dirx = -1
                    self.diry = 0
                    self.turns[self.head.position[:]] = [self.dirx, self.diry]

                elif keys[pygame.K_RIGHT]:
                    self.dirx = 1
                    self.diry = 0
                    self.turns[self.head.position[:]] = [self.dirx, self.diry]

                elif keys[pygame.K_UP]:
                    self.dirx = 0
                    self.diry = -1
                    self.turns[self.head.position[:]] = [self.dirx, self.diry]

                elif keys[pygame.K_DOWN]:
                    self.dirx = 0
                    self.diry = 1
                    self.turns[self.head.position[:]] = [self.dirx, self.diry]

        for i, c in enumerate(self.body):
            p = c.position[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body) - 1:
                    self.turns.pop(p)
            else:
                if c.dirx == -1 and c.position[0] <= 0:
                    c.position = (c.rows - 1, c.position[1])
                elif c.dirx == 1 and c.position[0] >= c.rows - 1:
                    c.position = (0, c.position[1])
                elif c.diry == 1 and c.position[1] >= c.rows - 1:
                    c.position = (c.position[0], 0)
                elif c.diry == -1 and c.position[1] <= 0:
                    c.position = (c.position[0], c.rows - 1)
                else:
                    c.move(c.dirx, c.diry)

    def reset(self, position):
        self.head = cubito(position)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirx = 0
        self.diry = 1

    def addCubito(self):
        tail = self.body[-1]
        dx, dy = tail.dirx, tail.diry

        if dx == 1 and dy == 0:
            self.body.append(cubito((tail.position[0] - 1, tail.position[1])))
        elif dx == -1 and dy == 0:
            self.body.append(cubito((tail.position[0] + 1, tail.position[1])))
        elif dx == 0 and dy == 1:
            self.body.append(cubito((tail.position[0], tail.position[1] - 1)))
        elif dx == 0 and dy == -1:
            self.body.append(cubito((tail.position[0], tail.position[1] + 1)))

        self.body[-1].dirx = dx
        self.body[-1].diry = dy

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface)
            else:
                c.draw(surface)


def drawGrid(width, rows, surface):
    espacio = width // rows

    x = 0
    y = 0

    for l in range(rows):
        x = x + espacio
        y = y + espacio

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, width))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (width, y))


def redrawWindow(surface):
    global rows, width, serpiente, comida
    surface.fill((0, 0, 0))
    serpiente.draw(surface)
    comida.draw(surface)
    drawGrid(width, rows, surface)
    pygame.display.update()


def comidaRandom(rows, item):
    positions = item.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z: z.position == (x, y), positions))) > 0:
            continue
        else:
            break

    return x, y


def main():
    global width, rows, serpiente, comida
    width = 500
    rows = 10
    win = pygame.display.set_mode((width, width))
    serpiente = snake((255, 0, 0), (10, 10))
    comida = cubito(comidaRandom(rows, serpiente), color=(0, 255, 0))
    flag = True

    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        serpiente.move()
        if serpiente.body[0].position == comida.position:
            serpiente.addCubito()
            comida = cubito(comidaRandom(rows, serpiente), color=(0, 255, 0))

        for x in range(len(serpiente.body)):
            if serpiente.body[x].position in list(map(lambda z:z.position, serpiente.body[x+1:])):
                print("Perdiste, lograste comer:", len(serpiente.body))
                serpiente.reset((10,10))

        redrawWindow(win)

    pass


main()
