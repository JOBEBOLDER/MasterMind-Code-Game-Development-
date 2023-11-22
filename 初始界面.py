import turtle

# 设置屏幕
screen = turtle.Screen()
screen.title("Welcome To CS5001 MindMaster Code GAME")

# 创建画笔
pen = turtle.Turtle()
pen.speed(0)
pen.up()

# 画游戏主板
def draw_main_board():
    pen.goto(-200, 250)  # 根据实际情况调整位置
    pen.down()
    for i in range(10):  # 画十行
        for j in range(4):  # 画四列
            pen.circle(20)  # 圆的半径
            pen.up()
            pen.forward(50)  # 圆之间的距离
            pen.down()
        pen.up()
        pen.backward(200)  # 返回行的起始位置
        pen.right(90)
        pen.forward(50)  # 下一行的位置
        pen.left(90)
        pen.down()

# 画小圆点的得分板
def draw_scoring_pegs():
    pen.goto(250, 250)  # 根据实际情况调整位置
    pen.down()
    for i in range(10):  # 画十行
        for j in range(4):  # 画四个点
            pen.dot(10)  # 点的大小
            pen.up()
            pen.forward(20)  # 点之间的距离
            pen.down()
        pen.up()
        pen.backward(80)  # 返回行的起始位置
        pen.right(90)
        pen.forward(50)  # 下一行的位置
        pen.left(90)
        pen.down()

# 画颜色选择按钮
def draw_color_buttons():
    colors = ["red", "blue", "green", "yellow", "purple", "black"]
    pen.goto(-200, -200)  # 根据实际情况调整位置
    for color in colors:
        pen.fillcolor(color)
        pen.begin_fill()
        pen.circle(20)
        pen.end_fill()
        pen.up()
        pen.forward(50)
        pen.down()

# 画确认和取消按钮
def draw_confirmation_buttons():
    pen.goto(100, -200)  # 根据实际情况调整位置
    # 绿色确认按钮
    pen.fillcolor("green")
    pen.begin_fill()
    pen.circle(20)
    pen.end_fill()
    pen.up()
    pen.forward(50)
    pen.down()
    # 红色取消按钮
    pen.fillcolor("red")
    pen.begin_fill()
    pen.circle(20)
    pen.end_fill()

# 画退出按钮
def draw_quit_button():
    pen.goto(200, -200)  # 根据实际情况调整位置
    pen.fillcolor("brown")
    pen.begin_fill()
    pen.circle(20)
    pen.end_fill()

# 组合所有的画图函数
def draw_game():
    draw_main_board()
    draw_scoring_pegs()
    draw_color_buttons()
    draw_confirmation_buttons()
    draw_quit_button()

# 绘制游戏界面
draw_game()

# 隐藏画笔
pen.hideturtle()

# 保持窗口打开
turtle.done()
