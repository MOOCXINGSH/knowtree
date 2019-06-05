import matplotlib.pyplot as plt
from random_walk import RandomWalk

# 创建一个RandomWalk实例，并指定走5000步
rw = RandomWalk(5000)
rw.fill_walk()  # 开始获取随机漫步数据，其实获取的是两个包含x和y值的数据点列表
plt.scatter(rw.x_values, rw.y_values, s=15)
plt.show()
