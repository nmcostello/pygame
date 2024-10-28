from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import pygame
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius == ASTEROID_MIN_RADIUS:
            return

        spawn_angle = random.uniform(20, 50)
        asteroid_one_velocity = pygame.math.Vector2.rotate(self.velocity, spawn_angle)
        asteroid_two_velocity = pygame.math.Vector2.rotate(self.velocity, -spawn_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_one.velocity = asteroid_one_velocity * 1.2
        asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_two.velocity = asteroid_two_velocity * 1.2
