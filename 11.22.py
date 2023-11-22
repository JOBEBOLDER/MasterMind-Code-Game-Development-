import turtle
from Marble import Marble
from Point import Point
import random


# get username from the input
def userinput():
    turtle.textinput("username", ' Name of the player:')


# def load_leaderboard(self):
#     # Load leaderboard from file or create new file
#     try

# 随机生成4个颜色
def secret_code(color, length=4):
    return random.sample(color, length)

#生成画板
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


# 6个colors choices
m_color_circle_list = []
m_list = []
small_m_list = []

# 初始化6个颜色选择，
def color_choices():
    turtle.tracer(0)
    color = ['black', 'red', 'yellow', 'blue', 'purple', 'green']
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

#主要的main game loop，并且handle 点击事件
# 全局变量
selected_color = ""
def start_game(x, y):
    global selected_color, m_list

    # 检查是否点击了颜色选择区域
    for color_circle in m_color_circle_list:
        if color_circle.clicked_in_region(x, y):
            selected_color = color_circle.get_color()
            color_circle.set_color('white')
            color_circle.draw()
            break  # 退出循环，因为已经找到点击的颜色

    # 如果已选择颜色，并且存在未上色的圆圈
    if selected_color and m_list:
        for marble_row in m_list:
            for marble in marble_row:
                if marble.is_empty:  # 检查圆圈是否未上色
                    marble.set_color(selected_color)
                    marble.draw()
                    marble.is_empty = False  # 标记为已上色
                    return  # 上色后返回，等待下一次点击


def


#退出游戏
def quit_game():
    turtle.bye()

if __name__ == '__main__':
    userinput()
    draw_main_board()
    color_choices()
    draw_buttons()
    draw_circle_1()
    turtle.onscreenclick(start_game, btn=1, add=None)
    turtle.mainloop()
    turtle.done()




