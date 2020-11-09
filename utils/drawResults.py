#!/usr/bin/env python
# encoding: utf-8
# @author: lishaogang
# @file: drawResults.py
# @time: 2020/10/30 0030 9:22
# @desc:

import matplotlib.pyplot as plt
import numpy as np
import xlrd

def read_excel(fname):
    # 打开文件
    workBook = xlrd.open_workbook(fname)
    hvs = []
    igds = []
    for i in range(7):
        sheet = workBook.sheet_by_index(i) # sheet索引从0开始
        hvs.append(sheet.row_values(1)[1:11])
        igds.append(sheet.row_values(2)[1:11])
    return hvs, igds
    # # 5. 获取单元格内容(三种方式)
    # print(sheet1_content1.cell(1, 0).value)
    # print(sheet1_content1.cell_value(2, 2))
    # print(sheet1_content1.row(2)[2].value)
    #
    # # 6. 获取单元格内容的数据类型
    # # Tips: python读取excel中单元格的内容返回的有5种类型 [0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error]
    # print(sheet1_content1.cell(1, 0).ctype)


def draw_box(data, name):
    '''
    根据数据画盒图
    :param data:
    :return:
    '''
    plt.figure()
    plt.boxplot(data, notch=False, sym='o', vert=True)
    # plt.xticks([1,2, 3],['MOEA/D', 'MOEA/D-DE', 'MOEA/D-CoDE'])
    plt.title(name)
    plt.show()


if __name__ == '__main__':
    # a = [np.array([1,2,3,4,5,6,7]), np.array([3,4,5,6,7,8,9])]
    # draw_box(a, "name")
    hvs, igds = read_excel('../results/excels/dtlz4.xls')
    hvs1, igds1 = read_excel('../results/excels/dtlz4.xls')
    hvs2, igds2 = read_excel('../results/excels/dtlz4.xls')
    for i in range(7):
        data = [hvs[i],hvs1[i], hvs2[i]]
        draw_box(data, 'DTLZ{}结果对比箱图'.format(i+1))

