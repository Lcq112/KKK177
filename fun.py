"""几个有意思的小程序，直接运行就能看效果： python fun.py"""

import math
import time
import sys


def heart():
    """用数学公式画一个心形"""
    print('\n[1] 心形')
    for y in range(15, -15, -1):
        line = ''
        for x in range(-30, 31):
            # 心形不等式：(x^2+y^2-1)^3 - x^2*y^3 <= 0
            px, py = x / 15, y / 15
            if (px * px + py * py - 1) ** 3 - px * px * py ** 3 <= 0:
                line += '♥'
            else:
                line += ' '
        print(line)


def sine_wave():
    """一行数学函数变成一条波"""
    print('\n[2] 正弦波')
    for i in range(24):
        x = math.sin(i / 2.5)
        print(' ' * int(20 + x * 18) + '*')


def multiplication_table():
    """一个表达式打印九九乘法表"""
    print('\n[3] 九九乘法表')
    print('\n'.join(
        ' '.join(f'{j}x{i}={i * j:2d}' for j in range(1, i + 1))
        for i in range(1, 10)
    ))


def infinite_fib():
    """无限生成器只取前 12 个"""
    print('\n[4] 无限斐波那契')

    def fib():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b

    gen = fib()
    print([next(gen) for _ in range(12)])


def progress_bar():
    """不换行刷新的进度条"""
    print('\n[5] 进度条')
    for i in range(21):
        bar = '#' * i + '-' * (20 - i)
        sys.stdout.write(f'\r    [{bar}] {i * 5:3d}%')
        sys.stdout.flush()
        time.sleep(0.04)
    print()


def word_count():
    """三行统计词频"""
    print('\n[6] 词频统计')
    from collections import Counter
    text = 'the quick brown fox jumps over the lazy dog the fox'
    print(Counter(text.split()).most_common(3))


def transpose():
    """zip 一行转置矩阵"""
    print('\n[7] 矩阵转置')
    m = [[1, 2, 3], [4, 5, 6]]
    print('原矩阵:', m)
    print('转置后:', list(map(list, zip(*m))))


if __name__ == '__main__':
    heart()
    sine_wave()
    multiplication_table()
    infinite_fib()
    progress_bar()
    word_count()
    transpose()
    print('\n全部跑完 ✓')
