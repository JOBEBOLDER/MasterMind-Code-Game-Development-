import time
import turtle
from Marble import Marble
from Point import Point
import random

# 生成画板
def draw_main_board():
    # initialize the screen
    screen = turtle.Screen()
    screen.title("Welcome To Kitu's MindMaster Code GAME!!")
    turtle.screensize(800, 900)
    turtle.setup(800, 900)

    # pen control 创建画笔
    pen = turtle.Turtle()
    pen.speed(10)  # fast speed:10,normal:6

    pen.up()
    pen.goto(-380, 400)
    pen.pendown()
    pen.color('black')
    pen.width(7)
    pen.fd(500)
    pen.right(90)
    pen.fd(630)
    pen.right(90)
    pen.fd(500)
    pen.right(90)
    pen.fd(630)

    # pen.goto(0, 0)
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
    pen.goto(368, -245)  # 紫色框的起始位置
    pen.down()
    pen.color('purple')
    pen.width(7)
    pen.forward(750)  # 紫色框的宽度
    pen.right(90)
    pen.forward(-180)  # 紫色框的高度
    pen.right(90)
    pen.forward(750)  # 返回起点的相反方向
    pen.right(90)
    pen.forward(-180)  # 完成框的四边


# 生成两个button，用于user确认和删除
def draw_buttons():
    screen = turtle.Screen()
    turtle.tracer(0)
    screen.addshape('checkbutton.gif')
    # 创建一个新的 Turtle 对象来显示图像
    img_turtle = turtle.Turtle()
    img_turtle.up()  # 确保不在移动时绘制线条
    img_turtle.shape('checkbutton.gif')  # 设置形状为图像
    img_turtle.goto(100, -320)  # 移动到指定位置
    screen.addshape('xbutton.gif')
    img_turtle = turtle.Turtle()
    img_turtle.up()
    img_turtle.shape('xbutton.gif')
    img_turtle.goto(180, -320)
    screen.addshape('quit.gif')
    img_turtle = turtle.Turtle()
    img_turtle.up()
    img_turtle.shape('quit.gif')
    img_turtle.goto(280, -320)
# 随机生成4个颜色
def secret_code(color, length=4):
    return random.sample(color, length)
# 初始化6个颜色选择，
def color_choices(color):
    turtle.tracer(0)
    x = -300
    y = -350
    for i in color:
        a = Marble(Point(x, y), 'black', size=15)
        a.set_color(i)
        a.draw()
        m_color_circle_list.append(a)
        x = x + 40
    turtle.update()
# 把圆圈实例化，给用户点击用的
def draw_circle_1():
    turtle.tracer(0)
    y = 300
    x = -300
    for i in range(10):  # 十次大循环
        m_item_list = []
        x_0 = x
        for j in range(4):
            m = Marble(Point(x_0, y), 'black')
            m.draw_empty()
            m_item_list.append(m)
            x_0 = x_0 + 60
        x_1 = x_0 + 50
        small_m_item_list = []
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
        m_list.append(m_item_list)
        small_m_list.append(small_m_item_list)
        turtle.update()
def fill_color(color_circle):
    global need_check_answer
    for i in m_list:
        for j, k in enumerate(i):
            if k.is_empty == True and need_check_answer == 0:
                # 检查是否点击了颜色选择区域
                selected_color = color_circle.get_color()
                color_circle.draw_empty()
                if k.is_empty:  # 检查圆圈是否未上色
                    k.set_color(selected_color)
                    k.draw()
                    k.is_empty = False  # 标记为已上色
                if j == 3:
                    need_check_answer = 1
                return
            elif need_check_answer == 1:
                print("you need to check answer,otherwise u cant not continue the game")
                return
            else:
                continue
def confirm_answer():
    global need_check_answer
    global game_count
    if need_check_answer == 1:
        get_current_color = lambda m_list, game_count: [i.color for i in m_list[game_count]]
        current_color = get_current_color(m_list, game_count)
        print(f"current_color:{current_color}")
        print(f"correct_color:{correct_color}")
        black = 0
        red = 0
        for i, k in enumerate(current_color):
            for j, l in enumerate(correct_color):
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
        for i,j in enumerate(small_circle_color):
            small_circle = small_m_list[game_count][i]
            small_circle.set_color(j)
            small_circle.draw()
        need_check_answer = 0
        game_count += 1
        if black == 4:
            write_leaderboard(username, game_count)
        color_choices(color)
def load_leaderboard():
    screen = turtle.Screen()
    s = turtle.Turtle()
    s.goto(150, 100)
    try:
        with open("leaderboard.txt", 'r') as f:
            text = ""
            lines = f.readlines()
            for i in lines:
                text = text + i + '\n'
            turtle.write(text)
    except Exception as e:
        print(e.__traceback__)
def write_leaderboard(username,game_count):
    # 弹出you win
    print("你赢了")
    screen = turtle.Screen()
    screen.title('success')
    screen.addshape('winner.gif')
    win_msg_turtle = turtle.Turtle()
    win_msg_turtle.up()
    win_msg_turtle.shape('winner.gif')
    win_msg_turtle.goto(100, 100)

    try:
        with open("leaderboard.txt", 'a') as f:
            f.write(f"{username} {game_count}")
    except Exception as e:
        print(e.__traceback__)


# 退出游戏
def on_quit_button_click():
    # 弹出退出的信息提示
    print("quit")
    screen = turtle.Screen()
    screen.title('退出')
    screen.addshape('quitmsg.gif')
    quit_msg_turtle = turtle.Turtle()
    quit_msg_turtle.up()
    quit_msg_turtle.shape('quitmsg.gif')
    quit_msg_turtle.goto(100, 100)


def handle_click(x, y):
    check_button_x = [100 - 22, 100 + 22]
    check_button_y = [-320 - 40, -320 + 40]
    quit_button_x = [280 - 40, 280 + 40]
    quit_button_y = [-320 - 22, -320 + 22]
    if check_button_x[0] <= x <= check_button_x[1] and check_button_y[0] <= y <= check_button_y[1]:
        confirm_answer()
    elif quit_button_x[0] <= x <= quit_button_x[1] and quit_button_y[0] <= y <= quit_button_y[1]:
        on_quit_button_click()
    else:
        for color_circle in m_color_circle_list:
            if color_circle.clicked_in_region(x, y):
                fill_color(color_circle)


if __name__ == '__main__':
    # 主要的main game loop，并且handle 点击事件
    # 6个colors choices
    m_color_circle_list = []
    m_list = []
    small_m_list = []
    color = ['black', 'red', 'yellow', 'blue', 'purple', 'green']
    need_check_answer = 0
    game_count = 0
    correct_color = secret_code(color)
    color_choices(color)

    username = turtle.textinput("username", ' Name of the player:')
    draw_main_board()
    draw_buttons()
    draw_circle_1()
    load_leaderboard()
    turtle.onscreenclick(handle_click)

    print("Click handlers set up. Entering main loop.")
    turtle.mainloop()
