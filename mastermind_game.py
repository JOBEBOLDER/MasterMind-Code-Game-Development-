"""
CS5001
    Fall 2023
    jieyao chen
    final project :mastermind code game

"""
import turtle
import other necessary libraries

#define global variables/constants
LEADERBOARD_FILE = 'leaderboard.txt'
ERROR_LOG_FILE = 'mastermind_errors.err'
#define other necessary global variables

#define necessary classes(point,marble,etc)based on starter code
class Point:
    #class definition


class Marble:



class Board:



# define main game class:
class MastermindGame:
    def __init__(self):
        #initialize game state and Turtle graphics setup
        self.setup_graphics()
        self.load_leaderboard()

    def setup_graphics(self):
        # set up turtle graphics window,buttons ,and board
        #初始化界面，popup，userinput界面
        #加载顺序：三个框，底部buttons，然后10个空白圈循环，然后最后是6个颜色圈，



    def loar_leaderboard(self):
        #load leaderboard from file or create new file

    def start_game(self):
        # main game loop

    def draw_board(self):
        # draw game board with all elements

    def handle_guess(self):
        # handle player's guess logic

    def update_leaderboard(self):
        # update leaderboard with new scores

    def save_leaderboard(self):
        # save current leaderboard to file

    def display_error(self):
        # log error to error log file

    def log_error(self,error):
        # log error to error log file


    def quit_game(self):
        #break game


def get_user_name():
    # get player name through a popup

def main():
    game = MastermindGame()
    game.start_game()


