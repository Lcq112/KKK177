import os, random, shutil, sys, time

os.system('')                       # Windows: 打开 ANSI 转义支持
CHARS = ' ..·+*✦✦'                  # 越往后越亮
W, H = shutil.get_terminal_size((100, 30))
W, H = max(W - 1, 20), max(H - 2, 10)

stars = [[random.choice('   .·') for _ in range(W)] for _ in range(H)]

try:
    sys.stdout.write('\033[2J\033[?25l')          # 清屏 + 隐藏光标
    while True:
        for _ in range(W * H // 30):              # 每帧随机点亮/熄灭
            x, y = random.randrange(W), random.randrange(H)
            stars[y][x] = random.choice(CHARS) if random.random() < 0.25 else ' '
        sys.stdout.write('\033[H' + '\n'.join(''.join(r) for r in stars))
        sys.stdout.flush()
        time.sleep(0.09)
except KeyboardInterrupt:
    pass
finally:
    sys.stdout.write('\033[?25h\033[0m\n')        # 恢复光标