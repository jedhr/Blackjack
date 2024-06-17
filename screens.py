"""Program screens."""
import pygame
import sys
from settings import*
from buttons import*


# screen parent class
class Screen:
    """Screen base."""
    
    # initiator method
    def __init__(self) -> None:
        """Initialise screen."""
        # initialise fps
        self.clock = pygame.time.Clock()  # define FPS
        self.run_display: bool = True

        # create display
        self.screen = pygame.display.set_mode((SCREEN_W, SCREEN_H), pygame.RESIZABLE)
        pygame.display.set_caption(NAME)
        self.display_surf = pygame.display.get_surface()

        self.screen_centerx = pygame.display.get_surface().get_rect().centerx
        self.screen_centery = pygame.display.get_surface().get_rect().centery

    # event handler
    def event_handler(self) -> None:
        """Handle user-interaction events."""
        # update clock ticks and display
        self.clock.tick(FPS)
        pygame.display.update()

        # event handler
        for event in pygame.event.get():
            # quit program if user chooses to quit (click X on window)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # ensure everything is centered regardless of screen size
            if event.type == pygame.VIDEORESIZE:
                self.screen_centerx = pygame.display.get_surface().get_rect().centerx
                self.screen_centery = pygame.display.get_surface().get_rect().centery


# main menu screen
class MainMenu(Screen):
    """Main menu screen."""

    # initiator method
    def __init__(self) -> None:
        """Initialise main menu screen."""
        Screen.__init__(self)  # get parent class info

        # title
        self.title = p_font(40).render(NAME, True, D1_GREEN)      

    # create widgets
    def create_widgets(self) -> None:
        """Create widgets on screen."""
        # title
        title_rect = self.title.get_rect(
            center=(self.screen_centerx, self.screen_centery/2.5))
        self.display_surf.blit(self.title, title_rect)

        # buttons
        self.play_button = Button("Play", 30, D1_GREEN, WHITE,
                                  D1_GREEN, WHITE, D1_GREEN,
                                  100, 40, self.screen_centerx, self.screen_centery)
        self.play_button.show_button(self.display_surf)

    # display screen
    def run(self) -> None:
        """Run main menu screen"""
        while self.run_display:
            # graphical components
            self.display_surf.fill(WHITE)  # bg
            self.create_widgets()

            # update
            self.event_handler()
