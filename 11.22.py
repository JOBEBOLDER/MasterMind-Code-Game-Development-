import turtle
from Marble import Marble
from Point import Point
import random


# get username from the input
def userinput():
    username = turtle.textinput("username", ' Name of the player:')

    if username:
        with open('leaderboard.txt', 'a') as file:
            file.write(username + '\n')

    return username



#生成画板
def draw_main_board():
        # initialize the screen
        #leaderboard的tittle
        pen = turtle.Turtle()
        pen.speed(10)

        screen = turtle.Screen()
        screen.title("Welcome To Kitu's MindMaster Code GAME!!")
        turtle.screensize(800, 900)
        turtle.setup(800, 900)

        # pen control 创建画笔
         # fast speed:10,normal:6

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


        # pen.goto(0, 0)蓝色框leaderboard
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
        x = 230
        y = 355
        turtle.hideturtle()
        pen.up()
        pen.goto(x, y)
        pen.color('blue')
        info = 'Leader Board'
        turtle.pencolor('blue')
        pen.write("Leader Board", align="center", font=("Arial", 25, "normal"))


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

#生成两个button，用于user确认和删除
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
    turtle.hideturtle()

def draw_circle_1():
    turtle.tracer(0)
    y = 300
    x = -300
    for i in range(10):#十次大循环
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


#把圆圈实例化，给用户点击用的


#主要的main game loop，并且handle 点击事件
# 全局变量
selected_color = ""
click_count = 0

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


def fill_color(color_circle):
    global need_check_answer, click_count
    if need_check_answer == 0:
        selected_color = color_circle.get_color()
        current_round = m_list[game_count]
        if click_count < len(current_round):
            marble = current_round[click_count]
            marble.set_color(selected_color)
            marble.draw()
            marble.is_empty = False
            click_count += 1
            if click_count == len(current_round):
                need_check_answer = 1


def get_current_color(m_list, game_count):
    colors = []
    for marble in m_list[game_count]:
        colors.append(marble.color)
    return colors


#这个函数不是很懂
def confirm_answer():
    global need_check_answer, game_count, click_count
    if need_check_answer == 1:
        current_color =get_current_color(m_list, game_count)
        print(f'current_color:{current_color}')
        print(f'correct_color:{correct_color}')

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

        for i, j in enumerate(small_circle_color):
            small_circle = small_m_list[game_count][i]
            small_circle.set_color(j)
            small_circle.draw()

        need_check_answer = 0
        game_count += 1

        if black == 4:
            write_leaderboard(username, game_count)
            color_choices(color)  # 仅调用一次
            need_check_answer = 0
            game_count += 1
            click_count = 0  # 重置 click_count 为下一轮做准备

def load_leaderboard():
    screen = turtle.Screen()
    s = turtle.Turtle()
    s.hideturtle()
    s.up()
    s.goto(150,100)

    try:
        with open('leaderboard.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                s.write(line, move=False, align="left", font=("Arial", 12, "normal"))
                s.sety(s.ycor() - 20)
    except Exception as e:
        print('Error:', e)


def write_leaderboard(username, game_count):
    print('you win!')
    screen = turtle.Screen()
    screen.addshape('winner.gif')
    win_turtle = turtle.Turtle
    win_turtle.up()
    win_turtle.shape('winner.gif')
    win_turtle.goto(0, 0)

    try:
        with open("leaderboard.txt", 'a') as f:
            f.write(f"{username} {game_count}")

    # 找不到leaderboard文件报错
    except Exception as e:
        screen.title('Error')
        screen.addshape('file_error.gif')

        msg_turtle = turtle.Turtle()
        msg_turtle.up()
        msg_turtle.shape('file_error.gif')
        msg_turtle.goto(0, 0)

        screen.onclick(lambda x, y: screen.bye())

        screen.mainloop()



def on_quit_button_click():
    print("quit")
    # 使用已经存在的屏幕对象
    global screen
    if 'quitmsg.gif' not in screen.getshapes():
        screen.addshape('quitmsg.gif')
    quit_turtle = turtle.Turtle()
    quit_turtle.up()
    quit_turtle.shape('quitmsg.gif')
    quit_turtle.goto(0, 0)



if __name__ == '__main__':
    #首先获取用户名
    username = userinput()


    # 初始化全局变量
    # 6个colors choices,主要的main game loop，并且handle 点击事件
    screen = turtle.Screen()
    m_color_circle_list = []
    m_list = []
    small_m_list = []
    color = ['black', 'red', 'yellow', 'blue', 'purple', 'green']
    need_check_answer = 0
    game_count = 0
    correct_color = secret_code(color)

    # 用户名输入完成猴，开始绘制游戏界面
    draw_main_board()
    draw_circle_1()
    load_leaderboard()
    draw_buttons()


    #初始化颜色选择区
    color_choices(color)

    # 设置点击事件处理器
    turtle.onscreenclick(handle_click)

    # 启动turtle主循环
    turtle.mainloop()
    turtle.done()





