import random

import turtle


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


    def confirm_answer(self, need_check_answer, correct_color, game_count, m_list, small_m_list):

        if need_check_answer == 1:
            print("qwe123123")
            current_round_circles = self.guessing_list[game_count]
            current_color = []
            for circle in current_round_circles:
                current_color.append(circle.color)
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
            for i, j in enumerate(small_circle_color):
                small_circle = small_m_list[game_count][i]
                small_circle.set_color(j)
                small_circle.draw()

            game_count += 1
            if black == 4:
                return "success", game_count
            else:
                return "failed", game_count
        else:
            return "noconfirm", game_count

    def delete_answer(self, game_count, m_list,need_check_answer):
        for marble in reversed(self.guessing_list[game_count]):
            if not marble.is_empty:
                # 重置这个圆圈为未填充状态
                marble.draw_empty()
                need_check_answer = 0
                reset_color = marble.get_color()
                self.m_color_circle_list[self.color.index(reset_color)].set_color(reset_color)
                self.m_color_circle_list[self.color.index(reset_color)].draw()
                break

    def write_leaderboard(self, username, game_count, current_rank):
        try:
            before_rank = current_rank[username]
            if game_count < before_rank:
                current_rank[username] = game_count
            with open("leaderboard.txt", 'w') as f:
                for key, value in current_rank.items():
                    f.write(f"{key},{value}\n")
        except KeyError:
            with open("leaderboard.txt", 'a') as f:
                f.write(f"{username},{game_count}\n")

    def load_leaderboard(self):

        self.pen.clear()
        self.pen.up()
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