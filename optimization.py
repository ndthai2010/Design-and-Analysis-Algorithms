import numpy as np
from pylab import *
import sys


def rosembrock(x):
    """
    Tính giá trị của hàm số Rosembrock với mảng x
    """
    return 100.0 * (x[1] - x[0]**2)**2 + (1 - x[0])**2


def nabla(x):
    """
    Tính giá trị Nabla
    """
    def f1(x): return -400*x[0]*(x[1]-x[0]**2) - 2*(1-x[0])
    def f2(x): return 200*(x[1] - x[0]**2)
    return np.array([f1(x), f2(x)])


def hessian_matrix(x):

    return np.matrix([[-400*x[1]+1200*x[0]**2 + 2, -400*x[0]], [-400*x[0], 200]])


def backtracking_line_search(x, delta_x, delta_f, rosembrock, params):
    alpha = params[0]
    beta = params[1]
    t = 1 # Giá trị bước ban đầu 
    while rosembrock(x + t * delta_x) > rosembrock(x) + alpha * t * np.dot(delta_f, delta_x):
        t = beta * t

    return t


def gradient_descent(init_x, rosembrock, nabla, backtracking_line_search, conv_tol=10e-5, params=[10e-4, .5]):

    x = init_x
    step = 0
    while np.linalg.norm(nabla(x), 2) > conv_tol:
        delta_x = -nabla(x)
        t = backtracking_line_search(x, delta_x, -delta_x, rosembrock, params)
        x = x + t * delta_x
        step += 1

    return x, step


def newtons_method(init_x, rosembrock, nabla, hessian_matrix, backtracking_line_search, conv_tol=10e-6, params=[10e-4, .5]):

    x = init_x
    step = 0
    l = sys.maxsize
    while l / 2 > conv_tol:
        delta_x = - np.dot(np.linalg.inv(hessian_matrix(x)), nabla(x))
        delta_x = np.array([delta_x[0, 0]], delta_x[0, 1])
        l = np.dot(np.dot(np.transpose(nabla(x)),
                   np.linalg.inv(hessian_matrix(x))), nabla(x))
        t = backtracking_line_search(x, delta_x, -delta_x, rosembrock, params)
        x = x + t * delta_x
        step += 1

    return x, step


# Chạy thuật toán
print("Gradient descent with (1.2, 1.2)") # Điểm xuất phát
beta = .5
alpha = 10e-4
conv_tol = 10e-5
step = 0
init_x = np.array([1.2, 1.2])
opt_x, step = gradient_descent(
    init_x, rosembrock, nabla, backtracking_line_search)
print(opt_x) # Nghiệm cực tiểu
print(step) # Số bước
print(rosembrock(opt_x)) #Giá trị nghiệm cực tiểu tại hàm Rosembrock

# Thay thế bằng một điểm xuất phát khác
print("Gradient descent with (-1.2, 1)")
init_x = np.array([-1.2, 1])
x_opt, step = gradient_descent(
    init_x, rosembrock, nabla, backtracking_line_search)
print(opt_x) # Nghiệm cực tiểu
print(step) # Số bước
print(rosembrock(opt_x)) # Giá trị nghiệm cực tiểu tại hàm Rosembrock


print("Newton's Method:")
init_x = np.array([1.2, 1.2])
opt_x, step = newtons_method(
    init_x, rosembrock, nabla, hessian_matrix, backtracking_line_search)
print(opt_x) # Nghiệm cực tiểu
print(step) # Số bước
print(rosembrock(opt_x)) # Giá trị nghiệm cực tiểu tại hàm Rosembrock

"""
Dựa vào kết quả tính toán bên trên, ta có thể thấy rằng,
phương pháp Newton không chỉ tính toán nghiệm cực tiểu
nhanh hơn mà còn chính xác hơn phương pháp Backtracking line search
"""
