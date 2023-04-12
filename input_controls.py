"""
Module containing classes to manage keyboard, mouse, joy-pad input.

This module requires Pygame 2.3.0+
"""

import pygame


class KeyboardInput:
    """Keybindings for keyboard controls."""
    def __init__(self):
        self.quit_key = pygame.K_q
        self.player_up = pygame.K_UP
        self.player_down = pygame.K_DOWN
        self.pause = pygame.K_p
