a=0
b=1
c=2
d=3
e=4
f=5
g=6
h=7

board=[[[a,1],[a,2],[a,3],[a,4],[a,5],[a,6],[a,7],[a,8]],
[[b,1],[b,2],[b,3],[b,4],[b,5],[b,6],[b,7],[b,8]],
[[c,1],[c,2],[c,3],[c,4],[c,5],[c,6],[c,7],[c,8]],
[[d,1],[d,2],[d,3],[d,4],[d,5],[d,6],[d,7],[d,8]],
[[e,1],[e,2],[e,3],[e,4],[e,5],[e,6],[e,7],[e,8]],
[[f,1],[f,2],[f,3],[f,4],[f,5],[f,6],[f,7],[f,8]],
[[g,1],[g,2],[g,3],[g,4],[g,5],[g,6],[g,7],[g,8]],
[[h,1],[h,2],[h,3],[h,4],[h,5],[h,6],[h,7],[h,8]]]

class square:

    def __init__(self,occupied,attacked,coordinate):
        self.occupied = occupied
        self.attacked = attacked
        self.coordinate = coordinate
        self.occupied_by = None
        self.occupied_colour = None

    def is_it_occupied(self):
        for i in piece_tuple:
            if i.chess_replace() == self.coordinate and i.captured==False:
                self.occupied = True
                self.occupied_by = i.piece_type
                self.occupied_colour = i.colour
                break
        else:
            self.occupied = False
            self.occupied_by = None

    def is_it_attacked(self):
        for i in piece_tuple:
            if self.coordinate in i.potential_attack_list:
                self.attacked=True
                break

class pawn_w:

    def __init__(self,position,has_moved,captured,colour):
        self.position = position
        self.has_moved = has_moved
        self.position_chess=self.position.copy()
        self.captured=captured
        self.piece_type="w_pawn"
        self.colour=colour
        self.potential_attack_list = []
        self.potential_move_list = []
        self.potential_move_coordinate = []
        self.potential_move_of_two_squares_coordinate = []
        self.potential_capture_down_coordinate = []
        self.potential_capture_down_coordinate = []
        self.selected=False

    def move_of_two_squares(self):
        for i in square_tuple:
            if i.coordinate == pawn_w.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if i.coordinate == pawn_w.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+2]) and i.occupied==False and self.captured==False and self.has_moved == False:
                        self.position=board[self.position[0]][board[self.position[0]].index(self.position)+2]
                        self.has_moved=True
                        break

    def move(self):
        for i in square_tuple:
            if i.coordinate == pawn_w.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False and self.captured==False:
                self.position=board[self.position[0]][board[self.position[0]].index(self.position)+1]
                self.has_moved=True
                break

    def capture_down(self):
        for i in square_tuple:
            if i.coordinate == pawn_w.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                for x in piece_tuple:
                    if x.chess_replace()==i.coordinate:
                        x.captured=True
                self.position=board[self.position[0]-1][board[self.position[0]].index(self.position)+1]
                self.has_moved=True
                break

    def capture_up(self):
        for i in square_tuple:
            if i.coordinate == pawn_w.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                for x in piece_tuple:
                    if x.chess_replace()==i.coordinate:
                        x.captured=True
                self.position=board[self.position[0]+1][board[self.position[0]].index(self.position)+1]
                self.has_moved=True
                break

    def potential_move_of_two_squares(self):
            for i in square_tuple:
                if self.has_moved == True:
                    break
                if i.coordinate == pawn_w.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                    for i in square_tuple:
                        if i.coordinate == pawn_w.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+2]) and i.occupied==False and self.captured==False and self.has_moved == False:
                            potential=board[self.position[0]][board[self.position[0]].index(self.position)+2]
                            self.potential_move_list.append(pawn_w.static_chess_replace(potential))
                            self.potential_move_of_two_squares_coordinate.append(pawn_w.static_chess_replace(potential))

    def potential_move(self):
        for i in square_tuple:
            if self.position[1] == 8:
                break
            if i.coordinate == pawn_w.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False and self.captured==False:
                potential=board[self.position[0]][board[self.position[0]].index(self.position)+1]
                self.potential_move_list.append(pawn_w.static_chess_replace(potential))
                self.potential_move_coordinate.append(pawn_w.static_chess_replace(potential))

    def potential_capture_down(self):
        for i in square_tuple:
            if self.position in board[0] or self.position[1] == 8:
                break
            if i.coordinate == pawn_w.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                potential=board[self.position[0]-1][board[self.position[0]].index(self.position)+1]
                self.potential_attack_list.append(pawn_w.static_chess_replace(potential))
                self.potential_capture_down_coordinate.append(pawn_w.static_chess_replace(potential))

    def potential_capture_up(self):
        for i in square_tuple:
            if self.position in board[7] or self.position[1] == 8:
                break
            if i.coordinate == pawn_w.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                potential=board[self.position[0]+1][board[self.position[0]].index(self.position)+1]
                self.potential_attack_list.append(pawn_w.static_chess_replace(potential))
                self.potential_capture_up_coordinate.append(pawn_w.static_chess_replace(potential))

    @staticmethod
    def list_replace(list,remove,add):
        list_copy=list.copy()
        for i in list_copy:
            if i== remove:
                list_copy.remove(i)
                list_copy.insert(0,add)
                return list_copy

    @staticmethod
    def static_chess_replace(coord):
            if coord[0] == 0:
                return pawn_w.list_replace(coord,0,"a")
            if coord[0] == 1:
                return pawn_w.list_replace(coord,1,"b")
            if coord[0] == 2:
                return pawn_w.list_replace(coord,2,"c")
            if coord[0] == 3:
                return pawn_w.list_replace(coord,3,"d")
            if coord[0] == 4:
                return pawn_w.list_replace(coord,4,"e")
            if coord[0] == 5:
                return pawn_w.list_replace(coord,5,"f")
            if coord[0] == 6:
                return pawn_w.list_replace(coord,6,"g")
            if coord[0] == 7:
                return pawn_w.list_replace(coord,7,"h")

    def chess_replace(self):
        self.position_chess=self.position.copy()
        if self.position_chess[0] == 0:
            return self.list_replace(self.position_chess,0,"a")
        if self.position_chess[0] == 1:
            return self.list_replace(self.position_chess,1,"b")
        if self.position_chess[0] == 2:
            return self.list_replace(self.position_chess,2,"c")
        if self.position_chess[0] == 3:
            return self.list_replace(self.position_chess,3,"d")
        if self.position_chess[0] == 4:
            return self.list_replace(self.position_chess,4,"e")
        if self.position_chess[0] == 5:
            return self.list_replace(self.position_chess,5,"f")
        if self.position_chess[0] == 6:
            return self.list_replace(self.position_chess,6,"g")
        if self.position_chess[0] == 7:
            return self.list_replace(self.position_chess,7,"h")

    def chess_replace_p(self):
        for i in self.potential_move_list:
            if i[0] == 0:
                self.list_replace(i,0,"a")
            if i[0] == 1:
                self.list_replace(i,1,"b")
            if i[0] == 2:
                self.list_replace(i,2,"c")
            if i[0] == 3:
                self.list_replace(i,3,"d")
            if i[0] == 4:
                self.list_replace(i,4,"e")
            if i[0] == 5:
                self.list_replace(i,5,"f")
            if i[0] == 6:
                self.list_replace(i,6,"g")
            if i[0] == 7:
                self.list_replace(i,7,"h")

    def chess_replace_a(self):
        for i in self.potential_attack_list:
            if i[0] == 0:
                self.list_replace(i,0,"a")
            if i[0] == 1:
                self.list_replace(i,1,"b")
            if i[0] == 2:
                self.list_replace(i,2,"c")
            if i[0] == 3:
                self.list_replace(i,3,"d")
            if i[0] == 4:
                self.list_replace(i,4,"e")
            if i[0] == 5:
                self.list_replace(i,5,"f")
            if i[0] == 6:
                self.list_replace(i,6,"g")
            if i[0] == 7:
                self.list_replace(i,7,"h")

class pawn_b:

    def __init__(self,position,has_moved,captured,colour):
        self.position = position
        self.has_moved = has_moved
        self.position_chess=self.position.copy()
        self.captured = captured
        self.piece_type="b_pawn"
        self.colour=colour
        self.potential_attack_list = []
        self.potential_move_list  = []
        self.potential_move_coordinate = []
        self.potential_move_of_two_squares_coordinate = []
        self.potential_capture_up_coordinate = []
        self.potential_capture_down_coordinate = []
        self.selected=False

    def move_of_two_squares(self):
        for i in square_tuple:
            if i.coordinate == pawn_b.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if i.coordinate == pawn_b.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-2]) and i.occupied==False and self.captured==False and self.has_moved == False:
                        self.position=board[self.position[0]][board[self.position[0]].index(self.position)-2]
                        self.has_moved = True
                        break

    def move(self):
        for i in square_tuple:
            if i.coordinate == pawn_b.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False and self.captured==False:
                self.position=board[self.position[0]][board[self.position[0]].index(self.position)-1]
                self.has_moved=True
                break

    def capture_down(self):
        for i in square_tuple:
            if i.coordinate == pawn_b.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                for x in piece_tuple:
                    if x.chess_replace()==i.coordinate:
                        x.captured=True
                self.position=board[self.position[0]-1][board[self.position[0]].index(self.position)-1]
                self.has_moved=True
                break

    def capture_up(self):
        for i in square_tuple:
            if i.coordinate == pawn_b.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                for x in piece_tuple:
                    if x.chess_replace()==i.coordinate:
                        x.captured=True
                self.position=board[self.position[0]+1][board[self.position[0]].index(self.position)-1]
                self.has_moved=True
                break

    def potential_move_of_two_squares(self):
        for i in square_tuple:
            if self.has_moved == True:
                break
            if i.coordinate == pawn_b.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if i.coordinate == pawn_b.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-2]) and i.occupied==False and self.captured==False and self.has_moved == False:
                        potential=board[self.position[0]][board[self.position[0]].index(self.position)-2]
                        self.potential_move_list.append(pawn_b.static_chess_replace(potential))
                        self.potential_move_of_two_squares_coordinate.append(pawn_b.static_chess_replace(potential))

    def potential_move(self):
        for i in square_tuple:
            if self.position[1] == 1:
                break
            if i.coordinate == pawn_b.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False and self.captured==False:
                potential=board[self.position[0]][board[self.position[0]].index(self.position)-1]
                self.potential_move_list.append(pawn_b.static_chess_replace(potential))
                self.potential_move_coordinate.append(pawn_b.static_chess_replace(potential))

    def potential_capture_down(self):
        for i in square_tuple:
            if self.position in board[0]:
                break
            if i.coordinate == pawn_b.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                potential=board[self.position[0]-1][board[self.position[0]].index(self.position)-1]
                self.potential_attack_list.append(pawn_b.static_chess_replace(potential))
                self.potential_capture_down_coordinate.append(pawn_b.static_chess_replace(potential))

    def potential_capture_up(self):
        for i in square_tuple:
            if self.position in board[7]:
                break
            if i.coordinate == pawn_b.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                potential=board[self.position[0]+1][board[self.position[0]].index(self.position)-1]
                self.potential_attack_list.append(pawn_b.static_chess_replace(potential))
                self.potential_capture_up_coordinate.append(pawn_b.static_chess_replace(potential))

    @staticmethod
    def list_replace(list,remove,add):
        list_copy=list.copy()
        for i in list_copy:
            if i== remove:
                list_copy.remove(i)
                list_copy.insert(0,add)
                return list_copy

    @staticmethod
    def static_chess_replace(coord):
            if coord[0] == 0:
                return pawn_b.list_replace(coord,0,"a")
            if coord[0] == 1:
                return pawn_b.list_replace(coord,1,"b")
            if coord[0] == 2:
                return pawn_b.list_replace(coord,2,"c")
            if coord[0] == 3:
                return pawn_b.list_replace(coord,3,"d")
            if coord[0] == 4:
                return pawn_b.list_replace(coord,4,"e")
            if coord[0] == 5:
                return pawn_b.list_replace(coord,5,"f")
            if coord[0] == 6:
                return pawn_b.list_replace(coord,6,"g")
            if coord[0] == 7:
                return pawn_b.list_replace(coord,7,"h")

    def chess_replace(self):
        self.position_chess=self.position.copy()
        if self.position_chess[0] == 0:
            return self.list_replace(self.position_chess,0,"a")
        if self.position_chess[0] == 1:
            return self.list_replace(self.position_chess,1,"b")
        if self.position_chess[0] == 2:
            return self.list_replace(self.position_chess,2,"c")
        if self.position_chess[0] == 3:
            return self.list_replace(self.position_chess,3,"d")
        if self.position_chess[0] == 4:
            return self.list_replace(self.position_chess,4,"e")
        if self.position_chess[0] == 5:
            return self.list_replace(self.position_chess,5,"f")
        if self.position_chess[0] == 6:
            return self.list_replace(self.position_chess,6,"g")
        if self.position_chess[0] == 7:
            return self.list_replace(self.position_chess,7,"h")

    def chess_replace_p(self):
        for i in self.potential_move_list:
            if i[0] == 0:
                self.list_replace(i,0,"a")
            if i[0] == 1:
                self.list_replace(i,1,"b")
            if i[0] == 2:
                self.list_replace(i,2,"c")
            if i[0] == 3:
                self.list_replace(i,3,"d")
            if i[0] == 4:
                self.list_replace(i,4,"e")
            if i[0] == 5:
                self.list_replace(i,5,"f")
            if i[0] == 6:
                self.list_replace(i,6,"g")
            if i[0] == 7:
                self.list_replace(i,7,"h")

    def chess_replace_a(self):
        for i in self.potential_attack_list:
            if i[0] == 0:
                self.list_replace(i,0,"a")
            if i[0] == 1:
                self.list_replace(i,1,"b")
            if i[0] == 2:
                self.list_replace(i,2,"c")
            if i[0] == 3:
                self.list_replace(i,3,"d")
            if i[0] == 4:
                self.list_replace(i,4,"e")
            if i[0] == 5:
                self.list_replace(i,5,"f")
            if i[0] == 6:
                self.list_replace(i,6,"g")
            if i[0] == 7:
                self.list_replace(i,7,"h")

class queen:

    def __init__(self,position,has_moved,captured,piece_type,colour):
        self.position = position
        self.has_moved = has_moved
        self.position_chess=self.position.copy()
        self.captured=captured
        self.piece_type=piece_type
        self.selected=False
        self.colour=colour
        self.potential_attack_list = []
        self.potential_move_list = []
        self.potential_move_up_7_coordinate = []
        self.potential_move_up_6_coordinate = []
        self.potential_move_up_5_coordinate = []
        self.potential_move_up_4_coordinate = []
        self.potential_move_up_3_coordinate = []
        self.potential_move_up_2_coordinate = []
        self.potential_move_up_coordinate = []
        self.potential_attack_up_7_coordinate = []
        self.potential_attack_up_6_coordinate = []
        self.potential_attack_up_5_coordinate = []
        self.potential_attack_up_4_coordinate = []
        self.potential_attack_up_3_coordinate = []
        self.potential_attack_up_2_coordinate = []
        self.potential_attack_up_coordinate = []
        self.potential_move_down_7_coordinate = []
        self.potential_move_down_6_coordinate = []
        self.potential_move_down_5_coordinate = []
        self.potential_move_down_4_coordinate = []
        self.potential_move_down_3_coordinate = []
        self.potential_move_down_2_coordinate = []
        self.potential_move_down_coordinate = []
        self.potential_attack_down_7_coordinate = []
        self.potential_attack_down_6_coordinate = []
        self.potential_attack_down_5_coordinate = []
        self.potential_attack_down_4_coordinate = []
        self.potential_attack_down_3_coordinate = []
        self.potential_attack_down_2_coordinate = []
        self.potential_attack_down_coordinate = []
        self.potential_move_right_7_coordinate = []
        self.potential_move_right_6_coordinate = []
        self.potential_move_right_5_coordinate = []
        self.potential_move_right_4_coordinate = []
        self.potential_move_right_3_coordinate = []
        self.potential_move_right_2_coordinate = []
        self.potential_move_right_coordinate = []
        self.potential_attack_right_7_coordinate = []
        self.potential_attack_right_6_coordinate = []
        self.potential_attack_right_5_coordinate = []
        self.potential_attack_right_4_coordinate = []
        self.potential_attack_right_3_coordinate = []
        self.potential_attack_right_2_coordinate = []
        self.potential_attack_right_coordinate = []
        self.potential_move_left_7_coordinate = []
        self.potential_move_left_6_coordinate = []
        self.potential_move_left_5_coordinate = []
        self.potential_move_left_4_coordinate = []
        self.potential_move_left_3_coordinate = []
        self.potential_move_left_2_coordinate = []
        self.potential_move_left_coordinate = []
        self.potential_attack_left_7_coordinate = []
        self.potential_attack_left_6_coordinate = []
        self.potential_attack_left_5_coordinate = []
        self.potential_attack_left_4_coordinate = []
        self.potential_attack_left_3_coordinate = []
        self.potential_attack_left_2_coordinate = []
        self.potential_attack_left_coordinate = []
        self.potential_move_up_right_7_coordinate = []
        self.potential_move_up_right_6_coordinate = []
        self.potential_move_up_right_5_coordinate = []
        self.potential_move_up_right_4_coordinate = []
        self.potential_move_up_right_3_coordinate = []
        self.potential_move_up_right_2_coordinate = []
        self.potential_move_up_right_coordinate = []
        self.potential_move_up_left_7_coordinate = []
        self.potential_move_up_left_6_coordinate = []
        self.potential_move_up_left_5_coordinate = []
        self.potential_move_up_left_4_coordinate = []
        self.potential_move_up_left_3_coordinate = []
        self.potential_move_up_left_2_coordinate = []
        self.potential_move_up_left_coordinate = []
        self.potential_move_down_right_7_coordinate = []
        self.potential_move_down_right_6_coordinate = []
        self.potential_move_down_right_5_coordinate = []
        self.potential_move_down_right_4_coordinate = []
        self.potential_move_down_right_3_coordinate = []
        self.potential_move_down_right_2_coordinate = []
        self.potential_move_down_right_coordinate = []
        self.potential_move_down_left_7_coordinate = []
        self.potential_move_down_left_6_coordinate = []
        self.potential_move_down_left_5_coordinate = []
        self.potential_move_down_left_4_coordinate = []
        self.potential_move_down_left_3_coordinate = []
        self.potential_move_down_left_2_coordinate = []
        self.potential_move_down_left_coordinate = []
        self.potential_attack_up_right_7_coordinate = []
        self.potential_attack_up_right_6_coordinate = []
        self.potential_attack_up_right_5_coordinate = []
        self.potential_attack_up_right_4_coordinate = []
        self.potential_attack_up_right_3_coordinate = []
        self.potential_attack_up_right_2_coordinate = []
        self.potential_attack_up_right_coordinate = []
        self.potential_attack_up_left_7_coordinate = []
        self.potential_attack_up_left_6_coordinate = []
        self.potential_attack_up_left_5_coordinate = []
        self.potential_attack_up_left_4_coordinate = []
        self.potential_attack_up_left_3_coordinate = []
        self.potential_attack_up_left_2_coordinate = []
        self.potential_attack_up_left_coordinate = []
        self.potential_attack_down_left_7_coordinate = []
        self.potential_attack_down_left_6_coordinate = []
        self.potential_attack_down_left_5_coordinate = []
        self.potential_attack_down_left_4_coordinate = []
        self.potential_attack_down_left_3_coordinate = []
        self.potential_attack_down_left_2_coordinate = []
        self.potential_attack_down_left_coordinate = []
        self.potential_attack_down_right_7_coordinate = []
        self.potential_attack_down_right_6_coordinate = []
        self.potential_attack_down_right_5_coordinate = []
        self.potential_attack_down_right_4_coordinate = []
        self.potential_attack_down_right_3_coordinate = []
        self.potential_attack_down_right_2_coordinate = []
        self.potential_attack_down_right_coordinate = []

    def move_up(self):
        for i in square_tuple:
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False and self.captured==False:
                self.position=board[self.position[0]][board[self.position[0]].index(self.position)+1]
                self.has_moved=True
                break

    def move_up_2(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                done = 0
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+2]) and i.occupied==False and self.captured==False:
                        self.position=board[self.position[0]][board[self.position[0]].index(self.position)+2]
                        self.has_moved=True
                        done=1
                        break

    def move_up_3(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+3]) and i.occupied==False and self.captured==False:
                                self.position=board[self.position[0]][board[self.position[0]].index(self.position)+3]
                                self.has_moved=True
                                done=1
                                break

    def move_up_4(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+4]) and i.occupied==False and self.captured==False:
                                        self.position=board[self.position[0]][board[self.position[0]].index(self.position)+4]
                                        print(self.position)
                                        self.has_moved=True
                                        self.has_moved=True
                                        done=1
                                        break

    def move_up_5(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+5]) and i.occupied==False and self.captured==False:
                                                print(self.position)
                                                self.position=board[self.position[0]][board[self.position[0]].index(self.position)+5]
                                                self.has_moved=True
                                                done=1
                                                break

    def move_up_6(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+6]) and i.occupied==False and self.captured==False:
                                                        self.position=board[self.position[0]][board[self.position[0]].index(self.position)+6]
                                                        self.has_moved=True
                                                        done=1
                                                        break

    def move_up_7(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+6]) and i.occupied==False and self.captured==False:
                                                        for i in square_tuple:
                                                            if done == 1:
                                                                break
                                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+7]) and i.occupied==False and self.captured==False:
                                                                self.position=board[self.position[0]][board[self.position[0]].index(self.position)+7]
                                                                self.has_moved=True
                                                                done=1
                                                                break



    def move_down(self):
        for i in square_tuple:
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False and self.captured==False:
                self.position=board[self.position[0]][board[self.position[0]].index(self.position)-1]
                self.has_moved=True
                break

    def move_down_2(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                done = 0
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-2]) and i.occupied==False and self.captured==False:
                        self.position=board[self.position[0]][board[self.position[0]].index(self.position)-2]
                        self.has_moved=True
                        done=1
                        break

    def move_down_3(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-3]) and i.occupied==False and self.captured==False:
                                self.position=board[self.position[0]][board[self.position[0]].index(self.position)-3]
                                self.has_moved=True
                                done=1
                                break

    def move_down_4(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-4]) and i.occupied==False and self.captured==False:
                                        self.position=board[self.position[0]][board[self.position[0]].index(self.position)-4]
                                        self.has_moved=True
                                        self.has_moved=True
                                        done=1
                                        break

    def move_down_5(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-5]) and i.occupied==False and self.captured==False:
                                                self.position=board[self.position[0]][board[self.position[0]].index(self.position)-5]
                                                self.has_moved=True
                                                done=1
                                                break

    def move_down_6(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-6]) and i.occupied==False and self.captured==False:
                                                        self.position=board[self.position[0]][board[self.position[0]].index(self.position)-6]
                                                        self.has_moved=True
                                                        done=1
                                                        break

    def move_down_7(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-6]) and i.occupied==False and self.captured==False:
                                                        for i in square_tuple:
                                                            if done == 1:
                                                                break
                                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-7]) and i.occupied==False and self.captured==False:
                                                                self.position=board[self.position[0]][board[self.position[0]].index(self.position)-7]
                                                                self.has_moved=True
                                                                done=1
                                                                break

    def move_right(self):
        for i in square_tuple:
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                self.position=board[self.position[0]+1][board[self.position[0]].index(self.position)]
                self.has_moved=True
                break

    def move_right_2(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                done = 0
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                        self.position=board[self.position[0]+2][board[self.position[0]].index(self.position)]
                        self.has_moved=True
                        done=1
                        break

    def move_right_3(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                self.position=board[self.position[0]+3][board[self.position[0]].index(self.position)]
                                self.has_moved=True
                                done=1
                                break

    def move_right_4(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                        self.position=board[self.position[0]+4][board[self.position[0]].index(self.position)]
                                        print(self.position)
                                        self.has_moved=True
                                        self.has_moved=True
                                        done=1
                                        break

    def move_right_5(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                        for i in square_tuple:
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                print(self.position)
                                                self.position=board[self.position[0]+5][board[self.position[0]].index(self.position)]
                                                self.has_moved=True
                                                done=1
                                                break

    def move_right_6(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+6][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                        self.position=board[self.position[0]+6][board[self.position[0]].index(self.position)]
                                                        self.has_moved=True
                                                        done=1
                                                        break

    def move_right_7(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+6][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                        for i in square_tuple:
                                                            if done == 1:
                                                                break
                                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+7][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                                self.position=board[self.position[0]+7][board[self.position[0]].index(self.position)]
                                                                self.has_moved=True
                                                                done=1
                                                                break


    def move_left(self):
        for i in square_tuple:
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                self.position=board[self.position[0]-1][board[self.position[0]].index(self.position)]
                self.has_moved=True
                break

    def move_left_2(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                done = 0
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                        self.position=board[self.position[0]-2][board[self.position[0]].index(self.position)]
                        self.has_moved=True
                        done=1
                        break

    def move_left_3(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                self.position=board[self.position[0]-3][board[self.position[0]].index(self.position)]
                                self.has_moved=True
                                done=1
                                break

    def move_left_4(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                        self.position=board[self.position[0]-4][board[self.position[0]].index(self.position)]
                                        print(self.position)
                                        self.has_moved=True
                                        self.has_moved=True
                                        done=1
                                        break

    def move_left_5(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                        for i in square_tuple:
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                print(self.position)
                                                self.position=board[self.position[0]-5][board[self.position[0]].index(self.position)]
                                                self.has_moved=True
                                                done=1
                                                break

    def move_left_6(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-6][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                        self.position=board[self.position[0]-6][board[self.position[0]].index(self.position)]
                                                        self.has_moved=True
                                                        done=1
                                                        break

    def move_left_7(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-6][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                        for i in square_tuple:
                                                            if done == 1:
                                                                break
                                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-7][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                                self.position=board[self.position[0]-7][board[self.position[0]].index(self.position)]
                                                                self.has_moved=True
                                                                done=1
                                                                break


    def move_up_right(self):
        for i in square_tuple:
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and i.occupied==False and self.captured==False:
                self.position=board[self.position[0]+1][board[self.position[0]].index(self.position)+1]
                self.has_moved=True
                break

    def move_up_right_2(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                done = 0
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)+2]) and i.occupied==False and self.captured==False:
                        self.position=board[self.position[0]+2][board[self.position[0]].index(self.position)+2]
                        self.has_moved=True
                        done=1
                        break

    def move_up_right_3(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)+3]) and i.occupied==False and self.captured==False:
                                self.position=board[self.position[0]+3][board[self.position[0]].index(self.position)+3]
                                self.has_moved=True
                                done=1
                                break

    def move_up_right_4(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)+4]) and i.occupied==False and self.captured==False:
                                        self.position=board[self.position[0]+4][board[self.position[0]].index(self.position)+4]
                                        print(self.position)
                                        self.has_moved=True
                                        self.has_moved=True
                                        done=1
                                        break

    def move_up_right_5(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)+5]) and i.occupied==False and self.captured==False:
                                                print(self.position)
                                                self.position=board[self.position[0]+5][board[self.position[0]].index(self.position)+5]
                                                self.has_moved=True
                                                done=1
                                                break

    def move_up_right_6(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)+5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+6][board[self.position[0]].index(self.position)+6]) and i.occupied==False and self.captured==False:
                                                        self.position=board[self.position[0]+6][board[self.position[0]].index(self.position)+6]
                                                        self.has_moved=True
                                                        done=1
                                                        break

    def move_up_right_7(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)+5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+6][board[self.position[0]].index(self.position)+6]) and i.occupied==False and self.captured==False:
                                                        for i in square_tuple:
                                                            if done == 1:
                                                                break
                                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+7][board[self.position[0]].index(self.position)+7]) and i.occupied==False and self.captured==False:
                                                                self.position=board[self.position[0]+7][board[self.position[0]].index(self.position)+7]
                                                                self.has_moved=True
                                                                done=1
                                                                break


    def move_up_left(self):
        for i in square_tuple:
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and i.occupied==False and self.captured==False:
                self.position=board[self.position[0]-1][board[self.position[0]].index(self.position)+1]
                self.has_moved=True
                break

    def move_up_left_2(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                done = 0
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)+2]) and i.occupied==False and self.captured==False:
                        self.position=board[self.position[0]-2][board[self.position[0]].index(self.position)+2]
                        self.has_moved=True
                        done=1
                        break

    def move_up_left_3(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)+3]) and i.occupied==False and self.captured==False:
                                self.position=board[self.position[0]-3][board[self.position[0]].index(self.position)+3]
                                self.has_moved=True
                                done=1
                                break

    def move_up_left_4(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)+4]) and i.occupied==False and self.captured==False:
                                        self.position=board[self.position[0]-4][board[self.position[0]].index(self.position)+4]
                                        print(self.position)
                                        self.has_moved=True
                                        self.has_moved=True
                                        done=1
                                        break

    def move_up_left_5(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)+5]) and i.occupied==False and self.captured==False:
                                                print(self.position)
                                                self.position=board[self.position[0]-5][board[self.position[0]].index(self.position)+5]
                                                self.has_moved=True
                                                done=1
                                                break

    def move_up_left_6(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)+5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-6][board[self.position[0]].index(self.position)+6]) and i.occupied==False and self.captured==False:
                                                        self.position=board[self.position[0]-6][board[self.position[0]].index(self.position)+6]
                                                        self.has_moved=True
                                                        done=1
                                                        break

    def move_up_left_7(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)+5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-6][board[self.position[0]].index(self.position)+6]) and i.occupied==False and self.captured==False:
                                                        for i in square_tuple:
                                                            if done == 1:
                                                                break
                                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-7][board[self.position[0]].index(self.position)+7]) and i.occupied==False and self.captured==False:
                                                                self.position=board[self.position[0]-7][board[self.position[0]].index(self.position)+7]
                                                                self.has_moved=True
                                                                done=1
                                                                break


    def move_down_right(self):
        for i in square_tuple:
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and i.occupied==False and self.captured==False:
                self.position=board[self.position[0]+1][board[self.position[0]].index(self.position)-1]
                self.has_moved=True
                break

    def move_down_right_2(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                done = 0
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)-2]) and i.occupied==False and self.captured==False:
                        self.position=board[self.position[0]+2][board[self.position[0]].index(self.position)-2]
                        self.has_moved=True
                        done=1
                        break

    def move_down_right_3(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)-3]) and i.occupied==False and self.captured==False:
                                self.position=board[self.position[0]+3][board[self.position[0]].index(self.position)-3]
                                self.has_moved=True
                                done=1
                                break

    def move_down_right_4(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)-4]) and i.occupied==False and self.captured==False:
                                        self.position=board[self.position[0]+4][board[self.position[0]].index(self.position)-4]
                                        print(self.position)
                                        self.has_moved=True
                                        self.has_moved=True
                                        done=1
                                        break

    def move_down_right_5(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)-5]) and i.occupied==False and self.captured==False:
                                                print(self.position)
                                                self.position=board[self.position[0]+5][board[self.position[0]].index(self.position)-5]
                                                self.has_moved=True
                                                done=1
                                                break

    def move_down_right_6(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)-5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+6][board[self.position[0]].index(self.position)-6]) and i.occupied==False and self.captured==False:
                                                        self.position=board[self.position[0]+6][board[self.position[0]].index(self.position)-6]
                                                        self.has_moved=True
                                                        done=1
                                                        break

    def move_down_right_7(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)-5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+6][board[self.position[0]].index(self.position)-6]) and i.occupied==False and self.captured==False:
                                                        for i in square_tuple:
                                                            if done == 1:
                                                                break
                                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+7][board[self.position[0]].index(self.position)-7]) and i.occupied==False and self.captured==False:
                                                                self.position=board[self.position[0]+7][board[self.position[0]].index(self.position)-7]
                                                                self.has_moved=True
                                                                done=1
                                                                break


    def move_down_left(self):
        for i in square_tuple:
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and i.occupied==False and self.captured==False:
                self.position=board[self.position[0]-1][board[self.position[0]].index(self.position)-1]
                self.has_moved=True
                break

    def move_down_left_2(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                done = 0
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)-2]) and i.occupied==False and self.captured==False:
                        self.position=board[self.position[0]-2][board[self.position[0]].index(self.position)-2]
                        self.has_moved=True
                        done=1
                        break

    def move_down_left_3(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)-3]) and i.occupied==False and self.captured==False:
                                self.position=board[self.position[0]-3][board[self.position[0]].index(self.position)-3]
                                self.has_moved=True
                                done=1
                                break

    def move_down_left_4(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)-4]) and i.occupied==False and self.captured==False:
                                        self.position=board[self.position[0]-4][board[self.position[0]].index(self.position)-4]
                                        print(self.position)
                                        self.has_moved=True
                                        self.has_moved=True
                                        done=1
                                        break

    def move_down_left_5(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)-5]) and i.occupied==False and self.captured==False:
                                                print(self.position)
                                                self.position=board[self.position[0]-5][board[self.position[0]].index(self.position)-5]
                                                self.has_moved=True
                                                done=1
                                                break

    def move_down_left_6(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)-5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-6][board[self.position[0]].index(self.position)-6]) and i.occupied==False and self.captured==False:
                                                        self.position=board[self.position[0]-6][board[self.position[0]].index(self.position)-6]
                                                        self.has_moved=True
                                                        done=1
                                                        break

    def move_down_left_7(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)-5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-6][board[self.position[0]].index(self.position)-6]) and i.occupied==False and self.captured==False:
                                                        for i in square_tuple:
                                                            if done == 1:
                                                                break
                                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-7][board[self.position[0]].index(self.position)-7]) and i.occupied==False and self.captured==False:
                                                                self.position=board[self.position[0]-7][board[self.position[0]].index(self.position)-7]
                                                                self.has_moved=True
                                                                done=1
                                                                break


    def attack_up(self):
        for i in square_tuple:
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                for x in piece_tuple:
                    if x.chess_replace()==i.coordinate:
                        x.captured=True
                self.position=board[self.position[0]][board[self.position[0]].index(self.position)+1]
                self.has_moved=True
                break

    def attack_up_2(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                done = 0
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+2]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                        for x in piece_tuple:
                            if x.chess_replace()==i.coordinate:
                                x.captured=True
                        self.position=board[self.position[0]][board[self.position[0]].index(self.position)+2]
                        self.has_moved=True
                        done=1
                        break

    def attack_up_3(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+3]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                for x in piece_tuple:
                                    if x.chess_replace()==i.coordinate:
                                        x.captured=True
                                self.position=board[self.position[0]][board[self.position[0]].index(self.position)+3]
                                self.has_moved=True
                                done=1
                                break

    def attack_up_4(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+4]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                        for x in piece_tuple:
                                            if x.chess_replace()==i.coordinate:
                                                x.captured=True
                                        self.position=board[self.position[0]][board[self.position[0]].index(self.position)+4]
                                        self.has_moved=True
                                        done=1
                                        break

    def attack_up_5(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+5]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                for x in piece_tuple:
                                                    if x.chess_replace()==i.coordinate:
                                                        x.captured=True
                                                self.position=board[self.position[0]][board[self.position[0]].index(self.position)+5]
                                                self.has_moved=True
                                                done=1
                                                break

    def attack_up_6(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+6]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                        for x in piece_tuple:
                                                            if x.chess_replace()==i.coordinate:
                                                                x.captured=True
                                                        self.position=board[self.position[0]][board[self.position[0]].index(self.position)+6]
                                                        self.has_moved=True
                                                        done=1
                                                        break

    def attack_up_7(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+6]) and i.occupied==False and self.captured==False:
                                                        for i in square_tuple:
                                                            if done == 1:
                                                                break
                                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+7]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                                for x in piece_tuple:
                                                                    if x.chess_replace()==i.coordinate:
                                                                        x.captured=True
                                                                self.position=board[self.position[0]][board[self.position[0]].index(self.position)+7]
                                                                self.has_moved=True
                                                                done=1
                                                                break


    def attack_down(self):
        for i in square_tuple:
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                for x in piece_tuple:
                    if x.chess_replace()==i.coordinate:
                        x.captured=True
                self.position=board[self.position[0]][board[self.position[0]].index(self.position)-1]
                self.has_moved=True
                break

    def attack_down_2(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                done = 0
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-2]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                        for x in piece_tuple:
                            if x.chess_replace()==i.coordinate:
                                x.captured=True
                        self.position=board[self.position[0]][board[self.position[0]].index(self.position)-2]
                        self.has_moved=True
                        done=1
                        break

    def attack_down_3(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-3]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                for x in piece_tuple:
                                    if x.chess_replace()==i.coordinate:
                                        x.captured=True
                                self.position=board[self.position[0]][board[self.position[0]].index(self.position)-3]
                                self.has_moved=True
                                done=1
                                break

    def attack_down_4(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-4]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                        for x in piece_tuple:
                                            if x.chess_replace()==i.coordinate:
                                                x.captured=True
                                        self.position=board[self.position[0]][board[self.position[0]].index(self.position)-4]
                                        self.has_moved=True
                                        done=1
                                        break

    def attack_down_5(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-5]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                for x in piece_tuple:
                                                    if x.chess_replace()==i.coordinate:
                                                        x.captured=True
                                                self.position=board[self.position[0]][board[self.position[0]].index(self.position)-5]
                                                self.has_moved=True
                                                done=1
                                                break

    def attack_down_6(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-5]) and i.occupied==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-6]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                        for x in piece_tuple:
                                                            if x.chess_replace()==i.coordinate:
                                                                x.captured=True
                                                        self.position=board[self.position[0]][board[self.position[0]].index(self.position)-6]
                                                        self.has_moved=True
                                                        done=1
                                                        break

    def attack_down_7(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-6]) and i.occupied==False and self.captured==False:
                                                        for i in square_tuple:
                                                            if done == 1:
                                                                break
                                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-7]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                                for x in piece_tuple:
                                                                    if x.chess_replace()==i.coordinate:
                                                                        x.captured=True
                                                                self.position=board[self.position[0]][board[self.position[0]].index(self.position)-7]
                                                                self.has_moved=True
                                                                done=1
                                                                break


    def attack_right(self):
        for i in square_tuple:
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                for x in piece_tuple:
                    if x.chess_replace()==i.coordinate:
                        x.captured=True
                self.position=board[self.position[0]+1][board[self.position[0]].index(self.position)]
                self.has_moved=True
                break

    def attack_right_2(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                done = 0
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                        for x in piece_tuple:
                            if x.chess_replace()==i.coordinate:
                                x.captured=True
                        self.position=board[self.position[0]+2][board[self.position[0]].index(self.position)]
                        self.has_moved=True
                        done=1
                        break

    def attack_right_3(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                            for i in square_tuple:
                                if done == 1:
                                    break
                                if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                    for x in piece_tuple:
                                        if x.chess_replace()==i.coordinate:
                                            x.captured=True
                                            print(x.captured)
                                    self.position=board[self.position[0]+3][board[self.position[0]].index(self.position)]
                                    self.has_moved=True
                                    done=1
                                    break

    def attack_right_4(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                        for x in piece_tuple:
                                            if x.chess_replace()==i.coordinate:
                                                x.captured=True
                                        self.position=board[self.position[0]+4][board[self.position[0]].index(self.position)]
                                        self.has_moved=True
                                        done=1
                                        break

    def attack_right_5(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                        for i in square_tuple:
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                for x in piece_tuple:
                                                    if x.chess_replace()==i.coordinate:
                                                        x.captured=True
                                                self.position=board[self.position[0]+5][board[self.position[0]].index(self.position)]
                                                self.has_moved=True
                                                done=1
                                                break

    def attack_right_6(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+6][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                        for x in piece_tuple:
                                                            if x.chess_replace()==i.coordinate:
                                                                x.captured=True
                                                        self.position=board[self.position[0]+6][board[self.position[0]].index(self.position)]
                                                        self.has_moved=True
                                                        done=1
                                                        break

    def attack_right_7(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+6][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                        for i in square_tuple:
                                                            if done == 1:
                                                                break
                                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+7][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                                for x in piece_tuple:
                                                                    if x.chess_replace()==i.coordinate:
                                                                        x.captured=True
                                                                self.position=board[self.position[0]+7][board[self.position[0]].index(self.position)]
                                                                self.has_moved=True
                                                                done=1
                                                                break


    def attack_left(self):
        for i in square_tuple:
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                for x in piece_tuple:
                    if x.chess_replace()==i.coordinate:
                        x.captured=True
                self.position=board[self.position[0]-1][board[self.position[0]].index(self.position)]
                self.has_moved=True
                break

    def attack_left_2(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                done = 0
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                        for x in piece_tuple:
                            if x.chess_replace()==i.coordinate:
                                x.captured=True
                        self.position=board[self.position[0]-2][board[self.position[0]].index(self.position)]
                        self.has_moved=True
                        done=1
                        break

    def attack_left_3(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                for x in piece_tuple:
                                    if x.chess_replace()==i.coordinate:
                                        x.captured=True
                                self.position=board[self.position[0]-3][board[self.position[0]].index(self.position)]
                                self.has_moved=True
                                done=1
                                break

    def attack_left_4(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                        for x in piece_tuple:
                                            if x.chess_replace()==i.coordinate:
                                                x.captured=True
                                        self.position=board[self.position[0]-4][board[self.position[0]].index(self.position)]
                                        self.has_moved=True
                                        done=1
                                        break

    def attack_left_5(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                for x in piece_tuple:
                                                    if x.chess_replace()==i.coordinate:
                                                        x.captured=True
                                                self.position=board[self.position[0]-5][board[self.position[0]].index(self.position)]
                                                self.has_moved=True
                                                done=1
                                                break

    def attack_left_6(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-6][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                        for x in piece_tuple:
                                                            if x.chess_replace()==i.coordinate:
                                                                x.captured=True
                                                        self.position=board[self.position[0]-6][board[self.position[0]].index(self.position)]
                                                        self.has_moved=True
                                                        done=1
                                                        break

    def attack_left_7(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-6][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                        for i in square_tuple:
                                                            if done == 1:
                                                                break
                                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-7][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                                for x in piece_tuple:
                                                                    if x.chess_replace()==i.coordinate:
                                                                        x.captured=True
                                                                self.position=board[self.position[0]-7][board[self.position[0]].index(self.position)]
                                                                self.has_moved=True
                                                                done=1
                                                                break


    def attack_up_right(self):
        for i in square_tuple:
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                for x in piece_tuple:
                    if x.chess_replace()==i.coordinate:
                        x.captured=True
                self.position=board[self.position[0]+1][board[self.position[0]].index(self.position)+1]
                self.has_moved=True
                break

    def attack_up_right_2(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                done = 0
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)+2]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                        for x in piece_tuple:
                            if x.chess_replace()==i.coordinate:
                                x.captured=True
                        self.position=board[self.position[0]+2][board[self.position[0]].index(self.position)+2]
                        self.has_moved=True
                        done=1
                        break

    def attack_up_right_3(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)+3]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                for x in piece_tuple:
                                    if x.chess_replace()==i.coordinate:
                                        x.captured=True
                                self.position=board[self.position[0]+3][board[self.position[0]].index(self.position)+3]
                                self.has_moved=True
                                done=1
                                break

    def attack_up_right_4(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)+4]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                        for x in piece_tuple:
                                            if x.chess_replace()==i.coordinate:
                                                x.captured=True
                                        self.position=board[self.position[0]+4][board[self.position[0]].index(self.position)+4]
                                        print(self.position)
                                        self.has_moved=True
                                        self.has_moved=True
                                        done=1
                                        break

    def attack_up_right_5(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)+5]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                for x in piece_tuple:
                                                    if x.chess_replace()==i.coordinate:
                                                        x.captured=True
                                                self.position=board[self.position[0]+5][board[self.position[0]].index(self.position)+5]
                                                self.has_moved=True
                                                done=1
                                                break

    def attack_up_right_6(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)+5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+6][board[self.position[0]].index(self.position)+6]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                            for x in piece_tuple:
                                                                if x.chess_replace()==i.coordinate:
                                                                    x.captured=True
                                                            self.position=board[self.position[0]+6][board[self.position[0]].index(self.position)+6]
                                                            self.has_moved=True
                                                            done=1
                                                            break

    def attack_up_right_7(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)+5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+6][board[self.position[0]].index(self.position)+6]) and i.occupied==False and self.captured==False:
                                                        for i in square_tuple:
                                                            if done == 1:
                                                                break
                                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+7][board[self.position[0]].index(self.position)+7]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                                for x in piece_tuple:
                                                                    if x.chess_replace()==i.coordinate:
                                                                        x.captured=True
                                                                self.position=board[self.position[0]+7][board[self.position[0]].index(self.position)+7]
                                                                self.has_moved=True
                                                                done=1
                                                                break


    def attack_up_left(self):
        for i in square_tuple:
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                for x in piece_tuple:
                    if x.chess_replace()==i.coordinate:
                        x.captured=True
                self.position=board[self.position[0]-1][board[self.position[0]].index(self.position)+1]
                self.has_moved=True
                break

    def attack_up_left_2(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                done = 0
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)+2]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                        for x in piece_tuple:
                            if x.chess_replace()==i.coordinate:
                                x.captured=True
                        self.position=board[self.position[0]-2][board[self.position[0]].index(self.position)+2]
                        self.has_moved=True
                        done=1
                        break

    def attack_up_left_3(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)+3]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                for x in piece_tuple:
                                    if x.chess_replace()==i.coordinate:
                                        x.captured=True
                                self.position=board[self.position[0]-3][board[self.position[0]].index(self.position)+3]
                                self.has_moved=True
                                done=1
                                break

    def attack_up_left_4(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)+4]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                        for x in piece_tuple:
                                            if x.chess_replace()==i.coordinate:
                                                x.captured=True
                                        self.position=board[self.position[0]-4][board[self.position[0]].index(self.position)+4]
                                        self.has_moved=True
                                        done=1
                                        break

    def attack_up_left_5(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)+5]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                for x in piece_tuple:
                                                    if x.chess_replace()==i.coordinate:
                                                        x.captured=True
                                                self.position=board[self.position[0]-5][board[self.position[0]].index(self.position)+5]
                                                self.has_moved=True
                                                done=1
                                                break

    def attack_up_left_6(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)+5]) and i.occupied==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-6][board[self.position[0]].index(self.position)+6]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                        for x in piece_tuple:
                                                            if x.chess_replace()==i.coordinate:
                                                                x.captured=True
                                                        self.position=board[self.position[0]-6][board[self.position[0]].index(self.position)+6]
                                                        self.has_moved=True
                                                        done=1
                                                        break

    def attack_up_left_7(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)+5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-6][board[self.position[0]].index(self.position)+6]) and i.occupied==False and self.captured==False:
                                                        for i in square_tuple:
                                                            if done == 1:
                                                                break
                                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-7][board[self.position[0]].index(self.position)+7]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                                for x in piece_tuple:
                                                                    if x.chess_replace()==i.coordinate:
                                                                        x.captured=True
                                                                self.position=board[self.position[0]-7][board[self.position[0]].index(self.position)+7]
                                                                self.has_moved=True
                                                                done=1
                                                                break


    def attack_down_right(self):
        for i in square_tuple:
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                for x in piece_tuple:
                    if x.chess_replace()==i.coordinate:
                        x.captured=True
                self.position=board[self.position[0]+1][board[self.position[0]].index(self.position)-1]
                self.has_moved=True
                break

    def attack_down_right_2(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                done = 0
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)-2]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                        for x in piece_tuple:
                            if x.chess_replace()==i.coordinate:
                                x.captured=True
                        self.position=board[self.position[0]+2][board[self.position[0]].index(self.position)-2]
                        self.has_moved=True
                        done=1
                        break

    def attack_down_right_3(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)-3]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                for x in piece_tuple:
                                    if x.chess_replace()==i.coordinate:
                                        x.captured=True
                                self.position=board[self.position[0]+3][board[self.position[0]].index(self.position)-3]
                                self.has_moved=True
                                done=1
                                break

    def attack_down_right_4(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)-4]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                        for x in piece_tuple:
                                            if x.chess_replace()==i.coordinate:
                                                x.captured=True
                                        self.position=board[self.position[0]+4][board[self.position[0]].index(self.position)-4]
                                        self.has_moved=True
                                        done=1
                                        break

    def attack_down_right_5(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)-5]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                for x in piece_tuple:
                                                    if x.chess_replace()==i.coordinate:
                                                        x.captured=True
                                                self.position=board[self.position[0]+5][board[self.position[0]].index(self.position)-5]
                                                self.has_moved=True
                                                done=1
                                                break

    def attack_down_right_6(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)-5]) and i.occupied==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+6][board[self.position[0]].index(self.position)-6]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                        for x in piece_tuple:
                                                            if x.chess_replace()==i.coordinate:
                                                                x.captured=True
                                                        self.position=board[self.position[0]+6][board[self.position[0]].index(self.position)-6]
                                                        self.has_moved=True
                                                        done=1
                                                        break

    def attack_down_right_7(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)-5]) and i.occupied==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+6][board[self.position[0]].index(self.position)-6]) and i.occupied==False:
                                                        for i in square_tuple:
                                                            if done == 1:
                                                                break
                                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+7][board[self.position[0]].index(self.position)-7]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                                for x in piece_tuple:
                                                                    if x.chess_replace()==i.coordinate:
                                                                        x.captured=True
                                                                self.position=board[self.position[0]+7][board[self.position[0]].index(self.position)-7]
                                                                self.has_moved=True
                                                                done=1
                                                                break


    def attack_down_left(self):
        for i in square_tuple:
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                for x in piece_tuple:
                    if x.chess_replace()==i.coordinate:
                        x.captured=True
                self.position=board[self.position[0]-1][board[self.position[0]].index(self.position)-1]
                self.has_moved=True
                break

    def attack_down_left_2(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                done = 0
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)-2]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                        for x in piece_tuple:
                            if x.chess_replace()==i.coordinate:
                                x.captured=True
                        self.position=board[self.position[0]-2][board[self.position[0]].index(self.position)-2]
                        self.has_moved=True
                        done=1
                        break

    def attack_down_left_3(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)-3]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                for x in piece_tuple:
                                    if x.chess_replace()==i.coordinate:
                                        x.captured=True
                                self.position=board[self.position[0]-3][board[self.position[0]].index(self.position)-3]
                                self.has_moved=True
                                done=1
                                break

    def attack_down_left_4(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)-4]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                        for x in piece_tuple:
                                            if x.chess_replace()==i.coordinate:
                                                x.captured=True
                                        self.position=board[self.position[0]-4][board[self.position[0]].index(self.position)-4]
                                        self.has_moved=True
                                        done=1
                                        break

    def attack_down_left_5(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)-5]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                for x in piece_tuple:
                                                    if x.chess_replace()==i.coordinate:
                                                        x.captured=True
                                                self.position=board[self.position[0]-5][board[self.position[0]].index(self.position)-5]
                                                self.has_moved=True
                                                done=1
                                                break

    def attack_down_left_6(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)-5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-6][board[self.position[0]].index(self.position)-6]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                        for x in piece_tuple:
                                                            if x.chess_replace()==i.coordinate:
                                                                x.captured=True
                                                        self.position=board[self.position[0]-6][board[self.position[0]].index(self.position)-6]
                                                        self.has_moved=True
                                                        done=1
                                                        break

    def attack_down_left_7(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)-5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-6][board[self.position[0]].index(self.position)-6]) and i.occupied==False and self.captured==False:
                                                        for i in square_tuple:
                                                            if done == 1:
                                                                break
                                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-7][board[self.position[0]].index(self.position)-7]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                                for x in piece_tuple:
                                                                    if x.chess_replace()==i.coordinate:
                                                                        x.captured=True
                                                                self.position=board[self.position[0]-7][board[self.position[0]].index(self.position)-7]
                                                                self.has_moved=True
                                                                done=1
                                                                break


    def potential_move_up(self):
        for i in square_tuple:
            if self.position[1] == 8:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False and self.captured==False:
                potential=board[self.position[0]][board[self.position[0]].index(self.position)+1]
                self.potential_move_list.append(queen.static_chess_replace(potential))
                self.potential_move_up_coordinate.append(queen.static_chess_replace(potential))
                break

    def potential_move_up_2(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+2]) and i.occupied==False and self.captured==False:
                        potential=board[self.position[0]][board[self.position[0]].index(self.position)+2]
                        self.potential_move_list.append(queen.static_chess_replace(potential))
                        self.potential_move_up_2_coordinate.append(queen.static_chess_replace(potential))
                        done=1
                        break

    def potential_move_up_3(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+3]) and i.occupied==False and self.captured==False:
                                potential=board[self.position[0]][board[self.position[0]].index(self.position)+3]
                                self.potential_move_list.append(queen.static_chess_replace(potential))
                                self.potential_move_up_3_coordinate.append(queen.static_chess_replace(potential))
                                done=1
                                break

    def potential_move_up_4(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 5:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+4]) and i.occupied==False and self.captured==False:
                                        potential=board[self.position[0]][board[self.position[0]].index(self.position)+4]
                                        self.potential_move_list.append(queen.static_chess_replace(potential))
                                        self.potential_move_up_4_coordinate.append(queen.static_chess_replace(potential))
                                        done=1
                                        break

    def potential_move_up_5(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 5:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 4:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+5]) and i.occupied==False and self.captured==False:
                                                potential=board[self.position[0]][board[self.position[0]].index(self.position)+5]
                                                self.potential_move_list.append(queen.static_chess_replace(potential))
                                                self.potential_move_up_5_coordinate.append(queen.static_chess_replace(potential))
                                                done=1
                                                break

    def potential_move_up_6(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 5:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 4:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[1] == 3:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+6]) and i.occupied==False and self.captured==False:
                                                        potential=board[self.position[0]][board[self.position[0]].index(self.position)+6]
                                                        self.potential_move_list.append(queen.static_chess_replace(potential))
                                                        self.potential_move_up_6_coordinate.append(queen.static_chess_replace(potential))
                                                        done=1
                                                        break

    def potential_move_up_7(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 5:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 4:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[1] == 3:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+6]) and i.occupied==False and self.captured==False:
                                                        for i in square_tuple:
                                                            if done == 1 or self.position[1] == 2 :
                                                                break
                                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+7]) and i.occupied==False and self.captured==False:
                                                                potential=board[self.position[0]][board[self.position[0]].index(self.position)+7]
                                                                self.potential_move_list.append(queen.static_chess_replace(potential))
                                                                self.potential_move_up_7_coordinate.append(queen.static_chess_replace(potential))
                                                                done=1
                                                                break


    def potential_attack_up(self):
        for i in square_tuple:
            if self.position[1] == 8:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                potential=board[self.position[0]][board[self.position[0]].index(self.position)+1]
                self.potential_attack_list.append(queen.static_chess_replace(potential))
                self.potential_attack_up_coordinate.append(queen.static_chess_replace(potential))
                break

    def potential_attack_up_2(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+2]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                        potential=board[self.position[0]][board[self.position[0]].index(self.position)+2]
                        self.potential_attack_list.append(queen.static_chess_replace(potential))
                        self.potential_attack_up_2_coordinate.append(queen.static_chess_replace(potential))
                        done=1
                        break

    def potential_attack_up_3(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+3]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                potential=board[self.position[0]][board[self.position[0]].index(self.position)+3]
                                self.potential_attack_list.append(queen.static_chess_replace(potential))
                                self.potential_attack_up_3_coordinate.append(queen.static_chess_replace(potential))
                                done=1
                                break

    def potential_attack_up_4(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 5:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+4]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                        potential=board[self.position[0]][board[self.position[0]].index(self.position)+4]
                                        self.potential_attack_list.append(queen.static_chess_replace(potential))
                                        self.potential_attack_up_4_coordinate.append(queen.static_chess_replace(potential))
                                        done=1
                                        break

    def potential_attack_up_5(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 5:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 4:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+5]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                potential=board[self.position[0]][board[self.position[0]].index(self.position)+5]
                                                self.potential_attack_list.append(queen.static_chess_replace(potential))
                                                self.potential_attack_up_5_coordinate.append(queen.static_chess_replace(potential))
                                                done=1
                                                break

    def potential_attack_up_6(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 5:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 4:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[1] == 3:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+6]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                        potential=board[self.position[0]][board[self.position[0]].index(self.position)+6]
                                                        self.potential_attack_list.append(queen.static_chess_replace(potential))
                                                        self.potential_attack_up_6_coordinate.append(queen.static_chess_replace(potential))
                                                        done=1
                                                        break

    def potential_attack_up_7(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 5:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 4:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[1] == 3:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+6]) and i.occupied==False and self.captured==False:
                                                        for i in square_tuple:
                                                            if done == 1 or self.position[1] == 2 :
                                                                break
                                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+7]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                                potential=board[self.position[0]][board[self.position[0]].index(self.position)+7]
                                                                self.potential_attack_list.append(queen.static_chess_replace(potential))
                                                                self.potential_attack_up_7_coordinate.append(queen.static_chess_replace(potential))
                                                                done=1
                                                                break


    def potential_move_down(self):
        for i in square_tuple:
            if self.position[1] == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False and self.captured==False:
                potential=board[self.position[0]][board[self.position[0]].index(self.position)-1]
                self.potential_move_list.append(queen.static_chess_replace(potential))
                self.potential_move_down_coordinate.append(queen.static_chess_replace(potential))
                break

    def potential_move_down_2(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-2]) and i.occupied==False and self.captured==False:
                        potential=board[self.position[0]][board[self.position[0]].index(self.position)-2]
                        self.potential_move_list.append(queen.static_chess_replace(potential))
                        self.potential_move_down_2_coordinate.append(queen.static_chess_replace(potential))
                        done=1
                        break

    def potential_move_down_3(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-3]) and i.occupied==False and self.captured==False:
                                potential=board[self.position[0]][board[self.position[0]].index(self.position)-3]
                                self.potential_move_list.append(queen.static_chess_replace(potential))
                                self.potential_move_down_3_coordinate.append(queen.static_chess_replace(potential))
                                done=1
                                break

    def potential_move_down_4(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 4:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-4]) and i.occupied==False and self.captured==False:
                                        potential=board[self.position[0]][board[self.position[0]].index(self.position)-4]
                                        self.potential_move_list.append(queen.static_chess_replace(potential))
                                        self.potential_move_down_4_coordinate.append(queen.static_chess_replace(potential))
                                        done=1
                                        break

    def potential_move_down_5(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 4:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 5:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-5]) and i.occupied==False and self.captured==False:
                                                potential=board[self.position[0]][board[self.position[0]].index(self.position)-5]
                                                self.potential_move_list.append(queen.static_chess_replace(potential))
                                                self.potential_move_down_5_coordinate.append(queen.static_chess_replace(potential))
                                                done=1
                                                break

    def potential_move_down_6(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 4:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 5:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[1] == 6:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-6]) and i.occupied==False and self.captured==False:
                                                        potential=board[self.position[0]][board[self.position[0]].index(self.position)-6]
                                                        self.potential_move_list.append(queen.static_chess_replace(potential))
                                                        self.potential_move_down_6_coordinate.append(queen.static_chess_replace(potential))
                                                        done=1
                                                        break

    def potential_move_down_7(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 4:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 5:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[1] == 6:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-6]) and i.occupied==False and self.captured==False:
                                                        for i in square_tuple:
                                                            if done == 1 or self.position[1] == 7:
                                                                break
                                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-7]) and i.occupied==False and self.captured==False:
                                                                potential=board[self.position[0]][board[self.position[0]].index(self.position)-7]
                                                                self.potential_move_list.append(queen.static_chess_replace(potential))
                                                                self.potential_move_down_7_coordinate.append(queen.static_chess_replace(potential))
                                                                done=1
                                                                break


    def potential_attack_down(self):
        for i in square_tuple:
            if self.position[1] == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                potential=board[self.position[0]][board[self.position[0]].index(self.position)-1]
                self.potential_attack_list.append(queen.static_chess_replace(potential))
                self.potential_attack_down_coordinate.append(queen.static_chess_replace(potential))
                break

    def potential_attack_down_2(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-2]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                        potential=board[self.position[0]][board[self.position[0]].index(self.position)-2]
                        self.potential_attack_list.append(queen.static_chess_replace(potential))
                        self.potential_attack_down_2_coordinate.append(queen.static_chess_replace(potential))
                        done=1
                        break

    def potential_attack_down_3(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-3]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                potential=board[self.position[0]][board[self.position[0]].index(self.position)-3]
                                self.potential_attack_list.append(queen.static_chess_replace(potential))
                                self.potential_attack_down_3_coordinate.append(queen.static_chess_replace(potential))
                                done=1
                                break

    def potential_attack_down_4(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 4:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-4]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                        potential=board[self.position[0]][board[self.position[0]].index(self.position)-4]
                                        self.potential_attack_list.append(queen.static_chess_replace(potential))
                                        self.potential_attack_down_4_coordinate.append(queen.static_chess_replace(potential))
                                        done=1
                                        break

    def potential_attack_down_5(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 4:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 5:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-5]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                potential=board[self.position[0]][board[self.position[0]].index(self.position)-5]
                                                self.potential_attack_list.append(queen.static_chess_replace(potential))
                                                self.potential_attack_down_5_coordinate.append(queen.static_chess_replace(potential))
                                                done=1
                                                break

    def potential_attack_down_6(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 4:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 5:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[1] == 6:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-6]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                        potential=board[self.position[0]][board[self.position[0]].index(self.position)-6]
                                                        self.potential_attack_list.append(queen.static_chess_replace(potential))
                                                        self.potential_attack_down_6_coordinate.append(queen.static_chess_replace(potential))
                                                        done=1
                                                        break

    def potential_attack_down_7(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 4:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 5:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[1] == 6:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-6]) and i.occupied==False and self.captured==False:
                                                        for i in square_tuple:
                                                            if done == 1 or self.position[1] == 7:
                                                                break
                                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-7]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                                potential=board[self.position[0]][board[self.position[0]].index(self.position)-7]
                                                                self.potential_attack_list.append(queen.static_chess_replace(potential))
                                                                self.potential_attack_down_7_coordinate.append(queen.static_chess_replace(potential))
                                                                done=1
                                                                break


    def potential_move_right(self):
        for i in square_tuple:
            if self.position[0] == 7:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                potential=board[self.position[0]+1][board[self.position[0]].index(self.position)]
                self.potential_move_list.append(queen.static_chess_replace(potential))
                self.potential_move_right_coordinate.append(queen.static_chess_replace(potential))
                break

    def potential_move_right_2(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[0] == 7:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[0] == 6:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                        potential=board[self.position[0]+2][board[self.position[0]].index(self.position)]
                        self.potential_move_list.append(queen.static_chess_replace(potential))
                        self.potential_move_right_2_coordinate.append(queen.static_chess_replace(potential))
                        done=1
                        break

    def potential_move_right_3(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[0] == 7:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[0] == 6:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[0] == 5:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                potential=board[self.position[0]+3][board[self.position[0]].index(self.position)]
                                self.potential_move_list.append(queen.static_chess_replace(potential))
                                self.potential_move_right_3_coordinate.append(queen.static_chess_replace(potential))
                                done=1
                                break

    def potential_move_right_4(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[0] == 7:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[0] == 6:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[0] == 5:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[0] == 4:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                        potential=board[self.position[0]+4][board[self.position[0]].index(self.position)]
                                        self.potential_move_list.append(queen.static_chess_replace(potential))
                                        self.potential_move_right_4_coordinate.append(queen.static_chess_replace(potential))
                                        done=1
                                        break

    def potential_move_right_5(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[0] == 7:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[0] == 6:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[0] == 5:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[0] == 4:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[0] == 3:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                potential=board[self.position[0]+5][board[self.position[0]].index(self.position)]
                                                self.potential_move_list.append(queen.static_chess_replace(potential))
                                                self.potential_move_right_5_coordinate.append(queen.static_chess_replace(potential))
                                                done=1
                                                break

    def potential_move_right_6(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[0] == 7:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[0] == 6:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[0] == 5:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[0] == 4:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[0] == 3:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[0] == 2:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+6][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                        potential=board[self.position[0]+6][board[self.position[0]].index(self.position)]
                                                        self.potential_move_list.append(queen.static_chess_replace(potential))
                                                        self.potential_move_right_6_coordinate.append(queen.static_chess_replace(potential))
                                                        done=1
                                                        break

    def potential_move_right_7(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[0] == 7:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[0] == 6:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[0] == 5:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[0] == 4:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[0] == 3:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[0] == 2:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+6][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                        for i in square_tuple:
                                                            if done == 1 or self.position[0] == 1:
                                                                break
                                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+7][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                                potential=board[self.position[0]+7][board[self.position[0]].index(self.position)]
                                                                self.potential_move_list.append(queen.static_chess_replace(potential))
                                                                self.potential_move_right_7_coordinate.append(queen.static_chess_replace(potential))
                                                                done=1
                                                                break


    def potential_attack_right(self):
        for i in square_tuple:
            if self.position[0] == 7:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                potential=board[self.position[0]+1][board[self.position[0]].index(self.position)]
                self.potential_attack_list.append(queen.static_chess_replace(potential))
                self.potential_attack_right_coordinate.append(queen.static_chess_replace(potential))
                break

    def potential_attack_right_2(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[0] == 7:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[0] == 6:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                        potential=board[self.position[0]+2][board[self.position[0]].index(self.position)]
                        self.potential_attack_list.append(queen.static_chess_replace(potential))
                        self.potential_attack_right_2_coordinate.append(queen.static_chess_replace(potential))
                        done=1
                        break

    def potential_attack_right_3(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[0] == 7:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[0] == 6:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[0] == 5:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                potential=board[self.position[0]+3][board[self.position[0]].index(self.position)]
                                self.potential_attack_list.append(queen.static_chess_replace(potential))
                                self.potential_attack_right_3_coordinate.append(queen.static_chess_replace(potential))
                                done=1
                                break

    def potential_attack_right_4(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[0] == 7:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[0] == 6:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[0] == 5:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[0] == 4:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                        potential=board[self.position[0]+4][board[self.position[0]].index(self.position)]
                                        self.potential_attack_list.append(queen.static_chess_replace(potential))
                                        self.potential_attack_right_4_coordinate.append(queen.static_chess_replace(potential))
                                        done=1
                                        break

    def potential_attack_right_5(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[0] == 7:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[0] == 6:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[0] == 5:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[0] == 4:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[0] == 3:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                potential=board[self.position[0]+5][board[self.position[0]].index(self.position)]
                                                self.potential_attack_list.append(queen.static_chess_replace(potential))
                                                self.potential_attack_right_5_coordinate.append(queen.static_chess_replace(potential))
                                                done=1
                                                break

    def potential_attack_right_6(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[0] == 7:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[0] == 6:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[0] == 5:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[0] == 4:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[0] == 3:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[0] == 2:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+6][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                        potential=board[self.position[0]+6][board[self.position[0]].index(self.position)]
                                                        self.potential_attack_list.append(queen.static_chess_replace(potential))
                                                        self.potential_attack_right_6_coordinate.append(queen.static_chess_replace(potential))
                                                        done=1
                                                        break

    def potential_attack_right_7(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[0] == 7:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[0] == 6:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[0] == 5:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[0] == 4:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[0] == 3:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[0] == 2:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+6][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                        for i in square_tuple:
                                                            if done == 1 or self.position[0] == 1:
                                                                break
                                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+7][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                                potential=board[self.position[0]+7][board[self.position[0]].index(self.position)]
                                                                self.potential_attack_list.append(queen.static_chess_replace(potential))
                                                                self.potential_attack_right_7_coordinate.append(queen.static_chess_replace(potential))
                                                                done=1
                                                                break


    def potential_move_left(self):
        for i in square_tuple:
            if self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                potential=board[self.position[0]-1][board[self.position[0]].index(self.position)]
                self.potential_move_list.append(queen.static_chess_replace(potential))
                self.potential_move_left_coordinate.append(queen.static_chess_replace(potential))
                break

    def potential_move_left_2(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[0] == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                        potential=board[self.position[0]-2][board[self.position[0]].index(self.position)]
                        self.potential_move_list.append(queen.static_chess_replace(potential))
                        self.potential_move_left_2_coordinate.append(queen.static_chess_replace(potential))
                        done=1
                        break

    def potential_move_left_3(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[0] == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[0] == 2:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                potential=board[self.position[0]-3][board[self.position[0]].index(self.position)]
                                self.potential_move_list.append(queen.static_chess_replace(potential))
                                self.potential_move_left_3_coordinate.append(queen.static_chess_replace(potential))
                                done=1
                                break

    def potential_move_left_4(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[0] == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[0] == 2:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[0] == 3:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                        potential=board[self.position[0]-4][board[self.position[0]].index(self.position)]
                                        self.potential_move_list.append(queen.static_chess_replace(potential))
                                        self.potential_move_left_4_coordinate.append(queen.static_chess_replace(potential))
                                        done=1
                                        break

    def potential_move_left_5(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[0] == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[0] == 2:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[0] == 3:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[0] == 4:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                potential=board[self.position[0]-5][board[self.position[0]].index(self.position)]
                                                self.potential_move_list.append(queen.static_chess_replace(potential))
                                                self.potential_move_left_5_coordinate.append(queen.static_chess_replace(potential))
                                                done=1
                                                break

    def potential_move_left_6(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[0] == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[0] == 2:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[0] == 3:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[0] == 4:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[0] == 5:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-6][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                        potential=board[self.position[0]-6][board[self.position[0]].index(self.position)]
                                                        self.potential_move_list.append(queen.static_chess_replace(potential))
                                                        self.potential_move_left_6_coordinate.append(queen.static_chess_replace(potential))
                                                        done=1
                                                        break

    def potential_move_left_7(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[0] == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[0] == 2:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[0] == 3:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[0] == 4:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[0] == 5:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-6][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                        for i in square_tuple:
                                                            if done == 1 or self.position[0] == 6:
                                                                break
                                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-7][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                                potential=board[self.position[0]-7][board[self.position[0]].index(self.position)]
                                                                self.potential_move_list.append(queen.static_chess_replace(potential))
                                                                self.potential_move_left_7_coordinate.append(queen.static_chess_replace(potential))
                                                                done=1
                                                                break


    def potential_attack_left(self):
        for i in square_tuple:
            if self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                potential=board[self.position[0]-1][board[self.position[0]].index(self.position)]
                self.potential_attack_list.append(queen.static_chess_replace(potential))
                self.potential_attack_left_coordinate.append(queen.static_chess_replace(potential))
                break

    def potential_attack_left_2(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[0] == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                        potential=board[self.position[0]-2][board[self.position[0]].index(self.position)]
                        self.potential_attack_list.append(queen.static_chess_replace(potential))
                        self.potential_attack_left_2_coordinate.append(queen.static_chess_replace(potential))
                        done=1
                        break

    def potential_attack_left_3(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[0] == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[0] == 2:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                potential=board[self.position[0]-3][board[self.position[0]].index(self.position)]
                                self.potential_attack_list.append(queen.static_chess_replace(potential))
                                self.potential_attack_left_3_coordinate.append(queen.static_chess_replace(potential))
                                done=1
                                break

    def potential_attack_left_4(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[0] == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[0] == 2:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[0] == 3:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                        potential=board[self.position[0]-4][board[self.position[0]].index(self.position)]
                                        self.potential_attack_list.append(queen.static_chess_replace(potential))
                                        self.potential_attack_left_4_coordinate.append(queen.static_chess_replace(potential))
                                        done=1
                                        break

    def potential_attack_left_5(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[0] == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[0] == 2:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[0] == 3:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[0] == 4:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                potential=board[self.position[0]-5][board[self.position[0]].index(self.position)]
                                                self.potential_attack_list.append(queen.static_chess_replace(potential))
                                                self.potential_attack_left_5_coordinate.append(queen.static_chess_replace(potential))
                                                done=1
                                                break

    def potential_attack_left_6(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[0] == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[0] == 2:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[0] == 3:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[0] == 4:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[0] == 5:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-6][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                        potential=board[self.position[0]-6][board[self.position[0]].index(self.position)]
                                                        self.potential_attack_list.append(queen.static_chess_replace(potential))
                                                        self.potential_attack_left_6_coordinate.append(queen.static_chess_replace(potential))
                                                        done=1
                                                        break

    def potential_attack_left_7(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[0] == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[0] == 2:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[0] == 3:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[0] == 4:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[0] == 5:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-6][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                        for i in square_tuple:
                                                            if done == 1 or self.position[0] == 6:
                                                                break
                                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-7][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                                potential=board[self.position[0]-7][board[self.position[0]].index(self.position)]
                                                                self.potential_attack_list.append(queen.static_chess_replace(potential))
                                                                self.potential_attack_left_7_coordinate.append(queen.static_chess_replace(potential))
                                                                done=1
                                                                break


    def potential_move_up_right(self):
        for i in square_tuple:
            if self.position[1] == 8 or self.position[0] == 7:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and i.occupied==False and self.captured==False:
                potential=board[self.position[0]+1][board[self.position[0]].index(self.position)+1]
                self.potential_move_list.append(queen.static_chess_replace(potential))
                self.potential_move_up_right_coordinate.append(queen.static_chess_replace(potential))
                break

    def potential_move_up_right_2(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8 or self.position[0] == 7:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7 or self.position[0] == 6:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)+2]) and i.occupied==False and self.captured==False:
                        potential=board[self.position[0]+2][board[self.position[0]].index(self.position)+2]
                        self.potential_move_list.append(queen.static_chess_replace(potential))
                        self.potential_move_up_right_2_coordinate.append(queen.static_chess_replace(potential))
                        done=1
                        break

    def potential_move_up_right_3(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8 or self.position[0] == 7:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7 or self.position[0] == 6:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6 or self.position[0] == 5:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)+3]) and i.occupied==False and self.captured==False:
                                potential=board[self.position[0]+3][board[self.position[0]].index(self.position)+3]
                                self.potential_move_list.append(queen.static_chess_replace(potential))
                                self.potential_move_up_right_3_coordinate.append(queen.static_chess_replace(potential))
                                done=1
                                break

    def potential_move_up_right_4(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8 or self.position[0] == 7:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7 or self.position[0] == 6:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6 or self.position[0] == 5:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 5 or self.position[0] == 4:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)+4]) and i.occupied==False and self.captured==False:
                                        potential=board[self.position[0]+4][board[self.position[0]].index(self.position)+4]
                                        self.potential_move_list.append(queen.static_chess_replace(potential))
                                        self.potential_move_up_right_4_coordinate.append(queen.static_chess_replace(potential))
                                        done=1
                                        break

    def potential_move_up_right_5(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8 or self.position[0] == 7:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7 or self.position[0] == 6:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6 or self.position[0] == 5:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 5 or self.position[0] == 4:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 4 or self.position[0] == 3:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)+5]) and i.occupied==False and self.captured==False:
                                                potential=board[self.position[0]+5][board[self.position[0]].index(self.position)+5]
                                                self.potential_move_list.append(queen.static_chess_replace(potential))
                                                self.potential_move_up_right_5_coordinate.append(queen.static_chess_replace(potential))
                                                done=1
                                                break

    def potential_move_up_right_6(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8 or self.position[0] == 7:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7 or self.position[0] == 6:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6 or self.position[0] == 5:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 5 or self.position[0] == 4:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 4 or self.position[0] == 3:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)+5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[1] == 3 or self.position[0] == 2:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+6][board[self.position[0]].index(self.position)+6]) and i.occupied==False and self.captured==False:
                                                        potential=board[self.position[0]+6][board[self.position[0]].index(self.position)+6]
                                                        self.potential_move_list.append(queen.static_chess_replace(potential))
                                                        self.potential_move_up_right_6_coordinate.append(queen.static_chess_replace(potential))
                                                        done=1
                                                        break

    def potential_move_up_right_7(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8 or self.position[0] == 7:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7 or self.position[0] == 6:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6 or self.position[0] == 5:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 5 or self.position[0] == 4:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 4 or self.position[0] == 3:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)+5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[1] == 3 or self.position[0] == 2:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+6][board[self.position[0]].index(self.position)+6]) and i.occupied==False and self.captured==False:
                                                        for i in square_tuple:
                                                            if done == 1 or self.position[1] == 2 or self.position[0] == 1:
                                                                break
                                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+7][board[self.position[0]].index(self.position)+7]) and i.occupied==False and self.captured==False:
                                                                potential=board[self.position[0]+7][board[self.position[0]].index(self.position)+7]
                                                                self.potential_move_list.append(queen.static_chess_replace(potential))
                                                                self.potential_move_up_right_7_coordinate.append(queen.static_chess_replace(potential))
                                                                done=1
                                                                break


    def potential_attack_up_right(self):
        for i in square_tuple:
            if self.position[1] == 8 or self.position[0] == 7:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                potential=board[self.position[0]+1][board[self.position[0]].index(self.position)+1]
                self.potential_attack_list.append(queen.static_chess_replace(potential))
                self.potential_attack_up_right_coordinate.append(queen.static_chess_replace(potential))
                break

    def potential_attack_up_right_2(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8 or self.position[0] == 7:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7 or self.position[0] == 6:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)+2]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                        potential=board[self.position[0]+2][board[self.position[0]].index(self.position)+2]
                        self.potential_attack_list.append(queen.static_chess_replace(potential))
                        self.potential_attack_up_right_2_coordinate.append(queen.static_chess_replace(potential))
                        done=1
                        break

    def potential_attack_up_right_3(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8 or self.position[0] == 7:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7 or self.position[0] == 6:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6 or self.position[0] == 5:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)+3]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                potential=board[self.position[0]+3][board[self.position[0]].index(self.position)+3]
                                self.potential_attack_list.append(queen.static_chess_replace(potential))
                                self.potential_attack_up_right_3_coordinate.append(queen.static_chess_replace(potential))
                                done=1
                                break

    def potential_attack_up_right_4(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8 or self.position[0] == 7:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7 or self.position[0] == 6:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6 or self.position[0] == 5:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 5 or self.position[0] == 4:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)+4]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                        potential=board[self.position[0]+4][board[self.position[0]].index(self.position)+4]
                                        self.potential_attack_list.append(queen.static_chess_replace(potential))
                                        self.potential_attack_up_right_4_coordinate.append(queen.static_chess_replace(potential))
                                        done=1
                                        break

    def potential_attack_up_right_5(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8 or self.position[0] == 7:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7 or self.position[0] == 6:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6 or self.position[0] == 5:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 5 or self.position[0] == 4:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 4 or self.position[0] == 3:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)+5]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                potential=board[self.position[0]+5][board[self.position[0]].index(self.position)+5]
                                                self.potential_attack_list.append(queen.static_chess_replace(potential))
                                                self.potential_attack_up_right_5_coordinate.append(queen.static_chess_replace(potential))
                                                done=1
                                                break

    def potential_attack_up_right_6(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8 or self.position[0] == 7:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7 or self.position[0] == 6:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6 or self.position[0] == 5:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 5 or self.position[0] == 4:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 4 or self.position[0] == 3:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)+5]) and i.occupied==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[1] == 3 or self.position[0] == 2:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+6][board[self.position[0]].index(self.position)+6]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                        potential=board[self.position[0]+6][board[self.position[0]].index(self.position)+6]
                                                        self.potential_attack_list.append(queen.static_chess_replace(potential))
                                                        self.potential_attack_up_right_6_coordinate.append(queen.static_chess_replace(potential))
                                                        done=1
                                                        break

    def potential_attack_up_right_7(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8 or self.position[0] == 7:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7 or self.position[0] == 6:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6 or self.position[0] == 5:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 5 or self.position[0] == 4:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 4 or self.position[0] == 3:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)+5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[1] == 3 or self.position[0] == 2:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+6][board[self.position[0]].index(self.position)+6]) and i.occupied==False and self.captured==False:
                                                        for i in square_tuple:
                                                            if done == 1 or self.position[1] == 2 or self.position[0] == 1:
                                                                break
                                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+7][board[self.position[0]].index(self.position)+7]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                                potential=board[self.position[0]+7][board[self.position[0]].index(self.position)+7]
                                                                self.potential_attack_list.append(queen.static_chess_replace(potential))
                                                                self.potential_attack_up_right_7_coordinate.append(queen.static_chess_replace(potential))
                                                                done=1
                                                                break


    def potential_move_up_left(self):
        for i in square_tuple:
            if self.position[1] == 8 or self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and i.occupied==False and self.captured==False:
                potential=board[self.position[0]-1][board[self.position[0]].index(self.position)+1]
                self.potential_move_list.append(queen.static_chess_replace(potential))
                self.potential_move_up_left_coordinate.append(queen.static_chess_replace(potential))
                break

    def potential_move_up_left_2(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8 or self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7 or self.position[0] == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)+2]) and i.occupied==False and self.captured==False:
                        potential=board[self.position[0]-2][board[self.position[0]].index(self.position)+2]
                        self.potential_move_list.append(queen.static_chess_replace(potential))
                        self.potential_move_up_left_2_coordinate.append(queen.static_chess_replace(potential))
                        done=1
                        break

    def potential_move_up_left_3(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8 or self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7 or self.position[0] == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6 or self.position[0] == 2:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)+3]) and i.occupied==False and self.captured==False:
                                potential=board[self.position[0]-3][board[self.position[0]].index(self.position)+3]
                                self.potential_move_list.append(queen.static_chess_replace(potential))
                                self.potential_move_up_left_3_coordinate.append(queen.static_chess_replace(potential))
                                done=1
                                break

    def potential_move_up_left_4(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8 or self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7 or self.position[0] == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6 or self.position[0] == 2:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 5 or self.position[0] == 3:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)+4]) and i.occupied==False and self.captured==False:
                                        potential=board[self.position[0]-4][board[self.position[0]].index(self.position)+4]
                                        self.potential_move_list.append(queen.static_chess_replace(potential))
                                        self.potential_move_up_left_4_coordinate.append(queen.static_chess_replace(potential))
                                        done=1
                                        break

    def potential_move_up_left_5(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8 or self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7 or self.position[0] == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6 or self.position[0] == 2:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 5 or self.position[0] == 3:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 4 or self.position[0] == 4:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)+5]) and i.occupied==False and self.captured==False:
                                                potential=board[self.position[0]-5][board[self.position[0]].index(self.position)+5]
                                                self.potential_move_list.append(queen.static_chess_replace(potential))
                                                self.potential_move_up_left_5_coordinate.append(queen.static_chess_replace(potential))
                                                done=1
                                                break

    def potential_move_up_left_6(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8 or self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7 or self.position[0] == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6 or self.position[0] == 2:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 5 or self.position[0] == 3:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 4 or self.position[0] == 4:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)+5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[1] == 3 or self.position[0] == 5:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-6][board[self.position[0]].index(self.position)+6]) and i.occupied==False and self.captured==False:
                                                        potential=board[self.position[0]-6][board[self.position[0]].index(self.position)+6]
                                                        self.potential_move_list.append(queen.static_chess_replace(potential))
                                                        self.potential_move_up_left_6_coordinate.append(queen.static_chess_replace(potential))
                                                        done=1
                                                        break

    def potential_move_up_left_7(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8 or self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7 or self.position[0] == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6 or self.position[0] == 2:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 5 or self.position[0] == 3:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 4 or self.position[0] == 4:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)+5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[1] == 3 or self.position[0] == 5:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-6][board[self.position[0]].index(self.position)+6]) and i.occupied==False and self.captured==False:
                                                        for i in square_tuple:
                                                            if done == 1 or self.position[1] == 2 or self.position[0] == 6:
                                                                break
                                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-7][board[self.position[0]].index(self.position)+7]) and i.occupied==False and self.captured==False:
                                                                potential=board[self.position[0]-7][board[self.position[0]].index(self.position)+7]
                                                                self.potential_move_list.append(queen.static_chess_replace(potential))
                                                                self.potential_move_up_left_7_coordinate.append(queen.static_chess_replace(potential))
                                                                done=1
                                                                break


    def potential_attack_up_left(self):
        for i in square_tuple:
            if self.position[1] == 8 or self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                potential=board[self.position[0]-1][board[self.position[0]].index(self.position)+1]
                self.potential_attack_list.append(queen.static_chess_replace(potential))
                self.potential_attack_up_left_coordinate.append(queen.static_chess_replace(potential))
                break

    def potential_attack_up_left_2(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8 or self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7 or self.position[0] == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)+2]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                        potential=board[self.position[0]-2][board[self.position[0]].index(self.position)+2]
                        self.potential_attack_list.append(queen.static_chess_replace(potential))
                        self.potential_attack_up_left_2_coordinate.append(queen.static_chess_replace(potential))
                        done=1
                        break

    def potential_attack_up_left_3(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8 or self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7 or self.position[0] == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6 or self.position[0] == 2:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)+3]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                potential=board[self.position[0]-3][board[self.position[0]].index(self.position)+3]
                                self.potential_attack_list.append(queen.static_chess_replace(potential))
                                self.potential_attack_up_left_3_coordinate.append(queen.static_chess_replace(potential))
                                done=1
                                break

    def potential_attack_up_left_4(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8 or self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7 or self.position[0] == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6 or self.position[0] == 2:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 5 or self.position[0] == 3:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)+4]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                        potential=board[self.position[0]-4][board[self.position[0]].index(self.position)+4]
                                        self.potential_attack_list.append(queen.static_chess_replace(potential))
                                        self.potential_attack_up_left_4_coordinate.append(queen.static_chess_replace(potential))
                                        done=1
                                        break

    def potential_attack_up_left_5(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8 or self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7 or self.position[0] == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6 or self.position[0] == 2:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 5 or self.position[0] == 3:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 4 or self.position[0] == 4:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)+5]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                potential=board[self.position[0]-5][board[self.position[0]].index(self.position)+5]
                                                self.potential_attack_list.append(queen.static_chess_replace(potential))
                                                self.potential_attack_up_left_5_coordinate.append(queen.static_chess_replace(potential))
                                                done=1
                                                break

    def potential_attack_up_left_6(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8 or self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7 or self.position[0] == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6 or self.position[0] == 2:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 5 or self.position[0] == 3:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 4 or self.position[0] == 4:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)+5]) and i.occupied==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[1] == 3 or self.position[0] == 5:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-6][board[self.position[0]].index(self.position)+6]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                        potential=board[self.position[0]-6][board[self.position[0]].index(self.position)+6]
                                                        self.potential_attack_list.append(queen.static_chess_replace(potential))
                                                        self.potential_attack_up_left_6_coordinate.append(queen.static_chess_replace(potential))
                                                        done=1
                                                        break

    def potential_attack_up_left_7(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8 or self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7 or self.position[0] == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6 or self.position[0] == 2:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 5 or self.position[0] == 3:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 4 or self.position[0] == 4:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)+5]) and i.occupied==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[1] == 3 or self.position[0] == 5:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-6][board[self.position[0]].index(self.position)+6]) and i.occupied==False:
                                                        for i in square_tuple:
                                                            if done == 1 or self.position[1] == 2 or self.position[0] == 6:
                                                                break
                                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-7][board[self.position[0]].index(self.position)+7]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                                potential=board[self.position[0]-7][board[self.position[0]].index(self.position)+7]
                                                                self.potential_attack_list.append(queen.static_chess_replace(potential))
                                                                self.potential_attack_up_left_7_coordinate.append(queen.static_chess_replace(potential))
                                                                done=1
                                                                break


    def potential_move_down_left(self):
        for i in square_tuple:
            if self.position[1] == 1 or self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and i.occupied==False and self.captured==False:
                potential=board[self.position[0]-1][board[self.position[0]].index(self.position)-1]
                self.potential_move_list.append(queen.static_chess_replace(potential))
                self.potential_move_down_left_coordinate.append(queen.static_chess_replace(potential))
                break

    def potential_move_down_left_2(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1 or self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2 or self.position[0] == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)-2]) and i.occupied==False and self.captured==False:
                        potential=board[self.position[0]-2][board[self.position[0]].index(self.position)-2]
                        self.potential_move_list.append(queen.static_chess_replace(potential))
                        self.potential_move_down_left_2_coordinate.append(queen.static_chess_replace(potential))
                        done=1
                        break

    def potential_move_down_left_3(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1 or self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2 or self.position[0] == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3 or self.position[0] == 2:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)-3]) and i.occupied==False and self.captured==False:
                                potential=board[self.position[0]-3][board[self.position[0]].index(self.position)-3]
                                self.potential_move_list.append(queen.static_chess_replace(potential))
                                self.potential_move_down_left_3_coordinate.append(queen.static_chess_replace(potential))
                                done=1
                                break

    def potential_move_down_left_4(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1 or self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2 or self.position[0] == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3 or self.position[0] == 2:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 4 or self.position[0] == 3:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)-4]) and i.occupied==False and self.captured==False:
                                        potential=board[self.position[0]-4][board[self.position[0]].index(self.position)-4]
                                        self.potential_move_list.append(queen.static_chess_replace(potential))
                                        self.potential_move_down_left_4_coordinate.append(queen.static_chess_replace(potential))
                                        done=1
                                        break

    def potential_move_down_left_5(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1 or self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2 or self.position[0] == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3 or self.position[0] == 2:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 4 or self.position[0] == 3:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 5 or self.position[0] == 4:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)-5]) and i.occupied==False and self.captured==False:
                                                potential=board[self.position[0]-5][board[self.position[0]].index(self.position)-5]
                                                self.potential_move_list.append(queen.static_chess_replace(potential))
                                                self.potential_move_down_left_5_coordinate.append(queen.static_chess_replace(potential))
                                                done=1
                                                break

    def potential_move_down_left_6(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1 or self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2 or self.position[0] == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3 or self.position[0] == 2:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 4 or self.position[0] == 3:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 5 or self.position[0] == 4:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)-5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[1] == 6 or self.position[0] == 5:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-6][board[self.position[0]].index(self.position)-6]) and i.occupied==False and self.captured==False:
                                                        potential=board[self.position[0]-6][board[self.position[0]].index(self.position)-6]
                                                        self.potential_move_list.append(queen.static_chess_replace(potential))
                                                        self.potential_move_down_left_6_coordinate.append(queen.static_chess_replace(potential))
                                                        done=1
                                                        break

    def potential_move_down_left_7(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1 or self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2 or self.position[0] == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3 or self.position[0] == 2:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 4 or self.position[0] == 3:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 5 or self.position[0] == 4:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)-5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[1] == 6 or self.position[0] == 5:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-6][board[self.position[0]].index(self.position)-6]) and i.occupied==False and self.captured==False:
                                                        for i in square_tuple:
                                                            if done == 1 or self.position[1] == 7 or self.position[0] == 6:
                                                                break
                                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-7][board[self.position[0]].index(self.position)-7]) and i.occupied==False and self.captured==False:
                                                                potential=board[self.position[0]-7][board[self.position[0]].index(self.position)-7]
                                                                self.potential_move_list.append(queen.static_chess_replace(potential))
                                                                self.potential_move_down_left_7_coordinate.append(queen.static_chess_replace(potential))
                                                                done=1
                                                                break



    def potential_attack_down_left(self):
        for i in square_tuple:
            if self.position[1] == 1 or self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                potential=board[self.position[0]-1][board[self.position[0]].index(self.position)-1]
                self.potential_attack_list.append(queen.static_chess_replace(potential))
                self.potential_attack_down_left_coordinate.append(queen.static_chess_replace(potential))
                break

    def potential_attack_down_left_2(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1 or self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2 or self.position[0] == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)-2]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                        potential=board[self.position[0]-2][board[self.position[0]].index(self.position)-2]
                        self.potential_attack_list.append(queen.static_chess_replace(potential))
                        self.potential_attack_down_left_2_coordinate.append(queen.static_chess_replace(potential))
                        done=1
                        break

    def potential_attack_down_left_3(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1 or self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2 or self.position[0] == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3 or self.position[0] == 2:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)-3]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                potential=board[self.position[0]-3][board[self.position[0]].index(self.position)-3]
                                self.potential_attack_list.append(queen.static_chess_replace(potential))
                                self.potential_attack_down_left_3_coordinate.append(queen.static_chess_replace(potential))
                                done=1
                                break

    def potential_attack_down_left_4(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1 or self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2 or self.position[0] == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3 or self.position[0] == 2:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 4 or self.position[0] == 3:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)-4]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                        potential=board[self.position[0]-4][board[self.position[0]].index(self.position)-4]
                                        self.potential_attack_list.append(queen.static_chess_replace(potential))
                                        self.potential_attack_down_left_4_coordinate.append(queen.static_chess_replace(potential))
                                        done=1
                                        break

    def potential_attack_down_left_5(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1 or self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2 or self.position[0] == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3 or self.position[0] == 2:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 4 or self.position[0] == 3:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 5 or self.position[0] == 4:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)-5]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                potential=board[self.position[0]-5][board[self.position[0]].index(self.position)-5]
                                                self.potential_attack_list.append(queen.static_chess_replace(potential))
                                                self.potential_attack_down_left_5_coordinate.append(queen.static_chess_replace(potential))
                                                done=1
                                                break

    def potential_attack_down_left_6(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1 or self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2 or self.position[0] == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3 or self.position[0] == 2:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 4 or self.position[0] == 3:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 5 or self.position[0] == 4:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)-5]) and i.occupied==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[1] == 6 or self.position[0] == 5:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-6][board[self.position[0]].index(self.position)-6]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                        potential=board[self.position[0]-6][board[self.position[0]].index(self.position)-6]
                                                        self.potential_attack_list.append(queen.static_chess_replace(potential))
                                                        self.potential_attack_down_left_6_coordinate.append(queen.static_chess_replace(potential))
                                                        done=1
                                                        break

    def potential_attack_down_left_7(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1 or self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2 or self.position[0] == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3 or self.position[0] == 2:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 4 or self.position[0] == 3:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 5 or self.position[0] == 4:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)-5]) and i.occupied==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[1] == 6 or self.position[0] == 5:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-6][board[self.position[0]].index(self.position)-6]) and i.occupied==False:
                                                        for i in square_tuple:
                                                            if done == 1 or self.position[1] == 7 or self.position[0] == 6:
                                                                break
                                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-7][board[self.position[0]].index(self.position)-7]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                                potential=board[self.position[0]-7][board[self.position[0]].index(self.position)-7]
                                                                self.potential_attack_list.append(queen.static_chess_replace(potential))
                                                                self.potential_attack_down_left_7_coordinate.append(queen.static_chess_replace(potential))
                                                                done=1
                                                                break


    def potential_move_down_right(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1 or self.position[0] == 7:
                break
            #print("test2")
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and i.occupied==False and self.captured==False:
                potential=board[self.position[0]+1][board[self.position[0]].index(self.position)-1]
                self.potential_move_list.append(queen.static_chess_replace(potential))
                self.potential_move_down_right_coordinate.append(queen.static_chess_replace(potential))
                done=1
                break

    def potential_move_down_right_2(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1 or self.position[0] == 7:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 2 or self.position[1] == 2 or self.position[0] == 6:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)-2]) and i.occupied==False and self.captured==False:
                        potential=board[self.position[0]+2][board[self.position[0]].index(self.position)-2]
                        self.potential_move_list.append(queen.static_chess_replace(potential))
                        self.potential_move_down_right_2_coordinate.append(queen.static_chess_replace(potential))
                        done=1
                        break

    def potential_move_down_right_3(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1 or self.position[0] == 7:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2 or self.position[0] == 6:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3 or self.position[0] == 5:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)-3]) and i.occupied==False and self.captured==False:
                                potential=board[self.position[0]+3][board[self.position[0]].index(self.position)-3]
                                self.potential_move_list.append(queen.static_chess_replace(potential))
                                self.potential_move_down_right_3_coordinate.append(queen.static_chess_replace(potential))
                                done=1
                                break

    def potential_move_down_right_4(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1 or self.position[0] == 7:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2 or self.position[0] == 6:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3 or self.position[0] == 5:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 4 or self.position[0] == 4:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)-4]) and i.occupied==False and self.captured==False:
                                        potential=board[self.position[0]+4][board[self.position[0]].index(self.position)-4]
                                        self.potential_move_list.append(queen.static_chess_replace(potential))
                                        self.potential_move_down_right_4_coordinate.append(queen.static_chess_replace(potential))
                                        done=1
                                        break

    def potential_move_down_right_5(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1 or self.position[0] == 7:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2 or self.position[0] == 6:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3 or self.position[0] == 5:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 4 or self.position[0] == 4:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 5 or self.position[0] == 3:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)-5]) and i.occupied==False and self.captured==False:
                                                potential=board[self.position[0]+5][board[self.position[0]].index(self.position)-5]
                                                self.potential_move_list.append(queen.static_chess_replace(potential))
                                                self.potential_move_down_right_5_coordinate.append(queen.static_chess_replace(potential))
                                                done=1
                                                break

    def potential_move_down_right_6(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1 or self.position[0] == 7:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2 or self.position[0] == 6:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3 or self.position[0] == 5:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 4 or self.position[0] == 4:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 5 or self.position[0] == 3:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)-5]) and i.occupied==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[1] == 6 or self.position[0] == 2:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+6][board[self.position[0]].index(self.position)-6]) and i.occupied==False and self.captured==False:
                                                        potential=board[self.position[0]+6][board[self.position[0]].index(self.position)-6]
                                                        self.potential_move_list.append(queen.static_chess_replace(potential))
                                                        self.potential_move_down_right_6_coordinate.append(queen.static_chess_replace(potential))
                                                        done=1
                                                        break

    def potential_move_down_right_7(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1 or self.position[0] == 7:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2 or self.position[0] == 6:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3 or self.position[0] == 5:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 4 or self.position[0] == 4:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 5 or self.position[0] == 3:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)-5]) and i.occupied==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[1] == 6 or self.position[0] == 2:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+6][board[self.position[0]].index(self.position)-6]) and i.occupied==False:
                                                        for i in square_tuple:
                                                            if done == 1 or self.position[1] == 7 or self.position[0] == 1:
                                                                break
                                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+7][board[self.position[0]].index(self.position)-7]) and i.occupied==False and self.captured==False:
                                                                potential=board[self.position[0]+7][board[self.position[0]].index(self.position)-7]
                                                                self.potential_move_list.append(queen.static_chess_replace(potential))
                                                                self.potential_move_down_right_7_coordinate.append(queen.static_chess_replace(potential))
                                                                done=1
                                                                break


    def potential_attack_down_right(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1 or self.position[0] == 7:
                break
            #print("test2")
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                potential=board[self.position[0]+1][board[self.position[0]].index(self.position)-1]
                self.potential_attack_list.append(queen.static_chess_replace(potential))
                self.potential_attack_down_right_coordinate.append(queen.static_chess_replace(potential))
                done=1
                break

    def potential_attack_down_right_2(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1 or self.position[0] == 7:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 2 or self.position[1] == 2 or self.position[0] == 6:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)-2]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                        potential=board[self.position[0]+2][board[self.position[0]].index(self.position)-2]
                        self.potential_attack_list.append(queen.static_chess_replace(potential))
                        self.potential_attack_down_right_2_coordinate.append(queen.static_chess_replace(potential))
                        done=1
                        break

    def potential_attack_down_right_3(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1 or self.position[0] == 7:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2 or self.position[0] == 6:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3 or self.position[0] == 5:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)-3]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                potential=board[self.position[0]+3][board[self.position[0]].index(self.position)-3]
                                self.potential_attack_list.append(queen.static_chess_replace(potential))
                                self.potential_attack_down_right_3_coordinate.append(queen.static_chess_replace(potential))
                                done=1
                                break

    def potential_attack_down_right_4(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1 or self.position[0] == 7:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2 or self.position[0] == 6:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3 or self.position[0] == 5:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 4 or self.position[0] == 4:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)-4]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                        potential=board[self.position[0]+4][board[self.position[0]].index(self.position)-4]
                                        self.potential_attack_list.append(queen.static_chess_replace(potential))
                                        self.potential_attack_down_right_4_coordinate.append(queen.static_chess_replace(potential))
                                        done=1
                                        break

    def potential_attack_down_right_5(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1 or self.position[0] == 7:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2 or self.position[0] == 6:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3 or self.position[0] == 5:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 4 or self.position[0] == 4:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 5 or self.position[0] == 3:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)-5]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                potential=board[self.position[0]+5][board[self.position[0]].index(self.position)-5]
                                                self.potential_attack_list.append(queen.static_chess_replace(potential))
                                                self.potential_attack_down_right_5_coordinate.append(queen.static_chess_replace(potential))
                                                done=1
                                                break

    def potential_attack_down_right_6(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1 or self.position[0] == 7:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2 or self.position[0] == 6:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3 or self.position[0] == 5:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 4 or self.position[0] == 4:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 5 or self.position[0] == 3:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)-5]) and i.occupied==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[1] == 6 or self.position[0] == 2:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+6][board[self.position[0]].index(self.position)-6]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                        potential=board[self.position[0]+6][board[self.position[0]].index(self.position)-6]
                                                        self.potential_attack_list.append(queen.static_chess_replace(potential))
                                                        self.potential_attack_down_right_6_coordinate.append(queen.static_chess_replace(potential))
                                                        done=1
                                                        break

    def potential_attack_down_right_7(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1 or self.position[0] == 7:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2 or self.position[0] == 6:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3 or self.position[0] == 5:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 4 or self.position[0] == 4:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 5 or self.position[0] == 3:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)-5]) and i.occupied==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[1] == 6 or self.position[0] == 2:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+6][board[self.position[0]].index(self.position)-6]) and i.occupied==False:
                                                        for i in square_tuple:
                                                            if done == 1 or self.position[1] == 7 or self.position[0] == 1:
                                                                break
                                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+7][board[self.position[0]].index(self.position)-7]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                                potential=board[self.position[0]+7][board[self.position[0]].index(self.position)-7]
                                                                self.potential_attack_list.append(queen.static_chess_replace(potential))
                                                                self.potential_attack_down_right_7_coordinate.append(queen.static_chess_replace(potential))
                                                                done=1
                                                                break



    @staticmethod
    def list_replace(list,remove,add):
        list_copy=list.copy()
        for i in list_copy:
            if i== remove:
                list_copy.remove(i)
                list_copy.insert(0,add)
                return list_copy

    def chess_replace(self):
        self.position_chess=self.position.copy()
        if self.position_chess[0] == 0:
            return self.list_replace(self.position_chess,0,"a")
        if self.position_chess[0] == 1:
            return self.list_replace(self.position_chess,1,"b")
        if self.position_chess[0] == 2:
            return self.list_replace(self.position_chess,2,"c")
        if self.position_chess[0] == 3:
            return self.list_replace(self.position_chess,3,"d")
        if self.position_chess[0] == 4:
            return self.list_replace(self.position_chess,4,"e")
        if self.position_chess[0] == 5:
            return self.list_replace(self.position_chess,5,"f")
        if self.position_chess[0] == 6:
            return self.list_replace(self.position_chess,6,"g")
        if self.position_chess[0] == 7:
            return self.list_replace(self.position_chess,7,"h")

    @staticmethod
    def static_chess_replace(coord):
            if coord[0] == 0:
                return queen.list_replace(coord,0,"a")
            if coord[0] == 1:
                return queen.list_replace(coord,1,"b")
            if coord[0] == 2:
                return queen.list_replace(coord,2,"c")
            if coord[0] == 3:
                return queen.list_replace(coord,3,"d")
            if coord[0] == 4:
                return queen.list_replace(coord,4,"e")
            if coord[0] == 5:
                return queen.list_replace(coord,5,"f")
            if coord[0] == 6:
                return queen.list_replace(coord,6,"g")
            if coord[0] == 7:
                return queen.list_replace(coord,7,"h")

class rook:

    def __init__(self,position,has_moved,captured,piece_type,colour):
        self.position = position
        self.has_moved = has_moved
        self.position_chess=self.position.copy()
        self.captured=captured
        self.piece_type=piece_type
        self.selected=False
        self.colour=colour
        self.potential_attack_list = []
        self.potential_move_list = []
        self.potential_move_up_7_coordinate = []
        self.potential_move_up_6_coordinate = []
        self.potential_move_up_5_coordinate = []
        self.potential_move_up_4_coordinate = []
        self.potential_move_up_3_coordinate = []
        self.potential_move_up_2_coordinate = []
        self.potential_move_up_coordinate = []
        self.potential_attack_up_7_coordinate = []
        self.potential_attack_up_6_coordinate = []
        self.potential_attack_up_5_coordinate = []
        self.potential_attack_up_4_coordinate = []
        self.potential_attack_up_3_coordinate = []
        self.potential_attack_up_2_coordinate = []
        self.potential_attack_up_coordinate = []
        self.potential_move_down_7_coordinate = []
        self.potential_move_down_6_coordinate = []
        self.potential_move_down_5_coordinate = []
        self.potential_move_down_4_coordinate = []
        self.potential_move_down_3_coordinate = []
        self.potential_move_down_2_coordinate = []
        self.potential_move_down_coordinate = []
        self.potential_attack_down_7_coordinate = []
        self.potential_attack_down_6_coordinate = []
        self.potential_attack_down_5_coordinate = []
        self.potential_attack_down_4_coordinate = []
        self.potential_attack_down_3_coordinate = []
        self.potential_attack_down_2_coordinate = []
        self.potential_attack_down_coordinate = []
        self.potential_move_right_7_coordinate = []
        self.potential_move_right_6_coordinate = []
        self.potential_move_right_5_coordinate = []
        self.potential_move_right_4_coordinate = []
        self.potential_move_right_3_coordinate = []
        self.potential_move_right_2_coordinate = []
        self.potential_move_right_coordinate = []
        self.potential_attack_right_7_coordinate = []
        self.potential_attack_right_6_coordinate = []
        self.potential_attack_right_5_coordinate = []
        self.potential_attack_right_4_coordinate = []
        self.potential_attack_right_3_coordinate = []
        self.potential_attack_right_2_coordinate = []
        self.potential_attack_right_coordinate = []
        self.potential_move_left_7_coordinate = []
        self.potential_move_left_6_coordinate = []
        self.potential_move_left_5_coordinate = []
        self.potential_move_left_4_coordinate = []
        self.potential_move_left_3_coordinate = []
        self.potential_move_left_2_coordinate = []
        self.potential_move_left_coordinate = []
        self.potential_attack_left_7_coordinate = []
        self.potential_attack_left_6_coordinate = []
        self.potential_attack_left_5_coordinate = []
        self.potential_attack_left_4_coordinate = []
        self.potential_attack_left_3_coordinate = []
        self.potential_attack_left_2_coordinate = []
        self.potential_attack_left_coordinate = []

    def move_up(self):
        for i in square_tuple:
            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False and self.captured==False:
                self.position=board[self.position[0]][board[self.position[0]].index(self.position)+1]
                self.has_moved=True
                break

    def move_up_2(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                done = 0
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+2]) and i.occupied==False and self.captured==False:
                        self.position=board[self.position[0]][board[self.position[0]].index(self.position)+2]
                        self.has_moved=True
                        done=1
                        break

    def move_up_3(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+3]) and i.occupied==False and self.captured==False:
                                self.position=board[self.position[0]][board[self.position[0]].index(self.position)+3]
                                self.has_moved=True
                                done=1
                                break

    def move_up_4(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+4]) and i.occupied==False and self.captured==False:
                                        self.position=board[self.position[0]][board[self.position[0]].index(self.position)+4]
                                        print(self.position)
                                        self.has_moved=True
                                        self.has_moved=True
                                        done=1
                                        break

    def move_up_5(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+5]) and i.occupied==False and self.captured==False:
                                                print(self.position)
                                                self.position=board[self.position[0]][board[self.position[0]].index(self.position)+5]
                                                self.has_moved=True
                                                done=1
                                                break

    def move_up_6(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+6]) and i.occupied==False and self.captured==False:
                                                        self.position=board[self.position[0]][board[self.position[0]].index(self.position)+6]
                                                        self.has_moved=True
                                                        done=1
                                                        break

    def move_up_7(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+6]) and i.occupied==False and self.captured==False:
                                                        for i in square_tuple:
                                                            if done == 1:
                                                                break
                                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+7]) and i.occupied==False and self.captured==False:
                                                                self.position=board[self.position[0]][board[self.position[0]].index(self.position)+7]
                                                                self.has_moved=True
                                                                done=1
                                                                break

    def move_down(self):
        for i in square_tuple:
            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False and self.captured==False:
                self.position=board[self.position[0]][board[self.position[0]].index(self.position)-1]
                self.has_moved=True
                break

    def move_down_2(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                done = 0
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-2]) and i.occupied==False and self.captured==False:
                        self.position=board[self.position[0]][board[self.position[0]].index(self.position)-2]
                        self.has_moved=True
                        done=1
                        break

    def move_down_3(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-3]) and i.occupied==False and self.captured==False:
                                self.position=board[self.position[0]][board[self.position[0]].index(self.position)-3]
                                self.has_moved=True
                                done=1
                                break

    def move_down_4(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-4]) and i.occupied==False and self.captured==False:
                                        self.position=board[self.position[0]][board[self.position[0]].index(self.position)-4]
                                        self.has_moved=True
                                        self.has_moved=True
                                        done=1
                                        break

    def move_down_5(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-5]) and i.occupied==False and self.captured==False:
                                                self.position=board[self.position[0]][board[self.position[0]].index(self.position)-5]
                                                self.has_moved=True
                                                done=1
                                                break

    def move_down_6(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-6]) and i.occupied==False and self.captured==False:
                                                        self.position=board[self.position[0]][board[self.position[0]].index(self.position)-6]
                                                        self.has_moved=True
                                                        done=1
                                                        break

    def move_down_7(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-6]) and i.occupied==False and self.captured==False:
                                                        for i in square_tuple:
                                                            if done == 1:
                                                                break
                                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-7]) and i.occupied==False and self.captured==False:
                                                                self.position=board[self.position[0]][board[self.position[0]].index(self.position)-7]
                                                                self.has_moved=True
                                                                done=1
                                                                break

    def move_right(self):
        for i in square_tuple:
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                self.position=board[self.position[0]+1][board[self.position[0]].index(self.position)]
                self.has_moved=True
                break

    def move_right_2(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                done = 0
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                        self.position=board[self.position[0]+2][board[self.position[0]].index(self.position)]
                        self.has_moved=True
                        done=1
                        break

    def move_right_3(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                self.position=board[self.position[0]+3][board[self.position[0]].index(self.position)]
                                self.has_moved=True
                                done=1
                                break

    def move_right_4(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                        self.position=board[self.position[0]+4][board[self.position[0]].index(self.position)]
                                        print(self.position)
                                        self.has_moved=True
                                        self.has_moved=True
                                        done=1
                                        break

    def move_right_5(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                        for i in square_tuple:
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                print(self.position)
                                                self.position=board[self.position[0]+5][board[self.position[0]].index(self.position)]
                                                self.has_moved=True
                                                done=1
                                                break

    def move_right_6(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+6][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                        self.position=board[self.position[0]+6][board[self.position[0]].index(self.position)]
                                                        self.has_moved=True
                                                        done=1
                                                        break

    def move_right_7(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+6][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                        for i in square_tuple:
                                                            if done == 1:
                                                                break
                                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+7][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                                self.position=board[self.position[0]+7][board[self.position[0]].index(self.position)]
                                                                self.has_moved=True
                                                                done=1
                                                                break


    def move_left(self):
        for i in square_tuple:
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                self.position=board[self.position[0]-1][board[self.position[0]].index(self.position)]
                self.has_moved=True
                break

    def move_left_2(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                done = 0
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                        self.position=board[self.position[0]-2][board[self.position[0]].index(self.position)]
                        self.has_moved=True
                        done=1
                        break

    def move_left_3(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                self.position=board[self.position[0]-3][board[self.position[0]].index(self.position)]
                                self.has_moved=True
                                done=1
                                break

    def move_left_4(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                        self.position=board[self.position[0]-4][board[self.position[0]].index(self.position)]
                                        print(self.position)
                                        self.has_moved=True
                                        self.has_moved=True
                                        done=1
                                        break

    def move_left_5(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                        for i in square_tuple:
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                print(self.position)
                                                self.position=board[self.position[0]-5][board[self.position[0]].index(self.position)]
                                                self.has_moved=True
                                                done=1
                                                break

    def move_left_6(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-6][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                        self.position=board[self.position[0]-6][board[self.position[0]].index(self.position)]
                                                        self.has_moved=True
                                                        done=1
                                                        break

    def move_left_7(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-6][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                        for i in square_tuple:
                                                            if done == 1:
                                                                break
                                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-7][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                                self.position=board[self.position[0]-7][board[self.position[0]].index(self.position)]
                                                                self.has_moved=True
                                                                done=1
                                                                break




    def attack_up(self):
        for i in square_tuple:
            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                for x in piece_tuple:
                    if x.chess_replace()==i.coordinate:
                        x.captured=True
                self.position=board[self.position[0]][board[self.position[0]].index(self.position)+1]
                self.has_moved=True
                break

    def attack_up_2(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                done = 0
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+2]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                        for x in piece_tuple:
                            if x.chess_replace()==i.coordinate:
                                x.captured=True
                        self.position=board[self.position[0]][board[self.position[0]].index(self.position)+2]
                        self.has_moved=True
                        done=1
                        break

    def attack_up_3(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+3]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                for x in piece_tuple:
                                    if x.chess_replace()==i.coordinate:
                                        x.captured=True
                                self.position=board[self.position[0]][board[self.position[0]].index(self.position)+3]
                                self.has_moved=True
                                done=1
                                break

    def attack_up_4(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+4]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                        for x in piece_tuple:
                                            if x.chess_replace()==i.coordinate:
                                                x.captured=True
                                        self.position=board[self.position[0]][board[self.position[0]].index(self.position)+4]
                                        self.has_moved=True
                                        done=1
                                        break

    def attack_up_5(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+5]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                for x in piece_tuple:
                                                    if x.chess_replace()==i.coordinate:
                                                        x.captured=True
                                                self.position=board[self.position[0]][board[self.position[0]].index(self.position)+5]
                                                self.has_moved=True
                                                done=1
                                                break

    def attack_up_6(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+6]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                        for x in piece_tuple:
                                                            if x.chess_replace()==i.coordinate:
                                                                x.captured=True
                                                        self.position=board[self.position[0]][board[self.position[0]].index(self.position)+6]
                                                        self.has_moved=True
                                                        done=1
                                                        break

    def attack_up_7(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+6]) and i.occupied==False and self.captured==False:
                                                        for i in square_tuple:
                                                            if done == 1:
                                                                break
                                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+7]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                                for x in piece_tuple:
                                                                    if x.chess_replace()==i.coordinate:
                                                                        x.captured=True
                                                                self.position=board[self.position[0]][board[self.position[0]].index(self.position)+7]
                                                                self.has_moved=True
                                                                done=1
                                                                break


    def attack_down(self):
        for i in square_tuple:
            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                for x in piece_tuple:
                    if x.chess_replace()==i.coordinate:
                        x.captured=True
                self.position=board[self.position[0]][board[self.position[0]].index(self.position)-1]
                self.has_moved=True
                break

    def attack_down_2(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                done = 0
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-2]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                        for x in piece_tuple:
                            if x.chess_replace()==i.coordinate:
                                x.captured=True
                        self.position=board[self.position[0]][board[self.position[0]].index(self.position)-2]
                        self.has_moved=True
                        done=1
                        break

    def attack_down_3(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-3]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                for x in piece_tuple:
                                    if x.chess_replace()==i.coordinate:
                                        x.captured=True
                                self.position=board[self.position[0]][board[self.position[0]].index(self.position)-3]
                                self.has_moved=True
                                done=1
                                break

    def attack_down_4(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-4]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                        for x in piece_tuple:
                                            if x.chess_replace()==i.coordinate:
                                                x.captured=True
                                        self.position=board[self.position[0]][board[self.position[0]].index(self.position)-4]
                                        self.has_moved=True
                                        done=1
                                        break

    def attack_down_5(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-5]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                for x in piece_tuple:
                                                    if x.chess_replace()==i.coordinate:
                                                        x.captured=True
                                                self.position=board[self.position[0]][board[self.position[0]].index(self.position)-5]
                                                self.has_moved=True
                                                done=1
                                                break

    def attack_down_6(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-5]) and i.occupied==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-6]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                        for x in piece_tuple:
                                                            if x.chess_replace()==i.coordinate:
                                                                x.captured=True
                                                        self.position=board[self.position[0]][board[self.position[0]].index(self.position)-6]
                                                        self.has_moved=True
                                                        done=1
                                                        break

    def attack_down_7(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-6]) and i.occupied==False and self.captured==False:
                                                        for i in square_tuple:
                                                            if done == 1:
                                                                break
                                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-7]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                                for x in piece_tuple:
                                                                    if x.chess_replace()==i.coordinate:
                                                                        x.captured=True
                                                                self.position=board[self.position[0]][board[self.position[0]].index(self.position)-7]
                                                                self.has_moved=True
                                                                done=1
                                                                break


    def attack_right(self):
        for i in square_tuple:
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                for x in piece_tuple:
                    if x.chess_replace()==i.coordinate:
                        x.captured=True
                self.position=board[self.position[0]+1][board[self.position[0]].index(self.position)]
                self.has_moved=True
                break

    def attack_right_2(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                done = 0
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                        for x in piece_tuple:
                            if x.chess_replace()==i.coordinate:
                                x.captured=True
                        self.position=board[self.position[0]+2][board[self.position[0]].index(self.position)]
                        self.has_moved=True
                        done=1
                        break

    def attack_right_3(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                            for i in square_tuple:
                                if done == 1:
                                    break
                                if i.coordinate == rook.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                    for x in piece_tuple:
                                        if x.chess_replace()==i.coordinate:
                                            x.captured=True
                                            print(x.captured)
                                    self.position=board[self.position[0]+3][board[self.position[0]].index(self.position)]
                                    self.has_moved=True
                                    done=1
                                    break

    def attack_right_4(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                        for x in piece_tuple:
                                            if x.chess_replace()==i.coordinate:
                                                x.captured=True
                                        self.position=board[self.position[0]+4][board[self.position[0]].index(self.position)]
                                        self.has_moved=True
                                        done=1
                                        break

    def attack_right_5(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                        for i in square_tuple:
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                for x in piece_tuple:
                                                    if x.chess_replace()==i.coordinate:
                                                        x.captured=True
                                                self.position=board[self.position[0]+5][board[self.position[0]].index(self.position)]
                                                self.has_moved=True
                                                done=1
                                                break

    def attack_right_6(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+6][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                        for x in piece_tuple:
                                                            if x.chess_replace()==i.coordinate:
                                                                x.captured=True
                                                        self.position=board[self.position[0]+6][board[self.position[0]].index(self.position)]
                                                        self.has_moved=True
                                                        done=1
                                                        break

    def attack_right_7(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+6][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                        for i in square_tuple:
                                                            if done == 1:
                                                                break
                                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+7][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                                for x in piece_tuple:
                                                                    if x.chess_replace()==i.coordinate:
                                                                        x.captured=True
                                                                self.position=board[self.position[0]+7][board[self.position[0]].index(self.position)]
                                                                self.has_moved=True
                                                                done=1
                                                                break


    def attack_left(self):
        for i in square_tuple:
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                for x in piece_tuple:
                    if x.chess_replace()==i.coordinate:
                        x.captured=True
                self.position=board[self.position[0]-1][board[self.position[0]].index(self.position)]
                self.has_moved=True
                break

    def attack_left_2(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                done = 0
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                        for x in piece_tuple:
                            if x.chess_replace()==i.coordinate:
                                x.captured=True
                        self.position=board[self.position[0]-2][board[self.position[0]].index(self.position)]
                        self.has_moved=True
                        done=1
                        break

    def attack_left_3(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                for x in piece_tuple:
                                    if x.chess_replace()==i.coordinate:
                                        x.captured=True
                                self.position=board[self.position[0]-3][board[self.position[0]].index(self.position)]
                                self.has_moved=True
                                done=1
                                break

    def attack_left_4(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                        for x in piece_tuple:
                                            if x.chess_replace()==i.coordinate:
                                                x.captured=True
                                        self.position=board[self.position[0]-4][board[self.position[0]].index(self.position)]
                                        self.has_moved=True
                                        done=1
                                        break

    def attack_left_5(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                for x in piece_tuple:
                                                    if x.chess_replace()==i.coordinate:
                                                        x.captured=True
                                                self.position=board[self.position[0]-5][board[self.position[0]].index(self.position)]
                                                self.has_moved=True
                                                done=1
                                                break

    def attack_left_6(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-6][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                        for x in piece_tuple:
                                                            if x.chess_replace()==i.coordinate:
                                                                x.captured=True
                                                        self.position=board[self.position[0]-6][board[self.position[0]].index(self.position)]
                                                        self.has_moved=True
                                                        done=1
                                                        break

    def attack_left_7(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-6][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                        for i in square_tuple:
                                                            if done == 1:
                                                                break
                                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-7][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                                for x in piece_tuple:
                                                                    if x.chess_replace()==i.coordinate:
                                                                        x.captured=True
                                                                self.position=board[self.position[0]-7][board[self.position[0]].index(self.position)]
                                                                self.has_moved=True
                                                                done=1
                                                                break


    def potential_move_up(self):
        for i in square_tuple:
            if self.position[1] == 8:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False and self.captured==False:
                potential=board[self.position[0]][board[self.position[0]].index(self.position)+1]
                self.potential_move_list.append(queen.static_chess_replace(potential))
                self.potential_move_up_coordinate.append(queen.static_chess_replace(potential))
                break

    def potential_move_up_2(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+2]) and i.occupied==False and self.captured==False:
                        potential=board[self.position[0]][board[self.position[0]].index(self.position)+2]
                        self.potential_move_list.append(queen.static_chess_replace(potential))
                        self.potential_move_up_2_coordinate.append(queen.static_chess_replace(potential))
                        done=1
                        break

    def potential_move_up_3(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+3]) and i.occupied==False and self.captured==False:
                                potential=board[self.position[0]][board[self.position[0]].index(self.position)+3]
                                self.potential_move_list.append(queen.static_chess_replace(potential))
                                self.potential_move_up_3_coordinate.append(queen.static_chess_replace(potential))
                                done=1
                                break

    def potential_move_up_4(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 5:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+4]) and i.occupied==False and self.captured==False:
                                        potential=board[self.position[0]][board[self.position[0]].index(self.position)+4]
                                        self.potential_move_list.append(queen.static_chess_replace(potential))
                                        self.potential_move_up_4_coordinate.append(queen.static_chess_replace(potential))
                                        done=1
                                        break

    def potential_move_up_5(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 5:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 4:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+5]) and i.occupied==False and self.captured==False:
                                                potential=board[self.position[0]][board[self.position[0]].index(self.position)+5]
                                                self.potential_move_list.append(queen.static_chess_replace(potential))
                                                self.potential_move_up_5_coordinate.append(queen.static_chess_replace(potential))
                                                done=1
                                                break

    def potential_move_up_6(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 5:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 4:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[1] == 3:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+6]) and i.occupied==False and self.captured==False:
                                                        potential=board[self.position[0]][board[self.position[0]].index(self.position)+6]
                                                        self.potential_move_list.append(queen.static_chess_replace(potential))
                                                        self.potential_move_up_6_coordinate.append(queen.static_chess_replace(potential))
                                                        done=1
                                                        break

    def potential_move_up_7(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 5:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 4:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[1] == 3:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+6]) and i.occupied==False and self.captured==False:
                                                        for i in square_tuple:
                                                            if done == 1 or self.position[1] == 2 :
                                                                break
                                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+7]) and i.occupied==False and self.captured==False:
                                                                potential=board[self.position[0]][board[self.position[0]].index(self.position)+7]
                                                                self.potential_move_list.append(queen.static_chess_replace(potential))
                                                                self.potential_move_up_7_coordinate.append(queen.static_chess_replace(potential))
                                                                done=1
                                                                break


    def potential_attack_up(self):
        for i in square_tuple:
            if self.position[1] == 8:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                potential=board[self.position[0]][board[self.position[0]].index(self.position)+1]
                self.potential_attack_list.append(queen.static_chess_replace(potential))
                self.potential_attack_up_coordinate.append(queen.static_chess_replace(potential))
                break

    def potential_attack_up_2(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+2]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                        potential=board[self.position[0]][board[self.position[0]].index(self.position)+2]
                        self.potential_attack_list.append(queen.static_chess_replace(potential))
                        self.potential_attack_up_2_coordinate.append(queen.static_chess_replace(potential))
                        done=1
                        break

    def potential_attack_up_3(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+3]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                potential=board[self.position[0]][board[self.position[0]].index(self.position)+3]
                                self.potential_attack_list.append(queen.static_chess_replace(potential))
                                self.potential_attack_up_3_coordinate.append(queen.static_chess_replace(potential))
                                done=1
                                break

    def potential_attack_up_4(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 5:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+4]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                        potential=board[self.position[0]][board[self.position[0]].index(self.position)+4]
                                        self.potential_attack_list.append(queen.static_chess_replace(potential))
                                        self.potential_attack_up_4_coordinate.append(queen.static_chess_replace(potential))
                                        done=1
                                        break

    def potential_attack_up_5(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 5:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 4:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+5]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                potential=board[self.position[0]][board[self.position[0]].index(self.position)+5]
                                                self.potential_attack_list.append(queen.static_chess_replace(potential))
                                                self.potential_attack_up_5_coordinate.append(queen.static_chess_replace(potential))
                                                done=1
                                                break

    def potential_attack_up_6(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 5:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 4:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[1] == 3:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+6]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                        potential=board[self.position[0]][board[self.position[0]].index(self.position)+6]
                                                        self.potential_attack_list.append(queen.static_chess_replace(potential))
                                                        self.potential_attack_up_6_coordinate.append(queen.static_chess_replace(potential))
                                                        done=1
                                                        break

    def potential_attack_up_7(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 5:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 4:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[1] == 3:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+6]) and i.occupied==False and self.captured==False:
                                                        for i in square_tuple:
                                                            if done == 1 or self.position[1] == 2 :
                                                                break
                                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+7]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                                potential=board[self.position[0]][board[self.position[0]].index(self.position)+7]
                                                                self.potential_attack_list.append(queen.static_chess_replace(potential))
                                                                self.potential_attack_up_7_coordinate.append(queen.static_chess_replace(potential))
                                                                done=1
                                                                break


    def potential_move_down(self):
        for i in square_tuple:
            if self.position[1] == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False and self.captured==False:
                potential=board[self.position[0]][board[self.position[0]].index(self.position)-1]
                self.potential_move_list.append(queen.static_chess_replace(potential))
                self.potential_move_down_coordinate.append(queen.static_chess_replace(potential))
                break

    def potential_move_down_2(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-2]) and i.occupied==False and self.captured==False:
                        potential=board[self.position[0]][board[self.position[0]].index(self.position)-2]
                        self.potential_move_list.append(queen.static_chess_replace(potential))
                        self.potential_move_down_2_coordinate.append(queen.static_chess_replace(potential))
                        done=1
                        break

    def potential_move_down_3(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-3]) and i.occupied==False and self.captured==False:
                                potential=board[self.position[0]][board[self.position[0]].index(self.position)-3]
                                self.potential_move_list.append(queen.static_chess_replace(potential))
                                self.potential_move_down_3_coordinate.append(queen.static_chess_replace(potential))
                                done=1
                                break

    def potential_move_down_4(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 4:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-4]) and i.occupied==False and self.captured==False:
                                        potential=board[self.position[0]][board[self.position[0]].index(self.position)-4]
                                        self.potential_move_list.append(queen.static_chess_replace(potential))
                                        self.potential_move_down_4_coordinate.append(queen.static_chess_replace(potential))
                                        done=1
                                        break

    def potential_move_down_5(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 4:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 5:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-5]) and i.occupied==False and self.captured==False:
                                                potential=board[self.position[0]][board[self.position[0]].index(self.position)-5]
                                                self.potential_move_list.append(queen.static_chess_replace(potential))
                                                self.potential_move_down_5_coordinate.append(queen.static_chess_replace(potential))
                                                done=1
                                                break

    def potential_move_down_6(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 4:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 5:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[1] == 6:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-6]) and i.occupied==False and self.captured==False:
                                                        potential=board[self.position[0]][board[self.position[0]].index(self.position)-6]
                                                        self.potential_move_list.append(queen.static_chess_replace(potential))
                                                        self.potential_move_down_6_coordinate.append(queen.static_chess_replace(potential))
                                                        done=1
                                                        break

    def potential_move_down_7(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 4:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 5:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[1] == 6:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-6]) and i.occupied==False and self.captured==False:
                                                        for i in square_tuple:
                                                            if done == 1 or self.position[1] == 7:
                                                                break
                                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-7]) and i.occupied==False and self.captured==False:
                                                                potential=board[self.position[0]][board[self.position[0]].index(self.position)-7]
                                                                self.potential_move_list.append(queen.static_chess_replace(potential))
                                                                self.potential_move_down_7_coordinate.append(queen.static_chess_replace(potential))
                                                                done=1
                                                                break


    def potential_attack_down(self):
        for i in square_tuple:
            if self.position[1] == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                potential=board[self.position[0]][board[self.position[0]].index(self.position)-1]
                self.potential_attack_list.append(queen.static_chess_replace(potential))
                self.potential_attack_down_coordinate.append(queen.static_chess_replace(potential))
                break

    def potential_attack_down_2(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-2]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                        potential=board[self.position[0]][board[self.position[0]].index(self.position)-2]
                        self.potential_attack_list.append(queen.static_chess_replace(potential))
                        self.potential_attack_down_2_coordinate.append(queen.static_chess_replace(potential))
                        done=1
                        break

    def potential_attack_down_3(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-3]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                potential=board[self.position[0]][board[self.position[0]].index(self.position)-3]
                                self.potential_attack_list.append(queen.static_chess_replace(potential))
                                self.potential_attack_down_3_coordinate.append(queen.static_chess_replace(potential))
                                done=1
                                break

    def potential_attack_down_4(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 4:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-4]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                        potential=board[self.position[0]][board[self.position[0]].index(self.position)-4]
                                        self.potential_attack_list.append(queen.static_chess_replace(potential))
                                        self.potential_attack_down_4_coordinate.append(queen.static_chess_replace(potential))
                                        done=1
                                        break

    def potential_attack_down_5(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 4:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 5:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-5]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                potential=board[self.position[0]][board[self.position[0]].index(self.position)-5]
                                                self.potential_attack_list.append(queen.static_chess_replace(potential))
                                                self.potential_attack_down_5_coordinate.append(queen.static_chess_replace(potential))
                                                done=1
                                                break

    def potential_attack_down_6(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 4:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 5:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[1] == 6:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-6]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                        potential=board[self.position[0]][board[self.position[0]].index(self.position)-6]
                                                        self.potential_attack_list.append(queen.static_chess_replace(potential))
                                                        self.potential_attack_down_6_coordinate.append(queen.static_chess_replace(potential))
                                                        done=1
                                                        break

    def potential_attack_down_7(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 4:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 5:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[1] == 6:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-6]) and i.occupied==False and self.captured==False:
                                                        for i in square_tuple:
                                                            if done == 1 or self.position[1] == 7:
                                                                break
                                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-7]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                                potential=board[self.position[0]][board[self.position[0]].index(self.position)-7]
                                                                self.potential_attack_list.append(queen.static_chess_replace(potential))
                                                                self.potential_attack_down_7_coordinate.append(queen.static_chess_replace(potential))
                                                                done=1
                                                                break


    def potential_move_right(self):
        for i in square_tuple:
            if self.position[0] == 7:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                potential=board[self.position[0]+1][board[self.position[0]].index(self.position)]
                self.potential_move_list.append(queen.static_chess_replace(potential))
                self.potential_move_right_coordinate.append(queen.static_chess_replace(potential))
                break

    def potential_move_right_2(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[0] == 7:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[0] == 6:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                        potential=board[self.position[0]+2][board[self.position[0]].index(self.position)]
                        self.potential_move_list.append(queen.static_chess_replace(potential))
                        self.potential_move_right_2_coordinate.append(queen.static_chess_replace(potential))
                        done=1
                        break

    def potential_move_right_3(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[0] == 7:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[0] == 6:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[0] == 5:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                potential=board[self.position[0]+3][board[self.position[0]].index(self.position)]
                                self.potential_move_list.append(queen.static_chess_replace(potential))
                                self.potential_move_right_3_coordinate.append(queen.static_chess_replace(potential))
                                done=1
                                break

    def potential_move_right_4(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[0] == 7:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[0] == 6:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[0] == 5:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[0] == 4:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                        potential=board[self.position[0]+4][board[self.position[0]].index(self.position)]
                                        self.potential_move_list.append(queen.static_chess_replace(potential))
                                        self.potential_move_right_4_coordinate.append(queen.static_chess_replace(potential))
                                        done=1
                                        break

    def potential_move_right_5(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[0] == 7:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[0] == 6:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[0] == 5:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[0] == 4:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[0] == 3:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                potential=board[self.position[0]+5][board[self.position[0]].index(self.position)]
                                                self.potential_move_list.append(queen.static_chess_replace(potential))
                                                self.potential_move_right_5_coordinate.append(queen.static_chess_replace(potential))
                                                done=1
                                                break

    def potential_move_right_6(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[0] == 7:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[0] == 6:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[0] == 5:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[0] == 4:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[0] == 3:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[0] == 2:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+6][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                        potential=board[self.position[0]+6][board[self.position[0]].index(self.position)]
                                                        self.potential_move_list.append(queen.static_chess_replace(potential))
                                                        self.potential_move_right_6_coordinate.append(queen.static_chess_replace(potential))
                                                        done=1
                                                        break

    def potential_move_right_7(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[0] == 7:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[0] == 6:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[0] == 5:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[0] == 4:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[0] == 3:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[0] == 2:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+6][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                        for i in square_tuple:
                                                            if done == 1 or self.position[0] == 1:
                                                                break
                                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+7][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                                potential=board[self.position[0]+7][board[self.position[0]].index(self.position)]
                                                                self.potential_move_list.append(queen.static_chess_replace(potential))
                                                                self.potential_move_right_7_coordinate.append(queen.static_chess_replace(potential))
                                                                done=1
                                                                break


    def potential_attack_right(self):
        for i in square_tuple:
            if self.position[0] == 7:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                potential=board[self.position[0]+1][board[self.position[0]].index(self.position)]
                self.potential_attack_list.append(queen.static_chess_replace(potential))
                self.potential_attack_right_coordinate.append(queen.static_chess_replace(potential))
                break

    def potential_attack_right_2(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[0] == 7:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[0] == 6:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                        potential=board[self.position[0]+2][board[self.position[0]].index(self.position)]
                        self.potential_attack_list.append(queen.static_chess_replace(potential))
                        self.potential_attack_right_2_coordinate.append(queen.static_chess_replace(potential))
                        done=1
                        break

    def potential_attack_right_3(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[0] == 7:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[0] == 6:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[0] == 5:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                potential=board[self.position[0]+3][board[self.position[0]].index(self.position)]
                                self.potential_attack_list.append(queen.static_chess_replace(potential))
                                self.potential_attack_right_3_coordinate.append(queen.static_chess_replace(potential))
                                done=1
                                break

    def potential_attack_right_4(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[0] == 7:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[0] == 6:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[0] == 5:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[0] == 4:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                        potential=board[self.position[0]+4][board[self.position[0]].index(self.position)]
                                        self.potential_attack_list.append(queen.static_chess_replace(potential))
                                        self.potential_attack_right_4_coordinate.append(queen.static_chess_replace(potential))
                                        done=1
                                        break

    def potential_attack_right_5(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[0] == 7:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[0] == 6:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[0] == 5:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[0] == 4:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[0] == 3:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                potential=board[self.position[0]+5][board[self.position[0]].index(self.position)]
                                                self.potential_attack_list.append(queen.static_chess_replace(potential))
                                                self.potential_attack_right_5_coordinate.append(queen.static_chess_replace(potential))
                                                done=1
                                                break

    def potential_attack_right_6(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[0] == 7:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[0] == 6:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[0] == 5:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[0] == 4:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[0] == 3:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[0] == 2:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+6][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                        potential=board[self.position[0]+6][board[self.position[0]].index(self.position)]
                                                        self.potential_attack_list.append(queen.static_chess_replace(potential))
                                                        self.potential_attack_right_6_coordinate.append(queen.static_chess_replace(potential))
                                                        done=1
                                                        break

    def potential_attack_right_7(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[0] == 7:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[0] == 6:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[0] == 5:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[0] == 4:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[0] == 3:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[0] == 2:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]+6][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                        for i in square_tuple:
                                                            if done == 1 or self.position[0] == 1:
                                                                break
                                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]+7][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                                potential=board[self.position[0]+7][board[self.position[0]].index(self.position)]
                                                                self.potential_attack_list.append(queen.static_chess_replace(potential))
                                                                self.potential_attack_right_7_coordinate.append(queen.static_chess_replace(potential))
                                                                done=1
                                                                break


    def potential_move_left(self):
        for i in square_tuple:
            if self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                potential=board[self.position[0]-1][board[self.position[0]].index(self.position)]
                self.potential_move_list.append(queen.static_chess_replace(potential))
                self.potential_move_left_coordinate.append(queen.static_chess_replace(potential))
                break

    def potential_move_left_2(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[0] == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                        potential=board[self.position[0]-2][board[self.position[0]].index(self.position)]
                        self.potential_move_list.append(queen.static_chess_replace(potential))
                        self.potential_move_left_2_coordinate.append(queen.static_chess_replace(potential))
                        done=1
                        break

    def potential_move_left_3(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[0] == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[0] == 2:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                potential=board[self.position[0]-3][board[self.position[0]].index(self.position)]
                                self.potential_move_list.append(queen.static_chess_replace(potential))
                                self.potential_move_left_3_coordinate.append(queen.static_chess_replace(potential))
                                done=1
                                break

    def potential_move_left_4(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[0] == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[0] == 2:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[0] == 3:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                        potential=board[self.position[0]-4][board[self.position[0]].index(self.position)]
                                        self.potential_move_list.append(queen.static_chess_replace(potential))
                                        self.potential_move_left_4_coordinate.append(queen.static_chess_replace(potential))
                                        done=1
                                        break

    def potential_move_left_5(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[0] == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[0] == 2:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[0] == 3:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[0] == 4:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                potential=board[self.position[0]-5][board[self.position[0]].index(self.position)]
                                                self.potential_move_list.append(queen.static_chess_replace(potential))
                                                self.potential_move_left_5_coordinate.append(queen.static_chess_replace(potential))
                                                done=1
                                                break

    def potential_move_left_6(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[0] == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[0] == 2:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[0] == 3:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[0] == 4:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[0] == 5:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-6][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                        potential=board[self.position[0]-6][board[self.position[0]].index(self.position)]
                                                        self.potential_move_list.append(queen.static_chess_replace(potential))
                                                        self.potential_move_left_6_coordinate.append(queen.static_chess_replace(potential))
                                                        done=1
                                                        break

    def potential_move_left_7(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[0] == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[0] == 2:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[0] == 3:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[0] == 4:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[0] == 5:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-6][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                        for i in square_tuple:
                                                            if done == 1 or self.position[0] == 6:
                                                                break
                                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-7][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                                potential=board[self.position[0]-7][board[self.position[0]].index(self.position)]
                                                                self.potential_move_list.append(queen.static_chess_replace(potential))
                                                                self.potential_move_left_7_coordinate.append(queen.static_chess_replace(potential))
                                                                done=1
                                                                break


    def potential_attack_left(self):
        for i in square_tuple:
            if self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                potential=board[self.position[0]-1][board[self.position[0]].index(self.position)]
                self.potential_attack_list.append(queen.static_chess_replace(potential))
                self.potential_attack_left_coordinate.append(queen.static_chess_replace(potential))
                break

    def potential_attack_left_2(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[0] == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                        potential=board[self.position[0]-2][board[self.position[0]].index(self.position)]
                        self.potential_attack_list.append(queen.static_chess_replace(potential))
                        self.potential_attack_left_2_coordinate.append(queen.static_chess_replace(potential))
                        done=1
                        break

    def potential_attack_left_3(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[0] == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[0] == 2:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                potential=board[self.position[0]-3][board[self.position[0]].index(self.position)]
                                self.potential_attack_list.append(queen.static_chess_replace(potential))
                                self.potential_attack_left_3_coordinate.append(queen.static_chess_replace(potential))
                                done=1
                                break

    def potential_attack_left_4(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[0] == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[0] == 2:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[0] == 3:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                        potential=board[self.position[0]-4][board[self.position[0]].index(self.position)]
                                        self.potential_attack_list.append(queen.static_chess_replace(potential))
                                        self.potential_attack_left_4_coordinate.append(queen.static_chess_replace(potential))
                                        done=1
                                        break

    def potential_attack_left_5(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[0] == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[0] == 2:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[0] == 3:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[0] == 4:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                potential=board[self.position[0]-5][board[self.position[0]].index(self.position)]
                                                self.potential_attack_list.append(queen.static_chess_replace(potential))
                                                self.potential_attack_left_5_coordinate.append(queen.static_chess_replace(potential))
                                                done=1
                                                break

    def potential_attack_left_6(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[0] == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[0] == 2:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[0] == 3:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[0] == 4:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[0] == 5:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-6][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                        potential=board[self.position[0]-6][board[self.position[0]].index(self.position)]
                                                        self.potential_attack_list.append(queen.static_chess_replace(potential))
                                                        self.potential_attack_left_6_coordinate.append(queen.static_chess_replace(potential))
                                                        done=1
                                                        break

    def potential_attack_left_7(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[0] == 0:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[0] == 1:
                        break
                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[0] == 2:
                                break
                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[0] == 3:
                                        break
                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[0] == 4:
                                                break
                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[0] == 5:
                                                        break
                                                    if i.coordinate == queen.static_chess_replace(board[self.position[0]-6][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                                                        for i in square_tuple:
                                                            if done == 1 or self.position[0] == 6:
                                                                break
                                                            if i.coordinate == queen.static_chess_replace(board[self.position[0]-7][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                                potential=board[self.position[0]-7][board[self.position[0]].index(self.position)]
                                                                self.potential_attack_list.append(queen.static_chess_replace(potential))
                                                                self.potential_attack_left_7_coordinate.append(queen.static_chess_replace(potential))
                                                                done=1
                                                                break


    @staticmethod
    def list_replace(list,remove,add):
        list_copy=list.copy()
        for i in list_copy:
            if i== remove:
                list_copy.remove(i)
                list_copy.insert(0,add)
                return list_copy

    def chess_replace(self):
            self.position_chess=self.position.copy()
            if self.position_chess[0] == 0:
                return self.list_replace(self.position_chess,0,"a")
            if self.position_chess[0] == 1:
                return self.list_replace(self.position_chess,1,"b")
            if self.position_chess[0] == 2:
                return self.list_replace(self.position_chess,2,"c")
            if self.position_chess[0] == 3:
                return self.list_replace(self.position_chess,3,"d")
            if self.position_chess[0] == 4:
                return self.list_replace(self.position_chess,4,"e")
            if self.position_chess[0] == 5:
                return self.list_replace(self.position_chess,5,"f")
            if self.position_chess[0] == 6:
                return self.list_replace(self.position_chess,6,"g")
            if self.position_chess[0] == 7:
                return self.list_replace(self.position_chess,7,"h")

    @staticmethod
    def static_chess_replace(coord):
            if coord[0] == 0:
                return rook.list_replace(coord,0,"a")
            if coord[0] == 1:
                return rook.list_replace(coord,1,"b")
            if coord[0] == 2:
                return rook.list_replace(coord,2,"c")
            if coord[0] == 3:
                return rook.list_replace(coord,3,"d")
            if coord[0] == 4:
                return rook.list_replace(coord,4,"e")
            if coord[0] == 5:
                return rook.list_replace(coord,5,"f")
            if coord[0] == 6:
                return rook.list_replace(coord,6,"g")
            if coord[0] == 7:
                return rook.list_replace(coord,7,"h")

class bishop:


    def __init__(self,position,has_moved,captured,piece_type,colour):
        self.position = position
        self.has_moved = has_moved
        self.position_chess=self.position.copy()
        self.captured=captured
        self.piece_type=piece_type
        self.selected=False
        self.colour=colour
        self.potential_attack_list = []
        self.potential_move_list = []
        self.potential_move_up_right_7_coordinate = []
        self.potential_move_up_right_6_coordinate = []
        self.potential_move_up_right_5_coordinate = []
        self.potential_move_up_right_4_coordinate = []
        self.potential_move_up_right_3_coordinate = []
        self.potential_move_up_right_2_coordinate = []
        self.potential_move_up_right_coordinate = []
        self.potential_move_up_left_7_coordinate = []
        self.potential_move_up_left_6_coordinate = []
        self.potential_move_up_left_5_coordinate = []
        self.potential_move_up_left_4_coordinate = []
        self.potential_move_up_left_3_coordinate = []
        self.potential_move_up_left_2_coordinate = []
        self.potential_move_up_left_coordinate = []
        self.potential_move_down_right_7_coordinate = []
        self.potential_move_down_right_6_coordinate = []
        self.potential_move_down_right_5_coordinate = []
        self.potential_move_down_right_4_coordinate = []
        self.potential_move_down_right_3_coordinate = []
        self.potential_move_down_right_2_coordinate = []
        self.potential_move_down_right_coordinate = []
        self.potential_move_down_left_7_coordinate = []
        self.potential_move_down_left_6_coordinate = []
        self.potential_move_down_left_5_coordinate = []
        self.potential_move_down_left_4_coordinate = []
        self.potential_move_down_left_3_coordinate = []
        self.potential_move_down_left_2_coordinate = []
        self.potential_move_down_left_coordinate = []
        self.potential_attack_up_right_7_coordinate = []
        self.potential_attack_up_right_6_coordinate = []
        self.potential_attack_up_right_5_coordinate = []
        self.potential_attack_up_right_4_coordinate = []
        self.potential_attack_up_right_3_coordinate = []
        self.potential_attack_up_right_2_coordinate = []
        self.potential_attack_up_right_coordinate = []
        self.potential_attack_up_left_7_coordinate = []
        self.potential_attack_up_left_6_coordinate = []
        self.potential_attack_up_left_5_coordinate = []
        self.potential_attack_up_left_4_coordinate = []
        self.potential_attack_up_left_3_coordinate = []
        self.potential_attack_up_left_2_coordinate = []
        self.potential_attack_up_left_coordinate = []
        self.potential_attack_down_left_7_coordinate = []
        self.potential_attack_down_left_6_coordinate = []
        self.potential_attack_down_left_5_coordinate = []
        self.potential_attack_down_left_4_coordinate = []
        self.potential_attack_down_left_3_coordinate = []
        self.potential_attack_down_left_2_coordinate = []
        self.potential_attack_down_left_coordinate = []
        self.potential_attack_down_right_7_coordinate = []
        self.potential_attack_down_right_6_coordinate = []
        self.potential_attack_down_right_5_coordinate = []
        self.potential_attack_down_right_4_coordinate = []
        self.potential_attack_down_right_3_coordinate = []
        self.potential_attack_down_right_2_coordinate = []
        self.potential_attack_down_right_coordinate = []


    def move_up_right(self):
        for i in square_tuple:
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and i.occupied==False and self.captured==False:
                self.position=board[self.position[0]+1][board[self.position[0]].index(self.position)+1]
                self.has_moved=True
                break

    def move_up_right_2(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                done = 0
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)+2]) and i.occupied==False and self.captured==False:
                        self.position=board[self.position[0]+2][board[self.position[0]].index(self.position)+2]
                        self.has_moved=True
                        done=1
                        break

    def move_up_right_3(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)+3]) and i.occupied==False and self.captured==False:
                                self.position=board[self.position[0]+3][board[self.position[0]].index(self.position)+3]
                                self.has_moved=True
                                done=1
                                break

    def move_up_right_4(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)+4]) and i.occupied==False and self.captured==False:
                                        self.position=board[self.position[0]+4][board[self.position[0]].index(self.position)+4]
                                        print(self.position)
                                        self.has_moved=True
                                        self.has_moved=True
                                        done=1
                                        break

    def move_up_right_5(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)+5]) and i.occupied==False and self.captured==False:
                                                print(self.position)
                                                self.position=board[self.position[0]+5][board[self.position[0]].index(self.position)+5]
                                                self.has_moved=True
                                                done=1
                                                break

    def move_up_right_6(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)+5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+6][board[self.position[0]].index(self.position)+6]) and i.occupied==False and self.captured==False:
                                                        self.position=board[self.position[0]+6][board[self.position[0]].index(self.position)+6]
                                                        self.has_moved=True
                                                        done=1
                                                        break

    def move_up_right_7(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)+5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+6][board[self.position[0]].index(self.position)+6]) and i.occupied==False and self.captured==False:
                                                        for i in square_tuple:
                                                            if done == 1:
                                                                break
                                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+7][board[self.position[0]].index(self.position)+7]) and i.occupied==False and self.captured==False:
                                                                self.position=board[self.position[0]+7][board[self.position[0]].index(self.position)+7]
                                                                self.has_moved=True
                                                                done=1
                                                                break


    def move_up_left(self):
        for i in square_tuple:
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and i.occupied==False and self.captured==False:
                self.position=board[self.position[0]-1][board[self.position[0]].index(self.position)+1]
                self.has_moved=True
                break

    def move_up_left_2(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                done = 0
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)+2]) and i.occupied==False and self.captured==False:
                        self.position=board[self.position[0]-2][board[self.position[0]].index(self.position)+2]
                        self.has_moved=True
                        done=1
                        break

    def move_up_left_3(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)+3]) and i.occupied==False and self.captured==False:
                                self.position=board[self.position[0]-3][board[self.position[0]].index(self.position)+3]
                                self.has_moved=True
                                done=1
                                break

    def move_up_left_4(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)+4]) and i.occupied==False and self.captured==False:
                                        self.position=board[self.position[0]-4][board[self.position[0]].index(self.position)+4]
                                        print(self.position)
                                        self.has_moved=True
                                        self.has_moved=True
                                        done=1
                                        break

    def move_up_left_5(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)+5]) and i.occupied==False and self.captured==False:
                                                print(self.position)
                                                self.position=board[self.position[0]-5][board[self.position[0]].index(self.position)+5]
                                                self.has_moved=True
                                                done=1
                                                break

    def move_up_left_6(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)+5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-6][board[self.position[0]].index(self.position)+6]) and i.occupied==False and self.captured==False:
                                                        self.position=board[self.position[0]-6][board[self.position[0]].index(self.position)+6]
                                                        self.has_moved=True
                                                        done=1
                                                        break

    def move_up_left_7(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)+5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-6][board[self.position[0]].index(self.position)+6]) and i.occupied==False and self.captured==False:
                                                        for i in square_tuple:
                                                            if done == 1:
                                                                break
                                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-7][board[self.position[0]].index(self.position)+7]) and i.occupied==False and self.captured==False:
                                                                self.position=board[self.position[0]-7][board[self.position[0]].index(self.position)+7]
                                                                self.has_moved=True
                                                                done=1
                                                                break


    def move_down_right(self):
        for i in square_tuple:
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and i.occupied==False and self.captured==False:
                self.position=board[self.position[0]+1][board[self.position[0]].index(self.position)-1]
                self.has_moved=True
                break

    def move_down_right_2(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                done = 0
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)-2]) and i.occupied==False and self.captured==False:
                        self.position=board[self.position[0]+2][board[self.position[0]].index(self.position)-2]
                        self.has_moved=True
                        done=1
                        break

    def move_down_right_3(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)-3]) and i.occupied==False and self.captured==False:
                                self.position=board[self.position[0]+3][board[self.position[0]].index(self.position)-3]
                                self.has_moved=True
                                done=1
                                break

    def move_down_right_4(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)-4]) and i.occupied==False and self.captured==False:
                                        self.position=board[self.position[0]+4][board[self.position[0]].index(self.position)-4]
                                        print(self.position)
                                        self.has_moved=True
                                        self.has_moved=True
                                        done=1
                                        break

    def move_down_right_5(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)-5]) and i.occupied==False and self.captured==False:
                                                print(self.position)
                                                self.position=board[self.position[0]+5][board[self.position[0]].index(self.position)-5]
                                                self.has_moved=True
                                                done=1
                                                break

    def move_down_right_6(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)-5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+6][board[self.position[0]].index(self.position)-6]) and i.occupied==False and self.captured==False:
                                                        self.position=board[self.position[0]+6][board[self.position[0]].index(self.position)-6]
                                                        self.has_moved=True
                                                        done=1
                                                        break

    def move_down_right_7(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)-5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+6][board[self.position[0]].index(self.position)-6]) and i.occupied==False and self.captured==False:
                                                        for i in square_tuple:
                                                            if done == 1:
                                                                break
                                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+7][board[self.position[0]].index(self.position)-7]) and i.occupied==False and self.captured==False:
                                                                self.position=board[self.position[0]+7][board[self.position[0]].index(self.position)-7]
                                                                self.has_moved=True
                                                                done=1
                                                                break


    def move_down_left(self):
        for i in square_tuple:
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and i.occupied==False and self.captured==False:
                self.position=board[self.position[0]-1][board[self.position[0]].index(self.position)-1]
                self.has_moved=True
                break

    def move_down_left_2(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                done = 0
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)-2]) and i.occupied==False and self.captured==False:
                        self.position=board[self.position[0]-2][board[self.position[0]].index(self.position)-2]
                        self.has_moved=True
                        done=1
                        break

    def move_down_left_3(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)-3]) and i.occupied==False and self.captured==False:
                                self.position=board[self.position[0]-3][board[self.position[0]].index(self.position)-3]
                                self.has_moved=True
                                done=1
                                break

    def move_down_left_4(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)-4]) and i.occupied==False and self.captured==False:
                                        self.position=board[self.position[0]-4][board[self.position[0]].index(self.position)-4]
                                        print(self.position)
                                        self.has_moved=True
                                        self.has_moved=True
                                        done=1
                                        break

    def move_down_left_5(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)-5]) and i.occupied==False and self.captured==False:
                                                print(self.position)
                                                self.position=board[self.position[0]-5][board[self.position[0]].index(self.position)-5]
                                                self.has_moved=True
                                                done=1
                                                break

    def move_down_left_6(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)-5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-6][board[self.position[0]].index(self.position)-6]) and i.occupied==False and self.captured==False:
                                                        self.position=board[self.position[0]-6][board[self.position[0]].index(self.position)-6]
                                                        self.has_moved=True
                                                        done=1
                                                        break

    def move_down_left_7(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)-5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-6][board[self.position[0]].index(self.position)-6]) and i.occupied==False and self.captured==False:
                                                        for i in square_tuple:
                                                            if done == 1:
                                                                break
                                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-7][board[self.position[0]].index(self.position)-7]) and i.occupied==False and self.captured==False:
                                                                self.position=board[self.position[0]-7][board[self.position[0]].index(self.position)-7]
                                                                self.has_moved=True
                                                                done=1
                                                                break


    def attack_up_right(self):
        for i in square_tuple:
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                for x in piece_tuple:
                    if x.chess_replace()==i.coordinate:
                        x.captured=True
                self.position=board[self.position[0]+1][board[self.position[0]].index(self.position)+1]
                self.has_moved=True
                break

    def attack_up_right_2(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                done = 0
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)+2]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                        for x in piece_tuple:
                            if x.chess_replace()==i.coordinate:
                                x.captured=True
                        self.position=board[self.position[0]+2][board[self.position[0]].index(self.position)+2]
                        self.has_moved=True
                        done=1
                        break

    def attack_up_right_3(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)+3]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                for x in piece_tuple:
                                    if x.chess_replace()==i.coordinate:
                                        x.captured=True
                                self.position=board[self.position[0]+3][board[self.position[0]].index(self.position)+3]
                                self.has_moved=True
                                done=1
                                break

    def attack_up_right_4(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)+4]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                        for x in piece_tuple:
                                            if x.chess_replace()==i.coordinate:
                                                x.captured=True
                                        self.position=board[self.position[0]+4][board[self.position[0]].index(self.position)+4]
                                        print(self.position)
                                        self.has_moved=True
                                        self.has_moved=True
                                        done=1
                                        break

    def attack_up_right_5(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)+5]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                for x in piece_tuple:
                                                    if x.chess_replace()==i.coordinate:
                                                        x.captured=True
                                                self.position=board[self.position[0]+5][board[self.position[0]].index(self.position)+5]
                                                self.has_moved=True
                                                done=1
                                                break

    def attack_up_right_6(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)+5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+6][board[self.position[0]].index(self.position)+6]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                            for x in piece_tuple:
                                                                if x.chess_replace()==i.coordinate:
                                                                    x.captured=True
                                                            self.position=board[self.position[0]+6][board[self.position[0]].index(self.position)+6]
                                                            self.has_moved=True
                                                            done=1
                                                            break

    def attack_up_right_7(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)+5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+6][board[self.position[0]].index(self.position)+6]) and i.occupied==False and self.captured==False:
                                                        for i in square_tuple:
                                                            if done == 1:
                                                                break
                                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+7][board[self.position[0]].index(self.position)+7]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                                for x in piece_tuple:
                                                                    if x.chess_replace()==i.coordinate:
                                                                        x.captured=True
                                                                self.position=board[self.position[0]+7][board[self.position[0]].index(self.position)+7]
                                                                self.has_moved=True
                                                                done=1
                                                                break


    def attack_up_left(self):
        for i in square_tuple:
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                for x in piece_tuple:
                    if x.chess_replace()==i.coordinate:
                        x.captured=True
                self.position=board[self.position[0]-1][board[self.position[0]].index(self.position)+1]
                self.has_moved=True
                break

    def attack_up_left_2(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                done = 0
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)+2]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                        for x in piece_tuple:
                            if x.chess_replace()==i.coordinate:
                                x.captured=True
                        self.position=board[self.position[0]-2][board[self.position[0]].index(self.position)+2]
                        self.has_moved=True
                        done=1
                        break

    def attack_up_left_3(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)+3]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                for x in piece_tuple:
                                    if x.chess_replace()==i.coordinate:
                                        x.captured=True
                                self.position=board[self.position[0]-3][board[self.position[0]].index(self.position)+3]
                                self.has_moved=True
                                done=1
                                break

    def attack_up_left_4(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)+4]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                        for x in piece_tuple:
                                            if x.chess_replace()==i.coordinate:
                                                x.captured=True
                                        self.position=board[self.position[0]-4][board[self.position[0]].index(self.position)+4]
                                        self.has_moved=True
                                        done=1
                                        break

    def attack_up_left_5(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)+5]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                for x in piece_tuple:
                                                    if x.chess_replace()==i.coordinate:
                                                        x.captured=True
                                                self.position=board[self.position[0]-5][board[self.position[0]].index(self.position)+5]
                                                self.has_moved=True
                                                done=1
                                                break

    def attack_up_left_6(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)+5]) and i.occupied==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-6][board[self.position[0]].index(self.position)+6]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                        for x in piece_tuple:
                                                            if x.chess_replace()==i.coordinate:
                                                                x.captured=True
                                                        self.position=board[self.position[0]-6][board[self.position[0]].index(self.position)+6]
                                                        self.has_moved=True
                                                        done=1
                                                        break

    def attack_up_left_7(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)+5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-6][board[self.position[0]].index(self.position)+6]) and i.occupied==False and self.captured==False:
                                                        for i in square_tuple:
                                                            if done == 1:
                                                                break
                                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-7][board[self.position[0]].index(self.position)+7]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                                for x in piece_tuple:
                                                                    if x.chess_replace()==i.coordinate:
                                                                        x.captured=True
                                                                self.position=board[self.position[0]-7][board[self.position[0]].index(self.position)+7]
                                                                self.has_moved=True
                                                                done=1
                                                                break


    def attack_down_right(self):
        for i in square_tuple:
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                for x in piece_tuple:
                    if x.chess_replace()==i.coordinate:
                        x.captured=True
                self.position=board[self.position[0]+1][board[self.position[0]].index(self.position)-1]
                self.has_moved=True
                break

    def attack_down_right_2(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                done = 0
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)-2]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                        for x in piece_tuple:
                            if x.chess_replace()==i.coordinate:
                                x.captured=True
                        self.position=board[self.position[0]+2][board[self.position[0]].index(self.position)-2]
                        self.has_moved=True
                        done=1
                        break

    def attack_down_right_3(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)-3]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                for x in piece_tuple:
                                    if x.chess_replace()==i.coordinate:
                                        x.captured=True
                                self.position=board[self.position[0]+3][board[self.position[0]].index(self.position)-3]
                                self.has_moved=True
                                done=1
                                break

    def attack_down_right_4(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)-4]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                        for x in piece_tuple:
                                            if x.chess_replace()==i.coordinate:
                                                x.captured=True
                                        self.position=board[self.position[0]+4][board[self.position[0]].index(self.position)-4]
                                        self.has_moved=True
                                        done=1
                                        break

    def attack_down_right_5(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)-5]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                for x in piece_tuple:
                                                    if x.chess_replace()==i.coordinate:
                                                        x.captured=True
                                                self.position=board[self.position[0]+5][board[self.position[0]].index(self.position)-5]
                                                self.has_moved=True
                                                done=1
                                                break

    def attack_down_right_6(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)-5]) and i.occupied==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+6][board[self.position[0]].index(self.position)-6]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                        for x in piece_tuple:
                                                            if x.chess_replace()==i.coordinate:
                                                                x.captured=True
                                                        self.position=board[self.position[0]+6][board[self.position[0]].index(self.position)-6]
                                                        self.has_moved=True
                                                        done=1
                                                        break

    def attack_down_right_7(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)-5]) and i.occupied==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+6][board[self.position[0]].index(self.position)-6]) and i.occupied==False:
                                                        for i in square_tuple:
                                                            if done == 1:
                                                                break
                                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+7][board[self.position[0]].index(self.position)-7]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                                for x in piece_tuple:
                                                                    if x.chess_replace()==i.coordinate:
                                                                        x.captured=True
                                                                self.position=board[self.position[0]+7][board[self.position[0]].index(self.position)-7]
                                                                self.has_moved=True
                                                                done=1
                                                                break


    def attack_down_left(self):
        for i in square_tuple:
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                for x in piece_tuple:
                    if x.chess_replace()==i.coordinate:
                        x.captured=True
                self.position=board[self.position[0]-1][board[self.position[0]].index(self.position)-1]
                self.has_moved=True
                break

    def attack_down_left_2(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                done = 0
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)-2]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                        for x in piece_tuple:
                            if x.chess_replace()==i.coordinate:
                                x.captured=True
                        self.position=board[self.position[0]-2][board[self.position[0]].index(self.position)-2]
                        self.has_moved=True
                        done=1
                        break

    def attack_down_left_3(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)-3]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                for x in piece_tuple:
                                    if x.chess_replace()==i.coordinate:
                                        x.captured=True
                                self.position=board[self.position[0]-3][board[self.position[0]].index(self.position)-3]
                                self.has_moved=True
                                done=1
                                break

    def attack_down_left_4(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)-4]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                        for x in piece_tuple:
                                            if x.chess_replace()==i.coordinate:
                                                x.captured=True
                                        self.position=board[self.position[0]-4][board[self.position[0]].index(self.position)-4]
                                        self.has_moved=True
                                        done=1
                                        break

    def attack_down_left_5(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)-5]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                for x in piece_tuple:
                                                    if x.chess_replace()==i.coordinate:
                                                        x.captured=True
                                                self.position=board[self.position[0]-5][board[self.position[0]].index(self.position)-5]
                                                self.has_moved=True
                                                done=1
                                                break

    def attack_down_left_6(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)-5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-6][board[self.position[0]].index(self.position)-6]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                        for x in piece_tuple:
                                                            if x.chess_replace()==i.coordinate:
                                                                x.captured=True
                                                        self.position=board[self.position[0]-6][board[self.position[0]].index(self.position)-6]
                                                        self.has_moved=True
                                                        done=1
                                                        break

    def attack_down_left_7(self):
        done = 0
        for i in square_tuple:
            if done == 1:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)-5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1:
                                                        break
                                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-6][board[self.position[0]].index(self.position)-6]) and i.occupied==False and self.captured==False:
                                                        for i in square_tuple:
                                                            if done == 1:
                                                                break
                                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-7][board[self.position[0]].index(self.position)-7]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                                for x in piece_tuple:
                                                                    if x.chess_replace()==i.coordinate:
                                                                        x.captured=True
                                                                self.position=board[self.position[0]-7][board[self.position[0]].index(self.position)-7]
                                                                self.has_moved=True
                                                                done=1
                                                                break




    def potential_move_up_right(self):
        for i in square_tuple:
            if self.position[1] == 8 or self.position[0] == 7:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and i.occupied==False and self.captured==False:
                potential=board[self.position[0]+1][board[self.position[0]].index(self.position)+1]
                self.potential_move_list.append(rook.static_chess_replace(potential))
                self.potential_move_up_right_coordinate.append(rook.static_chess_replace(potential))
                break

    def potential_move_up_right_2(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8 or self.position[0] == 7:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7 or self.position[0] == 6:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)+2]) and i.occupied==False and self.captured==False:
                        potential=board[self.position[0]+2][board[self.position[0]].index(self.position)+2]
                        self.potential_move_list.append(rook.static_chess_replace(potential))
                        self.potential_move_up_right_2_coordinate.append(rook.static_chess_replace(potential))
                        done=1
                        break

    def potential_move_up_right_3(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8 or self.position[0] == 7:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7 or self.position[0] == 6:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6 or self.position[0] == 5:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)+3]) and i.occupied==False and self.captured==False:
                                potential=board[self.position[0]+3][board[self.position[0]].index(self.position)+3]
                                self.potential_move_list.append(rook.static_chess_replace(potential))
                                self.potential_move_up_right_3_coordinate.append(rook.static_chess_replace(potential))
                                done=1
                                break

    def potential_move_up_right_4(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8 or self.position[0] == 7:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7 or self.position[0] == 6:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6 or self.position[0] == 5:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 5 or self.position[0] == 4:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)+4]) and i.occupied==False and self.captured==False:
                                        potential=board[self.position[0]+4][board[self.position[0]].index(self.position)+4]
                                        self.potential_move_list.append(rook.static_chess_replace(potential))
                                        self.potential_move_up_right_4_coordinate.append(rook.static_chess_replace(potential))
                                        done=1
                                        break

    def potential_move_up_right_5(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8 or self.position[0] == 7:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7 or self.position[0] == 6:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6 or self.position[0] == 5:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 5 or self.position[0] == 4:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 4 or self.position[0] == 3:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)+5]) and i.occupied==False and self.captured==False:
                                                potential=board[self.position[0]+5][board[self.position[0]].index(self.position)+5]
                                                self.potential_move_list.append(rook.static_chess_replace(potential))
                                                self.potential_move_up_right_5_coordinate.append(rook.static_chess_replace(potential))
                                                done=1
                                                break

    def potential_move_up_right_6(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8 or self.position[0] == 7:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7 or self.position[0] == 6:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6 or self.position[0] == 5:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 5 or self.position[0] == 4:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 4 or self.position[0] == 3:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)+5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[1] == 3 or self.position[0] == 2:
                                                        break
                                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+6][board[self.position[0]].index(self.position)+6]) and i.occupied==False and self.captured==False:
                                                        potential=board[self.position[0]+6][board[self.position[0]].index(self.position)+6]
                                                        self.potential_move_list.append(rook.static_chess_replace(potential))
                                                        self.potential_move_up_right_6_coordinate.append(rook.static_chess_replace(potential))
                                                        done=1
                                                        break

    def potential_move_up_right_7(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8 or self.position[0] == 7:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7 or self.position[0] == 6:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6 or self.position[0] == 5:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 5 or self.position[0] == 4:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 4 or self.position[0] == 3:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)+5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[1] == 3 or self.position[0] == 2:
                                                        break
                                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+6][board[self.position[0]].index(self.position)+6]) and i.occupied==False and self.captured==False:
                                                        for i in square_tuple:
                                                            if done == 1 or self.position[1] == 2 or self.position[0] == 1:
                                                                break
                                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+7][board[self.position[0]].index(self.position)+7]) and i.occupied==False and self.captured==False:
                                                                potential=board[self.position[0]+7][board[self.position[0]].index(self.position)+7]
                                                                self.potential_move_list.append(rook.static_chess_replace(potential))
                                                                self.potential_move_up_right_7_coordinate.append(rook.static_chess_replace(potential))
                                                                done=1
                                                                break


    def potential_attack_up_right(self):
        for i in square_tuple:
            if self.position[1] == 8 or self.position[0] == 7:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                potential=board[self.position[0]+1][board[self.position[0]].index(self.position)+1]
                self.potential_attack_list.append(rook.static_chess_replace(potential))
                self.potential_attack_up_right_coordinate.append(rook.static_chess_replace(potential))
                break

    def potential_attack_up_right_2(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8 or self.position[0] == 7:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7 or self.position[0] == 6:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)+2]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                        potential=board[self.position[0]+2][board[self.position[0]].index(self.position)+2]
                        self.potential_attack_list.append(rook.static_chess_replace(potential))
                        self.potential_attack_up_right_2_coordinate.append(rook.static_chess_replace(potential))
                        done=1
                        break

    def potential_attack_up_right_3(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8 or self.position[0] == 7:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7 or self.position[0] == 6:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6 or self.position[0] == 5:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)+3]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                potential=board[self.position[0]+3][board[self.position[0]].index(self.position)+3]
                                self.potential_attack_list.append(rook.static_chess_replace(potential))
                                self.potential_attack_up_right_3_coordinate.append(rook.static_chess_replace(potential))
                                done=1
                                break

    def potential_attack_up_right_4(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8 or self.position[0] == 7:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7 or self.position[0] == 6:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6 or self.position[0] == 5:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 5 or self.position[0] == 4:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)+4]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                        potential=board[self.position[0]+4][board[self.position[0]].index(self.position)+4]
                                        self.potential_attack_list.append(rook.static_chess_replace(potential))
                                        self.potential_attack_up_right_4_coordinate.append(rook.static_chess_replace(potential))
                                        done=1
                                        break

    def potential_attack_up_right_5(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8 or self.position[0] == 7:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7 or self.position[0] == 6:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6 or self.position[0] == 5:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 5 or self.position[0] == 4:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 4 or self.position[0] == 3:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)+5]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                potential=board[self.position[0]+5][board[self.position[0]].index(self.position)+5]
                                                self.potential_attack_list.append(rook.static_chess_replace(potential))
                                                self.potential_attack_up_right_5_coordinate.append(rook.static_chess_replace(potential))
                                                done=1
                                                break

    def potential_attack_up_right_6(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8 or self.position[0] == 7:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7 or self.position[0] == 6:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6 or self.position[0] == 5:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 5 or self.position[0] == 4:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 4 or self.position[0] == 3:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)+5]) and i.occupied==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[1] == 3 or self.position[0] == 2:
                                                        break
                                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+6][board[self.position[0]].index(self.position)+6]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                        potential=board[self.position[0]+6][board[self.position[0]].index(self.position)+6]
                                                        self.potential_attack_list.append(rook.static_chess_replace(potential))
                                                        self.potential_attack_up_right_6_coordinate.append(rook.static_chess_replace(potential))
                                                        done=1
                                                        break

    def potential_attack_up_right_7(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8 or self.position[0] == 7:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7 or self.position[0] == 6:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6 or self.position[0] == 5:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 5 or self.position[0] == 4:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 4 or self.position[0] == 3:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)+5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[1] == 3 or self.position[0] == 2:
                                                        break
                                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+6][board[self.position[0]].index(self.position)+6]) and i.occupied==False and self.captured==False:
                                                        for i in square_tuple:
                                                            if done == 1 or self.position[1] == 2 or self.position[0] == 1:
                                                                break
                                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+7][board[self.position[0]].index(self.position)+7]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                                potential=board[self.position[0]+7][board[self.position[0]].index(self.position)+7]
                                                                self.potential_attack_list.append(rook.static_chess_replace(potential))
                                                                self.potential_attack_up_right_7_coordinate.append(rook.static_chess_replace(potential))
                                                                done=1
                                                                break


    def potential_move_up_left(self):
        for i in square_tuple:
            if self.position[1] == 8 or self.position[0] == 0:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and i.occupied==False and self.captured==False:
                potential=board[self.position[0]-1][board[self.position[0]].index(self.position)+1]
                self.potential_move_list.append(rook.static_chess_replace(potential))
                self.potential_move_up_left_coordinate.append(rook.static_chess_replace(potential))
                break

    def potential_move_up_left_2(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8 or self.position[0] == 0:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7 or self.position[0] == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)+2]) and i.occupied==False and self.captured==False:
                        potential=board[self.position[0]-2][board[self.position[0]].index(self.position)+2]
                        self.potential_move_list.append(rook.static_chess_replace(potential))
                        self.potential_move_up_left_2_coordinate.append(rook.static_chess_replace(potential))
                        done=1
                        break

    def potential_move_up_left_3(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8 or self.position[0] == 0:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7 or self.position[0] == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6 or self.position[0] == 2:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)+3]) and i.occupied==False and self.captured==False:
                                potential=board[self.position[0]-3][board[self.position[0]].index(self.position)+3]
                                self.potential_move_list.append(rook.static_chess_replace(potential))
                                self.potential_move_up_left_3_coordinate.append(rook.static_chess_replace(potential))
                                done=1
                                break

    def potential_move_up_left_4(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8 or self.position[0] == 0:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7 or self.position[0] == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6 or self.position[0] == 2:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 5 or self.position[0] == 3:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)+4]) and i.occupied==False and self.captured==False:
                                        potential=board[self.position[0]-4][board[self.position[0]].index(self.position)+4]
                                        self.potential_move_list.append(rook.static_chess_replace(potential))
                                        self.potential_move_up_left_4_coordinate.append(rook.static_chess_replace(potential))
                                        done=1
                                        break

    def potential_move_up_left_5(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8 or self.position[0] == 0:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7 or self.position[0] == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6 or self.position[0] == 2:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 5 or self.position[0] == 3:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 4 or self.position[0] == 4:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)+5]) and i.occupied==False and self.captured==False:
                                                potential=board[self.position[0]-5][board[self.position[0]].index(self.position)+5]
                                                self.potential_move_list.append(rook.static_chess_replace(potential))
                                                self.potential_move_up_left_5_coordinate.append(rook.static_chess_replace(potential))
                                                done=1
                                                break

    def potential_move_up_left_6(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8 or self.position[0] == 0:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7 or self.position[0] == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6 or self.position[0] == 2:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 5 or self.position[0] == 3:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 4 or self.position[0] == 4:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)+5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[1] == 3 or self.position[0] == 5:
                                                        break
                                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-6][board[self.position[0]].index(self.position)+6]) and i.occupied==False and self.captured==False:
                                                        potential=board[self.position[0]-6][board[self.position[0]].index(self.position)+6]
                                                        self.potential_move_list.append(rook.static_chess_replace(potential))
                                                        self.potential_move_up_left_6_coordinate.append(rook.static_chess_replace(potential))
                                                        done=1
                                                        break

    def potential_move_up_left_7(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8 or self.position[0] == 0:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7 or self.position[0] == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6 or self.position[0] == 2:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 5 or self.position[0] == 3:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 4 or self.position[0] == 4:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)+5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[1] == 3 or self.position[0] == 5:
                                                        break
                                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-6][board[self.position[0]].index(self.position)+6]) and i.occupied==False and self.captured==False:
                                                        for i in square_tuple:
                                                            if done == 1 or self.position[1] == 2 or self.position[0] == 6:
                                                                break
                                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-7][board[self.position[0]].index(self.position)+7]) and i.occupied==False and self.captured==False:
                                                                potential=board[self.position[0]-7][board[self.position[0]].index(self.position)+7]
                                                                self.potential_move_list.append(rook.static_chess_replace(potential))
                                                                self.potential_move_up_left_7_coordinate.append(rook.static_chess_replace(potential))
                                                                done=1
                                                                break


    def potential_attack_up_left(self):
        for i in square_tuple:
            if self.position[1] == 8 or self.position[0] == 0:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                potential=board[self.position[0]-1][board[self.position[0]].index(self.position)+1]
                self.potential_attack_list.append(rook.static_chess_replace(potential))
                self.potential_attack_up_left_coordinate.append(rook.static_chess_replace(potential))
                break

    def potential_attack_up_left_2(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8 or self.position[0] == 0:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7 or self.position[0] == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)+2]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                        potential=board[self.position[0]-2][board[self.position[0]].index(self.position)+2]
                        self.potential_attack_list.append(rook.static_chess_replace(potential))
                        self.potential_attack_up_left_2_coordinate.append(rook.static_chess_replace(potential))
                        done=1
                        break

    def potential_attack_up_left_3(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8 or self.position[0] == 0:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7 or self.position[0] == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6 or self.position[0] == 2:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)+3]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                potential=board[self.position[0]-3][board[self.position[0]].index(self.position)+3]
                                self.potential_attack_list.append(rook.static_chess_replace(potential))
                                self.potential_attack_up_left_3_coordinate.append(rook.static_chess_replace(potential))
                                done=1
                                break

    def potential_attack_up_left_4(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8 or self.position[0] == 0:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7 or self.position[0] == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6 or self.position[0] == 2:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 5 or self.position[0] == 3:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)+4]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                        potential=board[self.position[0]-4][board[self.position[0]].index(self.position)+4]
                                        self.potential_attack_list.append(rook.static_chess_replace(potential))
                                        self.potential_attack_up_left_4_coordinate.append(rook.static_chess_replace(potential))
                                        done=1
                                        break

    def potential_attack_up_left_5(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8 or self.position[0] == 0:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7 or self.position[0] == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6 or self.position[0] == 2:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 5 or self.position[0] == 3:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 4 or self.position[0] == 4:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)+5]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                potential=board[self.position[0]-5][board[self.position[0]].index(self.position)+5]
                                                self.potential_attack_list.append(rook.static_chess_replace(potential))
                                                self.potential_attack_up_left_5_coordinate.append(rook.static_chess_replace(potential))
                                                done=1
                                                break

    def potential_attack_up_left_6(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8 or self.position[0] == 0:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7 or self.position[0] == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6 or self.position[0] == 2:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 5 or self.position[0] == 3:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 4 or self.position[0] == 4:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)+5]) and i.occupied==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[1] == 3 or self.position[0] == 5:
                                                        break
                                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-6][board[self.position[0]].index(self.position)+6]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                        potential=board[self.position[0]-6][board[self.position[0]].index(self.position)+6]
                                                        self.potential_attack_list.append(rook.static_chess_replace(potential))
                                                        self.potential_attack_up_left_6_coordinate.append(rook.static_chess_replace(potential))
                                                        done=1
                                                        break

    def potential_attack_up_left_7(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 8 or self.position[0] == 0:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 7 or self.position[0] == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)+2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 6 or self.position[0] == 2:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)+3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 5 or self.position[0] == 3:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)+4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 4 or self.position[0] == 4:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)+5]) and i.occupied==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[1] == 3 or self.position[0] == 5:
                                                        break
                                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-6][board[self.position[0]].index(self.position)+6]) and i.occupied==False:
                                                        for i in square_tuple:
                                                            if done == 1 or self.position[1] == 2 or self.position[0] == 6:
                                                                break
                                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-7][board[self.position[0]].index(self.position)+7]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                                potential=board[self.position[0]-7][board[self.position[0]].index(self.position)+7]
                                                                self.potential_attack_list.append(rook.static_chess_replace(potential))
                                                                self.potential_attack_up_left_7_coordinate.append(rook.static_chess_replace(potential))
                                                                done=1
                                                                break


    def potential_move_down_left(self):
        for i in square_tuple:
            if self.position[1] == 1 or self.position[0] == 0:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and i.occupied==False and self.captured==False:
                potential=board[self.position[0]-1][board[self.position[0]].index(self.position)-1]
                self.potential_move_list.append(rook.static_chess_replace(potential))
                self.potential_move_down_left_coordinate.append(rook.static_chess_replace(potential))
                break

    def potential_move_down_left_2(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1 or self.position[0] == 0:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2 or self.position[0] == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)-2]) and i.occupied==False and self.captured==False:
                        potential=board[self.position[0]-2][board[self.position[0]].index(self.position)-2]
                        self.potential_move_list.append(rook.static_chess_replace(potential))
                        self.potential_move_down_left_2_coordinate.append(rook.static_chess_replace(potential))
                        done=1
                        break

    def potential_move_down_left_3(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1 or self.position[0] == 0:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2 or self.position[0] == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3 or self.position[0] == 2:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)-3]) and i.occupied==False and self.captured==False:
                                potential=board[self.position[0]-3][board[self.position[0]].index(self.position)-3]
                                self.potential_move_list.append(rook.static_chess_replace(potential))
                                self.potential_move_down_left_3_coordinate.append(rook.static_chess_replace(potential))
                                done=1
                                break

    def potential_move_down_left_4(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1 or self.position[0] == 0:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2 or self.position[0] == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3 or self.position[0] == 2:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 4 or self.position[0] == 3:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)-4]) and i.occupied==False and self.captured==False:
                                        potential=board[self.position[0]-4][board[self.position[0]].index(self.position)-4]
                                        self.potential_move_list.append(rook.static_chess_replace(potential))
                                        self.potential_move_down_left_4_coordinate.append(rook.static_chess_replace(potential))
                                        done=1
                                        break

    def potential_move_down_left_5(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1 or self.position[0] == 0:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2 or self.position[0] == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3 or self.position[0] == 2:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 4 or self.position[0] == 3:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 5 or self.position[0] == 4:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)-5]) and i.occupied==False and self.captured==False:
                                                potential=board[self.position[0]-5][board[self.position[0]].index(self.position)-5]
                                                self.potential_move_list.append(rook.static_chess_replace(potential))
                                                self.potential_move_down_left_5_coordinate.append(rook.static_chess_replace(potential))
                                                done=1
                                                break

    def potential_move_down_left_6(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1 or self.position[0] == 0:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2 or self.position[0] == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3 or self.position[0] == 2:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 4 or self.position[0] == 3:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 5 or self.position[0] == 4:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)-5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[1] == 6 or self.position[0] == 5:
                                                        break
                                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-6][board[self.position[0]].index(self.position)-6]) and i.occupied==False and self.captured==False:
                                                        potential=board[self.position[0]-6][board[self.position[0]].index(self.position)-6]
                                                        self.potential_move_list.append(rook.static_chess_replace(potential))
                                                        self.potential_move_down_left_6_coordinate.append(rook.static_chess_replace(potential))
                                                        done=1
                                                        break

    def potential_move_down_left_7(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1 or self.position[0] == 0:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2 or self.position[0] == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3 or self.position[0] == 2:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 4 or self.position[0] == 3:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 5 or self.position[0] == 4:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)-5]) and i.occupied==False and self.captured==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[1] == 6 or self.position[0] == 5:
                                                        break
                                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-6][board[self.position[0]].index(self.position)-6]) and i.occupied==False and self.captured==False:
                                                        for i in square_tuple:
                                                            if done == 1 or self.position[1] == 7 or self.position[0] == 6:
                                                                break
                                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-7][board[self.position[0]].index(self.position)-7]) and i.occupied==False and self.captured==False:
                                                                potential=board[self.position[0]-7][board[self.position[0]].index(self.position)-7]
                                                                self.potential_move_list.append(rook.static_chess_replace(potential))
                                                                self.potential_move_down_left_7_coordinate.append(rook.static_chess_replace(potential))
                                                                done=1
                                                                break



    def potential_attack_down_left(self):
        for i in square_tuple:
            if self.position[1] == 1 or self.position[0] == 0:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                potential=board[self.position[0]-1][board[self.position[0]].index(self.position)-1]
                self.potential_attack_list.append(rook.static_chess_replace(potential))
                self.potential_attack_down_left_coordinate.append(rook.static_chess_replace(potential))
                break

    def potential_attack_down_left_2(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1 or self.position[0] == 0:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2 or self.position[0] == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)-2]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                        potential=board[self.position[0]-2][board[self.position[0]].index(self.position)-2]
                        self.potential_attack_list.append(rook.static_chess_replace(potential))
                        self.potential_attack_down_left_2_coordinate.append(rook.static_chess_replace(potential))
                        done=1
                        break

    def potential_attack_down_left_3(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1 or self.position[0] == 0:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2 or self.position[0] == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3 or self.position[0] == 2:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)-3]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                potential=board[self.position[0]-3][board[self.position[0]].index(self.position)-3]
                                self.potential_attack_list.append(rook.static_chess_replace(potential))
                                self.potential_attack_down_left_3_coordinate.append(rook.static_chess_replace(potential))
                                done=1
                                break

    def potential_attack_down_left_4(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1 or self.position[0] == 0:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2 or self.position[0] == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3 or self.position[0] == 2:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 4 or self.position[0] == 3:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)-4]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                        potential=board[self.position[0]-4][board[self.position[0]].index(self.position)-4]
                                        self.potential_attack_list.append(rook.static_chess_replace(potential))
                                        self.potential_attack_down_left_4_coordinate.append(rook.static_chess_replace(potential))
                                        done=1
                                        break

    def potential_attack_down_left_5(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1 or self.position[0] == 0:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2 or self.position[0] == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3 or self.position[0] == 2:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 4 or self.position[0] == 3:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 5 or self.position[0] == 4:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)-5]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                potential=board[self.position[0]-5][board[self.position[0]].index(self.position)-5]
                                                self.potential_attack_list.append(rook.static_chess_replace(potential))
                                                self.potential_attack_down_left_5_coordinate.append(rook.static_chess_replace(potential))
                                                done=1
                                                break

    def potential_attack_down_left_6(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1 or self.position[0] == 0:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2 or self.position[0] == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3 or self.position[0] == 2:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 4 or self.position[0] == 3:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 5 or self.position[0] == 4:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)-5]) and i.occupied==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[1] == 6 or self.position[0] == 5:
                                                        break
                                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-6][board[self.position[0]].index(self.position)-6]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                        potential=board[self.position[0]-6][board[self.position[0]].index(self.position)-6]
                                                        self.potential_attack_list.append(rook.static_chess_replace(potential))
                                                        self.potential_attack_down_left_6_coordinate.append(rook.static_chess_replace(potential))
                                                        done=1
                                                        break

    def potential_attack_down_left_7(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1 or self.position[0] == 0:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2 or self.position[0] == 1:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3 or self.position[0] == 2:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 4 or self.position[0] == 3:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-4][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 5 or self.position[0] == 4:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-5][board[self.position[0]].index(self.position)-5]) and i.occupied==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[1] == 6 or self.position[0] == 5:
                                                        break
                                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]-6][board[self.position[0]].index(self.position)-6]) and i.occupied==False:
                                                        for i in square_tuple:
                                                            if done == 1 or self.position[1] == 7 or self.position[0] == 6:
                                                                break
                                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]-7][board[self.position[0]].index(self.position)-7]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                                potential=board[self.position[0]-7][board[self.position[0]].index(self.position)-7]
                                                                self.potential_attack_list.append(rook.static_chess_replace(potential))
                                                                self.potential_attack_down_left_7_coordinate.append(rook.static_chess_replace(potential))
                                                                done=1
                                                                break


    def potential_move_down_right(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1 or self.position[0] == 7:
                break
            #print("test2")
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and i.occupied==False and self.captured==False:
                potential=board[self.position[0]+1][board[self.position[0]].index(self.position)-1]
                self.potential_move_list.append(rook.static_chess_replace(potential))
                self.potential_move_down_right_coordinate.append(rook.static_chess_replace(potential))
                done=1
                break

    def potential_move_down_right_2(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1 or self.position[0] == 7:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 2 or self.position[1] == 2 or self.position[0] == 6:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)-2]) and i.occupied==False and self.captured==False:
                        potential=board[self.position[0]+2][board[self.position[0]].index(self.position)-2]
                        self.potential_move_list.append(rook.static_chess_replace(potential))
                        self.potential_move_down_right_2_coordinate.append(rook.static_chess_replace(potential))
                        done=1
                        break

    def potential_move_down_right_3(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1 or self.position[0] == 7:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2 or self.position[0] == 6:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3 or self.position[0] == 5:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)-3]) and i.occupied==False and self.captured==False:
                                potential=board[self.position[0]+3][board[self.position[0]].index(self.position)-3]
                                self.potential_move_list.append(rook.static_chess_replace(potential))
                                self.potential_move_down_right_3_coordinate.append(rook.static_chess_replace(potential))
                                done=1
                                break

    def potential_move_down_right_4(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1 or self.position[0] == 7:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2 or self.position[0] == 6:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3 or self.position[0] == 5:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 4 or self.position[0] == 4:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)-4]) and i.occupied==False and self.captured==False:
                                        potential=board[self.position[0]+4][board[self.position[0]].index(self.position)-4]
                                        self.potential_move_list.append(rook.static_chess_replace(potential))
                                        self.potential_move_down_right_4_coordinate.append(rook.static_chess_replace(potential))
                                        done=1
                                        break

    def potential_move_down_right_5(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1 or self.position[0] == 7:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2 or self.position[0] == 6:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3 or self.position[0] == 5:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 4 or self.position[0] == 4:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 5 or self.position[0] == 3:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)-5]) and i.occupied==False and self.captured==False:
                                                potential=board[self.position[0]+5][board[self.position[0]].index(self.position)-5]
                                                self.potential_move_list.append(rook.static_chess_replace(potential))
                                                self.potential_move_down_right_5_coordinate.append(rook.static_chess_replace(potential))
                                                done=1
                                                break

    def potential_move_down_right_6(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1 or self.position[0] == 7:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2 or self.position[0] == 6:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3 or self.position[0] == 5:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 4 or self.position[0] == 4:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 5 or self.position[0] == 3:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)-5]) and i.occupied==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[1] == 6 or self.position[0] == 2:
                                                        break
                                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+6][board[self.position[0]].index(self.position)-6]) and i.occupied==False and self.captured==False:
                                                        potential=board[self.position[0]+6][board[self.position[0]].index(self.position)-6]
                                                        self.potential_move_list.append(rook.static_chess_replace(potential))
                                                        self.potential_move_down_right_6_coordinate.append(rook.static_chess_replace(potential))
                                                        done=1
                                                        break

    def potential_move_down_right_7(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1 or self.position[0] == 7:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2 or self.position[0] == 6:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3 or self.position[0] == 5:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 4 or self.position[0] == 4:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 5 or self.position[0] == 3:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)-5]) and i.occupied==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[1] == 6 or self.position[0] == 2:
                                                        break
                                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+6][board[self.position[0]].index(self.position)-6]) and i.occupied==False:
                                                        for i in square_tuple:
                                                            if done == 1 or self.position[1] == 7 or self.position[0] == 1:
                                                                break
                                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+7][board[self.position[0]].index(self.position)-7]) and i.occupied==False and self.captured==False:
                                                                potential=board[self.position[0]+7][board[self.position[0]].index(self.position)-7]
                                                                self.potential_move_list.append(rook.static_chess_replace(potential))
                                                                self.potential_move_down_right_7_coordinate.append(rook.static_chess_replace(potential))
                                                                done=1
                                                                break


    def potential_attack_down_right(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1 or self.position[0] == 7:
                break
            #print("test2")
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                potential=board[self.position[0]+1][board[self.position[0]].index(self.position)-1]
                self.potential_attack_list.append(rook.static_chess_replace(potential))
                self.potential_attack_down_right_coordinate.append(rook.static_chess_replace(potential))
                done=1
                break

    def potential_attack_down_right_2(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1 or self.position[0] == 7:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 2 or self.position[1] == 2 or self.position[0] == 6:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)-2]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                        potential=board[self.position[0]+2][board[self.position[0]].index(self.position)-2]
                        self.potential_attack_list.append(rook.static_chess_replace(potential))
                        self.potential_attack_down_right_2_coordinate.append(rook.static_chess_replace(potential))
                        done=1
                        break

    def potential_attack_down_right_3(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1 or self.position[0] == 7:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2 or self.position[0] == 6:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3 or self.position[0] == 5:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)-3]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                potential=board[self.position[0]+3][board[self.position[0]].index(self.position)-3]
                                self.potential_attack_list.append(rook.static_chess_replace(potential))
                                self.potential_attack_down_right_3_coordinate.append(rook.static_chess_replace(potential))
                                done=1
                                break

    def potential_attack_down_right_4(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1 or self.position[0] == 7:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2 or self.position[0] == 6:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3 or self.position[0] == 5:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 4 or self.position[0] == 4:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)-4]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                        potential=board[self.position[0]+4][board[self.position[0]].index(self.position)-4]
                                        self.potential_attack_list.append(rook.static_chess_replace(potential))
                                        self.potential_attack_down_right_4_coordinate.append(rook.static_chess_replace(potential))
                                        done=1
                                        break

    def potential_attack_down_right_5(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1 or self.position[0] == 7:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2 or self.position[0] == 6:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3 or self.position[0] == 5:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 4 or self.position[0] == 4:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 5 or self.position[0] == 3:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)-5]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                potential=board[self.position[0]+5][board[self.position[0]].index(self.position)-5]
                                                self.potential_attack_list.append(rook.static_chess_replace(potential))
                                                self.potential_attack_down_right_5_coordinate.append(rook.static_chess_replace(potential))
                                                done=1
                                                break

    def potential_attack_down_right_6(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1 or self.position[0] == 7:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2 or self.position[0] == 6:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3 or self.position[0] == 5:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 4 or self.position[0] == 4:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 5 or self.position[0] == 3:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)-5]) and i.occupied==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[1] == 6 or self.position[0] == 2:
                                                        break
                                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+6][board[self.position[0]].index(self.position)-6]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                        potential=board[self.position[0]+6][board[self.position[0]].index(self.position)-6]
                                                        self.potential_attack_list.append(rook.static_chess_replace(potential))
                                                        self.potential_attack_down_right_6_coordinate.append(rook.static_chess_replace(potential))
                                                        done=1
                                                        break

    def potential_attack_down_right_7(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1 or self.position[0] == 7:
                break
            if i.coordinate == rook.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and i.occupied==False:
                for i in square_tuple:
                    if done == 1 or self.position[1] == 2 or self.position[0] == 6:
                        break
                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)-2]) and i.occupied==False:
                        for i in square_tuple:
                            if done == 1 or self.position[1] == 3 or self.position[0] == 5:
                                break
                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+3][board[self.position[0]].index(self.position)-3]) and i.occupied==False:
                                for i in square_tuple:
                                    if done == 1 or self.position[1] == 4 or self.position[0] == 4:
                                        break
                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+4][board[self.position[0]].index(self.position)-4]) and i.occupied==False:
                                        for i in square_tuple:
                                            if done == 1 or self.position[1] == 5 or self.position[0] == 3:
                                                break
                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+5][board[self.position[0]].index(self.position)-5]) and i.occupied==False:
                                                for i in square_tuple:
                                                    if done == 1 or self.position[1] == 6 or self.position[0] == 2:
                                                        break
                                                    if i.coordinate == rook.static_chess_replace(board[self.position[0]+6][board[self.position[0]].index(self.position)-6]) and i.occupied==False:
                                                        for i in square_tuple:
                                                            if done == 1 or self.position[1] == 7 or self.position[0] == 1:
                                                                break
                                                            if i.coordinate == rook.static_chess_replace(board[self.position[0]+7][board[self.position[0]].index(self.position)-7]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                                                                potential=board[self.position[0]+7][board[self.position[0]].index(self.position)-7]
                                                                self.potential_attack_list.append(rook.static_chess_replace(potential))
                                                                self.potential_attack_down_right_7_coordinate.append(rook.static_chess_replace(potential))
                                                                done=1
                                                                break


    @staticmethod
    def list_replace(list,remove,add):
        list_copy=list.copy()
        for i in list_copy:
            if i== remove:
                list_copy.remove(i)
                list_copy.insert(0,add)
                return list_copy

    def chess_replace(self):
        self.position_chess=self.position.copy()
        if self.position_chess[0] == 0:
            return self.list_replace(self.position_chess,0,"a")
        if self.position_chess[0] == 1:
            return self.list_replace(self.position_chess,1,"b")
        if self.position_chess[0] == 2:
            return self.list_replace(self.position_chess,2,"c")
        if self.position_chess[0] == 3:
            return self.list_replace(self.position_chess,3,"d")
        if self.position_chess[0] == 4:
            return self.list_replace(self.position_chess,4,"e")
        if self.position_chess[0] == 5:
            return self.list_replace(self.position_chess,5,"f")
        if self.position_chess[0] == 6:
            return self.list_replace(self.position_chess,6,"g")
        if self.position_chess[0] == 7:
            return self.list_replace(self.position_chess,7,"h")

    @staticmethod
    def static_chess_replace(coord):
            if coord[0] == 0:
                return rook.list_replace(coord,0,"a")
            if coord[0] == 1:
                return rook.list_replace(coord,1,"b")
            if coord[0] == 2:
                return rook.list_replace(coord,2,"c")
            if coord[0] == 3:
                return rook.list_replace(coord,3,"d")
            if coord[0] == 4:
                return rook.list_replace(coord,4,"e")
            if coord[0] == 5:
                return rook.list_replace(coord,5,"f")
            if coord[0] == 6:
                return rook.list_replace(coord,6,"g")
            if coord[0] == 7:
                return rook.list_replace(coord,7,"h")

class king:

    def __init__(self,position,has_moved,captured,piece_type,colour):
        self.position = position
        self.has_moved = has_moved
        self.position_chess=self.position.copy()
        self.captured=captured
        self.piece_type=piece_type
        self.selected=False
        self.colour=colour
        self.check=False
        self.potential_attack_list = []
        self.potential_move_list = []
        self.potential_move_up_coordinate = []
        self.potential_attack_up_coordinate = []
        self.potential_move_down_coordinate = []
        self.potential_attack_down_coordinate = []
        self.potential_move_right_coordinate = []
        self.potential_attack_right_coordinate = []
        self.potential_move_left_coordinate = []
        self.potential_attack_left_coordinate = []
        self.potential_move_up_right_coordinate = []
        self.potential_move_up_left_coordinate = []
        self.potential_move_down_right_coordinate = []
        self.potential_move_down_left_coordinate = []
        self.potential_attack_up_right_coordinate = []
        self.potential_attack_up_left_coordinate = []
        self.potential_attack_down_left_coordinate = []

    def move_up(self):
        for i in square_tuple:
            if i.coordinate == king.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False and self.captured==False:
                self.position=board[self.position[0]][board[self.position[0]].index(self.position)+1]
                self.has_moved=True
                break

    def move_down(self):
        for i in square_tuple:
            if i.coordinate == king.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False and self.captured==False:
                self.position=board[self.position[0]][board[self.position[0]].index(self.position)-1]
                self.has_moved=True
                break

    def move_right(self):
        for i in square_tuple:
            if i.coordinate == king.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                self.position=board[self.position[0]+1][board[self.position[0]].index(self.position)]
                self.has_moved=True
                break

    def move_left(self):
        for i in square_tuple:
            if i.coordinate == king.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                self.position=board[self.position[0]-1][board[self.position[0]].index(self.position)]
                self.has_moved=True
                break

    def move_up_right(self):
        for i in square_tuple:
            if i.coordinate == king.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and i.occupied==False and self.captured==False:
                self.position=board[self.position[0]+1][board[self.position[0]].index(self.position)+1]
                self.has_moved=True
                break

    def move_up_left(self):
        for i in square_tuple:
            if i.coordinate == king.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and i.occupied==False and self.captured==False:
                self.position=board[self.position[0]-1][board[self.position[0]].index(self.position)+1]
                self.has_moved=True
                break

    def move_down_right(self):
        for i in square_tuple:
            if i.coordinate == king.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and i.occupied==False and self.captured==False:
                self.position=board[self.position[0]+1][board[self.position[0]].index(self.position)-1]
                self.has_moved=True
                break

    def move_down_left(self):
        for i in square_tuple:
            if i.coordinate == king.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and i.occupied==False and self.captured==False:
                self.position=board[self.position[0]-1][board[self.position[0]].index(self.position)-1]
                self.has_moved=True
                break

    def attack_up(self):
        for i in square_tuple:
            if i.coordinate == king.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                for x in piece_tuple:
                    if x.chess_replace()==i.coordinate:
                        x.captured=True
                self.position=board[self.position[0]][board[self.position[0]].index(self.position)+1]
                self.has_moved=True
                break

    def attack_down(self):
        for i in square_tuple:
            if i.coordinate == king.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                for x in piece_tuple:
                    if x.chess_replace()==i.coordinate:
                        x.captured=True
                self.position=board[self.position[0]][board[self.position[0]].index(self.position)-1]
                self.has_moved=True
                break

    def attack_right(self):
        for i in square_tuple:
            if i.coordinate == king.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                for x in piece_tuple:
                    if x.chess_replace()==i.coordinate:
                        x.captured=True
                self.position=board[self.position[0]+1][board[self.position[0]].index(self.position)]
                self.has_moved=True
                break

    def attack_left(self):
        for i in square_tuple:
            if i.coordinate == king.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                for x in piece_tuple:
                    if x.chess_replace()==i.coordinate:
                        x.captured=True
                self.position=board[self.position[0]-1][board[self.position[0]].index(self.position)]
                self.has_moved=True
                break

    def attack_up_right(self):
        for i in square_tuple:
            if i.coordinate == king.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                for x in piece_tuple:
                    if x.chess_replace()==i.coordinate:
                        x.captured=True
                self.position=board[self.position[0]+1][board[self.position[0]].index(self.position)+1]
                self.has_moved=True
                break

    def attack_up_left(self):
        for i in square_tuple:
            if i.coordinate == king.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                for x in piece_tuple:
                    if x.chess_replace()==i.coordinate:
                        x.captured=True
                self.position=board[self.position[0]-1][board[self.position[0]].index(self.position)+1]
                self.has_moved=True
                break

    def attack_down_right(self):
        for i in square_tuple:
            if i.coordinate == king.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                for x in piece_tuple:
                    if x.chess_replace()==i.coordinate:
                        x.captured=True
                self.position=board[self.position[0]+1][board[self.position[0]].index(self.position)-1]
                self.has_moved=True
                break

    def attack_down_left(self):
        for i in square_tuple:
            if i.coordinate == king.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                for x in piece_tuple:
                    if x.chess_replace()==i.coordinate:
                        x.captured=True
                self.position=board[self.position[0]-1][board[self.position[0]].index(self.position)-1]
                self.has_moved=True
                break

    def potential_move_up(self):
        for i in square_tuple:
            if self.position[1] == 8:
                break
            if i.coordinate == king.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and i.occupied==False and self.captured==False:
                potential=board[self.position[0]][board[self.position[0]].index(self.position)+1]
                self.potential_move_list.append(king.static_chess_replace(potential))
                self.potential_move_up_coordinate.append(king.static_chess_replace(potential))
                break

    def potential_attack_up(self):
        for i in square_tuple:
            if self.position[1] == 8:
                break
            if i.coordinate == king.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)+1]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                potential=board[self.position[0]][board[self.position[0]].index(self.position)+1]
                self.potential_attack_list.append(king.static_chess_replace(potential))
                self.potential_attack_up_coordinate.append(king.static_chess_replace(potential))
                break

    def potential_move_down(self):
        for i in square_tuple:
            if self.position[1] == 1:
                break
            if i.coordinate == king.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and i.occupied==False and self.captured==False:
                potential=board[self.position[0]][board[self.position[0]].index(self.position)-1]
                self.potential_move_list.append(king.static_chess_replace(potential))
                self.potential_move_down_coordinate.append(king.static_chess_replace(potential))
                break

    def potential_attack_down(self):
        for i in square_tuple:
            if self.position[1] == 1:
                break
            if i.coordinate == queen.static_chess_replace(board[self.position[0]][board[self.position[0]].index(self.position)-1]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                potential=board[self.position[0]][board[self.position[0]].index(self.position)-1]
                self.potential_attack_list.append(queen.static_chess_replace(potential))
                self.potential_attack_down_coordinate.append(queen.static_chess_replace(potential))
                break

    def potential_move_right(self):
        for i in square_tuple:
            if self.position[0] == 7:
                break
            if i.coordinate == king.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                potential=board[self.position[0]+1][board[self.position[0]].index(self.position)]
                self.potential_move_list.append(king.static_chess_replace(potential))
                self.potential_move_right_coordinate.append(king.static_chess_replace(potential))
                break

    def potential_attack_right(self):
        for i in square_tuple:
            if self.position[0] == 7:
                break
            if i.coordinate == king.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                potential=board[self.position[0]+1][board[self.position[0]].index(self.position)]
                self.potential_attack_list.append(king.static_chess_replace(potential))
                self.potential_attack_right_coordinate.append(king.static_chess_replace(potential))
                break

    def potential_move_left(self):
        for i in square_tuple:
            if self.position[0] == 0:
                break
            if i.coordinate == king.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and i.occupied==False and self.captured==False:
                potential=board[self.position[0]-1][board[self.position[0]].index(self.position)]
                self.potential_move_list.append(king.static_chess_replace(potential))
                self.potential_move_left_coordinate.append(king.static_chess_replace(potential))
                break

    def potential_attack_left(self):
        for i in square_tuple:
            if self.position[0] == 0:
                break
            if i.coordinate == king.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                potential=board[self.position[0]-1][board[self.position[0]].index(self.position)]
                self.potential_attack_list.append(king.static_chess_replace(potential))
                self.potential_attack_left_coordinate.append(king.static_chess_replace(potential))
                break

    def potential_move_up_right(self):
        for i in square_tuple:
            if self.position[1] == 8 or self.position[0] == 7:
                break
            if i.coordinate == king.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and i.occupied==False and self.captured==False:
                potential=board[self.position[0]+1][board[self.position[0]].index(self.position)+1]
                self.potential_move_list.append(king.static_chess_replace(potential))
                self.potential_move_up_right_coordinate.append(king.static_chess_replace(potential))
                break

    def potential_attack_up_right(self):
        for i in square_tuple:
            if self.position[1] == 8 or self.position[0] == 7:
                break
            if i.coordinate == king.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+1]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                potential=board[self.position[0]+1][board[self.position[0]].index(self.position)+1]
                self.potential_attack_list.append(king.static_chess_replace(potential))
                self.potential_attack_up_right_coordinate.append(king.static_chess_replace(potential))
                break

    def potential_move_up_left(self):
        for i in square_tuple:
            if self.position[1] == 8 or self.position[0] == 0:
                break
            if i.coordinate == king.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and i.occupied==False and self.captured==False:
                potential=board[self.position[0]-1][board[self.position[0]].index(self.position)+1]
                self.potential_move_list.append(king.static_chess_replace(potential))
                self.potential_move_up_left_coordinate.append(king.static_chess_replace(potential))
                break

    def potential_attack_up_left(self):
        for i in square_tuple:
            if self.position[1] == 8 or self.position[0] == 0:
                break
            if i.coordinate == king.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+1]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                potential=board[self.position[0]-1][board[self.position[0]].index(self.position)+1]
                self.potential_attack_list.append(king.static_chess_replace(potential))
                self.potential_attack_up_left_coordinate.append(king.static_chess_replace(potential))
                break

    def potential_move_down_left(self):
        for i in square_tuple:
            if self.position[1] == 1 or self.position[0] == 0:
                break
            if i.coordinate == king.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and i.occupied==False and self.captured==False:
                potential=board[self.position[0]-1][board[self.position[0]].index(self.position)-1]
                self.potential_move_list.append(king.static_chess_replace(potential))
                self.potential_move_down_left_coordinate.append(king.static_chess_replace(potential))
                break

    def potential_attack_down_left(self):
        for i in square_tuple:
            if self.position[1] == 1 or self.position[0] == 0:
                break
            if i.coordinate == king.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-1]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                potential=board[self.position[0]-1][board[self.position[0]].index(self.position)-1]
                self.potential_attack_list.append(king.static_chess_replace(potential))
                self.potential_attack_down_left_coordinate.append(king.static_chess_replace(potential))
                break

    def potential_move_down_right(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1 or self.position[0] == 7:
                break
            if i.coordinate == king.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and i.occupied==False and self.captured==False:
                potential=board[self.position[0]+1][board[self.position[0]].index(self.position)-1]
                self.potential_move_list.append(king.static_chess_replace(potential))
                self.potential_move_down_right_coordinate.append(king.static_chess_replace(potential))
                done=1
                break

    def potential_attack_down_right(self):
        done = 0
        for i in square_tuple:
            if done == 1 or self.position[1] == 1 or self.position[0] == 7:
                break
            if i.coordinate == king.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-1]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                potential=board[self.position[0]+1][board[self.position[0]].index(self.position)-1]
                self.potential_attack_list.append(king.static_chess_replace(potential))
                self.potential_attack_down_right_coordinate.append(king.static_chess_replace(potential))
                done=1
                break


    @staticmethod
    def list_replace(list,remove,add):
        list_copy=list.copy()
        for i in list_copy:
            if i== remove:
                list_copy.remove(i)
                list_copy.insert(0,add)
                return list_copy

    def chess_replace(self):
        self.position_chess=self.position.copy()
        if self.position_chess[0] == 0:
            return self.list_replace(self.position_chess,0,"a")
        if self.position_chess[0] == 1:
            return self.list_replace(self.position_chess,1,"b")
        if self.position_chess[0] == 2:
            return self.list_replace(self.position_chess,2,"c")
        if self.position_chess[0] == 3:
            return self.list_replace(self.position_chess,3,"d")
        if self.position_chess[0] == 4:
            return self.list_replace(self.position_chess,4,"e")
        if self.position_chess[0] == 5:
            return self.list_replace(self.position_chess,5,"f")
        if self.position_chess[0] == 6:
            return self.list_replace(self.position_chess,6,"g")
        if self.position_chess[0] == 7:
            return self.list_replace(self.position_chess,7,"h")

    @staticmethod
    def static_chess_replace(coord):
            if coord[0] == 0:
                return king.list_replace(coord,0,"a")
            if coord[0] == 1:
                return king.list_replace(coord,1,"b")
            if coord[0] == 2:
                return king.list_replace(coord,2,"c")
            if coord[0] == 3:
                return king.list_replace(coord,3,"d")
            if coord[0] == 4:
                return king.list_replace(coord,4,"e")
            if coord[0] == 5:
                return king.list_replace(coord,5,"f")
            if coord[0] == 6:
                return king.list_replace(coord,6,"g")
            if coord[0] == 7:
                return king.list_replace(coord,7,"h")

    def am_I_in_check(self):
        for piece in piece_tuple:
            if self.chess_replace() in piece.potential_attack_list:
                self.check = True
                break
            else:
                self.check = False

class knight:

    def __init__(self,position,has_moved,captured,piece_type,colour):
        self.position = position
        self.has_moved = has_moved
        self.position_chess=self.position.copy()
        self.captured=captured
        self.piece_type=piece_type
        self.selected=False
        self.colour=colour
        self.potential_attack_list = []
        self.potential_move_list = []
        self.potential_move_1clock_coordinate = []
        self.potential_move_2clock_coordinate = []
        self.potential_move_4clock_coordinate = []
        self.potential_move_5clock_coordinate = []
        self.potential_move_7clock_coordinate = []
        self.potential_move_8clock_coordinate = []
        self.potential_move_10clock_coordinate = []
        self.potential_move_11clock_coordinate = []
        self.potential_attack_1clock_coordinate = []
        self.potential_attack_2clock_coordinate = []
        self.potential_attack_4clock_coordinate = []
        self.potential_attack_5clock_coordinate = []
        self.potential_attack_7clock_coordinate = []
        self.potential_attack_8clock_coordinate = []
        self.potential_attack_10clock_coordinate = []
        self.potential_attack_11clock_coordinate = []


    def move_1clock(self):
        for i in square_tuple:
            if i.coordinate == knight.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+2]) and i.occupied==False and self.captured==False:
                self.position=board[self.position[0]+1][board[self.position[0]].index(self.position)+2]
                self.has_moved=True
                break

    def move_2clock(self):
        for i in square_tuple:
            if i.coordinate == knight.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)+1]) and i.occupied==False and self.captured==False:
                self.position=board[self.position[0]+2][board[self.position[0]].index(self.position)+1]
                self.has_moved=True
                break

    def move_4clock(self):
        for i in square_tuple:
            if i.coordinate == knight.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)-1]) and i.occupied==False and self.captured==False:
                self.position=board[self.position[0]+2][board[self.position[0]].index(self.position)-1]
                self.has_moved=True
                break

    def move_5clock(self):
        for i in square_tuple:
            if i.coordinate == knight.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-2]) and i.occupied==False and self.captured==False:
                self.position=board[self.position[0]+1][board[self.position[0]].index(self.position)-2]
                self.has_moved=True
                break

    def move_7clock(self):
        for i in square_tuple:
            if i.coordinate == knight.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-2]) and i.occupied==False and self.captured==False:
                self.position=board[self.position[0]-1][board[self.position[0]].index(self.position)-2]
                self.has_moved=True
                break

    def move_8clock(self):
        for i in square_tuple:
            if i.coordinate == knight.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)-1]) and i.occupied==False and self.captured==False:
                self.position=board[self.position[0]-2][board[self.position[0]].index(self.position)-1]
                self.has_moved=True
                break

    def move_10clock(self):
        for i in square_tuple:
            if i.coordinate == knight.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)+1]) and i.occupied==False and self.captured==False:
                self.position=board[self.position[0]-2][board[self.position[0]].index(self.position)+1]
                self.has_moved=True
                break

    def move_11clock(self):
        for i in square_tuple:
            if i.coordinate == knight.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+2]) and i.occupied==False and self.captured==False:
                self.position=board[self.position[0]-1][board[self.position[0]].index(self.position)+2]
                self.has_moved=True
                break

    def attack_1clock(self):
        for i in square_tuple:
            if i.coordinate == knight.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+2]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                for x in piece_tuple:
                    if x.chess_replace()==i.coordinate:
                        x.captured=True
                self.position=board[self.position[0]+1][board[self.position[0]].index(self.position)+2]
                self.has_moved=True
                break

    def attack_2clock(self):
        for i in square_tuple:
            if i.coordinate == knight.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)+1]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                for x in piece_tuple:
                    if x.chess_replace()==i.coordinate:
                        x.captured=True
                self.position=board[self.position[0]+2][board[self.position[0]].index(self.position)+1]
                self.has_moved=True
                break

    def attack_4clock(self):
        for i in square_tuple:
            if i.coordinate == knight.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)-1]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                for x in piece_tuple:
                    if x.chess_replace()==i.coordinate:
                        x.captured=True
                self.position=board[self.position[0]+2][board[self.position[0]].index(self.position)-1]
                self.has_moved=True
                break

    def attack_5clock(self):
        for i in square_tuple:
            if i.coordinate == knight.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-2]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                for x in piece_tuple:
                    if x.chess_replace()==i.coordinate:
                        x.captured=True
                self.position=board[self.position[0]+1][board[self.position[0]].index(self.position)-2]
                self.has_moved=True
                break

    def attack_7clock(self):
        for i in square_tuple:
            if i.coordinate == knight.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-2]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                for x in piece_tuple:
                    if x.chess_replace()==i.coordinate:
                        x.captured=True
                self.position=board[self.position[0]-1][board[self.position[0]].index(self.position)-2]
                self.has_moved=True
                break

    def attack_8clock(self):
        for i in square_tuple:
            if i.coordinate == knight.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)-1]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                for x in piece_tuple:
                    if x.chess_replace()==i.coordinate:
                        x.captured=True
                self.position=board[self.position[0]-2][board[self.position[0]].index(self.position)-1]
                self.has_moved=True
                break

    def attack_10clock(self):
        for i in square_tuple:
            if i.coordinate == knight.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)+1]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                for x in piece_tuple:
                    if x.chess_replace()==i.coordinate:
                        x.captured=True
                self.position=board[self.position[0]-2][board[self.position[0]].index(self.position)+1]
                self.has_moved=True
                break

    def attack_11clock(self):
        for i in square_tuple:
            if i.coordinate == knight.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+2]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                for x in piece_tuple:
                    if x.chess_replace()==i.coordinate:
                        x.captured=True
                self.position=board[self.position[0]-1][board[self.position[0]].index(self.position)+2]
                self.has_moved=True
                break

    def potential_move_1clock(self):
        for i in square_tuple:
            if  self.position[0] >= 7 or self.position[1] >= 7:
                break
            if i.coordinate == knight.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+2]) and i.occupied==False and self.captured==False:
                potential=board[self.position[0]+1][board[self.position[0]].index(self.position)+2]
                self.potential_move_list.append(knight.static_chess_replace(potential))
                self.potential_move_1clock_coordinate.append(knight.static_chess_replace(potential))
                break

    def potential_move_2clock(self):
        for i in square_tuple:
            if  self.position[0] >= 6 or self.position[1] >= 7:
                break
            if i.coordinate == knight.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)+1]) and i.occupied==False and self.captured==False:
                potential=board[self.position[0]+2][board[self.position[0]].index(self.position)+1]
                self.potential_move_list.append(knight.static_chess_replace(potential))
                self.potential_move_2clock_coordinate.append(knight.static_chess_replace(potential))
                break

    def potential_move_4clock(self):
        for i in square_tuple:
            if  self.position[0] >= 6 or self.position[1] == 1:
                break
            if i.coordinate == knight.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)-1]) and i.occupied==False and self.captured==False:
                potential=board[self.position[0]+2][board[self.position[0]].index(self.position)-1]
                self.potential_move_list.append(knight.static_chess_replace(potential))
                self.potential_move_4clock_coordinate.append(knight.static_chess_replace(potential))
                break

    def potential_move_5clock(self):
        for i in square_tuple:
            if  self.position[0] == 7 or self.position[1] == 2:
                break
            if i.coordinate == knight.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-2]) and i.occupied==False and self.captured==False:
                potential=board[self.position[0]+1][board[self.position[0]].index(self.position)-2]
                self.potential_move_list.append(knight.static_chess_replace(potential))
                self.potential_move_5clock_coordinate.append(knight.static_chess_replace(potential))
                break

    def potential_move_7clock(self):
        for i in square_tuple:
            if  self.position[0] == 0 or self.position[1] <= 2:
                break
            if i.coordinate == knight.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-2]) and i.occupied==False and self.captured==False:
                potential=board[self.position[0]-1][board[self.position[0]].index(self.position)-2]
                self.potential_move_list.append(knight.static_chess_replace(potential))
                self.potential_move_7clock_coordinate.append(knight.static_chess_replace(potential))
                break

    def potential_move_8clock(self):
        for i in square_tuple:
            if  self.position[0] <= 1 or self.position[1] == 1:
                break
            if i.coordinate == knight.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)-1]) and i.occupied==False and self.captured==False:
                potential=board[self.position[0]-2][board[self.position[0]].index(self.position)-1]
                self.potential_move_list.append(knight.static_chess_replace(potential))
                self.potential_move_8clock_coordinate.append(knight.static_chess_replace(potential))
                break

    def potential_move_10clock(self):
        for i in square_tuple:
            if  self.position[0] <= 1 or self.position[1] == 8:
                break
            if i.coordinate == knight.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)+1]) and i.occupied==False and self.captured==False:
                potential=board[self.position[0]-2][board[self.position[0]].index(self.position)+1]
                self.potential_move_list.append(knight.static_chess_replace(potential))
                self.potential_move_10clock_coordinate.append(knight.static_chess_replace(potential))
                break

    def potential_move_11clock(self):
        for i in square_tuple:
            if self.position[0] == 0 or self.position[1] >= 7:
                break
            if i.coordinate == knight.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+2]) and i.occupied==False and self.captured==False:
                potential=board[self.position[0]-1][board[self.position[0]].index(self.position)+2]
                self.potential_move_list.append(knight.static_chess_replace(potential))
                self.potential_move_11clock_coordinate.append(knight.static_chess_replace(potential))
                break

    def potential_attack_1clock(self):
        for i in square_tuple:
            if  self.position[0] >= 7 or self.position[1] >= 7:
                break
            if i.coordinate == knight.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)+2]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                potential=board[self.position[0]+1][board[self.position[0]].index(self.position)+2]
                self.potential_attack_list.append(knight.static_chess_replace(potential))
                self.potential_attack_1clock_coordinate.append(knight.static_chess_replace(potential))
                break

    def potential_attack_2clock(self):
        for i in square_tuple:
            if  self.position[0] >= 6 or self.position[1] >= 8:
                break
            if i.coordinate == knight.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)+1]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                potential=board[self.position[0]+2][board[self.position[0]].index(self.position)+1]
                self.potential_attack_list.append(knight.static_chess_replace(potential))
                self.potential_attack_2clock_coordinate.append(knight.static_chess_replace(potential))
                break

    def potential_attack_4clock(self):
        for i in square_tuple:
            if  self.position[0] >= 6 or self.position[1] == 1:
                break
            if i.coordinate == knight.static_chess_replace(board[self.position[0]+2][board[self.position[0]].index(self.position)-1]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                potential=board[self.position[0]+2][board[self.position[0]].index(self.position)-1]
                self.potential_attack_list.append(knight.static_chess_replace(potential))
                self.potential_attack_4clock_coordinate.append(knight.static_chess_replace(potential))
                break

    def potential_attack_5clock(self):
        for i in square_tuple:
            if  self.position[0] == 7 or self.position[1] <= 2:
                break
            if i.coordinate == knight.static_chess_replace(board[self.position[0]+1][board[self.position[0]].index(self.position)-2]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                potential=board[self.position[0]+1][board[self.position[0]].index(self.position)-2]
                self.potential_attack_list.append(knight.static_chess_replace(potential))
                self.potential_attack_5clock_coordinate.append(knight.static_chess_replace(potential))
                break

    def potential_attack_7clock(self):
        for i in square_tuple:
            if  self.position[0] == 0 or self.position[1] <= 2:
                break
            if i.coordinate == knight.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)-2]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                potential=board[self.position[0]-1][board[self.position[0]].index(self.position)-2]
                self.potential_attack_list.append(knight.static_chess_replace(potential))
                self.potential_attack_7clock_coordinate.append(knight.static_chess_replace(potential))
                break

    def potential_attack_8clock(self):
        for i in square_tuple:
            if  self.position[0] <= 1 or self.position[1] == 1:
                break
            if i.coordinate == knight.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)-1]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                potential=board[self.position[0]-2][board[self.position[0]].index(self.position)-1]
                self.potential_attack_list.append(knight.static_chess_replace(potential))
                self.potential_attack_8clock_coordinate.append(knight.static_chess_replace(potential))
                break

    def potential_attack_10clock(self):
        for i in square_tuple:
            if  self.position[0] <= 1 or self.position[1] == 8:
                break
            if i.coordinate == knight.static_chess_replace(board[self.position[0]-2][board[self.position[0]].index(self.position)+1]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                potential=board[self.position[0]-2][board[self.position[0]].index(self.position)+1]
                self.potential_attack_list.append(knight.static_chess_replace(potential))
                self.potential_attack_10clock_coordinate.append(knight.static_chess_replace(potential))
                break

    def potential_attack_11clock(self):
        for i in square_tuple:
            if self.position[0] == 0 or self.position[1] >= 7:
                break
            if i.coordinate == knight.static_chess_replace(board[self.position[0]-1][board[self.position[0]].index(self.position)+2]) and self.captured==False and i.occupied == True and i.occupied_colour != self.colour:
                potential=board[self.position[0]-1][board[self.position[0]].index(self.position)+2]
                self.potential_attack_list.append(knight.static_chess_replace(potential))
                self.potential_attack_11clock_coordinate.append(knight.static_chess_replace(potential))
                break

    @staticmethod
    def list_replace(list,remove,add):
        list_copy=list.copy()
        for i in list_copy:
            if i== remove:
                list_copy.remove(i)
                list_copy.insert(0,add)
                return list_copy

    def chess_replace(self):
        self.position_chess=self.position.copy()
        if self.position_chess[0] == 0:
            return self.list_replace(self.position_chess,0,"a")
        if self.position_chess[0] == 1:
            return self.list_replace(self.position_chess,1,"b")
        if self.position_chess[0] == 2:
            return self.list_replace(self.position_chess,2,"c")
        if self.position_chess[0] == 3:
            return self.list_replace(self.position_chess,3,"d")
        if self.position_chess[0] == 4:
            return self.list_replace(self.position_chess,4,"e")
        if self.position_chess[0] == 5:
            return self.list_replace(self.position_chess,5,"f")
        if self.position_chess[0] == 6:
            return self.list_replace(self.position_chess,6,"g")
        if self.position_chess[0] == 7:
            return self.list_replace(self.position_chess,7,"h")

    @staticmethod
    def static_chess_replace(coord):
            if coord[0] == 0:
                return knight.list_replace(coord,0,"a")
            if coord[0] == 1:
                return knight.list_replace(coord,1,"b")
            if coord[0] == 2:
                return knight.list_replace(coord,2,"c")
            if coord[0] == 3:
                return knight.list_replace(coord,3,"d")
            if coord[0] == 4:
                return knight.list_replace(coord,4,"e")
            if coord[0] == 5:
                return knight.list_replace(coord,5,"f")
            if coord[0] == 6:
                return knight.list_replace(coord,6,"g")
            if coord[0] == 7:
                return knight.list_replace(coord,7,"h")


#white pawns
pawn_a_w = pawn_w(board[0][1],False,False,"white")

pawn_b_w = pawn_w(board[1][1],False,False,"white")

pawn_c_w = pawn_w(board[2][1],False,False,"white")

pawn_d_w = pawn_w(board[3][1],False,False,"white")

pawn_e_w = pawn_w(board[4][1],False,False,"white")

pawn_f_w = pawn_w(board[5][1],False,False,"white")

pawn_g_w = pawn_w(board[6][1],False,False,"white")


pawn_h_w = pawn_w(board[7][1],False,False,"white")

pawn_a_b = pawn_b(board[0][6],False,False,"black")


pawn_b_b = pawn_b(board[1][6],False,False,"black")


pawn_c_b = pawn_b(board[2][6],False,False,"black")


pawn_d_b = pawn_b(board[3][6],False,False,"black")


pawn_e_b = pawn_b(board[4][6],False,False,"black")


pawn_f_b = pawn_b(board[5][6],False,False,"black")


pawn_g_b = pawn_b(board[6][6],False,False,"black")


pawn_h_b = pawn_b(board[7][6],False,False,"black")



queen_1_w =queen(board[3][0],False,False,"w_queen","white")


queen_1_b =queen(board[4][7],False,False,"b_queen","black")


rook_1_w = rook(board[0][0],False,False,"w_rook","white")

rook_2_w = rook(board[7][0],False,False,"w_rook","white")

rook_1_b = rook(board[0][7],False,False,"b_rook","black")

rook_2_b = rook(board[7][7],False,False,"b_rook","black")

bishop_1_w = bishop(board[5][0],False,False,"w_bishop","white")

bishop_1_b = bishop(board[2][7],False,False,"b_bishop","black")

bishop_2_w = bishop(board[2][0],False,False,"w_bishop","white")

bishop_2_b = bishop(board[5][7],False,False,"b_bishop","black")

king_1_w = king(board[4][0],False,False,"w_king","white")

king_1_b = king(board[3][7],False,False,"b_king","black")

knight_1_w = knight(board[1][0],False,False,"w_knight","white")

knight_2_w = knight(board[6][0],False,False,"w_knight","white")

knight_1_b = knight(board[1][7],False,False,"b_knight","black")

knight_2_b = knight(board[6][7],False,False,"b_knight","black")


#Squares

square_a1 = square(False,False,["a",1])
square_a2 = square(False,False,["a",2])
square_a3 = square(False,False,["a",3])
square_a4 = square(False,False,["a",4])
square_a5 = square(False,False,["a",5])
square_a6 = square(False,False,["a",6])
square_a7 = square(False,False,["a",7])
square_a8 = square(False,False,["a",8])
square_b1 = square(False,False,["b",1])
square_b2 = square(False,False,["b",2])
square_b3 = square(False,False,["b",3])
square_b4 = square(False,False,["b",4])
square_b5 = square(False,False,["b",5])
square_b6 = square(False,False,["b",6])
square_b7 = square(False,False,["b",7])
square_b8 = square(False,False,["b",8])
square_c1 = square(False,False,["c",1])
square_c2 = square(False,False,["c",2])
square_c3 = square(False,False,["c",3])
square_c4 = square(False,False,["c",4])
square_c5 = square(False,False,["c",5])
square_c6 = square(False,False,["c",6])
square_c7 = square(False,False,["c",7])
square_c8 = square(False,False,["c",8])
square_d1 = square(False,False,["d",1])
square_d2 = square(False,False,["d",2])
square_d3 = square(False,False,["d",3])
square_d4 = square(False,False,["d",4])
square_d5 = square(False,False,["d",5])
square_d6 = square(False,False,["d",6])
square_d7 = square(False,False,["d",7])
square_d8 = square(False,False,["d",8])
square_e1 = square(False,False,["e",1])
square_e2 = square(False,False,["e",2])
square_e3 = square(False,False,["e",3])
square_e4 = square(False,False,["e",4])
square_e5 = square(False,False,["e",5])
square_e6 = square(False,False,["e",6])
square_e7 = square(False,False,["e",7])
square_e8 = square(False,False,["e",8])
square_f1 = square(False,False,["f",1])
square_f2 = square(False,False,["f",2])
square_f3 = square(False,False,["f",3])
square_f4 = square(False,False,["f",4])
square_f5 = square(False,False,["f",5])
square_f6 = square(False,False,["f",6])
square_f7 = square(False,False,["f",7])
square_f8 = square(False,False,["f",8])
square_g1 = square(False,False,["g",1])
square_g2 = square(False,False,["g",2])
square_g3 = square(False,False,["g",3])
square_g4 = square(False,False,["g",4])
square_g5 = square(False,False,["g",5])
square_g6 = square(False,False,["g",6])
square_g7 = square(False,False,["g",7])
square_g8 = square(False,False,["g",8])
square_h1 = square(False,False,["h",1])
square_h2 = square(False,False,["h",2])
square_h3 = square(False,False,["h",3])
square_h4 = square(False,False,["h",4])
square_h5 = square(False,False,["h",5])
square_h6 = square(False,False,["h",6])
square_h7 = square(False,False,["h",7])
square_h8 = square(False,False,["h",8])


square_tuple=(square_a1,square_a2,square_a3,square_a4,square_a5,square_a6,square_a7,square_a8,
square_b1,square_b2,square_b3,square_b4,square_b5,square_b6,square_b7,square_b8,
square_c1,square_c2,square_c3,square_c4,square_c5,square_c6,square_c7,square_c8,
square_d1,square_d2,square_d3,square_d4,square_d5,square_d6,square_d7,square_d8,
square_e1,square_e2,square_e3,square_e4,square_e5,square_e6,square_e7,square_e8,
square_f1,square_f2,square_f3,square_f4,square_f5,square_f6,square_f7,square_f8,
square_g1,square_g2,square_g3,square_g4,square_g5,square_g6,square_g7,square_g8,
square_h1,square_h2,square_h3,square_h4,square_h5,square_h6,square_h7,square_h8)

a_file_tuple=(square_a1,square_a2,square_a3,square_a4,square_a5,square_a6,square_a7,square_a8)
h_file_tuple=(square_h1,square_h2,square_h3,square_h4,square_h5,square_h6,square_h7,square_h8)

rank_1_tuple=(square_a1,square_b1,square_c1,square_d1,square_e1,square_f1,square_g1,square_h1)
rank_2_tuple=(square_a2,square_b2,square_c2,square_d2,square_e2,square_f2,square_g2,square_h2)
rank_3_tuple=(square_a3,square_b3,square_c3,square_d3,square_e3,square_f3,square_g3,square_h3)
rank_4_tuple=(square_a4,square_b4,square_c4,square_d4,square_e4,square_f4,square_g4,square_h4)
rank_5_tuple=(square_a5,square_b5,square_c5,square_d5,square_e5,square_f5,square_g5,square_h5)
rank_6_tuple=(square_a6,square_b6,square_c6,square_d6,square_e6,square_f6,square_g6,square_h6)
rank_7_tuple=(square_a7,square_b7,square_c7,square_d7,square_e7,square_f7,square_g7,square_h7)
rank_8_tuple=(square_a8,square_b8,square_c8,square_d8,square_e8,square_f8,square_g8,square_h8)

piece_tuple=(pawn_a_w,pawn_b_w,pawn_c_w,pawn_d_w,pawn_e_w,pawn_f_w,pawn_g_w,pawn_h_w,
pawn_a_b,pawn_b_b,pawn_c_b,pawn_d_b,pawn_e_b,pawn_f_b,pawn_g_b,pawn_h_b,queen_1_w,queen_1_b,rook_1_w,rook_2_w,rook_1_b,rook_2_b,bishop_1_w,bishop_2_w,bishop_2_b,bishop_1_b,knight_1_w,knight_2_w,knight_1_b,knight_2_b,king_1_w,king_1_b)

turn_counter = 0
whos_turn = None

def turn():

    global turn_counter
    global whos_turn
    turn_counter += 1

    if turn_counter%2 == 1:
        whos_turn = "white"
    else:
        whos_turn = "black"

    for i in square_tuple:
        i.is_it_attacked()
        i.is_it_occupied()

    for piece in piece_tuple:
        if piece.piece_type =="w_pawn" or piece.piece_type == "b_pawn":
            piece.potential_move_list =[]
            piece.potential_attack_list = []
            piece.potential_move_coordinate = []
            piece.potential_move_of_two_squares_coordinate = []
            piece.potential_capture_up_coordinate = []
            piece.potential_capture_down_coordinate = []
            piece.potential_move()
            piece.potential_move_of_two_squares()
            piece.potential_capture_up()
            piece.potential_capture_down()

        if piece.piece_type=="w_queen" or piece.piece_type=="b_queen":
            piece.potential_move_list =[]
            piece.potential_attack_list = []
            piece.potential_move_up_7_coordinate = []
            piece.potential_move_up_6_coordinate = []
            piece.potential_move_up_5_coordinate = []
            piece.potential_move_up_4_coordinate = []
            piece.potential_move_up_3_coordinate = []
            piece.potential_move_up_2_coordinate = []
            piece.potential_move_up_coordinate = []
            piece.potential_attack_up_7_coordinate = []
            piece.potential_attack_up_6_coordinate = []
            piece.potential_attack_up_5_coordinate = []
            piece.potential_attack_up_4_coordinate = []
            piece.potential_attack_up_3_coordinate = []
            piece.potential_attack_up_2_coordinate = []
            piece.potential_attack_up_coordinate = []
            piece.potential_move_down_7_coordinate = []
            piece.potential_move_down_6_coordinate = []
            piece.potential_move_down_5_coordinate = []
            piece.potential_move_down_4_coordinate = []
            piece.potential_move_down_3_coordinate = []
            piece.potential_move_down_2_coordinate = []
            piece.potential_move_down_coordinate = []
            piece.potential_attack_down_7_coordinate = []
            piece.potential_attack_down_6_coordinate = []
            piece.potential_attack_down_5_coordinate = []
            piece.potential_attack_down_4_coordinate = []
            piece.potential_attack_down_3_coordinate = []
            piece.potential_attack_down_2_coordinate = []
            piece.potential_attack_down_coordinate = []
            piece.potential_move_right_7_coordinate = []
            piece.potential_move_right_6_coordinate = []
            piece.potential_move_right_5_coordinate = []
            piece.potential_move_right_4_coordinate = []
            piece.potential_move_right_3_coordinate = []
            piece.potential_move_right_2_coordinate = []
            piece.potential_move_right_coordinate = []
            piece.potential_attack_right_7_coordinate = []
            piece.potential_attack_right_6_coordinate = []
            piece.potential_attack_right_5_coordinate = []
            piece.potential_attack_right_4_coordinate = []
            piece.potential_attack_right_3_coordinate = []
            piece.potential_attack_right_2_coordinate = []
            piece.potential_attack_right_coordinate = []
            piece.potential_move_left_7_coordinate = []
            piece.potential_move_left_6_coordinate = []
            piece.potential_move_left_5_coordinate = []
            piece.potential_move_left_4_coordinate = []
            piece.potential_move_left_3_coordinate = []
            piece.potential_move_left_2_coordinate = []
            piece.potential_move_left_coordinate = []
            piece.potential_attack_left_7_coordinate = []
            piece.potential_attack_left_6_coordinate = []
            piece.potential_attack_left_5_coordinate = []
            piece.potential_attack_left_4_coordinate = []
            piece.potential_attack_left_3_coordinate = []
            piece.potential_attack_left_2_coordinate = []
            piece.potential_attack_left_coordinate = []
            piece.potential_move_up_right_7_coordinate = []
            piece.potential_move_up_right_6_coordinate = []
            piece.potential_move_up_right_5_coordinate = []
            piece.potential_move_up_right_4_coordinate = []
            piece.potential_move_up_right_3_coordinate = []
            piece.potential_move_up_right_2_coordinate = []
            piece.potential_move_up_right_coordinate = []
            piece.potential_move_up_left_7_coordinate = []
            piece.potential_move_up_left_6_coordinate = []
            piece.potential_move_up_left_5_coordinate = []
            piece.potential_move_up_left_4_coordinate = []
            piece.potential_move_up_left_3_coordinate = []
            piece.potential_move_up_left_2_coordinate = []
            piece.potential_move_up_left_coordinate = []
            piece.potential_move_down_left_7_coordinate = []
            piece.potential_move_down_left_6_coordinate = []
            piece.potential_move_down_left_5_coordinate = []
            piece.potential_move_down_left_4_coordinate = []
            piece.potential_move_down_left_3_coordinate = []
            piece.potential_move_down_left_2_coordinate = []
            piece.potential_move_down_left_coordinate = []
            piece.potential_move_down_right_7_coordinate = []
            piece.potential_move_down_right_6_coordinate = []
            piece.potential_move_down_right_5_coordinate = []
            piece.potential_move_down_right_4_coordinate = []
            piece.potential_move_down_right_3_coordinate = []
            piece.potential_move_down_right_2_coordinate = []
            piece.potential_move_down_right_coordinate = []
            piece.potential_attack_up_right_7_coordinate = []
            piece.potential_attack_up_right_6_coordinate = []
            piece.potential_attack_up_right_5_coordinate = []
            piece.potential_attack_up_right_4_coordinate = []
            piece.potential_attack_up_right_3_coordinate = []
            piece.potential_attack_up_right_2_coordinate = []
            piece.potential_attack_up_right_coordinate = []
            piece.potential_attack_up_left_7_coordinate = []
            piece.potential_attack_up_left_6_coordinate = []
            piece.potential_attack_up_left_5_coordinate = []
            piece.potential_attack_up_left_4_coordinate = []
            piece.potential_attack_up_left_3_coordinate = []
            piece.potential_attack_up_left_2_coordinate = []
            piece.potential_attack_up_left_coordinate = []
            piece.potential_attack_down_left_7_coordinate = []
            piece.potential_attack_down_left_6_coordinate = []
            piece.potential_attack_down_left_5_coordinate = []
            piece.potential_attack_down_left_4_coordinate = []
            piece.potential_attack_down_left_3_coordinate = []
            piece.potential_attack_down_left_2_coordinate = []
            piece.potential_attack_down_left_coordinate = []
            piece.potential_attack_down_right_7_coordinate = []
            piece.potential_attack_down_right_6_coordinate = []
            piece.potential_attack_down_right_5_coordinate = []
            piece.potential_attack_down_right_4_coordinate = []
            piece.potential_attack_down_right_3_coordinate = []
            piece.potential_attack_down_right_2_coordinate = []
            piece.potential_attack_down_right_coordinate = []
            piece.potential_move_up()
            piece.potential_move_up_2()
            piece.potential_move_up_3()
            piece.potential_move_up_4()
            piece.potential_move_up_5()
            piece.potential_move_up_6()
            piece.potential_move_up_7()
            piece.potential_move_down()
            piece.potential_move_down_2()
            piece.potential_move_down_3()
            piece.potential_move_down_4()
            piece.potential_move_down_5()
            piece.potential_move_down_6()
            piece.potential_move_down_7()
            piece.potential_attack_down()
            piece.potential_attack_down_2()
            piece.potential_attack_down_3()
            piece.potential_attack_down_4()
            piece.potential_attack_down_5()
            piece.potential_attack_down_6()
            piece.potential_attack_down_7()
            piece.potential_attack_up()
            piece.potential_attack_up_2()
            piece.potential_attack_up_3()
            piece.potential_attack_up_4()
            piece.potential_attack_up_5()
            piece.potential_attack_up_6()
            piece.potential_attack_up_7()
            piece.potential_move_right()
            piece.potential_move_right_2()
            piece.potential_move_right_3()
            piece.potential_move_right_4()
            piece.potential_move_right_5()
            piece.potential_move_right_6()
            piece.potential_move_right_7()
            piece.potential_attack_right()
            piece.potential_attack_right_2()
            piece.potential_attack_right_3()
            piece.potential_attack_right_4()
            piece.potential_attack_right_5()
            piece.potential_attack_right_6()
            piece.potential_attack_right_7()
            piece.potential_move_left()
            piece.potential_move_left_2()
            piece.potential_move_left_3()
            piece.potential_move_left_4()
            piece.potential_move_left_5()
            piece.potential_move_left_6()
            piece.potential_move_left_7()
            piece.potential_attack_left()
            piece.potential_attack_left_2()
            piece.potential_attack_left_3()
            piece.potential_attack_left_4()
            piece.potential_attack_left_5()
            piece.potential_attack_left_6()
            piece.potential_attack_left_7()
            piece.potential_move_up_right()
            piece.potential_move_up_right_2()
            piece.potential_move_up_right_3()
            piece.potential_move_up_right_4()
            piece.potential_move_up_right_5()
            piece.potential_move_up_right_6()
            piece.potential_move_up_right_7()
            piece.potential_move_up_left()
            piece.potential_move_up_left_2()
            piece.potential_move_up_left_3()
            piece.potential_move_up_left_4()
            piece.potential_move_up_left_5()
            piece.potential_move_up_left_6()
            piece.potential_move_up_left_7()
            piece.potential_move_down_right()
            piece.potential_move_down_right_2()
            piece.potential_move_down_right_3()
            piece.potential_move_down_right_4()
            piece.potential_move_down_right_5()
            piece.potential_move_down_right_6()
            piece.potential_move_down_right_7()
            piece.potential_move_down_left()
            piece.potential_move_down_left_2()
            piece.potential_move_down_left_3()
            piece.potential_move_down_left_4()
            piece.potential_move_down_left_5()
            piece.potential_move_down_left_6()
            piece.potential_move_down_left_7()
            piece.potential_attack_up_right()
            piece.potential_attack_up_right_2()
            piece.potential_attack_up_right_3()
            piece.potential_attack_up_right_4()
            piece.potential_attack_up_right_5()
            piece.potential_attack_up_right_6()
            piece.potential_attack_up_right_7()
            piece.potential_attack_up_left()
            piece.potential_attack_up_left_2()
            piece.potential_attack_up_left_3()
            piece.potential_attack_up_left_4()
            piece.potential_attack_up_left_5()
            piece.potential_attack_up_left_6()
            piece.potential_attack_up_left_7()
            piece.potential_attack_down_right()
            piece.potential_attack_down_right_2()
            piece.potential_attack_down_right_3()
            piece.potential_attack_down_right_4()
            piece.potential_attack_down_right_5()
            piece.potential_attack_down_right_6()
            piece.potential_attack_down_right_7()
            piece.potential_attack_down_left()
            piece.potential_attack_down_left_2()
            piece.potential_attack_down_left_3()
            piece.potential_attack_down_left_4()
            piece.potential_attack_down_left_5()
            piece.potential_attack_down_left_6()
            piece.potential_attack_down_left_7()

        if piece.piece_type=="w_rook" or piece.piece_type=="b_rook":
            piece.potential_move_list =[]
            piece.potential_attack_list = []
            piece.potential_move_up_7_coordinate = []
            piece.potential_move_up_6_coordinate = []
            piece.potential_move_up_5_coordinate = []
            piece.potential_move_up_4_coordinate = []
            piece.potential_move_up_3_coordinate = []
            piece.potential_move_up_2_coordinate = []
            piece.potential_move_up_coordinate = []
            piece.potential_attack_up_7_coordinate = []
            piece.potential_attack_up_6_coordinate = []
            piece.potential_attack_up_5_coordinate = []
            piece.potential_attack_up_4_coordinate = []
            piece.potential_attack_up_3_coordinate = []
            piece.potential_attack_up_2_coordinate = []
            piece.potential_attack_up_coordinate = []
            piece.potential_move_down_7_coordinate = []
            piece.potential_move_down_6_coordinate = []
            piece.potential_move_down_5_coordinate = []
            piece.potential_move_down_4_coordinate = []
            piece.potential_move_down_3_coordinate = []
            piece.potential_move_down_2_coordinate = []
            piece.potential_move_down_coordinate = []
            piece.potential_attack_down_7_coordinate = []
            piece.potential_attack_down_6_coordinate = []
            piece.potential_attack_down_5_coordinate = []
            piece.potential_attack_down_4_coordinate = []
            piece.potential_attack_down_3_coordinate = []
            piece.potential_attack_down_2_coordinate = []
            piece.potential_attack_down_coordinate = []
            piece.potential_move_right_7_coordinate = []
            piece.potential_move_right_6_coordinate = []
            piece.potential_move_right_5_coordinate = []
            piece.potential_move_right_4_coordinate = []
            piece.potential_move_right_3_coordinate = []
            piece.potential_move_right_2_coordinate = []
            piece.potential_move_right_coordinate = []
            piece.potential_attack_right_7_coordinate = []
            piece.potential_attack_right_6_coordinate = []
            piece.potential_attack_right_5_coordinate = []
            piece.potential_attack_right_4_coordinate = []
            piece.potential_attack_right_3_coordinate = []
            piece.potential_attack_right_2_coordinate = []
            piece.potential_attack_right_coordinate = []
            piece.potential_move_left_7_coordinate = []
            piece.potential_move_left_6_coordinate = []
            piece.potential_move_left_5_coordinate = []
            piece.potential_move_left_4_coordinate = []
            piece.potential_move_left_3_coordinate = []
            piece.potential_move_left_2_coordinate = []
            piece.potential_move_left_coordinate = []
            piece.potential_attack_left_7_coordinate = []
            piece.potential_attack_left_6_coordinate = []
            piece.potential_attack_left_5_coordinate = []
            piece.potential_attack_left_4_coordinate = []
            piece.potential_attack_left_3_coordinate = []
            piece.potential_attack_left_2_coordinate = []
            piece.potential_attack_left_coordinate = []
            piece.potential_move_up()
            piece.potential_move_up_2()
            piece.potential_move_up_3()
            piece.potential_move_up_4()
            piece.potential_move_up_5()
            piece.potential_move_up_6()
            piece.potential_move_up_7()
            piece.potential_move_down()
            piece.potential_move_down_2()
            piece.potential_move_down_3()
            piece.potential_move_down_4()
            piece.potential_move_down_5()
            piece.potential_move_down_6()
            piece.potential_move_down_7()
            piece.potential_attack_down()
            piece.potential_attack_down_2()
            piece.potential_attack_down_3()
            piece.potential_attack_down_4()
            piece.potential_attack_down_5()
            piece.potential_attack_down_6()
            piece.potential_attack_down_7()
            piece.potential_attack_up()
            piece.potential_attack_up_2()
            piece.potential_attack_up_3()
            piece.potential_attack_up_4()
            piece.potential_attack_up_5()
            piece.potential_attack_up_6()
            piece.potential_attack_up_7()
            piece.potential_move_right()
            piece.potential_move_right_2()
            piece.potential_move_right_3()
            piece.potential_move_right_4()
            piece.potential_move_right_5()
            piece.potential_move_right_6()
            piece.potential_move_right_7()
            piece.potential_attack_right()
            piece.potential_attack_right_2()
            piece.potential_attack_right_3()
            piece.potential_attack_right_4()
            piece.potential_attack_right_5()
            piece.potential_attack_right_6()
            piece.potential_attack_right_7()
            piece.potential_move_left()
            piece.potential_move_left_2()
            piece.potential_move_left_3()
            piece.potential_move_left_4()
            piece.potential_move_left_5()
            piece.potential_move_left_6()
            piece.potential_move_left_7()
            piece.potential_attack_left()
            piece.potential_attack_left_2()
            piece.potential_attack_left_3()
            piece.potential_attack_left_4()
            piece.potential_attack_left_5()
            piece.potential_attack_left_6()
            piece.potential_attack_left_7()

        if piece.piece_type=="w_bishop" or piece.piece_type=="b_bishop":
            piece.potential_move_list =[]
            piece.potential_attack_list = []
            piece.potential_move_up_right_7_coordinate = []
            piece.potential_move_up_right_6_coordinate = []
            piece.potential_move_up_right_5_coordinate = []
            piece.potential_move_up_right_4_coordinate = []
            piece.potential_move_up_right_3_coordinate = []
            piece.potential_move_up_right_2_coordinate = []
            piece.potential_move_up_right_coordinate = []
            piece.potential_move_up_left_7_coordinate = []
            piece.potential_move_up_left_6_coordinate = []
            piece.potential_move_up_left_5_coordinate = []
            piece.potential_move_up_left_4_coordinate = []
            piece.potential_move_up_left_3_coordinate = []
            piece.potential_move_up_left_2_coordinate = []
            piece.potential_move_up_left_coordinate = []
            piece.potential_move_down_left_7_coordinate = []
            piece.potential_move_down_left_6_coordinate = []
            piece.potential_move_down_left_5_coordinate = []
            piece.potential_move_down_left_4_coordinate = []
            piece.potential_move_down_left_3_coordinate = []
            piece.potential_move_down_left_2_coordinate = []
            piece.potential_move_down_left_coordinate = []
            piece.potential_move_down_right_7_coordinate = []
            piece.potential_move_down_right_6_coordinate = []
            piece.potential_move_down_right_5_coordinate = []
            piece.potential_move_down_right_4_coordinate = []
            piece.potential_move_down_right_3_coordinate = []
            piece.potential_move_down_right_2_coordinate = []
            piece.potential_move_down_right_coordinate = []
            piece.potential_attack_up_right_7_coordinate = []
            piece.potential_attack_up_right_6_coordinate = []
            piece.potential_attack_up_right_5_coordinate = []
            piece.potential_attack_up_right_4_coordinate = []
            piece.potential_attack_up_right_3_coordinate = []
            piece.potential_attack_up_right_2_coordinate = []
            piece.potential_attack_up_right_coordinate = []
            piece.potential_attack_up_left_7_coordinate = []
            piece.potential_attack_up_left_6_coordinate = []
            piece.potential_attack_up_left_5_coordinate = []
            piece.potential_attack_up_left_4_coordinate = []
            piece.potential_attack_up_left_3_coordinate = []
            piece.potential_attack_up_left_2_coordinate = []
            piece.potential_attack_up_left_coordinate = []
            piece.potential_attack_down_left_7_coordinate = []
            piece.potential_attack_down_left_6_coordinate = []
            piece.potential_attack_down_left_5_coordinate = []
            piece.potential_attack_down_left_4_coordinate = []
            piece.potential_attack_down_left_3_coordinate = []
            piece.potential_attack_down_left_2_coordinate = []
            piece.potential_attack_down_left_coordinate = []
            piece.potential_attack_down_right_7_coordinate = []
            piece.potential_attack_down_right_6_coordinate = []
            piece.potential_attack_down_right_5_coordinate = []
            piece.potential_attack_down_right_4_coordinate = []
            piece.potential_attack_down_right_3_coordinate = []
            piece.potential_attack_down_right_2_coordinate = []
            piece.potential_attack_down_right_coordinate = []
            piece.potential_move_up_right()
            piece.potential_move_up_right_2()
            piece.potential_move_up_right_3()
            piece.potential_move_up_right_4()
            piece.potential_move_up_right_5()
            piece.potential_move_up_right_6()
            piece.potential_move_up_right_7()
            piece.potential_move_up_left()
            piece.potential_move_up_left_2()
            piece.potential_move_up_left_3()
            piece.potential_move_up_left_4()
            piece.potential_move_up_left_5()
            piece.potential_move_up_left_6()
            piece.potential_move_up_left_7()
            piece.potential_move_down_right()
            piece.potential_move_down_right_2()
            piece.potential_move_down_right_3()
            piece.potential_move_down_right_4()
            piece.potential_move_down_right_5()
            piece.potential_move_down_right_6()
            piece.potential_move_down_right_7()
            piece.potential_move_down_left()
            piece.potential_move_down_left_2()
            piece.potential_move_down_left_3()
            piece.potential_move_down_left_4()
            piece.potential_move_down_left_5()
            piece.potential_move_down_left_6()
            piece.potential_move_down_left_7()
            piece.potential_attack_up_right()
            piece.potential_attack_up_right_2()
            piece.potential_attack_up_right_3()
            piece.potential_attack_up_right_4()
            piece.potential_attack_up_right_5()
            piece.potential_attack_up_right_6()
            piece.potential_attack_up_right_7()
            piece.potential_attack_up_left()
            piece.potential_attack_up_left_2()
            piece.potential_attack_up_left_3()
            piece.potential_attack_up_left_4()
            piece.potential_attack_up_left_5()
            piece.potential_attack_up_left_6()
            piece.potential_attack_up_left_7()
            piece.potential_attack_down_right()
            piece.potential_attack_down_right_2()
            piece.potential_attack_down_right_3()
            piece.potential_attack_down_right_4()
            piece.potential_attack_down_right_5()
            piece.potential_attack_down_right_6()
            piece.potential_attack_down_right_7()
            piece.potential_attack_down_left()
            piece.potential_attack_down_left_2()
            piece.potential_attack_down_left_3()
            piece.potential_attack_down_left_4()
            piece.potential_attack_down_left_5()
            piece.potential_attack_down_left_6()
            piece.potential_attack_down_left_7()

        if piece.piece_type=="w_knight" or piece.piece_type=="b_knight":
            piece.potential_move_list = []
            piece.potential_attack_list = []
            piece.potential_move_1clock_coordinate = []
            piece.potential_move_2clock_coordinate = []
            piece.potential_move_4clock_coordinate = []
            piece.potential_move_5clock_coordinate = []
            piece.potential_move_7clock_coordinate = []
            piece.potential_move_8clock_coordinate = []
            piece.potential_move_10clock_coordinate = []
            piece.potential_move_11clock_coordinate = []
            piece.potential_attack_1clock_coordinate = []
            piece.potential_attack_2clock_coordinate = []
            piece.potential_attack_4clock_coordinate = []
            piece.potential_attack_5clock_coordinate = []
            piece.potential_attack_7clock_coordinate = []
            piece.potential_attack_8clock_coordinate = []
            piece.potential_attack_10clock_coordinate = []
            piece.potential_attack_11clock_coordinate = []

            piece.potential_move_1clock()
            piece.potential_move_2clock()
            piece.potential_move_4clock()
            piece.potential_move_5clock()
            piece.potential_move_7clock()
            piece.potential_move_8clock()
            piece.potential_move_10clock()
            piece.potential_move_11clock()
            piece.potential_attack_1clock()
            piece.potential_attack_2clock()
            piece.potential_attack_4clock()
            piece.potential_attack_5clock()
            piece.potential_attack_7clock()
            piece.potential_attack_8clock()
            piece.potential_attack_10clock()
            piece.potential_attack_11clock()


        if piece.piece_type=="w_king" or piece.piece_type=="b_king":
            piece.potential_move_list =[]
            piece.potential_attack_list = []
            piece.potential_move_up_coordinate = []
            piece.potential_attack_up_coordinate = []
            piece.potential_move_down_coordinate = []
            piece.potential_attack_down_coordinate = []
            piece.potential_move_right_coordinate = []
            piece.potential_attack_right_coordinate = []
            piece.potential_move_left_coordinate = []
            piece.potential_attack_left_coordinate = []
            piece.potential_move_up_right_coordinate = []
            piece.potential_move_up_left_coordinate = []
            piece.potential_move_down_left_coordinate = []
            piece.potential_move_down_right_coordinate = []
            piece.potential_attack_up_right_coordinate = []
            piece.potential_attack_up_left_coordinate = []
            piece.potential_attack_down_left_coordinate = []
            piece.potential_attack_down_right_coordinate = []
            piece.potential_move_up()
            piece.potential_move_down()
            piece.potential_attack_up()
            piece.potential_attack_down()
            piece.potential_move_right()
            piece.potential_attack_right()
            piece.potential_move_left()
            piece.potential_attack_left()
            piece.potential_move_up_right()
            piece.potential_move_up_left()
            piece.potential_move_down_right()
            piece.potential_move_down_left()
            piece.potential_attack_up_right()
            piece.potential_attack_up_left()
            piece.potential_attack_down_right()
            piece.potential_attack_down_left()
            piece.am_I_in_check()







    a8=' '
    b8=' '
    c8=' '
    d8=' '
    e8=' '
    f8=' '
    g8=' '
    h8=' '
    a7=' '
    b7=' '
    c7=' '
    d7=' '
    e7=' '
    f7=' '
    g7=' '
    h7=' '
    a6=' '
    b6=' '
    c6=' '
    d6=' '
    e6=' '
    f6=' '
    g6=' '
    h6=' '
    a5=' '
    b5=' '
    c5=' '
    d5=' '
    e5=' '
    f5=' '
    g5=' '
    h5=' '
    a4=' '
    b4=' '
    c4=' '
    d4=' '
    e4=' '
    f4=' '
    g4=' '
    h4=' '
    a3=' '
    b3=' '
    c3=' '
    d3=' '
    e3=' '
    f3=' '
    g3=' '
    h3=' '
    a2=' '
    b2=' '
    c2=' '
    d2=' '
    e2=' '
    f2=' '
    g2=' '
    h2=' '
    a1=' '
    b1=' '
    c1=' '
    d1=' '
    e1=' '
    f1=' '
    g1=' '
    h1=' '

    rank_8_gui = [a8,b8,c8,d8,e8,f8,g8,h8]
    rank_7_gui = [a7,b7,c7,d7,e7,f7,g7,h7]
    rank_6_gui = [a6,b6,c6,d6,e6,f6,g6,h6]
    rank_5_gui = [a5,b5,c5,d5,e5,f5,g5,h5]
    rank_4_gui = [a4,b4,c4,d4,e4,f4,g4,h4]
    rank_3_gui = [a3,b3,c3,d3,e3,f3,g3,h3]
    rank_2_gui = [a2,b2,c2,d2,e2,f2,g2,h2]
    rank_1_gui = [a1,b1,c1,d1,e1,f1,g1,h1]
    file_axis = "  a","b","c","d","e","f","g","h"

    for index,coor in enumerate(rank_1_tuple):
        if coor.occupied == True:
            if coor.occupied_by == "b_pawn":
                rank_1_gui[index]="P"
            elif coor.occupied_by == "w_pawn":
                rank_1_gui[index]="A"
            elif coor.occupied_by == "w_queen":
                rank_1_gui[index]="Q"
            elif coor.occupied_by == "b_queen":
                rank_1_gui[index]="q"
            elif coor.occupied_by == "w_rook":
                rank_1_gui[index]="R"
            elif coor.occupied_by == "b_rook":
                rank_1_gui[index]="r"
            elif coor.occupied_by == "b_bishop":
                rank_1_gui[index]="b"
            elif coor.occupied_by == "w_bishop":
                rank_1_gui[index]="B"
            elif coor.occupied_by == "w_king":
                rank_1_gui[index]="K"
            elif coor.occupied_by == "b_king":
                rank_1_gui[index]="k"
            elif coor.occupied_by == "w_knight":
                rank_1_gui[index]="Kn"
            elif coor.occupied_by == "b_knight":
                rank_1_gui[index]="kn"

    for index,coor in enumerate(rank_2_tuple):
        if coor.occupied == True:
            if coor.occupied_by == "b_pawn":
                rank_2_gui[index]="P"
            elif coor.occupied_by == "w_pawn":
                rank_2_gui[index]="A"
            elif coor.occupied_by == "w_queen":
                rank_2_gui[index]="Q"
            elif coor.occupied_by == "b_queen":
                rank_2_gui[index]="q"
            elif coor.occupied_by == "w_rook":
                rank_2_gui[index]="R"
            elif coor.occupied_by == "b_rook":
                rank_2_gui[index]="r"
            elif coor.occupied_by == "b_bishop":
                rank_2_gui[index]="b"
            elif coor.occupied_by == "w_bishop":
                rank_2_gui[index]="B"
            elif coor.occupied_by == "w_king":
                rank_2_gui[index]="K"
            elif coor.occupied_by == "b_king":
                rank_2_gui[index]="k"
            elif coor.occupied_by == "w_knight":
                rank_2_gui[index]="Kn"
            elif coor.occupied_by == "b_knight":
                rank_2_gui[index]="kn"

    for index,coor in enumerate(rank_3_tuple):
        if coor.occupied == True:
            if coor.occupied_by == "b_pawn":
                rank_3_gui[index]="P"
            elif coor.occupied_by == "w_pawn":
                rank_3_gui[index]="A"
            elif coor.occupied_by == "w_queen":
                rank_3_gui[index]="Q"
            elif coor.occupied_by == "b_queen":
                rank_3_gui[index]="q"
            elif coor.occupied_by == "w_rook":
                rank_3_gui[index]="R"
            elif coor.occupied_by == "b_rook":
                rank_3_gui[index]="r"
            elif coor.occupied_by == "b_bishop":
                rank_3_gui[index]="b"
            elif coor.occupied_by == "w_bishop":
                rank_3_gui[index]="B"
            elif coor.occupied_by == "w_king":
                rank_3_gui[index]="K"
            elif coor.occupied_by == "b_king":
                rank_3_gui[index]="k"
            elif coor.occupied_by == "w_knight":
                rank_3_gui[index]="Kn"
            elif coor.occupied_by == "b_knight":
                rank_3_gui[index]="kn"

    for index,coor in enumerate(rank_4_tuple):
        if coor.occupied == True:
            if coor.occupied_by == "b_pawn":
                rank_4_gui[index]="P"
            elif coor.occupied_by == "w_pawn":
                rank_4_gui[index]="A"
            elif coor.occupied_by == "w_queen":
                rank_4_gui[index]="Q"
            elif coor.occupied_by == "b_queen":
                rank_4_gui[index]="q"
            elif coor.occupied_by == "w_rook":
                rank_4_gui[index]="R"
            elif coor.occupied_by == "b_rook":
                rank_4_gui[index]="r"
            elif coor.occupied_by == "b_bishop":
                rank_4_gui[index]="b"
            elif coor.occupied_by == "w_bishop":
                rank_4_gui[index]="B"
            elif coor.occupied_by == "w_king":
                rank_4_gui[index]="K"
            elif coor.occupied_by == "b_king":
                rank_4_gui[index]="k"
            elif coor.occupied_by == "w_knight":
                rank_4_gui[index]="Kn"
            elif coor.occupied_by == "b_knight":
                rank_4_gui[index]="kn"

    for index,coor in enumerate(rank_5_tuple):
        if coor.occupied == True:
            if coor.occupied_by == "b_pawn":
                rank_5_gui[index]="P"
            elif coor.occupied_by == "w_pawn":
                rank_5_gui[index]="A"
            elif coor.occupied_by == "w_queen":
                rank_5_gui[index]="Q"
            elif coor.occupied_by == "b_queen":
                rank_5_gui[index]="q"
            elif coor.occupied_by == "w_rook":
                rank_5_gui[index]="R"
            elif coor.occupied_by == "b_rook":
                rank_5_gui[index]="r"
            elif coor.occupied_by == "b_bishop":
                rank_5_gui[index]="b"
            elif coor.occupied_by == "w_bishop":
                rank_5_gui[index]="B"
            elif coor.occupied_by == "w_king":
                rank_5_gui[index]="K"
            elif coor.occupied_by == "b_king":
                rank_5_gui[index]="k"
            elif coor.occupied_by == "w_knight":
                rank_5_gui[index]="Kn"
            elif coor.occupied_by == "b_knight":
                rank_5_gui[index]="kn"

    for index,coor in enumerate(rank_6_tuple):
        if coor.occupied == True:
            if coor.occupied_by == "b_pawn":
                rank_6_gui[index]="P"
            elif coor.occupied_by == "w_pawn":
                rank_6_gui[index]="A"
            elif coor.occupied_by == "w_queen":
                rank_6_gui[index]="Q"
            elif coor.occupied_by == "b_queen":
                rank_6_gui[index]="q"
            elif coor.occupied_by == "w_rook":
                rank_6_gui[index]="R"
            elif coor.occupied_by == "b_rook":
                rank_6_gui[index]="r"
            elif coor.occupied_by == "b_bishop":
                rank_6_gui[index]="b"
            elif coor.occupied_by == "w_bishop":
                rank_6_gui[index]="B"
            elif coor.occupied_by == "w_king":
                rank_6_gui[index]="K"
            elif coor.occupied_by == "b_king":
                rank_6_gui[index]="k"
            elif coor.occupied_by == "w_knight":
                rank_6_gui[index]="Kn"
            elif coor.occupied_by == "b_knight":
                rank_6_gui[index]="kn"

    for index,coor in enumerate(rank_7_tuple):
        if coor.occupied == True:
            if coor.occupied_by == "b_pawn":
                rank_7_gui[index]="P"
            elif coor.occupied_by == "w_pawn":
                rank_7_gui[index]="A"
            elif coor.occupied_by == "w_queen":
                rank_7_gui[index]="Q"
            elif coor.occupied_by == "b_queen":
                rank_7_gui[index]="q"
            elif coor.occupied_by == "w_rook":
                rank_7_gui[index]="R"
            elif coor.occupied_by == "b_rook":
                rank_7_gui[index]="r"
            elif coor.occupied_by == "b_bishop":
                rank_7_gui[index]="b"
            elif coor.occupied_by == "w_bishop":
                rank_7_gui[index]="B"
            elif coor.occupied_by == "w_king":
                rank_7_gui[index]="K"
            elif coor.occupied_by == "b_king":
                rank_7_gui[index]="k"
            elif coor.occupied_by == "w_knight":
                rank_7_gui[index]="Kn"
            elif coor.occupied_by == "b_knight":
                rank_7_gui[index]="kn"

    for index,coor in enumerate(rank_8_tuple):
        if coor.occupied == True:
            if coor.occupied_by == "b_pawn":
                rank_8_gui[index]="P"
            elif coor.occupied_by == "w_pawn":
                rank_8_gui[index]="A"
            elif coor.occupied_by == "w_queen":
                rank_8_gui[index]="Q"
            elif coor.occupied_by == "b_queen":
                rank_8_gui[index]="q"
            elif coor.occupied_by == "w_rook":
                rank_8_gui[index]="R"
            elif coor.occupied_by == "b_rook":
                rank_8_gui[index]="r"
            elif coor.occupied_by == "b_bishop":
                rank_8_gui[index]="b"
            elif coor.occupied_by == "w_bishop":
                rank_8_gui[index]="B"
            elif coor.occupied_by == "w_king":
                rank_8_gui[index]="K"
            elif coor.occupied_by == "b_king":
                rank_8_gui[index]="k"
            elif coor.occupied_by == "w_knight":
                rank_8_gui[index]="Kn"
            elif coor.occupied_by == "b_knight":
                rank_8_gui[index]="kn"

    print(whos_turn)
    print("8",rank_8_gui)
    print("7",rank_7_gui)
    print("6",rank_6_gui)
    print("5",rank_5_gui)
    print("4",rank_4_gui)
    print("3",rank_3_gui)
    print("2",rank_2_gui)
    print("1",rank_1_gui)
    return (file_axis)

print(turn())
