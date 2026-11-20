"""满屏星星：python stars.py    （按 Ctrl+C 退出）"""

import os
import random
import shutil
import sys
import time

os.system('')                       # Windows: 打开 ANSI 转义支持

CHARS = ' ..·+*✦✦'                  # 越往后越亮
W, H = shutil.get_terminal_size((100, 30))
W, H = max(W - 1, 20), max(H - 2, 10)

# 初始就是一片稀疏的星空
stars = [[random.choice('   .·') for _ in range(W)] for _ in range(H)]


def frame():
    return '\033[H' + '\n'.join(''.join(row) for row in stars)


try:
    sys.stdout.write('\033[2J\033[?25l')     # 清屏 + 隐藏光标
    while True:
        # 每帧随机让一部分星星闪烁、亮起或熄灭
        for _ in range(W * H // 30):
            x, y = random.randrange(W), random.randrange(H)
            stars[y][x] = random.choice(CHARS) if random.random() < 0.25 else ' '
        sys.stdout.write(frame())
        sys.stdout.flush()
        time.sleep(0.09)
except KeyboardInterrupt:
    pass
finally:
    sys.stdout.write('\033[?25h\033[0m\n')   # 恢复光标
    print('✨ 星空结束')
