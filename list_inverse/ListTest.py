# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 20:58:33 2019

@author: Elevenoo
"""

class Node:
    def __init__(self,item):
        self.item = item
        self.next = None
        

class SingleLinkedList:
    # 初始化
    def __init__(self):
        self.head = None
        self.size = 0
        
        
    # 在头节点添加
    def add(self,item):
        node = Node(item)
        node.next = self.head
        self.head = node
        self.size = self.size + 1
        
    # 在指定节点添加
    def insert(self,item,index):
        if index > self.size or index < 1:
            print("index out of list!, 0 < index < " + str(self.size))
        else:
            node = Node(item)
            cur = self.head
            i = 1
            while i < index:
                i = i + 1
                cur = cur.next
            
            nex = cur.next
            cur.next = node
            node.next = nex
            self.size = self.size + 1
                
        
    # 在尾节点添加
    def append(self, item):

        if not self.head:
            self.add(item)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(item)
            
        self.size = self.size + 1
        
        
    # 删除指定位置节点
    def delete_index(self,index):
        if index > self.size or index < 1:
            print("index out of list!, 0 < index < " + str(self.size))
        else:
            cur = self.head
            i = 1
            while i < index-1:
                i = i + 1
                cur = cur.next
            cur.next=cur.next.next
            self.size = self.size - 1
    
        
    # 查找item元素是否存在
    def search(self,item):
        cur = self.head
        while cur != None:
            if cur.item == item:
                return True
            else:
                cur = cur.next
        return False
    
    # 指定位置段的节点反转
    def inverse(self,m,n):
        if m < 1 or n > self.size:
            print("index out of list!, 0 < m,n < " + str(self.size))
        else:
            if m == n:
                return
            if m > n:
                temp = n
                n = m
                m = temp
                
                
#            # 方法一，逐次反转两个节点前保留后一个节点
#            print("method 1")
#            cur = self.head  
#            pre = None
#            i = 1
#            while i < m:
#                pre = cur
#                cur = cur.next
#                i = i + 1
#                
#            node_m_1 = pre
#            node_m = cur
#            
#            nex = cur.next
#            while i < n: 
#                pre = cur
#                cur = nex
#                nex = cur.next
#                cur.next = pre
#                i = i + 1
#            
#            if node_m_1 != None:
#                node_m_1.next = cur
#            else:
#                self.head = cur
#            node_m.next = nex
#            
            
            # 方法二,递归反转
            print("method 2")
            cur = self.head  
            pre = None
            i = 1
            while i < m:
                pre = cur
                cur = cur.next
                i = i + 1
            node_m_1 = pre
            node_m = cur
            
            while i < n:
                cur = cur.next
                i = i + 1
            node_n = cur
            nex = cur.next
            
            SingleLinkedList.recursiveinverse(node_m,node_n)
            
            if node_m_1 != None:
                node_m_1.next = node_n
            else:
                self.head = node_n
                
            node_m.next = nex
            
    # 递归反转
    def recursiveinverse(head,tail):
        if head != tail:
            newhead = head.next
            SingleLinkedList.recursiveinverse(newhead,tail)
            newhead.next = head


    # 获取链表的长度
    def length(self):
        return self.size
    
    # 遍历链表
    def display(self):
        if self.size == 0:
            print('None')
        else:
            cur = self.head
            print(cur.item)
            while cur.next:
                cur = cur.next
                print(cur.item)
                

if __name__ == "__main__":
    linklist = SingleLinkedList()
    for i in range(6):linklist.append(i+1)  
    linklist.display()
    print()
    linklist.inverse(3,5)
    linklist.display()


    
    
                
            
            

                
        