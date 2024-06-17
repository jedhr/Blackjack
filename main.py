"""
Play Blackjack with an Onslow Twist.

Created by: Jedh
Date: 2024-06-17
"""
import pygame
from screens import*

# run main
class Main:
    """Main program."""

    def __init__(self) -> None:
        """Initialise."""
        pygame.init()

        # screens
        self.main_menu = MainMenu()

    def run(self) -> None:
        """Run program."""
        self.main_menu.run()
        

if __name__ == "__main__":
    # run program
    main = Main()
    main.run()
