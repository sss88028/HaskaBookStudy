import random
import matplotlib.pyplot as plt

class TestClass:
    def __init__(self, radius):
        self._radius = radius

    def generate_length_method1(self):
        length = (random.random() + random.random()) * self._radius
        if length > self._radius:
            length = 2 * self._radius - length
        return length

    def generate_length_method2(self):
        return self._radius - abs((random.random() + random.random() - 1) * self._radius)

your_instance = TestClass(radius=50.0)

# 生成一些数据
num_samples = 20000
method1_lengths = [your_instance.generate_length_method1() for _ in range(num_samples)]
method2_lengths = [your_instance.generate_length_method2() for _ in range(num_samples)]

# 绘制直方图
plt.hist(method1_lengths, bins=50, alpha=0.5, label='Method 1')
plt.hist(method2_lengths, bins=50, alpha=0.5, label='Method 2')

# 添加标签和图例
plt.xlabel('Length')
plt.ylabel('Frequency')
plt.legend(loc='upper right')

# 显示图形
plt.show()