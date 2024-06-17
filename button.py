"""Create a button."""
import pygame
from settings import*

class Button:
    """Create a clickable button."""

    # initiator method
    def __init__(self, text: str, size: int,
                 t_colour: str, b_colour: str, o_colour: str, h_colour: str,
                 width: int, height: int, b_x: int, b_y: int) -> None:
        """Initialise."""
        # save colours
        self.b_colour = b_colour  # button colour
        self.o_colour = o_colour  # outline colour
        self.h_colour = h_colour  # hover colour
        self.current_colour = b_colour

        # save dimensions
        self.width = width
        self.height = height

        # create text
        self.text = s_font(size).render(text, True, t_colour)

        self.b_rect = pygame.Rect(b_x, b_y, self.width, self.height)
        self.text_rect = self.text.get_rect(center=(self.b_rect.centerx, self.b_rect.centery))

    # show button on display and allow use
    def show_button(self, surf) -> bool:
        """Show and use button."""
        # handle button position with changable screen
        

        # draw button
        pygame.draw.rect(surf, self.current_colour, self.b_rect, 0, 4)
        pygame.draw.rect(surf, self.o_colour, self.b_rect, 2, 4)
        surf.blit(self.text, self.text_rect)
        
        # handle collisions (user hovering or click)
        action = False
        clicked = False
        m_pos = pygame.mouse.get_pos()

        # mouse on button
        if self.b_rect.collidepoint(m_pos):
            self.current_colour = self.h_colour
            # button down
            if pygame.mouse.get_pressed()[0] == 1:
                clicked = True

            # button clicked
            if pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                action = True
        
        # mouse is not on button
        else:
            self.current_colour = self.b_colour
        return action

