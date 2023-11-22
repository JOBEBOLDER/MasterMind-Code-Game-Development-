import turtle
from Marble import Marble
from Point import Point


# get username from the input
def userinput():
    turtle.textinput("username", ' Name of the player:')


# def load_leaderboard(self):
#     # Load leaderboard from file or create new file
#     try


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

        m_color_circle_list = []
        color = ['black', 'red', 'yellow', 'blue', 'purple', 'green']
        x = -300
        y = -350
        for i in color:
            a = Marble(Point(x, y), 'black', size=20)
            a.set_color(i)
            a.draw()
            m_color_circle_list.append(a)
            x = x + 46


        pen.width(1)
        pen.speed(10)
        screen.tracer(0)
        pen.penup()
        pen.color('black')
        y = 300
        x = -300
        pen.goto(x, y )

        for i in range(10):  # 10次大循环
            s = x
            for j in range(4):  # 每个小循环里面4个大圈
                print(j)
                pen.down()
                pen.circle(20)
                pen.up()
                pen.goto(s + 60, y)
                s = s + 60
                # pen.forward(60)
            # 小圆圈横轴坐标起点
            s = s + 50
            x1 = s
            # 在每个大圈旁边画四个小圈，分成上下两排，每排两个
            pen.goto(x1, y + 10)  # 将画笔移动到小圈的上排起始位置
            for _ in range(2):  # 上排的两个小圈
                pen.down()
                pen.circle(5)
                pen.up()
                pen.goto(s + 15, y + 10)
                s = s + 10
                # pen.forward(20)

            pen.goto(x1 , y - 10)  # 将画笔移动到小圈的下排起始位置
            s = x1
            for _ in range(2):  # 下排的两个小圈
                pen.down()
                pen.circle(5)
                pen.up()
                pen.goto(s + 15, y - 10)
                s = s + 15
                # pen.forward(20)

            # 移动到下一行的起始位置
            y = y - 50
            pen.goto(x, y)


if __name__ == '__main__':
    userinput()
    draw_main_board()
    turtle.done()