import turtle

from Mastermind_Starter_code.Marble import Marble
from Mastermind_Starter_code.Point import Point


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

    # 添加gif
    screen.addshape('checkbutton.gif')
    # 创建一个新的 Turtle 对象来显示图像
    img_turtle = turtle.Turtle()
    img_turtle.up()  # 确保不在移动时绘制线条
    img_turtle.shape('checkbutton.gif')  # 设置形状为图像
    img_turtle.goto(10, -320)  # 移动到指定位置

    screen.addshape('xbutton.gif')
    img_turtle = turtle.Turtle()
    img_turtle.up()
    img_turtle.shape('xbutton.gif')
    img_turtle.goto(90, -320)

    screen.addshape('quit.gif')
    img_turtle = turtle.Turtle()
    img_turtle.up()
    img_turtle.shape('quit.gif')
    img_turtle.goto(280, -320)
    draw_circle_1()
    draw_circle_2()


m_list = []
small_m_list = []


def draw_circle_1():

    y = 300
    x = -300
    for i in range(10):  # 10次大循环
        m_item_list = []
        x_0 = x
        for j in range(4):  # 每个小循环里面4个大圈
            m = Marble(Point(x_0, y), 'black')
            m.draw_empty()
            m_item_list.append(m)
            x_0 = x_0 + 60
        # 小圆圈横轴坐标起点
        x1 = x_0 + 50
        small_m_item_list = []
        # 在每个大圈旁边画四个小圈，分成上下两排，每排两个
        x_2 = x1
        for _ in range(2):  # 上排的两个小圈
            small_m = Marble(Point(x_2, y + 15), 'black', size=5)
            small_m.draw_empty()
            small_m_item_list.append(small_m)
            x_2 = x_2 + 15
        x_3 = x1
        for _ in range(2):  # 下排的两个小圈
            small_m = Marble(Point(x_3, y - 5), 'black', size=5)
            small_m.draw_empty()
            small_m_item_list.append(small_m)
            x_3 = x_3 + 15
        # 移动到下一行的起始位置
        y = y - 50
        m_list.append(m_item_list)
        small_m_list.append(small_m_item_list)


m_color_circle_list = []


def draw_circle_2():
    color = ['black', 'red', 'yellow', 'blue', 'purple', 'green']
    x = -300
    y = -350
    for i in color:
        a = Marble(Point(x, y), 'black', size=15)
        a.set_color(i)
        a.draw()
        m_color_circle_list.append(a)
        x = x + 40

selected_color= ""
def play_game(x, y):
    for i in m_list:
        for j in i:
            for k in m_color_circle_list:
                if k.clicked_in_region(x, y):
                    selected_color = k.get_color()
                    print("zg"+selected_color)
                    break
            j.set_color(selected_color)
            j.draw()



if __name__ == '__main__':

    draw_main_board()
    turtle.onscreenclick(play_game, btn=1, add=None)
    turtle.mainloop()
    turtle.done()


