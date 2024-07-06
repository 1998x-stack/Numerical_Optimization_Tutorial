# 00_3.1._Step_Length

"""
Lecture: /03._Line_Search_Methods
Content: 00_3.1._Step_Length
"""

import numpy as np

def armijo_condition(f, xk, pk, alpha, c1=1e-4):
    """
    检查是否满足Armijo条件
    Args:
        f (callable): 目标函数
        xk (np.array): 当前点
        pk (np.array): 搜索方向
        alpha (float): 步长
        c1 (float): Armijo条件的参数，默认值为1e-4
    
    Returns:
        bool: 是否满足Armijo条件
    """
    return f(xk + alpha * pk) <= f(xk) + c1 * alpha * np.dot(gradient(f, xk), pk)

def wolfe_conditions(f, xk, pk, alpha, c1=1e-4, c2=0.9):
    """
    检查是否满足Wolfe条件
    Args:
        f (callable): 目标函数
        xk (np.array): 当前点
        pk (np.array): 搜索方向
        alpha (float): 步长
        c1 (float): Wolfe条件的参数，默认值为1e-4
        c2 (float): Wolfe条件的参数，默认值为0.9
    
    Returns:
        bool: 是否满足Wolfe条件
    """
    return armijo_condition(f, xk, pk, alpha, c1) and np.dot(gradient(f, xk + alpha * pk), pk) >= c2 * np.dot(gradient(f, xk), pk)

def backtracking_line_search(f, xk, pk, alpha=1, rho=0.5, c1=1e-4):
    """
    使用回溯法选择步长，满足Armijo条件
    Args:
        f (callable): 目标函数
        xk (np.array): 当前点
        pk (np.array): 搜索方向
        alpha (float): 初始步长，默认值为1
        rho (float): 步长缩减系数，默认值为0.5
        c1 (float): Armijo条件的参数，默认值为1e-4
    
    Returns:
        float: 选择的步长
    """
    while not armijo_condition(f, xk, pk, alpha, c1):
        alpha *= rho
    return alpha

def gradient(f, x, eps=1e-8):
    """
    计算目标函数的梯度
    Args:
        f (callable): 目标函数
        x (np.array): 当前点
        eps (float): 数值梯度计算的步长，默认值为1e-8
    
    Returns:
        np.array: 梯度向量
    """
    grad = np.zeros_like(x)
    for i in range(len(x)):
        x1, x2 = np.copy(x), np.copy(x)
        x1[i] -= eps
        x2[i] += eps
        grad[i] = (f(x2) - f(x1)) / (2 * eps)
    return grad

def test_function(x):
    """
    测试用的目标函数
    Args:
        x (np.array): 输入向量
    
    Returns:
        float: 目标函数值
    """
    return np.sum(x**2)

# 示例使用
xk = np.array([1.0, 1.0])
pk = -gradient(test_function, xk)
alpha = backtracking_line_search(test_function, xk, pk)

print(f"选择的步长: {alpha}")
