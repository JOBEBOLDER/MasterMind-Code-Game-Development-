"""
CS5001
   Fall 2023
   Jieyao chen
   final project: MasterMind Code Game
   will create functions that use lists to create, shuffle,
   and deal cards to a number up to 4 “hands”.
"""

#
import turtle
from Marble import Marble
from Point import Point
import random


# 生成画板
def draw_main_board():
    """
    Draw all rectangles of the main game board
    :return:none
    """
    global screen
    screen.title("Welcome To Kitu's MindMaster Code GAME!!")
    turtle.screensize(800, 900)
    turtle.setup(800, 900)

    # pen control
    pen = turtle.Turtle()
    pen.speed(10)  # fast speed:10,normal:6

    pen.up()
    pen.goto(-380, 400)
    pen.pendown()
    pen.color('black')  # start position of the purple square
    pen.width(7)
    pen.fd(500)  # the width
    pen.right(90)
    pen.fd(630)  # the height
    pen.right(90)
    pen.fd(500)
    pen.right(90)
    pen.fd(630)  # finish drawing the four sides

    pen.up()
    pen.goto(135, 400)
    pen.pendown()
    pen.color('blue')
    pen.width(7)
    pen.fd(-630)
    pen.right(90)
    pen.fd(230)
    pen.right(90)
    pen.fd(-630)
    pen.right(90)
    pen.fd(230)

    pen.up()
    pen.speed(10)
    pen.goto(368, -245)
    pen.down()
    pen.color('purple')
    pen.width(7)
    pen.forward(750)
    pen.right(90)
    pen.forward(-180)
    pen.right(90)
    pen.forward(750)
    pen.right(90)
    pen.forward(-180)


# 生成两个button，用于user确认和删除
def draw_buttons():
    """
    A set of clickable, colored guess buttons that
    allows a player to choose one color at a time for a guess,
    no  duplicate colors
    :return: none
    """
    # checkbutton.gif
    # Create a new Turtle object to display the image
    screen.addshape('checkbutton.gif')
    img_turtle = turtle.Turtle()
    img_turtle.up()  # make sure don't draw line while drawing
    img_turtle.shape('checkbutton.gif')  # register the shape is the image
    img_turtle.goto(100, -320)  # move the gif to the position

    # xbutton.gif
    screen.addshape('xbutton.gif')
    img_turtle = turtle.Turtle()
    img_turtle.up()
    img_turtle.shape('xbutton.gif')
    img_turtle.goto(180, -320)

    # quit.gif
    screen.addshape('quit.gif')
    img_turtle = turtle.Turtle()
    img_turtle.up()
    img_turtle.shape('quit.gif')
    img_turtle.goto(280, -320)


def secret_code(color, length=4):
    """
    # randomly generate 4 different colors
    :param color: generate from the original color list:
    color = ['black', 'red', 'yellow', 'blue', 'purple', 'green']
    :param length: amount:4
    :return: the generated result
    """
    return random.sample(color, length)


def color_choices(color):
    """
    # Initializing and drawing 6 color choices area
    :param color: the color list
    :return:none
    """
    turtle.tracer(0)  # cancel the animation effect
    # the starting position of the selection circle area
    x = -250
    y = -345
    for i in color:
        a = Marble(Point(x, y), i, size=15)
        a.draw()
        m_color_circle_list.append(a)
        x = x + 40
    turtle.update()


# Instantiate the circle for users to click on
def draw_circle_1():
    turtle.tracer(0)
    y = 300
    x = -250
    add_arrow(x-50, y+13)
    for i in range(10):  # ten loops
        m_item_list = []  # the four circles list
        x_0 = x
        for j in range(4):
            m = Marble(Point(x_0, y), 'black')
            m.draw_empty()
            m_item_list.append(m)
            x_0 = x_0 + 60
        x_1 = x_0 + 50
        small_m_item_list = []  # the small circles list
        x_2 = x_1
        for _ in range(2):
            small_m = Marble(Point(x_2, y + 18), 'black', size=5)
            small_m.draw_empty()
            small_m_item_list.append(small_m)
            x_2 = x_2 + 15
        x_3 = x_1
        for _ in range(2):
            small_m = Marble(Point(x_3, y - 2), 'black', size=5)
            small_m.draw_empty()
            small_m_item_list.append(small_m)
            x_3 = x_3 + 15

        y = y - 50
        guessing_list.append(m_item_list)
        feedback_list.append(small_m_item_list)
        turtle.update()


def reset_color_circle():
    for i, marble in enumerate(m_color_circle_list):
        marble.set_color(COLOR[i])
        marble.draw()


def fill_color(color_circle):
    global need_check_answer
    print(game_count)
    for j, k in enumerate(guessing_list[game_count]):
        if k.is_empty is True and need_check_answer == 0:
            # 获取玩家选择的颜色
            selected_color = color_circle.get_color()
            print(selected_color)
            #使颜色选择圆圈变为空，表示这个颜色已被选择
            color_circle.draw_empty()

            if k.is_empty:  # 检查圆圈是否未上色
                k.set_color(selected_color)
                k.draw()
            if j == 3:
                need_check_answer = 1

            return
        # 表示选的圆圈还没到4个，需要check answer
        elif need_check_answer == 1:
            print("you need to check answer,otherwise u cant not continue the game")
            return

        else:
            continue


def confirm_answer():
    """
    When the player completes a round of color guessing,
    this function is called to check the correctness
    of the guess and give appropriate feedback based on the results.
    :return: none
    """
    global need_check_answer
    global game_count

    # check if need to check answers
    if need_check_answer == 1:
        current_round_circles = guessing_list[game_count]
        current_color = []
        for circle in current_round_circles:
            current_color.append(circle.color)
        print(f"current_color:{current_color}")
        print(f"correct_color:{correct_color}")
        #
        black = 0
        red = 0
        for i, k in enumerate(current_color):
            for j, l in enumerate(correct_color):
                # 在颜色相同的情况下，再比较内部的索引（位置情况）
                if l == k:
                    if i == j:
                        black += 1
                    else:
                        red += 1
        white = 4 - black - red
        print(black, red, white)

        small_circle_color = []
        for i in range(black):
            small_circle_color.append('black')
        for i in range(red):
            small_circle_color.append('red')
        for i in range(white):
            small_circle_color.append('white')
        print(small_circle_color)
        for i, j in enumerate(small_circle_color):
            small_circle = feedback_list[game_count][i]
            small_circle.set_color(j)
            small_circle.draw()

        arrow_x = current_round_circles[0].position.x - 55
        arrow_y = current_round_circles[0].position.y - 35
        add_arrow(arrow_x, arrow_y)
        # 重置，表示可以下一轮的猜测
        need_check_answer = 0
        game_count += 1
        # 如果猜对了所有颜色位置（black=4）调用win函数
        if black == 4:
            win(username, game_count)
        else:
            if game_count == 10:
                lose()
                correct_answer = (turtle.textinput
                                  ("correct answer",
                                   f"{correct_color}"))

        reset_color_circle()


def add_arrow(x, y):
    global screen
    screen.addshape('images.gif')
    arrow_msg_turtle = turtle.Turtle()
    arrow_msg_turtle.up()
    arrow_msg_turtle.shape('images.gif')
    arrow_msg_turtle.goto(x, y)
    turtle.update()


def delete_answer(game_count,color):
    global need_check_answer
    # Starting from the last one, find the first already filled circle
    for marble in reversed(guessing_list[game_count]):
        if not marble.is_empty:
            # 重置这个圆圈为未填充状态
            marble.draw_empty()
            need_check_answer = 0
            reset_color = marble.get_color()
            m_color_circle_list[color.index(reset_color)].set_color(reset_color)
            m_color_circle_list[color.index(reset_color)].draw()
            break


def load_leaderboard():
    global pen
    pen.clear()
    pen.up()
    user_rank_dic = {}

    # processing of ranking list information
    try:
        with open("leaderboard.txt", 'r') as f:
            lines = f.readlines()

            # Create an empty list to store tuples of (score, row)
            score_line_pairs = []

            # Iterate through each row, extract scores and store them with the rows
            for line in lines:
                parts = line.split(':')
                score = int(parts[0])
                score_line_pairs.append((score, line))

            # sorting based on scores
            # score_line_pairs.sort(key=lambda pair: pair[0])
            score_line_pairs.sort()
            print(score_line_pairs)
            # Extract sorted rows from sorted list
            # sorted_lines = [pair[1] for pair in score_line_pairs]
            # print(sorted_lines)
            top_five = score_line_pairs[:5]

            # move to the start of the title
            pen.goto(150, 360)
            pen.color('blue')
            pen.write("Leaderboard:", font=("Arial", 22, "italic"))

            # write the leaderboard
            y_offset = -30
            for i in top_five:
                a = i[1].split(':')
                user_rank_dic[a[1]] = a[0].strip()
                pen.goto(155, 330 + y_offset)
                pen.write(a[0] + ': ' + a[1], font=("Arial", 18, "normal"))
                y_offset = y_offset - 30  # move to the next line

            return user_rank_dic

    except Exception as e:
        print(e)
        print(e.__traceback__.tb_lineno)


def win(username, game_count):
    # 弹出you win
    print("YOU WIN!!!")
    # 使用已经存在的屏幕对象
    global screen
    if 'winner.gif' not in screen.getshapes():
        screen.addshape('winner.gif')
    win_msg_turtle = turtle.Turtle()
    win_msg_turtle.up()
    win_msg_turtle.shape('winner.gif')
    win_msg_turtle.goto(0, 0)
    turtle.update()

    current_rank = load_leaderboard()
    print(current_rank)
    try:
        before_rank = current_rank[username]
        if game_count < before_rank:
            current_rank[username] = game_count
        with open("leaderboard.txt", 'w') as f:
            for key, value in current_rank.items():
                f.write(f"{key},{value}\n")
    except KeyError:
        with open("leaderboard.txt", 'a') as f:
            f.write(f"{game_count}:{username}\n")

    load_leaderboard()


# pop out the lose game message
def lose():
    print("you lost!")
    global screen
    if 'Lose.gif' not in screen.getshapes():
        screen.addshape('Lose.gif')
    lose_msg_turtle = turtle.Turtle()
    lose_msg_turtle.up()
    lose_msg_turtle.shape('Lose.gif')
    lose_msg_turtle.goto(0, 0)
    turtle.update()

# 退出游戏
def on_quit_button_click():
    # 弹出退出的信息提示
    screen.title('QUIT')
    screen.addshape('quitmsg.gif')
    quit_msg_turtle = turtle.Turtle()
    quit_msg_turtle.up()
    quit_msg_turtle.shape('quitmsg.gif')
    quit_msg_turtle.goto(0, 0)
    turtle.update()


def handle_click(x, y):
    """
    the main game loop,and handle the clicking events
    :param x:
    :param y:
    :return:none
    """
    check_button_x = [100 - 22, 100 + 22]
    check_button_y = [-320 - 40, -320 + 40]

    delete_button_x = [180 - 22, 180 + 22]
    delete_button_y = [-320 - 40, -320+40]

    quit_button_x = [280 - 40, 280 + 40]
    quit_button_y = [-320 - 22, -320 + 22]

    if check_button_x[0] <= x <= check_button_x[1] and check_button_y[0] <= y <= check_button_y[1]:
        confirm_answer()

    elif quit_button_x[0] <= x <= quit_button_x[1] and quit_button_y[0] <= y <= quit_button_y[1]:
        on_quit_button_click()

    elif delete_button_x[0] <= x <= delete_button_x[1] and delete_button_y[0] <= y <= delete_button_y[1]:
        delete_answer(game_count, COLOR)

    else:
        for color_circle in m_color_circle_list:
            if color_circle.clicked_in_region(x, y) and color_circle.is_empty is False:
                fill_color(color_circle)



if __name__ == '__main__':
    # Stores the circle of the color selection region.
    m_color_circle_list = []

    # Storage player speculations
    guessing_list = []

    # Storing feedback, i.e. indications of "bulls" and "cows".
    feedback_list = []

    # the original colors list
    COLOR = ['black', 'red', 'yellow', 'blue', 'purple', 'green']

    # 这是一个标志变量，用于指示是否需要对当前玩家的猜测进行检查。
    # 通常在玩家完成一次猜测后设置为1，表示需要评估猜测结果。
    need_check_answer = 0

    # 这个变量用于追踪玩家已经进行了多少次猜测。
    # 它在游戏过程中递增，并可能用于限制猜测次数或用于评估玩家的表现。
    game_count = 0

    # This is a secret color code generated by the secret_code function,
    # and the player needs to guess the combination.
    correct_color = secret_code(COLOR)
    #测试用
    print(correct_color)

    # initialize the screen,user can input their names
    screen = turtle.Screen()
    username = turtle.textinput("username", ' Name of the player:')

    # the functions to be called:
    draw_main_board()
    color_choices(COLOR)
    draw_buttons()
    draw_circle_1()
    pen = turtle.Turtle()
    load_leaderboard()
    turtle.onscreenclick(handle_click)

    print("Click handlers set up. Entering main loop.")
    turtle.mainloop()
