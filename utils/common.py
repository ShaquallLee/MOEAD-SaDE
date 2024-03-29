#!/usr/bin/env python
# encoding: utf-8
# @author: lishaogang
# @file: common.py
# @time: 2020/10/18 0018 16:27
# @desc:
import random
import math
import time
import matplotlib.pyplot as plt

def get_random_list(size):
    '''
    h获取长度为size随机列表
    :param size:
    :return:
    '''
    perm = [x for x in range(size)]
    random.shuffle(perm)
    return perm

def fitness_function(y, namda, idealpoint):
    '''
    使用切比雪夫分布函数计算fitness
    :param y:
    :param namda:
    :param idealpoint:
    :return:
    '''
    max_fun = -1.0e+30
    for n in range(len(y)):
        diff = math.fabs(y[n]-idealpoint[n])
        if namda[n] == 0:
            feval = 0.0001*diff
        else:
            feval = diff*namda[n]
        if feval > max_fun:
            max_fun=feval
    fitness = max_fun

    return fitness

def extract_info(model):
    '''
    从model运行结果中拿出后面要用的信息
    :param model:
    :return:
    '''
    x = []
    y = []
    z = []
    pops = []
    for p in model.pop:
        xx, yy, zz = p.pop_fitness
        pops.append(p.pop_fitness)
        x.append(xx)
        y.append(yy)
        z.append(zz)
    return pops, x, y, z

def draw_scatter3D(pname, hv_score, igd, reference_point, x, y, z, pareto_front):
    '''
    画3D散点图
    :param hv_score:
    :param igd:
    :param x:
    :param y:
    :param z:
    :return:
    '''
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z)
    x_r, y_r, z_r = reference_point
    ax.scatter(x_r, y_r, z_r, c='r')
    x_p = []
    y_p = []
    z_p =[]
    for i,j,k in pareto_front:
        x_p.append(i)
        y_p.append(j)
        z_p.append(k)
    ax.scatter(x_p, y_p, z_p, c="g")
    ax.set_xlabel('func1')
    ax.set_ylabel('func2')
    ax.set_zlabel('func3')
    title = '{} pareto front\nHV:{}\nIGD:{}'.format(pname, hv_score, igd)
    ax.set_title(title)
    plt.savefig('./results/photos/p/{}_s_{}.png'.format(pname, time.time()))
    plt.show()

def draw_igd(distances, model):
    '''
    画IGD变化趋势图
    :param distances:
    :param model:
    :return:
    '''
    plt.figure()
    plt.plot(distances[1:])
    plt.xlabel("generation")
    plt.ylabel("IGD")
    plt.savefig('./results/photos/igd/{}_{}.png'.format(model.problem.name(), time.time()))
    plt.show()
