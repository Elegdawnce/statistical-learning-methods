import numpy as np
import random
import math

def calculate(A_p_i,B_p_i,C_p_i,y_j):
    return (A_p_i * math.pow(B_p_i,y_j) * math.pow((1-B_p_i),(1-y_j))) / \
           (A_p_i * math.pow(B_p_i,y_j) * math.pow((1-B_p_i),(1-y_j)) + (1 - A_p_i) * math.pow(C_p_i,y_j) * math.pow((1-C_p_i),(1-y_j)))


def e_step(A_p_i,B_p_i,C_p_i,y):
    u = []
    for y_j in y:
        u_j = calculate(A_p_i,B_p_i,C_p_i,y_j)
        u.append(u_j)
    return u

def m_step(u,y):
    A_p_i = sum(u) / len(u)
    B_p_i = sum([u_j * y_j for u_j,y_j in zip(u,y)]) / sum(u)
    C_p_i = sum([(1 - u_j) * y_j for u_j,y_j in zip(u,y)]) /sum([1 - u_j for u_j in u])

    return [A_p_i,B_p_i,C_p_i]



def run(y,A_p,B_p,C_p,iter_num):
    for iter in range(iter_num):
        u = e_step(A_p,B_p,C_p,y)
        print(iter,[A_p,B_p,C_p])
        if [A_p,B_p,C_p] == m_step(u,y):
            print('%d:end' %iter)
            break
        else:
            [A_p,B_p,C_p] = m_step(u,y)

if __name__ == '__main__':
    # initialization
    A_p_0 = 0.5
    B_p_0 = 0.5
    C_p_0 = 0.5
    iter_num = 20
    # watching objects
    y = []
    for i in range(20):
        y.append(random.randrange(0,2,1))
    print(y)
    # iteration
    run(y,A_p_0,B_p_0,C_p_0,iter_num)