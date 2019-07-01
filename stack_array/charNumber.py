# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 20:36:45 2019

@author: Elevenoo
"""
import numpy as np

class Stack:

    def __init__(self):
        self.top = 0
        self.size = 0
        self.data = []
        
    # 压入元素
    def push(self,item):
        self.data.insert(self.top,item)     
        self.top += 1
        self.size = self.size + 1
    # 弹出栈顶元素  
    def pop(self):
        self.top -= 1
        self.size -= 1
        return self.data[self.top]
    # 可视化
    def display(self):
        for i in range(self.size):
            print(self.data[i],end=' ')
       
    
if __name__=="__main__":
    
    # 初始化随机01数组(默认数组长度>1)
    length = 20
    myarray = np.random.randint(0,2,length)
    print("array:",end=' ')
    for n in range(length):print(myarray[n],end=' ')
    # 初始化栈保存未被消除元素
    s = Stack()
    # 标志delta_size用于判断是否消除完毕（则最后一次出栈的元素遍历后没有消除全部入栈，栈的长度不变）
    delta_size = -1
    
    pre_size = 0
    while delta_size != 0:
        # 经历过遍历后的栈中保存了前一轮未被消除的元素，pop出后再次遍历
        if s.size != 0:
            length = 0
            while s.size != 0:
                myarray[length] = s.pop()
                length += 1
        # 若元素左右相同不被消除，压入栈中保存，注意边界元素myarray[0]和myarray[length-1]
        if myarray[0] == myarray[1]:s.push(myarray[0])
        i = 1
        while i < length - 1:
            if myarray[i] == myarray[i-1] and myarray[i] == myarray[i+1]:s.push(myarray[i])
            i += 1
        if myarray[length-2] == myarray[length-1]:s.push(myarray[length-1])
        
        # 查看每次压入栈的元素
        print()
        print("stack:",end='')
        s.display()
        
        # 遍历结束后若栈中没有元素或只有一个元素，则循环结束
        if s.size == 0 or s.size == 1:break
     
        # 判断是否有新被消除的元素
        delta_size = s.size - pre_size
        pre_size = s.size

    # 若没有（delta_size==0）则判断结束，输出栈的长度即剩余元素的个数
    print()
    print("result: " + str(s.size))

    
    

        
