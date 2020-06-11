import pygame
# print(dir(pygame))
import chessv6

pygame.init()

display_width = 800
display_height = 800

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("chess")

paint_black=(0,0,0)
paint_white=(255,255,255)
paint_red=(255,0,0)
paint_green=(0,255,0)
paint_blue=(0,0,255)
clock = pygame.time.Clock()
crashed = False
counter=1
white_pawn_image = pygame.image.load("white_pawn.png")
black_pawn_image = pygame.image.load("black_pawn.png")
white_queen_image = pygame.image.load("white_queen.png")
black_queen_image = pygame.image.load("black_queen.png")
white_rook_image = pygame.image.load("white_rook.png")
black_rook_image = pygame.image.load("black_rook.png")
white_bishop_image = pygame.image.load("white_bishop.png")
black_bishop_image = pygame.image.load("black_bishop.png")
white_king_image = pygame.image.load("white_king.png")
black_king_image = pygame.image.load("black_king.png")
white_knight_image = pygame.image.load("white_knight.png")
black_knight_image = pygame.image.load("black_knight.png")

def chess_board_gui(x,y):
    gameDisplay.blit(chess_board_image,(x,y))

def gui_turn():
    for square in square_gui_tuple:
        square.clicked=False
    for piece in chessv6.piece_tuple:
        piece.chess_replace()


class pawn_gui:

    def __init__(self,identity,colour):
        self.identity=identity
        self.colour=colour
        self.selected=False

    def display_piece(self):
        for square in square_gui_tuple:
            if square.coordinate == self.identity.chess_replace() and self.identity.captured == False:
                if self.colour == "white":
                    gameDisplay.blit(white_pawn_image,(square.x,square.y))
                    continue
                if self.colour == "black":
                    gameDisplay.blit(black_pawn_image,(square.x,square.y))

pawn_a_w_gui = pawn_gui(chessv6.pawn_a_w,"white")
pawn_b_w_gui = pawn_gui(chessv6.pawn_b_w,"white")
pawn_c_w_gui = pawn_gui(chessv6.pawn_c_w,"white")
pawn_d_w_gui = pawn_gui(chessv6.pawn_d_w,"white")
pawn_e_w_gui = pawn_gui(chessv6.pawn_e_w,"white")
pawn_f_w_gui = pawn_gui(chessv6.pawn_f_w,"white")
pawn_g_w_gui = pawn_gui(chessv6.pawn_g_w,"white")
pawn_h_w_gui = pawn_gui(chessv6.pawn_h_w,"white")

pawn_a_b_gui = pawn_gui(chessv6.pawn_a_b,"black")
pawn_b_b_gui = pawn_gui(chessv6.pawn_b_b,"black")
pawn_c_b_gui = pawn_gui(chessv6.pawn_c_b,"black")
pawn_d_b_gui = pawn_gui(chessv6.pawn_d_b,"black")
pawn_e_b_gui = pawn_gui(chessv6.pawn_e_b,"black")
pawn_f_b_gui = pawn_gui(chessv6.pawn_f_b,"black")
pawn_g_b_gui = pawn_gui(chessv6.pawn_g_b,"black")
pawn_h_b_gui = pawn_gui(chessv6.pawn_h_b,"black")

# pawn_gui_tuple = (pawn_a_w_gui,pawn_b_w_gui,pawn_c_w_gui,pawn_d_w_gui,pawn_e_w_gui,pawn_f_w_gui,pawn_g_w_gui,pawn_h_w_gui,pawn_a_b_gui,pawn_b_b_gui,pawn_c_b_gui,pawn_d_b_gui,pawn_e_b_gui,pawn_f_b_gui,pawn_g_b_gui,pawn_h_b_gui)

class queen_gui:

    def __init__(self,identity,colour):
        self.identity=identity
        self.colour=colour
        self.selected=False

    def display_piece(self):
        for square in square_gui_tuple:
            if square.coordinate == self.identity.chess_replace() and self.identity.captured == False:
                if self.colour == "white":
                    gameDisplay.blit(white_queen_image,(square.x,square.y))
                    continue
                if self.colour == "black":
                    gameDisplay.blit(black_queen_image,(square.x,square.y))

queen_1_w_gui = queen_gui(chessv6.queen_1_w,"white")
queen_1_b_gui = queen_gui(chessv6.queen_1_b,"black")


class rook_gui:

    def __init__(self,identity,colour):
        self.identity=identity
        self.colour=colour
        self.selected=False

    def display_piece(self):
        for square in square_gui_tuple:
            if square.coordinate == self.identity.chess_replace() and self.identity.captured == False:
                if self.colour == "white":
                    gameDisplay.blit(white_rook_image,(square.x,square.y))
                    continue
                if self.colour == "black":
                    gameDisplay.blit(black_rook_image,(square.x,square.y))

rook_1_w_gui = rook_gui(chessv6.rook_1_w,"white")
rook_1_b_gui = rook_gui(chessv6.rook_1_b,"black")
rook_2_w_gui = rook_gui(chessv6.rook_2_w,"white")
rook_2_b_gui = rook_gui(chessv6.rook_2_b,"black")

class king_gui:

    def __init__(self,identity,colour):
        self.identity=identity
        self.colour=colour
        self.selected=False

    def display_piece(self):
        for square in square_gui_tuple:
            if square.coordinate == self.identity.chess_replace() and self.identity.captured == False:
                if self.colour == "white":
                    gameDisplay.blit(white_king_image,(square.x,square.y))
                    continue
                if self.colour == "black":
                    gameDisplay.blit(black_king_image,(square.x,square.y))

king_1_w_gui = king_gui(chessv6.king_1_w,"white")
king_1_b_gui = king_gui(chessv6.king_1_b,"black")

class bishop_gui:

    def __init__(self,identity,colour):
        self.identity=identity
        self.colour=colour
        self.selected=False

    def display_piece(self):
        for square in square_gui_tuple:
            if square.coordinate == self.identity.chess_replace() and self.identity.captured == False:
                if self.colour == "white":
                    gameDisplay.blit(white_bishop_image,(square.x,square.y))
                    continue
                if self.colour == "black":
                    gameDisplay.blit(black_bishop_image,(square.x,square.y))

bishop_1_w_gui = bishop_gui(chessv6.bishop_1_w,"white")
bishop_1_b_gui = bishop_gui(chessv6.bishop_1_b,"black")
bishop_2_w_gui = bishop_gui(chessv6.bishop_2_w,"white")
bishop_2_b_gui = bishop_gui(chessv6.bishop_2_b,"black")

class knight_gui:

    def __init__(self,identity,colour):
        self.identity=identity
        self.colour=colour
        self.selected=False

    def display_piece(self):
        for square in square_gui_tuple:
            if square.coordinate == self.identity.chess_replace() and self.identity.captured == False:
                if self.colour == "white":
                    gameDisplay.blit(white_knight_image,(square.x,square.y))
                    continue
                if self.colour == "black":
                    gameDisplay.blit(black_knight_image,(square.x,square.y))

knight_1_w_gui = knight_gui(chessv6.knight_1_w,"white")
knight_1_b_gui = knight_gui(chessv6.knight_1_b,"black")
knight_2_w_gui = knight_gui(chessv6.knight_2_w,"white")
knight_2_b_gui = knight_gui(chessv6.knight_2_b,"black")

class square_gui:

    def __init__(self,x,y,colour,identity):
        self.x = x
        self.y = y
        self.colour = colour
        self.identity=identity
        self.coordinate=identity.coordinate
        self.clicked=False

    def draw_square(self):
        pygame.draw.rect(gameDisplay,self.colour,[self.x,self.y,100,100])

    def display_potential_moves(self):
        pygame.draw.rect(gameDisplay,paint_green,[self.x+40,self.y+40,20,20])

    def display_potential_attacks(self):
        pygame.draw.rect(gameDisplay,paint_red,[self.x+40,self.y+40,20,20])

    def button(self):
        if pygame.mouse.get_pressed()[0] == 1:
            if self.x+100 > pygame.mouse.get_pos()[0] > self.x and self.y+100 > pygame.mouse.get_pos()[1] > self.y :
                for piece in chessv6.piece_tuple:
                    if self.coordinate in piece.potential_attack_list or self.coordinate in piece.potential_move_list:
                        if piece.piece_type =="w_pawn" and chessv6.whos_turn == "white":
                            if self.coordinate in piece.potential_move_coordinate and piece.selected == True:
                                if piece.is_pinned() == True:
                                    break
                                piece.move()
                                gui_turn()
                            if self.coordinate in piece.potential_move_of_two_squares_coordinate and piece.selected == True:
                                if piece.is_pinned() == True:
                                    break
                                piece.move_of_two_squares()
                                gui_turn()
                            if self.coordinate in piece.potential_capture_up_coordinate and piece.selected == True:
                                if piece.is_pinned() == True:
                                    break
                                piece.capture_up()
                                gui_turn()
                            if self.coordinate in piece.potential_capture_down_coordinate and piece.selected == True:
                                if piece.is_pinned() == True:
                                    break
                                piece.capture_down()
                                gui_turn()

                        if piece.piece_type == "b_pawn" and chessv6.whos_turn == "black":

                            if self.coordinate in piece.potential_move_coordinate and piece.selected == True:
                                if piece.is_pinned() == True:
                                    break
                                piece.move()
                                gui_turn()
                            if self.coordinate in piece.potential_move_of_two_squares_coordinate and piece.selected == True:
                                if piece.is_pinned() == True:
                                    break
                                piece.move_of_two_squares()
                                gui_turn()
                            if self.coordinate in piece.potential_capture_up_coordinate and piece.selected == True:
                                if piece.is_pinned() == True:
                                    break
                                piece.capture_up()
                                gui_turn()
                            if self.coordinate in piece.potential_capture_down_coordinate and piece.selected == True:
                                if piece.is_pinned() == True:
                                    break
                                piece.capture_down()
                                gui_turn()

                        if piece.piece_type == "w_queen" and chessv6.whos_turn == "white":

                            if self.coordinate in piece.potential_move_up_coordinate and piece.selected == True:
                                piece.move_up()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_2_coordinate and piece.selected == True:
                                piece.move_up_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_3_coordinate and piece.selected == True:
                                piece.move_up_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_4_coordinate and piece.selected == True:
                                piece.move_up_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_5_coordinate and piece.selected == True:
                                piece.move_up_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_6_coordinate and piece.selected == True:
                                piece.move_up_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_7_coordinate and piece.selected == True:
                                piece.move_up_7()
                                gui_turn()
                                chessv6.turn()

                            if self.coordinate in piece.potential_attack_up_coordinate and piece.selected == True:
                                piece.attack_up()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_2_coordinate and piece.selected == True:
                                piece.attack_up_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_3_coordinate and piece.selected == True:
                                piece.attack_up_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_4_coordinate and piece.selected == True:
                                piece.attack_up_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_5_coordinate and piece.selected == True:
                                piece.attack_up_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_6_coordinate and piece.selected == True:
                                piece.attack_up_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_7_coordinate and piece.selected == True:
                                piece.attack_up_7()
                                gui_turn()
                                chessv6.turn()

                            if self.coordinate in piece.potential_move_down_coordinate and piece.selected == True:
                                piece.move_down()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_2_coordinate and piece.selected == True:
                                piece.move_down_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_3_coordinate and piece.selected == True:
                                piece.move_down_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_4_coordinate and piece.selected == True:
                                piece.move_down_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_5_coordinate and piece.selected == True:
                                piece.move_down_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_6_coordinate and piece.selected == True:
                                piece.move_down_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_7_coordinate and piece.selected == True:
                                piece.move_down_7()
                                gui_turn()
                                chessv6.turn()

                            if self.coordinate in piece.potential_attack_down_coordinate and piece.selected == True:
                                piece.attack_down()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_2_coordinate and piece.selected == True:
                                piece.attack_down_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_3_coordinate and piece.selected == True:
                                piece.attack_down_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_4_coordinate and piece.selected == True:
                                piece.attack_down_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_5_coordinate and piece.selected == True:
                                piece.attack_down_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_6_coordinate and piece.selected == True:
                                piece.attack_down_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_7_coordinate and piece.selected == True:
                                piece.attack_down_7()
                                gui_turn()
                                chessv6.turn()


                            if self.coordinate in piece.potential_move_right_coordinate and piece.selected == True:
                                piece.move_right()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_right_2_coordinate and piece.selected == True:
                                piece.move_right_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_right_3_coordinate and piece.selected == True:
                                piece.move_right_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_right_4_coordinate and piece.selected == True:
                                piece.move_right_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_right_5_coordinate and piece.selected == True:
                                piece.move_right_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_right_6_coordinate and piece.selected == True:
                                piece.move_right_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_right_7_coordinate and piece.selected == True:
                                piece.move_right_7()
                                gui_turn()
                                chessv6.turn()

                            if self.coordinate in piece.potential_attack_right_coordinate and piece.selected == True:
                                piece.attack_right()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_right_2_coordinate and piece.selected == True:
                                piece.attack_right_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_right_3_coordinate and piece.selected == True:
                                piece.attack_right_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_right_4_coordinate and piece.selected == True:
                                piece.attack_right_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_right_5_coordinate and piece.selected == True:
                                piece.attack_right_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_right_6_coordinate and piece.selected == True:
                                piece.attack_right_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_right_7_coordinate and piece.selected == True:
                                piece.attack_right_7()
                                gui_turn()
                                chessv6.turn()


                            if self.coordinate in piece.potential_move_left_coordinate and piece.selected == True:
                                piece.move_left()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_left_2_coordinate and piece.selected == True:
                                piece.move_left_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_left_3_coordinate and piece.selected == True:
                                piece.move_left_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_left_4_coordinate and piece.selected == True:
                                piece.move_left_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_left_5_coordinate and piece.selected == True:
                                piece.move_left_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_left_6_coordinate and piece.selected == True:
                                piece.move_left_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_left_7_coordinate and piece.selected == True:
                                piece.move_left_7()
                                gui_turn()
                                chessv6.turn()

                            if self.coordinate in piece.potential_attack_left_coordinate and piece.selected == True:
                                piece.attack_left()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_left_2_coordinate and piece.selected == True:
                                piece.attack_left_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_left_3_coordinate and piece.selected == True:
                                piece.attack_left_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_left_4_coordinate and piece.selected == True:
                                piece.attack_left_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_left_5_coordinate and piece.selected == True:
                                piece.attack_left_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_left_6_coordinate and piece.selected == True:
                                piece.attack_left_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_left_7_coordinate and piece.selected == True:
                                piece.attack_left_7()
                                gui_turn()
                                chessv6.turn()

                            if self.coordinate in piece.potential_move_up_right_coordinate and piece.selected == True:
                                piece.move_up_right()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_right_2_coordinate and piece.selected == True:
                                piece.move_up_right_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_right_3_coordinate and piece.selected == True:
                                piece.move_up_right_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_right_4_coordinate and piece.selected == True:
                                piece.move_up_right_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_right_5_coordinate and piece.selected == True:
                                piece.move_up_right_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_right_6_coordinate and piece.selected == True:
                                piece.move_up_right_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_right_7_coordinate and piece.selected == True:
                                piece.move_up_right_7()
                                gui_turn()
                                chessv6.turn()


                            if self.coordinate in piece.potential_move_up_left_coordinate and piece.selected == True:
                                piece.move_up_left()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_left_2_coordinate and piece.selected == True:
                                piece.move_up_left_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_left_3_coordinate and piece.selected == True:
                                piece.move_up_left_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_left_4_coordinate and piece.selected == True:
                                piece.move_up_left_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_left_5_coordinate and piece.selected == True:
                                piece.move_up_left_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_left_6_coordinate and piece.selected == True:
                                piece.move_up_left_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_left_7_coordinate and piece.selected == True:
                                piece.move_up_left_7()
                                gui_turn()
                                chessv6.turn()

                            if self.coordinate in piece.potential_move_down_right_coordinate and piece.selected == True:
                                piece.move_down_right()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_right_2_coordinate and piece.selected == True:
                                piece.move_down_right_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_right_3_coordinate and piece.selected == True:
                                piece.move_down_right_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_right_4_coordinate and piece.selected == True:
                                piece.move_down_right_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_right_5_coordinate and piece.selected == True:
                                piece.move_down_right_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_right_6_coordinate and piece.selected == True:
                                piece.move_down_right_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_right_7_coordinate and piece.selected == True:
                                piece.move_down_right_7()
                                gui_turn()
                                chessv6.turn()

                            if self.coordinate in piece.potential_move_down_left_coordinate and piece.selected == True:
                                piece.move_down_left()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_left_2_coordinate and piece.selected == True:
                                piece.move_down_left_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_left_3_coordinate and piece.selected == True:
                                piece.move_down_left_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_left_4_coordinate and piece.selected == True:
                                piece.move_down_left_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_left_5_coordinate and piece.selected == True:
                                piece.move_down_left_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_left_6_coordinate and piece.selected == True:
                                piece.move_down_left_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_left_7_coordinate and piece.selected == True:
                                piece.move_down_left_7()
                                gui_turn()
                                chessv6.turn()


                            if self.coordinate in piece.potential_attack_up_right_coordinate and piece.selected == True:
                                piece.attack_up_right()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_right_2_coordinate and piece.selected == True:
                                piece.attack_up_right_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_right_3_coordinate and piece.selected == True:
                                piece.attack_up_right_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_right_4_coordinate and piece.selected == True:
                                piece.attack_up_right_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_right_5_coordinate and piece.selected == True:
                                piece.attack_up_right_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_right_6_coordinate and piece.selected == True:
                                piece.attack_up_right_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_right_7_coordinate and piece.selected == True:
                                piece.attack_up_right_7()
                                gui_turn()
                                chessv6.turn()


                            if self.coordinate in piece.potential_attack_up_left_coordinate and piece.selected == True:
                                piece.attack_up_left()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_left_2_coordinate and piece.selected == True:
                                piece.attack_up_left_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_left_3_coordinate and piece.selected == True:
                                piece.attack_up_left_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_left_4_coordinate and piece.selected == True:
                                piece.attack_up_left_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_left_5_coordinate and piece.selected == True:
                                piece.attack_up_left_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_left_6_coordinate and piece.selected == True:
                                piece.attack_up_left_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_left_7_coordinate and piece.selected == True:
                                piece.attack_up_left_7()
                                gui_turn()
                                chessv6.turn()

                            if self.coordinate in piece.potential_attack_down_right_coordinate and piece.selected == True:
                                piece.attack_down_right()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_right_2_coordinate and piece.selected == True:
                                piece.attack_down_right_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_right_3_coordinate and piece.selected == True:
                                piece.attack_down_right_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_right_4_coordinate and piece.selected == True:
                                piece.attack_down_right_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_right_5_coordinate and piece.selected == True:
                                piece.attack_down_right_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_right_6_coordinate and piece.selected == True:
                                piece.attack_down_right_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_right_7_coordinate and piece.selected == True:
                                piece.attack_down_right_7()
                                gui_turn()
                                chessv6.turn()

                            if self.coordinate in piece.potential_attack_down_left_coordinate and piece.selected == True:
                                piece.attack_down_left()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_left_2_coordinate and piece.selected == True:
                                piece.attack_down_left_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_left_3_coordinate and piece.selected == True:
                                piece.attack_down_left_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_left_4_coordinate and piece.selected == True:
                                piece.attack_down_left_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_left_5_coordinate and piece.selected == True:
                                piece.attack_down_left_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_left_6_coordinate and piece.selected == True:
                                piece.attack_down_left_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_left_7_coordinate and piece.selected == True:
                                piece.attack_down_left_7()
                                gui_turn()
                                chessv6.turn()

                        if piece.piece_type == "b_queen" and chessv6.whos_turn == "black":

                            if self.coordinate in piece.potential_move_up_coordinate and piece.selected == True:
                                piece.move_up()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_2_coordinate and piece.selected == True:
                                piece.move_up_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_3_coordinate and piece.selected == True:
                                piece.move_up_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_4_coordinate and piece.selected == True:
                                piece.move_up_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_5_coordinate and piece.selected == True:
                                piece.move_up_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_6_coordinate and piece.selected == True:
                                piece.move_up_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_7_coordinate and piece.selected == True:
                                piece.move_up_7()
                                gui_turn()
                                chessv6.turn()

                            if self.coordinate in piece.potential_attack_up_coordinate and piece.selected == True:
                                piece.attack_up()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_2_coordinate and piece.selected == True:
                                piece.attack_up_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_3_coordinate and piece.selected == True:
                                piece.attack_up_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_4_coordinate and piece.selected == True:
                                piece.attack_up_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_5_coordinate and piece.selected == True:
                                piece.attack_up_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_6_coordinate and piece.selected == True:
                                piece.attack_up_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_7_coordinate and piece.selected == True:
                                piece.attack_up_7()
                                gui_turn()
                                chessv6.turn()

                            if self.coordinate in piece.potential_move_down_coordinate and piece.selected == True:
                                piece.move_down()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_2_coordinate and piece.selected == True:
                                piece.move_down_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_3_coordinate and piece.selected == True:
                                piece.move_down_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_4_coordinate and piece.selected == True:
                                piece.move_down_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_5_coordinate and piece.selected == True:
                                piece.move_down_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_6_coordinate and piece.selected == True:
                                piece.move_down_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_7_coordinate and piece.selected == True:
                                piece.move_down_7()
                                gui_turn()
                                chessv6.turn()

                            if self.coordinate in piece.potential_attack_down_coordinate and piece.selected == True:
                                piece.attack_down()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_2_coordinate and piece.selected == True:
                                piece.attack_down_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_3_coordinate and piece.selected == True:
                                piece.attack_down_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_4_coordinate and piece.selected == True:
                                piece.attack_down_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_5_coordinate and piece.selected == True:
                                piece.attack_down_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_6_coordinate and piece.selected == True:
                                piece.attack_down_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_7_coordinate and piece.selected == True:
                                piece.attack_down_7()
                                gui_turn()
                                chessv6.turn()


                            if self.coordinate in piece.potential_move_right_coordinate and piece.selected == True:
                                piece.move_right()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_right_2_coordinate and piece.selected == True:
                                piece.move_right_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_right_3_coordinate and piece.selected == True:
                                piece.move_right_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_right_4_coordinate and piece.selected == True:
                                piece.move_right_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_right_5_coordinate and piece.selected == True:
                                piece.move_right_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_right_6_coordinate and piece.selected == True:
                                piece.move_right_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_right_7_coordinate and piece.selected == True:
                                piece.move_right_7()
                                gui_turn()
                                chessv6.turn()

                            if self.coordinate in piece.potential_attack_right_coordinate and piece.selected == True:
                                piece.attack_right()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_right_2_coordinate and piece.selected == True:
                                piece.attack_right_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_right_3_coordinate and piece.selected == True:
                                piece.attack_right_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_right_4_coordinate and piece.selected == True:
                                piece.attack_right_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_right_5_coordinate and piece.selected == True:
                                piece.attack_right_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_right_6_coordinate and piece.selected == True:
                                piece.attack_right_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_right_7_coordinate and piece.selected == True:
                                piece.attack_right_7()
                                gui_turn()
                                chessv6.turn()


                            if self.coordinate in piece.potential_move_left_coordinate and piece.selected == True:
                                piece.move_left()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_left_2_coordinate and piece.selected == True:
                                piece.move_left_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_left_3_coordinate and piece.selected == True:
                                piece.move_left_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_left_4_coordinate and piece.selected == True:
                                piece.move_left_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_left_5_coordinate and piece.selected == True:
                                piece.move_left_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_left_6_coordinate and piece.selected == True:
                                piece.move_left_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_left_7_coordinate and piece.selected == True:
                                piece.move_left_7()
                                gui_turn()
                                chessv6.turn()

                            if self.coordinate in piece.potential_attack_left_coordinate and piece.selected == True:
                                piece.attack_left()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_left_2_coordinate and piece.selected == True:
                                piece.attack_left_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_left_3_coordinate and piece.selected == True:
                                piece.attack_left_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_left_4_coordinate and piece.selected == True:
                                piece.attack_left_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_left_5_coordinate and piece.selected == True:
                                piece.attack_left_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_left_6_coordinate and piece.selected == True:
                                piece.attack_left_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_left_7_coordinate and piece.selected == True:
                                piece.attack_left_7()
                                gui_turn()
                                chessv6.turn()

                            if self.coordinate in piece.potential_move_up_right_coordinate and piece.selected == True:
                                piece.move_up_right()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_right_2_coordinate and piece.selected == True:
                                piece.move_up_right_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_right_3_coordinate and piece.selected == True:
                                piece.move_up_right_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_right_4_coordinate and piece.selected == True:
                                piece.move_up_right_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_right_5_coordinate and piece.selected == True:
                                piece.move_up_right_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_right_6_coordinate and piece.selected == True:
                                piece.move_up_right_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_right_7_coordinate and piece.selected == True:
                                piece.move_up_right_7()
                                gui_turn()
                                chessv6.turn()


                            if self.coordinate in piece.potential_move_up_left_coordinate and piece.selected == True:
                                piece.move_up_left()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_left_2_coordinate and piece.selected == True:
                                piece.move_up_left_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_left_3_coordinate and piece.selected == True:
                                piece.move_up_left_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_left_4_coordinate and piece.selected == True:
                                piece.move_up_left_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_left_5_coordinate and piece.selected == True:
                                piece.move_up_left_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_left_6_coordinate and piece.selected == True:
                                piece.move_up_left_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_left_7_coordinate and piece.selected == True:
                                piece.move_up_left_7()
                                gui_turn()
                                chessv6.turn()

                            if self.coordinate in piece.potential_move_down_right_coordinate and piece.selected == True:
                                piece.move_down_right()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_right_2_coordinate and piece.selected == True:
                                piece.move_down_right_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_right_3_coordinate and piece.selected == True:
                                piece.move_down_right_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_right_4_coordinate and piece.selected == True:
                                piece.move_down_right_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_right_5_coordinate and piece.selected == True:
                                piece.move_down_right_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_right_6_coordinate and piece.selected == True:
                                piece.move_down_right_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_right_7_coordinate and piece.selected == True:
                                piece.move_down_right_7()
                                gui_turn()
                                chessv6.turn()

                            if self.coordinate in piece.potential_move_down_left_coordinate and piece.selected == True:
                                piece.move_down_left()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_left_2_coordinate and piece.selected == True:
                                piece.move_down_left_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_left_3_coordinate and piece.selected == True:
                                piece.move_down_left_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_left_4_coordinate and piece.selected == True:
                                piece.move_down_left_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_left_5_coordinate and piece.selected == True:
                                piece.move_down_left_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_left_6_coordinate and piece.selected == True:
                                piece.move_down_left_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_left_7_coordinate and piece.selected == True:
                                piece.move_down_left_7()
                                gui_turn()
                                chessv6.turn()


                            if self.coordinate in piece.potential_attack_up_right_coordinate and piece.selected == True:
                                piece.attack_up_right()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_right_2_coordinate and piece.selected == True:
                                piece.attack_up_right_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_right_3_coordinate and piece.selected == True:
                                piece.attack_up_right_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_right_4_coordinate and piece.selected == True:
                                piece.attack_up_right_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_right_5_coordinate and piece.selected == True:
                                piece.attack_up_right_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_right_6_coordinate and piece.selected == True:
                                piece.attack_up_right_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_right_7_coordinate and piece.selected == True:
                                piece.attack_up_right_7()
                                gui_turn()
                                chessv6.turn()


                            if self.coordinate in piece.potential_attack_up_left_coordinate and piece.selected == True:
                                piece.attack_up_left()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_left_2_coordinate and piece.selected == True:
                                piece.attack_up_left_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_left_3_coordinate and piece.selected == True:
                                piece.attack_up_left_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_left_4_coordinate and piece.selected == True:
                                piece.attack_up_left_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_left_5_coordinate and piece.selected == True:
                                piece.attack_up_left_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_left_6_coordinate and piece.selected == True:
                                piece.attack_up_left_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_left_7_coordinate and piece.selected == True:
                                piece.attack_up_left_7()
                                gui_turn()
                                chessv6.turn()

                            if self.coordinate in piece.potential_attack_down_right_coordinate and piece.selected == True:
                                piece.attack_down_right()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_right_2_coordinate and piece.selected == True:
                                piece.attack_down_right_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_right_3_coordinate and piece.selected == True:
                                piece.attack_down_right_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_right_4_coordinate and piece.selected == True:
                                piece.attack_down_right_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_right_5_coordinate and piece.selected == True:
                                piece.attack_down_right_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_right_6_coordinate and piece.selected == True:
                                piece.attack_down_right_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_right_7_coordinate and piece.selected == True:
                                piece.attack_down_right_7()
                                gui_turn()
                                chessv6.turn()

                            if self.coordinate in piece.potential_attack_down_left_coordinate and piece.selected == True:
                                piece.attack_down_left()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_left_2_coordinate and piece.selected == True:
                                piece.attack_down_left_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_left_3_coordinate and piece.selected == True:
                                piece.attack_down_left_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_left_4_coordinate and piece.selected == True:
                                piece.attack_down_left_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_left_5_coordinate and piece.selected == True:
                                piece.attack_down_left_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_left_6_coordinate and piece.selected == True:
                                piece.attack_down_left_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_left_7_coordinate and piece.selected == True:
                                piece.attack_down_left_7()
                                gui_turn()
                                chessv6.turn()

                        if piece.piece_type == "w_rook" and chessv6.whos_turn == "white":

                            if self.coordinate in piece.potential_move_up_coordinate and piece.selected == True:
                                piece.move_up()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_2_coordinate and piece.selected == True:
                                piece.move_up_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_3_coordinate and piece.selected == True:
                                piece.move_up_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_4_coordinate and piece.selected == True:
                                piece.move_up_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_5_coordinate and piece.selected == True:
                                piece.move_up_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_6_coordinate and piece.selected == True:
                                piece.move_up_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_7_coordinate and piece.selected == True:
                                piece.move_up_7()
                                gui_turn()
                                chessv6.turn()

                            if self.coordinate in piece.potential_attack_up_coordinate and piece.selected == True:
                                piece.attack_up()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_2_coordinate and piece.selected == True:
                                piece.attack_up_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_3_coordinate and piece.selected == True:
                                piece.attack_up_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_4_coordinate and piece.selected == True:
                                piece.attack_up_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_5_coordinate and piece.selected == True:
                                piece.attack_up_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_6_coordinate and piece.selected == True:
                                piece.attack_up_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_7_coordinate and piece.selected == True:
                                piece.attack_up_7()
                                gui_turn()
                                chessv6.turn()

                            if self.coordinate in piece.potential_move_down_coordinate and piece.selected == True:
                                piece.move_down()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_2_coordinate and piece.selected == True:
                                piece.move_down_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_3_coordinate and piece.selected == True:
                                piece.move_down_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_4_coordinate and piece.selected == True:
                                piece.move_down_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_5_coordinate and piece.selected == True:
                                piece.move_down_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_6_coordinate and piece.selected == True:
                                piece.move_down_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_7_coordinate and piece.selected == True:
                                piece.move_down_7()
                                gui_turn()
                                chessv6.turn()

                            if self.coordinate in piece.potential_attack_down_coordinate and piece.selected == True:
                                piece.attack_down()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_2_coordinate and piece.selected == True:
                                piece.attack_down_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_3_coordinate and piece.selected == True:
                                piece.attack_down_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_4_coordinate and piece.selected == True:
                                piece.attack_down_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_5_coordinate and piece.selected == True:
                                piece.attack_down_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_6_coordinate and piece.selected == True:
                                piece.attack_down_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_7_coordinate and piece.selected == True:
                                piece.attack_down_7()
                                gui_turn()
                                chessv6.turn()


                            if self.coordinate in piece.potential_move_right_coordinate and piece.selected == True:
                                piece.move_right()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_right_2_coordinate and piece.selected == True:
                                piece.move_right_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_right_3_coordinate and piece.selected == True:
                                piece.move_right_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_right_4_coordinate and piece.selected == True:
                                piece.move_right_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_right_5_coordinate and piece.selected == True:
                                piece.move_right_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_right_6_coordinate and piece.selected == True:
                                piece.move_right_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_right_7_coordinate and piece.selected == True:
                                piece.move_right_7()
                                gui_turn()
                                chessv6.turn()

                            if self.coordinate in piece.potential_attack_right_coordinate and piece.selected == True:
                                piece.attack_right()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_right_2_coordinate and piece.selected == True:
                                piece.attack_right_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_right_3_coordinate and piece.selected == True:
                                piece.attack_right_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_right_4_coordinate and piece.selected == True:
                                piece.attack_right_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_right_5_coordinate and piece.selected == True:
                                piece.attack_right_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_right_6_coordinate and piece.selected == True:
                                piece.attack_right_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_right_7_coordinate and piece.selected == True:
                                piece.attack_right_7()
                                gui_turn()
                                chessv6.turn()


                            if self.coordinate in piece.potential_move_left_coordinate and piece.selected == True:
                                piece.move_left()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_left_2_coordinate and piece.selected == True:
                                piece.move_left_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_left_3_coordinate and piece.selected == True:
                                piece.move_left_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_left_4_coordinate and piece.selected == True:
                                piece.move_left_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_left_5_coordinate and piece.selected == True:
                                piece.move_left_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_left_6_coordinate and piece.selected == True:
                                piece.move_left_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_left_7_coordinate and piece.selected == True:
                                piece.move_left_7()
                                gui_turn()
                                chessv6.turn()

                            if self.coordinate in piece.potential_attack_left_coordinate and piece.selected == True:
                                piece.attack_left()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_left_2_coordinate and piece.selected == True:
                                piece.attack_left_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_left_3_coordinate and piece.selected == True:
                                piece.attack_left_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_left_4_coordinate and piece.selected == True:
                                piece.attack_left_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_left_5_coordinate and piece.selected == True:
                                piece.attack_left_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_left_6_coordinate and piece.selected == True:
                                piece.attack_left_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_left_7_coordinate and piece.selected == True:
                                piece.attack_left_7()
                                gui_turn()
                                chessv6.turn()

                        if piece.piece_type == "b_rook" and chessv6.whos_turn == "black":

                            if self.coordinate in piece.potential_move_up_coordinate and piece.selected == True:
                                piece.move_up()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_2_coordinate and piece.selected == True:
                                piece.move_up_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_3_coordinate and piece.selected == True:
                                piece.move_up_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_4_coordinate and piece.selected == True:
                                piece.move_up_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_5_coordinate and piece.selected == True:
                                piece.move_up_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_6_coordinate and piece.selected == True:
                                piece.move_up_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_7_coordinate and piece.selected == True:
                                piece.move_up_7()
                                gui_turn()
                                chessv6.turn()

                            if self.coordinate in piece.potential_attack_up_coordinate and piece.selected == True:
                                piece.attack_up()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_2_coordinate and piece.selected == True:
                                piece.attack_up_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_3_coordinate and piece.selected == True:
                                piece.attack_up_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_4_coordinate and piece.selected == True:
                                piece.attack_up_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_5_coordinate and piece.selected == True:
                                piece.attack_up_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_6_coordinate and piece.selected == True:
                                piece.attack_up_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_7_coordinate and piece.selected == True:
                                piece.attack_up_7()
                                gui_turn()
                                chessv6.turn()

                            if self.coordinate in piece.potential_move_down_coordinate and piece.selected == True:
                                piece.move_down()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_2_coordinate and piece.selected == True:
                                piece.move_down_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_3_coordinate and piece.selected == True:
                                piece.move_down_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_4_coordinate and piece.selected == True:
                                piece.move_down_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_5_coordinate and piece.selected == True:
                                piece.move_down_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_6_coordinate and piece.selected == True:
                                piece.move_down_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_7_coordinate and piece.selected == True:
                                piece.move_down_7()
                                gui_turn()
                                chessv6.turn()

                            if self.coordinate in piece.potential_attack_down_coordinate and piece.selected == True:
                                piece.attack_down()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_2_coordinate and piece.selected == True:
                                piece.attack_down_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_3_coordinate and piece.selected == True:
                                piece.attack_down_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_4_coordinate and piece.selected == True:
                                piece.attack_down_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_5_coordinate and piece.selected == True:
                                piece.attack_down_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_6_coordinate and piece.selected == True:
                                piece.attack_down_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_7_coordinate and piece.selected == True:
                                piece.attack_down_7()
                                gui_turn()
                                chessv6.turn()


                            if self.coordinate in piece.potential_move_right_coordinate and piece.selected == True:
                                piece.move_right()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_right_2_coordinate and piece.selected == True:
                                piece.move_right_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_right_3_coordinate and piece.selected == True:
                                piece.move_right_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_right_4_coordinate and piece.selected == True:
                                piece.move_right_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_right_5_coordinate and piece.selected == True:
                                piece.move_right_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_right_6_coordinate and piece.selected == True:
                                piece.move_right_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_right_7_coordinate and piece.selected == True:
                                piece.move_right_7()
                                gui_turn()
                                chessv6.turn()

                            if self.coordinate in piece.potential_attack_right_coordinate and piece.selected == True:
                                piece.attack_right()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_right_2_coordinate and piece.selected == True:
                                piece.attack_right_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_right_3_coordinate and piece.selected == True:
                                piece.attack_right_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_right_4_coordinate and piece.selected == True:
                                piece.attack_right_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_right_5_coordinate and piece.selected == True:
                                piece.attack_right_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_right_6_coordinate and piece.selected == True:
                                piece.attack_right_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_right_7_coordinate and piece.selected == True:
                                piece.attack_right_7()
                                gui_turn()
                                chessv6.turn()


                            if self.coordinate in piece.potential_move_left_coordinate and piece.selected == True:
                                piece.move_left()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_left_2_coordinate and piece.selected == True:
                                piece.move_left_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_left_3_coordinate and piece.selected == True:
                                piece.move_left_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_left_4_coordinate and piece.selected == True:
                                piece.move_left_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_left_5_coordinate and piece.selected == True:
                                piece.move_left_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_left_6_coordinate and piece.selected == True:
                                piece.move_left_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_left_7_coordinate and piece.selected == True:
                                piece.move_left_7()
                                gui_turn()
                                chessv6.turn()

                            if self.coordinate in piece.potential_attack_left_coordinate and piece.selected == True:
                                piece.attack_left()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_left_2_coordinate and piece.selected == True:
                                piece.attack_left_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_left_3_coordinate and piece.selected == True:
                                piece.attack_left_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_left_4_coordinate and piece.selected == True:
                                piece.attack_left_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_left_5_coordinate and piece.selected == True:
                                piece.attack_left_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_left_6_coordinate and piece.selected == True:
                                piece.attack_left_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_left_7_coordinate and piece.selected == True:
                                piece.attack_left_7()
                                gui_turn()
                                chessv6.turn()

                        if piece.piece_type == "w_bishop" and chessv6.whos_turn == "white":

                            if self.coordinate in piece.potential_move_up_right_coordinate and piece.selected == True:
                                piece.move_up_right()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_right_2_coordinate and piece.selected == True:
                                piece.move_up_right_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_right_3_coordinate and piece.selected == True:
                                piece.move_up_right_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_right_4_coordinate and piece.selected == True:
                                piece.move_up_right_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_right_5_coordinate and piece.selected == True:
                                piece.move_up_right_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_right_6_coordinate and piece.selected == True:
                                piece.move_up_right_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_right_7_coordinate and piece.selected == True:
                                piece.move_up_right_7()
                                gui_turn()
                                chessv6.turn()


                            if self.coordinate in piece.potential_move_up_left_coordinate and piece.selected == True:
                                piece.move_up_left()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_left_2_coordinate and piece.selected == True:
                                piece.move_up_left_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_left_3_coordinate and piece.selected == True:
                                piece.move_up_left_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_left_4_coordinate and piece.selected == True:
                                piece.move_up_left_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_left_5_coordinate and piece.selected == True:
                                piece.move_up_left_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_left_6_coordinate and piece.selected == True:
                                piece.move_up_left_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_left_7_coordinate and piece.selected == True:
                                piece.move_up_left_7()
                                gui_turn()
                                chessv6.turn()

                            if self.coordinate in piece.potential_move_down_right_coordinate and piece.selected == True:
                                piece.move_down_right()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_right_2_coordinate and piece.selected == True:
                                piece.move_down_right_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_right_3_coordinate and piece.selected == True:
                                piece.move_down_right_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_right_4_coordinate and piece.selected == True:
                                piece.move_down_right_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_right_5_coordinate and piece.selected == True:
                                piece.move_down_right_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_right_6_coordinate and piece.selected == True:
                                piece.move_down_right_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_right_7_coordinate and piece.selected == True:
                                piece.move_down_right_7()
                                gui_turn()
                                chessv6.turn()

                            if self.coordinate in piece.potential_move_down_left_coordinate and piece.selected == True:
                                piece.move_down_left()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_left_2_coordinate and piece.selected == True:
                                piece.move_down_left_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_left_3_coordinate and piece.selected == True:
                                piece.move_down_left_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_left_4_coordinate and piece.selected == True:
                                piece.move_down_left_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_left_5_coordinate and piece.selected == True:
                                piece.move_down_left_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_left_6_coordinate and piece.selected == True:
                                piece.move_down_left_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_left_7_coordinate and piece.selected == True:
                                piece.move_down_left_7()
                                gui_turn()
                                chessv6.turn()


                            if self.coordinate in piece.potential_attack_up_right_coordinate and piece.selected == True:
                                piece.attack_up_right()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_right_2_coordinate and piece.selected == True:
                                piece.attack_up_right_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_right_3_coordinate and piece.selected == True:
                                piece.attack_up_right_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_right_4_coordinate and piece.selected == True:
                                piece.attack_up_right_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_right_5_coordinate and piece.selected == True:
                                piece.attack_up_right_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_right_6_coordinate and piece.selected == True:
                                piece.attack_up_right_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_right_7_coordinate and piece.selected == True:
                                piece.attack_up_right_7()
                                gui_turn()
                                chessv6.turn()


                            if self.coordinate in piece.potential_attack_up_left_coordinate and piece.selected == True:
                                piece.attack_up_left()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_left_2_coordinate and piece.selected == True:
                                piece.attack_up_left_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_left_3_coordinate and piece.selected == True:
                                piece.attack_up_left_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_left_4_coordinate and piece.selected == True:
                                piece.attack_up_left_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_left_5_coordinate and piece.selected == True:
                                piece.attack_up_left_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_left_6_coordinate and piece.selected == True:
                                piece.attack_up_left_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_left_7_coordinate and piece.selected == True:
                                piece.attack_up_left_7()
                                gui_turn()
                                chessv6.turn()

                            if self.coordinate in piece.potential_attack_down_right_coordinate and piece.selected == True:
                                piece.attack_down_right()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_right_2_coordinate and piece.selected == True:
                                piece.attack_down_right_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_right_3_coordinate and piece.selected == True:
                                piece.attack_down_right_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_right_4_coordinate and piece.selected == True:
                                piece.attack_down_right_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_right_5_coordinate and piece.selected == True:
                                piece.attack_down_right_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_right_6_coordinate and piece.selected == True:
                                piece.attack_down_right_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_right_7_coordinate and piece.selected == True:
                                piece.attack_down_right_7()
                                gui_turn()
                                chessv6.turn()

                            if self.coordinate in piece.potential_attack_down_left_coordinate and piece.selected == True:
                                piece.attack_down_left()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_left_2_coordinate and piece.selected == True:
                                piece.attack_down_left_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_left_3_coordinate and piece.selected == True:
                                piece.attack_down_left_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_left_4_coordinate and piece.selected == True:
                                piece.attack_down_left_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_left_5_coordinate and piece.selected == True:
                                piece.attack_down_left_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_left_6_coordinate and piece.selected == True:
                                piece.attack_down_left_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_left_7_coordinate and piece.selected == True:
                                piece.attack_down_left_7()
                                gui_turn()
                                chessv6.turn()

                        if piece.piece_type == "b_bishop" and chessv6.whos_turn == "black":

                            if self.coordinate in piece.potential_move_up_right_coordinate and piece.selected == True:
                                piece.move_up_right()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_right_2_coordinate and piece.selected == True:
                                piece.move_up_right_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_right_3_coordinate and piece.selected == True:
                                piece.move_up_right_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_right_4_coordinate and piece.selected == True:
                                piece.move_up_right_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_right_5_coordinate and piece.selected == True:
                                piece.move_up_right_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_right_6_coordinate and piece.selected == True:
                                piece.move_up_right_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_right_7_coordinate and piece.selected == True:
                                piece.move_up_right_7()
                                gui_turn()
                                chessv6.turn()


                            if self.coordinate in piece.potential_move_up_left_coordinate and piece.selected == True:
                                piece.move_up_left()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_left_2_coordinate and piece.selected == True:
                                piece.move_up_left_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_left_3_coordinate and piece.selected == True:
                                piece.move_up_left_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_left_4_coordinate and piece.selected == True:
                                piece.move_up_left_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_left_5_coordinate and piece.selected == True:
                                piece.move_up_left_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_left_6_coordinate and piece.selected == True:
                                piece.move_up_left_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_left_7_coordinate and piece.selected == True:
                                piece.move_up_left_7()
                                gui_turn()
                                chessv6.turn()

                            if self.coordinate in piece.potential_move_down_right_coordinate and piece.selected == True:
                                piece.move_down_right()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_right_2_coordinate and piece.selected == True:
                                piece.move_down_right_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_right_3_coordinate and piece.selected == True:
                                piece.move_down_right_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_right_4_coordinate and piece.selected == True:
                                piece.move_down_right_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_right_5_coordinate and piece.selected == True:
                                piece.move_down_right_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_right_6_coordinate and piece.selected == True:
                                piece.move_down_right_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_right_7_coordinate and piece.selected == True:
                                piece.move_down_right_7()
                                gui_turn()
                                chessv6.turn()

                            if self.coordinate in piece.potential_move_down_left_coordinate and piece.selected == True:
                                piece.move_down_left()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_left_2_coordinate and piece.selected == True:
                                piece.move_down_left_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_left_3_coordinate and piece.selected == True:
                                piece.move_down_left_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_left_4_coordinate and piece.selected == True:
                                piece.move_down_left_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_left_5_coordinate and piece.selected == True:
                                piece.move_down_left_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_left_6_coordinate and piece.selected == True:
                                piece.move_down_left_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_left_7_coordinate and piece.selected == True:
                                piece.move_down_left_7()
                                gui_turn()
                                chessv6.turn()


                            if self.coordinate in piece.potential_attack_up_right_coordinate and piece.selected == True:
                                piece.attack_up_right()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_right_2_coordinate and piece.selected == True:
                                piece.attack_up_right_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_right_3_coordinate and piece.selected == True:
                                piece.attack_up_right_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_right_4_coordinate and piece.selected == True:
                                piece.attack_up_right_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_right_5_coordinate and piece.selected == True:
                                piece.attack_up_right_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_right_6_coordinate and piece.selected == True:
                                piece.attack_up_right_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_right_7_coordinate and piece.selected == True:
                                piece.attack_up_right_7()
                                gui_turn()
                                chessv6.turn()


                            if self.coordinate in piece.potential_attack_up_left_coordinate and piece.selected == True:
                                piece.attack_up_left()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_left_2_coordinate and piece.selected == True:
                                piece.attack_up_left_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_left_3_coordinate and piece.selected == True:
                                piece.attack_up_left_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_left_4_coordinate and piece.selected == True:
                                piece.attack_up_left_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_left_5_coordinate and piece.selected == True:
                                piece.attack_up_left_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_left_6_coordinate and piece.selected == True:
                                piece.attack_up_left_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_left_7_coordinate and piece.selected == True:
                                piece.attack_up_left_7()
                                gui_turn()
                                chessv6.turn()

                            if self.coordinate in piece.potential_attack_down_right_coordinate and piece.selected == True:
                                piece.attack_down_right()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_right_2_coordinate and piece.selected == True:
                                piece.attack_down_right_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_right_3_coordinate and piece.selected == True:
                                piece.attack_down_right_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_right_4_coordinate and piece.selected == True:
                                piece.attack_down_right_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_right_5_coordinate and piece.selected == True:
                                piece.attack_down_right_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_right_6_coordinate and piece.selected == True:
                                piece.attack_down_right_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_right_7_coordinate and piece.selected == True:
                                piece.attack_down_right_7()
                                gui_turn()
                                chessv6.turn()

                            if self.coordinate in piece.potential_attack_down_left_coordinate and piece.selected == True:
                                piece.attack_down_left()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_left_2_coordinate and piece.selected == True:
                                piece.attack_down_left_2()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_left_3_coordinate and piece.selected == True:
                                piece.attack_down_left_3()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_left_4_coordinate and piece.selected == True:
                                piece.attack_down_left_4()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_left_5_coordinate and piece.selected == True:
                                piece.attack_down_left_5()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_left_6_coordinate and piece.selected == True:
                                piece.attack_down_left_6()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_left_7_coordinate and piece.selected == True:
                                piece.attack_down_left_7()
                                gui_turn()
                                chessv6.turn()

                        if piece.piece_type == "w_king" and chessv6.whos_turn == "white":
                            if self.coordinate in piece.potential_move_up_coordinate and piece.selected == True:
                                piece.move_up()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_coordinate and piece.selected == True:
                                piece.attack_up()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_coordinate and piece.selected == True:
                                piece.move_down()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_coordinate and piece.selected == True:
                                piece.attack_down()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_right_coordinate and piece.selected == True:
                                piece.move_right()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_right_coordinate and piece.selected == True:
                                piece.attack_right()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_left_coordinate and piece.selected == True:
                                piece.move_left()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_left_coordinate and piece.selected == True:
                                piece.attack_left()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_right_coordinate and piece.selected == True:
                                piece.move_up_right()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_left_coordinate and piece.selected == True:
                                piece.move_up_left()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_right_coordinate and piece.selected == True:
                                piece.move_down_right()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_left_coordinate and piece.selected == True:
                                piece.move_down_left()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_right_coordinate and piece.selected == True:
                                piece.attack_up_right()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_left_coordinate and piece.selected == True:
                                piece.attack_up_left()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_right_coordinate and piece.selected == True:
                                piece.attack_down_right()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_left_coordinate and piece.selected == True:
                                piece.attack_down_left()
                                gui_turn()
                                chessv6.turn()

                        if piece.piece_type == "b_king" and chessv6.whos_turn == "black":
                            if self.coordinate in piece.potential_move_up_coordinate and piece.selected == True:
                                piece.move_up()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_coordinate and piece.selected == True:
                                piece.attack_up()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_coordinate and piece.selected == True:
                                piece.move_down()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_coordinate and piece.selected == True:
                                piece.attack_down()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_right_coordinate and piece.selected == True:
                                piece.move_right()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_right_coordinate and piece.selected == True:
                                piece.attack_right()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_left_coordinate and piece.selected == True:
                                piece.move_left()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_left_coordinate and piece.selected == True:
                                piece.attack_left()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_right_coordinate and piece.selected == True:
                                piece.move_up_right()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_up_left_coordinate and piece.selected == True:
                                piece.move_up_left()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_right_coordinate and piece.selected == True:
                                piece.move_down_right()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_down_left_coordinate and piece.selected == True:
                                piece.move_down_left()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_right_coordinate and piece.selected == True:
                                piece.attack_up_right()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_up_left_coordinate and piece.selected == True:
                                piece.attack_up_left()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_right_coordinate and piece.selected == True:
                                piece.attack_down_right()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_down_left_coordinate and piece.selected == True:
                                piece.attack_down_left()
                                gui_turn()
                                chessv6.turn()

                        if piece.piece_type == "w_knight" and chessv6.whos_turn == "white":

                            if self.coordinate in piece.potential_move_1clock_coordinate and piece.selected == True:
                                piece.move_1clock()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_2clock_coordinate and piece.selected == True:
                                piece.move_2clock()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_4clock_coordinate and piece.selected == True:
                                piece.move_4clock()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_5clock_coordinate and piece.selected == True:
                                piece.move_5clock()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_7clock_coordinate and piece.selected == True:
                                piece.move_7clock()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_8clock_coordinate and piece.selected == True:
                                piece.move_8clock()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_10clock_coordinate and piece.selected == True:
                                piece.move_10clock()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_11clock_coordinate and piece.selected == True:
                                piece.move_11clock()
                                gui_turn()
                                chessv6.turn()

                            if self.coordinate in piece.potential_attack_1clock_coordinate and piece.selected == True:
                                piece.attack_1clock()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_2clock_coordinate and piece.selected == True:
                                piece.attack_2clock()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_4clock_coordinate and piece.selected == True:
                                piece.attack_4clock()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_5clock_coordinate and piece.selected == True:
                                piece.attack_5clock()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_7clock_coordinate and piece.selected == True:
                                piece.attack_7clock()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_8clock_coordinate and piece.selected == True:
                                piece.attack_8clock()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_10clock_coordinate and piece.selected == True:
                                piece.attack_10clock()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_11clock_coordinate and piece.selected == True:
                                piece.attack_11clock()
                                gui_turn()
                                chessv6.turn()

                        if piece.piece_type == "b_knight" and chessv6.whos_turn == "black":

                            if self.coordinate in piece.potential_move_1clock_coordinate and piece.selected == True:
                                piece.move_1clock()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_2clock_coordinate and piece.selected == True:
                                piece.move_2clock()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_4clock_coordinate and piece.selected == True:
                                piece.move_4clock()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_5clock_coordinate and piece.selected == True:
                                piece.move_5clock()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_7clock_coordinate and piece.selected == True:
                                piece.move_7clock()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_8clock_coordinate and piece.selected == True:
                                piece.move_8clock()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_10clock_coordinate and piece.selected == True:
                                piece.move_10clock()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_move_11clock_coordinate and piece.selected == True:
                                piece.move_11clock()
                                gui_turn()
                                chessv6.turn()

                            if self.coordinate in piece.potential_attack_1clock_coordinate and piece.selected == True:
                                piece.attack_1clock()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_2clock_coordinate and piece.selected == True:
                                piece.attack_2clock()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_4clock_coordinate and piece.selected == True:
                                piece.attack_4clock()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_5clock_coordinate and piece.selected == True:
                                piece.attack_5clock()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_7clock_coordinate and piece.selected == True:
                                piece.attack_7clock()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_8clock_coordinate and piece.selected == True:
                                piece.attack_8clock()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_10clock_coordinate and piece.selected == True:
                                piece.attack_10clock()
                                gui_turn()
                                chessv6.turn()
                            if self.coordinate in piece.potential_attack_11clock_coordinate and piece.selected == True:
                                piece.attack_11clock()
                                gui_turn()
                                chessv6.turn()

        if pygame.mouse.get_pressed()[0] == 1:
            self.clicked=False

        if self.x+100 > pygame.mouse.get_pos()[0] > self.x and self.y+100 > pygame.mouse.get_pos()[1] > self.y :
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked=True

    def interact(self):
            for piece in chessv6.piece_tuple:
                if piece.chess_replace()==self.coordinate:
                    for square in square_gui_tuple:
                        if square.coordinate in piece.potential_move_list:
                            square.display_potential_moves()
                        if square.coordinate in piece.potential_attack_list:
                            square.display_potential_attacks()





a1 = square_gui(0,700,paint_blue,chessv6.square_a1)
a2 = square_gui(0,600,paint_white,chessv6.square_a2)
a3 = square_gui(0,500,paint_blue,chessv6.square_a3)
a4 = square_gui(0,400,paint_white,chessv6.square_a4)
a5 = square_gui(0,300,paint_blue,chessv6.square_a5)
a6 = square_gui(0,200,paint_white,chessv6.square_a6)
a7 = square_gui(0,100,paint_blue,chessv6.square_a7)
a8 = square_gui(0,0,paint_white,chessv6.square_a8)
b1 = square_gui(100,700,paint_white,chessv6.square_b1)
b2 = square_gui(100,600,paint_blue,chessv6.square_b2)
b3 = square_gui(100,500,paint_white,chessv6.square_b3)
b4 = square_gui(100,400,paint_blue,chessv6.square_b4)
b5 = square_gui(100,300,paint_white,chessv6.square_b5)
b6 = square_gui(100,200,paint_blue,chessv6.square_b6)
b7 = square_gui(100,100,paint_white,chessv6.square_b7)
b8 = square_gui(100,0,paint_blue,chessv6.square_b8)
c1 = square_gui(200,700,paint_blue,chessv6.square_c1)
c2 = square_gui(200,600,paint_white,chessv6.square_c2)
c3 = square_gui(200,500,paint_blue,chessv6.square_c3)
c4 = square_gui(200,400,paint_white,chessv6.square_c4)
c5 = square_gui(200,300,paint_blue,chessv6.square_c5)
c6 = square_gui(200,200,paint_white,chessv6.square_c6)
c7 = square_gui(200,100,paint_blue,chessv6.square_c7)
c8 = square_gui(200,0,paint_white,chessv6.square_c8)
d1 = square_gui(300,700,paint_white,chessv6.square_d1)
d2 = square_gui(300,600,paint_blue,chessv6.square_d2)
d3 = square_gui(300,500,paint_white,chessv6.square_d3)
d4 = square_gui(300,400,paint_blue,chessv6.square_d4)
d5 = square_gui(300,300,paint_white,chessv6.square_d5)
d6 = square_gui(300,200,paint_blue,chessv6.square_d6)
d7 = square_gui(300,100,paint_white,chessv6.square_d7)
d8 = square_gui(300,0,paint_blue,chessv6.square_d8)
e1 = square_gui(400,700,paint_blue,chessv6.square_e1)
e2 = square_gui(400,600,paint_white,chessv6.square_e2)
e3 = square_gui(400,500,paint_blue,chessv6.square_e3)
e4 = square_gui(400,400,paint_white,chessv6.square_e4)
e5 = square_gui(400,300,paint_blue,chessv6.square_e5)
e6 = square_gui(400,200,paint_white,chessv6.square_e6)
e7 = square_gui(400,100,paint_blue,chessv6.square_e7)
e8 = square_gui(400,0,paint_white,chessv6.square_e8)
f1 = square_gui(500,700,paint_white,chessv6.square_f1)
f2 = square_gui(500,600,paint_blue,chessv6.square_f2)
f3 = square_gui(500,500,paint_white,chessv6.square_f3)
f4 = square_gui(500,400,paint_blue,chessv6.square_f4)
f5 = square_gui(500,300,paint_white,chessv6.square_f5)
f6 = square_gui(500,200,paint_blue,chessv6.square_f6)
f7 = square_gui(500,100,paint_white,chessv6.square_f7)
f8 = square_gui(500,0,paint_blue,chessv6.square_f8)
g1 = square_gui(600,700,paint_blue,chessv6.square_g1)
g2 = square_gui(600,600,paint_white,chessv6.square_g2)
g3 = square_gui(600,500,paint_blue,chessv6.square_g3)
g4 = square_gui(600,400,paint_white,chessv6.square_g4)
g5 = square_gui(600,300,paint_blue,chessv6.square_g5)
g6 = square_gui(600,200,paint_white,chessv6.square_g6)
g7 = square_gui(600,100,paint_blue,chessv6.square_g7)
g8 = square_gui(600,0,paint_white,chessv6.square_g8)
h1 = square_gui(700,700,paint_white,chessv6.square_h1)
h2 = square_gui(700,600,paint_blue,chessv6.square_h2)
h3 = square_gui(700,500,paint_white,chessv6.square_h3)
h4 = square_gui(700,400,paint_blue,chessv6.square_h4)
h5 = square_gui(700,300,paint_white,chessv6.square_h5)
h6 = square_gui(700,200,paint_blue,chessv6.square_h6)
h7 = square_gui(700,100,paint_white,chessv6.square_h7)
h8 = square_gui(700,0,paint_blue,chessv6.square_h8)



square_gui_tuple =(a1,a2,a3,a4,a5,a6,a7,a8,b1,b2,b3,b4,b5,b6,b7,b8,c1,c2,c3,c4,c5,c6,c7,c8,d1,d2,d3,d4,d5,d6,d7,d8,e1,e2,e3,e4,e5,e6,e7,e8,f1,f2,f3,f4,f5,f6,f7,f8,g1,g2,g3,g4,g5,g6,g7,g8,h1,h2,h3,h4,h5,h6,h7,h8)

# x=display_width*0
y=display_height*0.75
# y=600
# y_change = 0

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            for piece in chessv6.piece_tuple:
                if piece.selected==True:
                    counter+=1
                    if counter%2==1:
                        piece.selected=False







    gameDisplay.fill(paint_blue)

    a1.draw_square()
    a2.draw_square()
    a3.draw_square()
    a4.draw_square()
    a5.draw_square()
    a6.draw_square()
    a7.draw_square()
    a8.draw_square()
    b1.draw_square()
    b2.draw_square()
    b3.draw_square()
    b4.draw_square()
    b5.draw_square()
    b6.draw_square()
    b7.draw_square()
    b8.draw_square()
    c1.draw_square()
    c2.draw_square()
    c3.draw_square()
    c4.draw_square()
    c5.draw_square()
    c6.draw_square()
    c7.draw_square()
    c8.draw_square()
    d1.draw_square()
    d2.draw_square()
    d3.draw_square()
    d4.draw_square()
    d5.draw_square()
    d6.draw_square()
    d7.draw_square()
    d8.draw_square()
    e1.draw_square()
    e2.draw_square()
    e3.draw_square()
    e4.draw_square()
    e5.draw_square()
    e6.draw_square()
    e7.draw_square()
    e8.draw_square()
    f1.draw_square()
    f2.draw_square()
    f3.draw_square()
    f4.draw_square()
    f5.draw_square()
    f6.draw_square()
    f7.draw_square()
    f8.draw_square()
    g1.draw_square()
    g2.draw_square()
    g3.draw_square()
    g4.draw_square()
    g5.draw_square()
    g6.draw_square()
    g7.draw_square()
    g8.draw_square()
    h1.draw_square()
    h2.draw_square()
    h3.draw_square()
    h4.draw_square()
    h5.draw_square()
    h6.draw_square()
    h7.draw_square()
    h8.draw_square()

    pawn_a_w_gui.display_piece()
    pawn_b_w_gui.display_piece()
    pawn_c_w_gui.display_piece()
    pawn_d_w_gui.display_piece()
    pawn_e_w_gui.display_piece()
    pawn_f_w_gui.display_piece()
    pawn_g_w_gui.display_piece()
    pawn_h_w_gui.display_piece()
    pawn_a_b_gui.display_piece()
    pawn_b_b_gui.display_piece()
    pawn_c_b_gui.display_piece()
    pawn_d_b_gui.display_piece()
    pawn_e_b_gui.display_piece()
    pawn_f_b_gui.display_piece()
    pawn_g_b_gui.display_piece()
    pawn_h_b_gui.display_piece()
    queen_1_w_gui.display_piece()
    queen_1_b_gui.display_piece()
    rook_1_w_gui.display_piece()
    rook_1_b_gui.display_piece()
    rook_2_w_gui.display_piece()
    rook_2_b_gui.display_piece()
    bishop_1_w_gui.display_piece()
    bishop_1_b_gui.display_piece()
    bishop_2_w_gui.display_piece()
    bishop_2_b_gui.display_piece()
    king_1_w_gui.display_piece()
    king_1_b_gui.display_piece()
    knight_1_w_gui.display_piece()
    knight_1_b_gui.display_piece()
    knight_2_w_gui.display_piece()
    knight_2_b_gui.display_piece()

    for square_gui in square_gui_tuple:
        square_gui.button()
        if square_gui.clicked==True:
            for piece in chessv6.piece_tuple:
                if piece.chess_replace() == square_gui.coordinate and piece.captured == False :
                    for piece2 in chessv6.piece_tuple:
                        if piece2.selected == True and piece!=piece2:
                            piece.selected = False
                            piece2.selected = False
                            break
                        piece.selected = True
        if square_gui.clicked==True and counter%2==1:
            square_gui.interact()

    # for square_gui in square_gui_tuple:
    #     square_gui.button()
    #     if square_gui.clicked==True and check1 == check2:
    #         square_gui.interact()



    pygame.display.update()
    clock.tick(20)

pygame.quit()
quit()
