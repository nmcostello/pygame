import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED


class Player(CircleShape):

    def __init__(self, x, y):
        """
        Initializes a new Player instance.

        Args:
            x (float): The x-coordinate of the player's initial position.
            y (float): The y-coordinate of the player's initial position.
        """
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    # in the player class
    def triangle(self):
        """
        Calculates the vertices of the triangle representing the player on the screen.

        Returns:
            list: A list of three pygame.Vector2 points representing the triangle vertices.
        """

        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        """
        Draws the player on the screen as a white triangle.

        Args:
            screen (pygame.Surface): The surface to draw the player on.
        """
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    def rotate(self, dt):
        """
         Rotates the player based on the player's turning speed and the elapsed time.

         Args:
             dt (float): The time difference since the last frame, in seconds.
         """
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        """
        Updates the player's state. Processes input to rotate the player if needed.

        Args:
            dt (float): The time difference since the last frame, in seconds.
        """
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt)
        if keys[pygame.K_d]:
            self.rotate(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)


    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
