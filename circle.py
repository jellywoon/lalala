import pygame
import random
class Circle:
    def __init__(self, x, y, color, radius, thickness, direction):
        self.x = x
        self.y = y
        self.radius = radius
        self.thickness = thickness
        self.color = color
        self.direction = direction
    def make_circle(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, self.thickness)
    def move(self):
        if self.direction == 'right':
            self.x += 1
            if (self.x + self.radius) == 800:
                self.direction = 'left'
        if self.direction == 'left':
            self.x -= 1
            if (self.x - self.radius) == 0:
                self.direction = 'right'