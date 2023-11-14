import math
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

    def generate_length_method3(self):
        return math.sqrt(random.random()) * self._radius

    def generate_length_method4(self):
        return random.random() * self._radius


seed_value = 100
# seed_value = int(time.time())
random.seed(seed_value)

your_instance = TestClass(radius=1)

# 生成一些数据
num_samples = 50000
method1_lengths = [your_instance.generate_length_method1() for _ in range(num_samples)]
method2_lengths = [your_instance.generate_length_method2() for _ in range(num_samples)]
method3_lengths = [your_instance.generate_length_method3() for _ in range(num_samples)]
method4_lengths = [your_instance.generate_length_method4() for _ in range(num_samples)]

# 绘制直方图
plt.hist(method1_lengths, bins=50, alpha=0.5, label='Method 1')
plt.hist(method2_lengths, bins=50, alpha=0.5, label='Method 2')
plt.hist(method3_lengths, bins=50, alpha=0.5, label='Method 3')
plt.hist(method4_lengths, bins=50, alpha=0.5, label='Method 4')

# 添加标签和图例
plt.xlabel('Length')
plt.ylabel('Frequency')
plt.legend(loc='upper right')

# 显示图形
plt.show()