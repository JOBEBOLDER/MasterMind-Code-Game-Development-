import turtle

from game_function import GameFunction
from game_ui import GameUi


class Game:
    username = ''
    game_count = 0
    color = ['black', 'red', 'yellow', 'blue', 'purple', 'green']
    m_list = []
    m_color_circle_list = []
    small_m_list = []
    need_check_answer = 0

    def __init__(self) -> None:
        super().__init__()
        # initialize the screen
        self.screen = turtle.Screen()
        self.leaderboard_pen = turtle.Turtle()
        self.game_ui = GameUi(self.screen)
        self.username = self.game_ui.get_username()
        self.game_ui.draw_main_board()
        self.m_list, self.small_m_list = self.game_ui.draw_circle_1()
        self.game_ui.draw_buttons()
        self.m_color_circle_list = self.game_ui.color_choices(self.color)
        self.game_func = GameFunction(self.screen, self.leaderboard_pen)
        self.correct_color = self.game_func.secret_code(self.color)
        self.game_func.load_leaderboard()

    def handle_click(self, x, y):
        check_button_x = [60 - 22, 60 + 22]
        check_button_y = [-325 - 40, -325 + 40]

        delete_button_x = [130 - 22, 130 + 22]
        delete_button_y = [-325 - 40, -325 + 40]

        quit_button_x = [280 - 40, 280 + 40]
        quit_button_y = [-325 - 22, -325 + 22]

        if check_button_x[0] <= x <= check_button_x[1] and check_button_y[0] <= y <= check_button_y[1]:
            print("123")
            result, self.game_count, self.need_check_answer = self.game_func.confirm_answer(self.need_check_answer, self.correct_color, self.game_count, self.m_list, self.small_m_list)
            self.game_func.reset_color_circle(self.color, self.m_color_circle_list)

            if result == 'success':
                current_rank = self.game_func.load_leaderboard()
                self.game_func.write_leaderboard(self.username, self.game_count, current_rank)
                current_rank = self.game_func.load_leaderboard()

            if self.game_count == 10 and result == 'failed':
                self.game_ui.lose_ui()


        elif quit_button_x[0] <= x <= quit_button_x[1] and quit_button_y[0] <= y <= quit_button_y[1]:
            self.game_ui.on_quit_button_click()

        elif delete_button_x[0] <= x <= delete_button_x[1] and delete_button_y[0] <= y <= delete_button_y[1]:
            self.need_check_answer,self.m_color_circle_list = self.game_func.delete_answer(self.game_count, self.m_list, self.m_color_circle_list,self.need_check_answer,self.color)
            # self.game_func.reset_color_circle(self.color, self.m_color_circle_list)

        else:
            for color_circle in self.m_color_circle_list:
                if color_circle.clicked_in_region(x, y) and color_circle.is_empty is False:
                    self.need_check_answer = self.game_func.fill_color(self.game_count, color_circle, self.m_list, self.need_check_answer)


if __name__ == '__main__':
    game = Game()
    turtle.onscreenclick(game.handle_click)
    print("Click handlers set up. Entering main loop.")
    turtle.mainloop()
