#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from com.guojun.tree.ITree import ITree


class BinarySearchTree(ITree):
    """
    二分搜索树的Python实现
    """

    class __Node :
        """
        私有内部类，树的节点
        """
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.__root = None
        self.__size = 0

    def size(self):
        return self.__size

    def add(self, e):
        self.__root = self.__add(self.__root, e)

    def __add(self, node, e):
        if node is None:
            node = self.__Node(e)
            self.__size = self.__size + 1
        else:
            if node.data > e :
                node.left = self.__add(node.left, e)
            else:
                node.right = self.__add(node.right, e)
        return node

    def contains(self, e):
        return self.__contains(self.__root, e)

    def __contains(self, node, e):
        if node is None:
            return False
        if node.data == e:
            return True
        elif node.data < e:
            return self.__contains(node.left, e)
        else:
            return self.__contains(node.right, e)

    def beforeTraverse(self):
        if self.__root is None:
            raise ValueError("没有数据！")
        stack = list([])
        stack.append(self.__root)
        while len(stack) > 0:
            node = stack.pop(-1)
            print(node.data)

            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)

    def centerTraverse(self):
        pass

    def afterTraverse(self):
        pass


if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.add(5)
    tree.add(3)
    tree.add(2)
    tree.add(4)
    tree.add(7)
    tree.add(6)
    tree.add(9)
    print(tree.size())
    print(tree.contains(2))
    tree.beforeTraverse()
