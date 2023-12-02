import unittest

from game_function import GameFunction


class MyTestCase(unittest.TestCase):
    '''
    1、正确答案：

    '''
    def setUp(self) -> None:
        self.correct_answer = ['black', 'red', 'blue', 'yellow']
        self.guess_answer = [['black', 'red', 'blue', 'yellow'], ['red', 'black', 'yellow', 'blue'],
                             ['black', 'blue', 'red', 'yellow'], ['purple', 'black', 'blue', 'yellow'],
                             ['blue', '', '', '']]
        self.expect_data = ['success', 'failed', 'failed', "failed", "noconfirm"]

    def test_confirm_answer(self):
        for i,j in enumerate(self.guess_answer):
            result, detail_result = GameFunction.confirm_answer(self.correct_answer, j)
            print(result)
            self.assertEqual(self.expect_data[i], result)  # add assertion here


if __name__ == '__main__':
    unittest.main()
