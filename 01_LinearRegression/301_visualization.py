import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def make_data():
    np.random.seed(20)
    x = np.random.rand(100) * 30 + 50  # square
    noise = np.random.rand(100) * 50
    y = x * 8 - 127  # price
    y = y - noise
    return x, y


def visualization(x, y):
    plt.xlabel('Square', fontsize=15)
    plt.ylabel('Price', fontsize=15)
    plt.scatter(x, y)
    x1, y1 = [50, 78], [253, 467]
    x2, y2 = [51, 78], [246, 486]
    plt.plot(x1, y1, c='r', label=r'$h_1(x)$')
    plt.plot(x2, y2, c='orange', label=r'$h_2(x)$')
    plt.tight_layout()  # 调整子图间距
    plt.legend(fontsize=15)
    plt.show()


if __name__ == '__main__':
    x, y = make_data()
    visualization(x, y)
