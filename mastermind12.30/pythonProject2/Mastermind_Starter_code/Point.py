class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def delta_x(self, other):
        return abs(self.x - other.x)

    def delta_y(self, other):
        return abs(self.y - other.y)


"""
Point 类
这个类很简单，它主要用于表示二维空间中的一个点。它有两个主要的属性：

self.x 和 self.y：这些属性存储点的 x 和 y 坐标。
delta_x 和 delta_y 方法：这些方法用于计算当前点与另一个点之间在 x 轴和 y 轴上的距离。

"""