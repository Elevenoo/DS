# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 9:30:07 2019

@author: Elevenoo
"""
##统计数组中元素重复次数并排序

import numpy as np


class sortItemCount:
    def __init__(self):
        self.item = []
        self.value = []
        self.length = 0
        
    ## 插入元素，同时统计该元素出现的次数并排序
    def insert(self,item):
        if self.length == 0:
            self.item.append(item)
            self.value.append(1)
            self.length += 1
        else:
            flag = 0
            for i in range(self.length):
                if self.item[i] == item:
                    self.value[i] += 1
                    flag = 1
                    ## 插入重复元素，可能需要重新排序，（段部分重排）
                    index = i
                    while self.value[index] > self.value[index-1] and index > 0:
                        self.value[index-1] , self.value[index] = self.value[index] , self.value[index-1]
                        self.item[index-1] , self.item[index] = self.item[index] , self.item[index-1]
                        index -= 1
                    break   
            ## 新元素插入不用排序
            if flag == 0:
                self.item.append(item)
                self.value.append(1)
                self.length += 1


if __name__=='__main__':

    ## 键入随机数组长度，初始化值范围为0~10的随机数组
    length = int(input('length = '))
    array = np.random.randint(0,10,length)
    for m in range(length):
        print(array[m],end=' ')
    
    ## 遍历array,自定义sortItemCount保存每种元素(item)和它出现的次数(value),并排序
    sIC = sortItemCount()
    for m in range(length):
        sIC.insert(array[m])

    item = sIC.item
    value = sIC.value
    
        


