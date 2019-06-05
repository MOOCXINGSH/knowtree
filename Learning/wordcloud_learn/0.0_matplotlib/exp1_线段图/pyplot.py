import matplotlib.pyplot as plt
# pyplot模块的plot函数可以接收输入参数和输出参数，还有线条粗细等参数，，例如下方的示例
s = [1, 4, 9, 16, 25]
plt.plot(s, linewidth=5)  # 这里只指定了一个列表，那么就当作是输出参数，输入参数从0开始，就会发现没有正确绘制数据
plt.title("Yang", fontsize=24)  # 指定标题，并设置标题字体大小
plt.xlabel("X_yang", fontsize=14)  # 指定X坐标轴的标签，并设置标签字体大小
plt.ylabel("Y_Value", fontsize=14)  # 指定Y坐标轴的标签，并设置标签字体大小
plt.tick_params(axis='both', labelsize=14)  # 参数axis值为both，代表要设置横纵的刻度标记，标记大小为14
plt.show()  # 打开matplotlib查看器，并显示绘制的图形
