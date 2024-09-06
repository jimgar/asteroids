import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for o in updatable:
            o.update(dt)

        for o in asteroids:
            if o.check_if_colliding(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if o.check_if_colliding(shot):
                    o.kill()
                    shot.kill()

        screen.fill("black")

        for o in drawable:
            o.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        delta = clock.tick(60)
        dt = delta / 1000


if __name__ == "__main__":
    main()
