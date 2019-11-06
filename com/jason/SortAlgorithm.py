#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/18 17:10
# @Author  : Jason
# @Site    : 
# @File    : SortAlgorithm.py
# @Software: PyCharm



def bubble_sort(nums,reverse=False):
    '''
    冒泡排序
    其时间复杂度是:冒泡排序的时间复杂度为O(n^2)。
    :param nums:一个list
    :param reverse:
    :return:
    '''

    for i in range(len(nums)):
        for j in range(0,len(nums) -i -1):
            if reverse:
                if nums[j] < nums[j + 1]:
                    tmp = nums[j + 1]
                    nums[j + 1] = nums[j]
                    nums[j] = tmp
            else:
                if nums[j] > nums[j +1]:
                    tmp = nums[j + 1]
                    nums[j+1]=nums[j]
                    nums[j] = tmp


def select_sort(nums,reverse=False):
    '''
    选择排序
    其时间复杂度是:O(n^2)。
    :param nums:
    :param reverse:
    :return:
    '''

    for i in range(len(nums)-1):
        index = i
        for j in range(i + 1,len(nums) ):
            if reverse:
                if nums[j] > nums[index]:
                    index = j
            else:
                if nums[j] < nums[index]:
                    index = j
        if index != i :
            tmp = nums[i]
            nums[i] = nums[index]
            nums[index] = tmp

def insert_sort(nums,reverse=False):
    '''
    插入排序
    时间复杂度是:O(n^2)。
    :param nums:
    :param reverse:
    :return:
    '''
    for i in range(1,len(nums)):
        for j in range(i-1,-1,-1):
            if reverse:
                if nums[j] < nums[j + 1]:
                    tmp = nums[j+1]
                    nums[j+1] = nums[j]
                    nums[j] = tmp
                else:
                    break
            else:
                if nums[j] > nums[j + 1]:
                    tmp = nums[j + 1]
                    nums [ j + 1] = nums[j]
                    nums[j] = tmp
                else:
                    break

def shell_sort(nums,reverse=False):
    '''
    希尔排序
    基本思想是：
将整个待排元素序列分割成若干个子序列（由相隔某个“增量”的元素组成的）分别进行直接插入排序
然后依次缩减增量再进行排序，待整个序列中的元素基本有序（增量足够小）时
再对全体元素进行一次直接插入排序。因为直接插入排序在元素基本有序的情况下（接近最好情况），效率是很高的，因此希尔排序在时间效率上比前两种方法有较大提高。

算法思路：
先取一个正整数 d1(d1 < n)，把全部记录分成 d1 个组，所有距离为 d1 的倍数的记录看成一组，然后在各组内进行插入排序
然后取 d2(d2 < d1)
重复上述分组和排序操作；直到取 di = 1(i >= 1) 位置，即所有记录成为一个组，最后对这个组进行插入排序。一般选 d1 约为 n/2，d2 为 d1 /2， d3 为 d2/2 ，…， di = 1
    :param reverse:
    :return:
    '''

    step = len(nums)//2
    while step > 0:
        for i in range(step,len(nums)):
            j = i - step
            while j >= 0:
                if reverse:
                    if nums[j + step] > nums[j]:
                        tmp = nums[j]
                        nums[j]=nums[j+step]
                        nums[j+step] = tmp
                        j -= step
                    else:
                        break
                elif nums[j+step] < nums[j]:
                    tmp = nums[j]
                    nums[j] = nums[j+step]
                    nums[j+step] = tmp
                    j -= step
                else:
                    break
        step = step //2




if __name__ == '__main__':
    list = [2,5,3,9,12,7,8,10]
    print(list)
    #bubble_sort(list)
    #select_sort(list)
    #insert_sort(list)
    shell_sort(list)
    print(list)


