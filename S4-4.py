# 输入两个坐标列表
lst1 = list(map(int, input("输入第一个点坐标，两个整数空格隔开：").split()))
lst2 = list(map(int, input("输入第二个点坐标，两个整数空格隔开：").split()))

# 曼哈顿距离公式：|x1 - x2| + |y1 - y2|
distance = abs(lst1[0] - lst2[0]) + abs(lst1[1] - lst2[1])
print(distance)
