# This file take inputs and handles the board per se

import pygame as p
import Chess_Engine


LOGWIDTH = 100
WIDTH = HEIGHT = 512
BUTTONSIZE = 30
DIMENSION = 8
SQ_SIZE = int(HEIGHT/DIMENSION)
MAX_FPS = 15
IMAGES = {}
BUTTONS = {}


# Initialise a dictionary of images and do it only once

def load_images():
    pieces = ["wP", "wR", "wN", "wB", "wQ", "wK", "bP", "bR", "bN", "bB", "bQ", "bK"]
    icons = ["leftArrow", "rightArrow"]

    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE,SQ_SIZE))
    for icon in icons:
        BUTTONS[icon] = p.transform.scale(p.image.load("images/" + icon + ".png"), (BUTTONSIZE,BUTTONSIZE))

    # Note that we can access the image by accessing the dictionary


# Main driver that handles user input and update the graphic

def main():

    p.init()
    screen = p.display.set_mode((WIDTH + LOGWIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"), p.Rect(0, 0, WIDTH, HEIGHT))
    screen.fill(p.Color("black"), rect = p.Rect(WIDTH, 0,LOGWIDTH, HEIGHT))
    gs = Chess_Engine.GameState()
    load_images()
    running = True
    sq_selected = () # No squares selected initially, tuple = (row, col)
    player_clicks = []  # Two tuples that keep tracks of player selection, e.g., [(2,3), (2, 5)] 
    BackButton = Button(image = "leftArrow", pos = [WIDTH + LOGWIDTH/4, 3/4*HEIGHT], size = [BUTTONSIZE, BUTTONSIZE], Screen = screen, bg = "White")
    ForwardButton = Button(image = "rightArrow", pos = [WIDTH + LOGWIDTH/4 , 3/4*HEIGHT + 2*BUTTONSIZE], size = [BUTTONSIZE, BUTTONSIZE], Screen = screen, bg = "White")
    while running:
        for e in p.event.get():
            
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                
                if location[0] < WIDTH:
                    col = location[0]//SQ_SIZE
                    row = location[1]//SQ_SIZE
                    
                    if sq_selected == (row, col): # This is tipically an undo move
                        sq_selected = ()
                        player_clicks = []
                    else:
                        sq_selected = (row, col)
                        player_clicks.append(sq_selected) #append for both 1st and 2nd click
                    if len(player_clicks) == 2:
                        print(player_clicks)
                        move = Chess_Engine.Move(player_clicks[0], player_clicks[1], gs.board, gs.WhiteToMove)
                        gs.makeMove(move)
                        sq_selected = ()
                        player_clicks = []
                else: 
                    if BackButton.click(location):
                        gs.goBackMove()
               #     ForwardButton.click()


        
        draw_game_state(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()



def draw_game_state(screen, gs):
    # Reponsible for the graphic
    draw_board(screen)
    draw_pieces(screen, gs.board)


def draw_board(screen):

    colors = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[(r+c)%2]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

def draw_pieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))



class Button:
    """Create a button, then blit the surface in the while loop"""
    def __init__(self, image, size,  pos, Screen, bg="black"):
        self.x, self.y = pos
        self.size = size
        self.image = image
        self.surface = p.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(BUTTONS[self.image], (self.size[0]/4, self.size[1]/5))
        self.rect = p.Rect(self.x, self.y, self.size[0], self.size[1])
        self.show(Screen)

    def change_button(self, bg="black"):
        """Change the button when you click"""
        self.surface.fill(bg)
        self.surface.blit(self.text, (self.size[0]/4, self.size[1]/5))
        self.rect = p.Rect(self.x, self.y, self.size[0], self.size[1])

    def show(self, screen):
        screen.blit(self.surface, (self.x, self.y))

    def click(self, location):
        x, y = location
        
        if self.rect.collidepoint(x, y):
            print("click")
            return True
                




if __name__ == "__main__":
    main()



















