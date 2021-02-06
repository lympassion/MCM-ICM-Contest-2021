"""
三种指标正向化
"""


def dataDirection_1(datas, offset=0):  # 极小型指标
    def normalization(data):
        return 1 / (data + offset)

    # 返回一个列表
    return list(map(normalization, datas))


def dataDirection_2(datas, x_min, x_max):  # 中间型指标
    def normalization(data):
        if data <= x_min or data >= x_max:
            return 0
        elif data > x_min and data < (x_min + x_max) / 2:
            return 2 * (data - x_min) / (x_max - x_min)
        elif data < x_max and data >= (x_min + x_max) / 2:
            return 2 * (x_max - data) / (x_max - x_min)

    return list(map(normalization, datas))


def dataDirection_3(datas, x_min, x_max, x_minimum, x_maximum):  # 区间型指标
    def normalization(data):
        if data >= x_min and data <= x_max:
            return 1
        elif data <= x_minimum or data >= x_maximum:
            return 0
        elif data > x_max and data < x_maximum:
            return 1 - (data - x_max) / (x_maximum - x_max)
        elif data < x_min and data > x_minimum:
            return 1 - (x_min - data) / (x_min - x_minimum)

    return list(map(normalization, datas))
