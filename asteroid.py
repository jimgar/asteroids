import random

import pygame

from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            surface=screen,
            color="white",
            center=self.position,
            radius=self.radius,
            width=2,
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)

        new_velocity_positive, new_velocity_negative = [
            self.velocity.rotate(random_angle),
            self.velocity.rotate(-random_angle),
        ]

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid_one, new_asteroid_two = [
            Asteroid(self.position[0], self.position[1], new_radius),
            Asteroid(self.position[0], self.position[1], new_radius),
        ]

        new_asteroid_one.velocity = new_velocity_positive * 1.2
        new_asteroid_two.velocity = new_velocity_negative
