import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 100)

y1 = 2*x+1
y2 = x**2

fig = plt.figure()

plt.plot(x, y1, color="red", linewidth=3,linestyle="--", label="linear")
plt.plot(x, y2, label=" exponent")

# 设置取值范围
plt.xlim((-1, 2))
plt.ylim((-2, 3))

# 设置坐标轴名称
plt.xlabel(" parameter ")
plt.ylabel("Degree")

# 改变坐标轴单位
new_ticks = np.linspace(-1, 2, 5)
print(new_ticks)
plt.xticks(new_ticks)

plt.yticks([-2, -1.8, -1, 1, 1.22, 3],
            ['really bad', 'bad', 'normal', 'good', 'really good'])

# get current axis  #改变坐标轴位置
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data', -1))
ax.spines['left'].set_position(('data', 0))

# 图例
plt.legend(loc='best')

# 标注
x0 = 0.2
y0 = 2*x0 + 1
plt.scatter(x0, y0)
plt.plot([x0, x0], [y0, 0.7], 'k--', lw=2.5)

plt.annotate(r'$2x+1=%s$' % y0, xy=(x0, y0), xycoords='data', xytext=(+30, -30),
             textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))

# 图中图

left, bottom, width, height = 0.2, 0.6, 0.25, 0.25
ax2 = fig.add_axes([left, bottom, width, height])
ax2.plot(y1, x, 'b')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('title inside 1')

# plt.savefig('fig.png', bbox_inches='tight')
# 图片保存
plt.savefig('./test2.jpg')
plt.show()