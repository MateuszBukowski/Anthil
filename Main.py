from random import random
from os import system

class Anthill():

    def __init__(self, x=30, y=30, name='Unknown'):
        self.x = x
        self.y = y
        self.name = name
        self.board_x = (self.x * 2) + 5
        self.board_y = self.y * 2
        self.field = []

    def make_new_field(self, ):
        self.xy_list = []
        self.y_list = []
        for point_x in range(self.x):
            for point_y in range(self.y):
                self.y_list.insert(point_y, 0)
            self.xy_list.append(self.y_list)
            self.y_list = []
        return self.xy_list
    
    def print_anthill(self, field):
        for line in field:
            print('* ', end=' ')
            for column in line:
                print(column, end=' ')
            print(' *')
        print('*' + (self.board_x - 2) * ' ' + '*')

    def print_header(self):
        print(self.board_x * '*')
        print('*' + (self.board_x - 2) * ' ' + '*')
        print('* Welcome to anthill: ', self.name)
        print('*' + (self.board_x - 2) * ' ' + '*')
        print(self.board_x * '*')

    def print_footer(self):
        print(self.board_x * '*')


def clear_screen():
    system('cls')




clear_screen

test_anhill = Anthill(x=30, y=30, name='Long time ago in grass')
test_anhill.field = test_anhill.make_new_field()
test_anhill.print_header()
test_anhill.print_anthill(test_anhill.field)
test_anhill.print_footer()


