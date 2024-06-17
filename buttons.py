"""Create a button."""
import pygame
from settings import*

# clickable button
class Button:
    """Create a clickable button."""

    # initiator method
    def __init__(self, text: str, t_size: int, t1_colour: str, t2_colour: str,
                 o_colour: str, b_colour: str, h_colour: str,
                 width: int, height: int, b_x: int, b_y: int) -> None:
            """Initialise button."""
            # save colours
            # text colours
            self.t1_colour = t1_colour
            self.t2_colour = t2_colour

            # button colours
            self.o_colour = o_colour
            self.b_colour = b_colour
            self.h_colour = h_colour
            self.current_colour = b_colour

            # save dimensions
            self.width = width
            self.height = height
            self.b_rect = pygame.Rect(b_x, b_y, self.width, self.height)

            # create text
            self.t1 = s_font(t_size).render(text, True, t1_colour)  # primary
            self.t2 = s_font(t_size).render(text, True, t2_colour)  # hover
            self.t_rect = self.t1.get_rect(center=(self.b_rect.centerx, self.b_rect.centery))

        # show button on display
    def show_button(self, surf) -> bool:
        """Show and use button."""
        # handle collisions
        action = False
        clicked = False
        m_pos = pygame.mouse.get_pos()

        # mouse on button
        if self.b_rect.collidepoint(m_pos):
            self.current_colour = self.h_colour
            pygame.draw.rect(surf, self.current_colour, self.b_rect, 0, 4)  # button bg
            surf.blit(self.t2, self.t_rect)  # hovered over text

            # button down
            if pygame.mouse.get_pressed()[0] == 1:
                    clicked = True

            # button clicked
            if pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                   clicked = False
                   action = True

        else:
            self.current_colour = self.b_colour
            pygame.draw.rect(surf, self.current_colour, self.b_rect, 0, 4)  # button bg
            surf.blit(self.t1, self.t_rect)  # not hovered over

        pygame.draw.rect(surf, self.o_colour, self.b_rect, 2, 4)  # outline

        return clicked