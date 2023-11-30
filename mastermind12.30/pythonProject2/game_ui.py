import turtle

from Mastermind_Starter_code.Marble import Marble
from Mastermind_Starter_code.Point import Point


class GameUi:
    pen = turtle.Turtle()
    def __init__(self, screen):
        super().__init__()
        self.screen = screen

    def get_username(self):
        username = turtle.textinput("username", ' Name of the player:')
        return username
    # 生成画板
    def draw_main_board(self):
        self.screen.title("Welcome To Kitu's MindMaster Code GAME!!")
        turtle.screensize(800, 900)
        turtle.setup(800, 900)

        # pen control 创建画笔
        pen = turtle.Turtle()
        pen.speed(10)  # fast speed:10,normal:6

        pen.up()
        pen.goto(-380, 350)
        pen.pendown()
        pen.color('black')
        pen.width(7)
        pen.fd(500)
        pen.right(90)
        pen.fd(590)
        pen.right(90)
        pen.fd(500)
        pen.right(90)
        pen.fd(590)

        # pen.goto(0, 0)
        pen.up()
        pen.goto(135, 350)
        pen.pendown()
        pen.color('blue')
        pen.width(7)
        pen.fd(-590)
        pen.right(90)
        pen.fd(230)
        pen.right(90)
        pen.fd(-590)
        pen.right(90)
        pen.fd(230)

        pen.up()
        pen.speed(10)
        pen.goto(368, -253)  # 紫色框的起始位置
        pen.down()
        pen.color('purple')
        pen.width(7)
        pen.forward(750)  # 紫色框的宽度
        pen.right(90)
        pen.forward(-175)  # 紫色框的高度
        pen.right(90)
        pen.forward(750)  # 返回起点的相反方向
        pen.right(90)
        pen.forward(-175)  # 完成框的四边
        pen.hideturtle()

    # 生成两个button，用于user确认和删除
    def draw_buttons(self):
        # 创建一个新的 Turtle 对象来显示图像
        self.screen.addshape('image.gif')
        img_turtle = turtle.Turtle()
        img_turtle.up()  # 确保不在移动时绘制线条
        img_turtle.shape('image.gif')  # 设置形状为图像
        img_turtle.goto(-10, 400)  # 移动到指定位置

        self.screen.addshape('checkbutton.gif')
        img_turtle = turtle.Turtle()
        img_turtle.up()  # 确保不在移动时绘制线条
        img_turtle.shape('checkbutton.gif')  # 设置形状为图像
        img_turtle.goto(60, -325)  # 移动到指定位置
        self.screen.addshape('xbutton.gif')
        img_turtle = turtle.Turtle()
        img_turtle.up()
        img_turtle.shape('xbutton.gif')
        img_turtle.goto(130, -325)
        self.screen.addshape('quit.gif')
        img_turtle = turtle.Turtle()
        img_turtle.up()
        img_turtle.shape('quit.gif')
        img_turtle.goto(280, -325)

    # 初始化6个颜色选择，
    def color_choices(self, color):
        m_color_circle_list = []
        turtle.tracer(0)
        x = -300
        y = -350
        for i in color:
            a = Marble(Point(x, y), i, size=15)
            a.draw()
            m_color_circle_list.append(a)
            x = x + 40
        turtle.update()
        return m_color_circle_list
    # 把圆圈实例化，给用户点击用的
    def draw_circle_1(self):
        m_list = []
        small_m_list = []
        turtle.tracer(0)
        y = 270
        x = -250
        self.add_arrow(1, x - 63, y + 13)
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
            turtle.hideturtle()
        return m_list, small_m_list

    def win_ui(self):
        # 弹出you win
        print("you win!!")
        # 使用已经存在的屏幕对象
        if 'winner.gif' not in self.screen.getshapes():
            self.screen.addshape('winner.gif')
        win_msg_turtle = turtle.Turtle()
        win_msg_turtle.up()
        win_msg_turtle.shape('winner.gif')
        win_msg_turtle.goto(0, 0)

    def lose_ui(self):
        #pop up lose game message
        print("you lose!!")
        if 'Lose.gif' not in self.screen.getshapes():
            self.screen.addshape('Lose.gif')
            lose_msg_turtle = turtle.Turtle()
            lose_msg_turtle.up()
            lose_msg_turtle.shape("Lose.gif")
            lose_msg_turtle.goto(0, 0)


    def on_quit_button_click(self):
        # 弹出退出的信息提示
        self.screen.title('quit')
        self.screen.addshape('quitmsg.gif')
        quit_msg_turtle = turtle.Turtle()
        quit_msg_turtle.up()
        quit_msg_turtle.shape('quitmsg.gif')
        quit_msg_turtle.goto(0, 0)
        turtle.update()

    def add_arrow(self, need_check_answer, x, y):
        if need_check_answer == 1:
            self.screen.addshape('arrow.gif')
            arrow_msg_turtle = turtle.Turtle()
            arrow_msg_turtle.up()
            arrow_msg_turtle.shape('arrow.gif')
            arrow_msg_turtle.goto(x, y)
            turtle.update()