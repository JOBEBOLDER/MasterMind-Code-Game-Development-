import random


class GameFunction:
    def __init__(self, screen, pen) -> None:
        super().__init__()
        self.pen = pen
        self.screen = screen
    # 随机生成4个颜色

    def secret_code(self, color, length=4):
        return random.sample(color, length)

    def reset_color_circle(self, color, m_color_circle_list):
        for i, j in enumerate(m_color_circle_list):
            j.set_color(color[i])
            j.draw()

    def fill_color(self, game_count, color_circle, m_list,need_check_answer):

        print(game_count)
        for j, k in enumerate(m_list[game_count]):
            if k.is_empty is True and need_check_answer == 0:
                # 检查是否点击了颜色选择区域
                selected_color = color_circle.get_color()
                print(selected_color)
                color_circle.draw_empty()

                if k.is_empty:  # 检查圆圈是否未上色
                    k.set_color(selected_color)
                    k.draw()

                if j == 3:
                    need_check_answer = 1

            elif need_check_answer == 1:
                print("you need to check answer,otherwise u cant not continue the game")

            else:
                continue

            return need_check_answer

    @classmethod
    def confirm_answer(cls, correct_color, current_answer):
        if '' not in current_answer:
            print(f"correct_color:{correct_color}")
            black = 0
            red = 0
            for i, k in enumerate(current_answer):
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
            if black == 4:
                return "success", small_circle_color
            else:
                return "failed", small_circle_color
        else:
            return "noconfirm", None

    def delete_answer(self, game_count, m_list, m_color_circle_list, need_check_answer, color):
        for marble in reversed(m_list[game_count]):
            if not marble.is_empty:
                # 重置这个圆圈为未填充状态
                marble.draw_empty()
                need_check_answer = 0
                reset_color = marble.get_color()
                m_color_circle_list[color.index(reset_color)].set_color(reset_color)
                m_color_circle_list[color.index(reset_color)].draw()
                break
        return need_check_answer, m_color_circle_list
    def write_leaderboard(self, username, game_count, current_rank):
        try:
            before_rank = current_rank[username]
            if game_count < before_rank:
                current_rank[username] = game_count
            with open("leaderboard.txt", 'w',encoding='utf8') as f:
                for key, value in current_rank.items():
                    f.write(f"{value}:{key}\n")
        except KeyError:
            with open("leaderboard.txt", 'a',encoding='utf8') as f:
                f.write(f"{game_count}:{username}\n")

    def load_leaderboard(self):
        self.pen.clear()
        self.pen.up()
        user_rank_dic = {}

        # processing of ranking list information
        try:
            with open("leaderboard.txt", 'r', encoding='utf8') as f:
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
                # Extract sorted rows from sorted list
                # sorted_lines = [pair[1] for pair in score_line_pairs]
                # print(sorted_lines)
                top_five = score_line_pairs[:5]

            # move to the start of the title
            self.pen.goto(150, 310)
            self.pen.color('blue')
            self.pen.write("Leaderboard 🏆:", font=("Arial", 22, "italic"))

            # write the leaderboard
            y_offset = -30
            for i in top_five:
                a = i[1].split(':')
                user_rank_dic[a[1]] = a[0].strip()
                self.pen.goto(155, 260 + y_offset)
                self.pen.write(a[0] + ': ' + a[1], font=("Arial", 18, "normal"))
                y_offset = y_offset - 40  # move to the next line
                self.pen.hideturtle()

            return user_rank_dic

        except Exception as e:
            print(e)
            print(e.__traceback__.tb_lineno)