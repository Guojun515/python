#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from abc import ABCMeta,abstractmethod


class ITree(metaclass=ABCMeta):
    """
    树的定义（抽象类）
    """
    @abstractmethod
    def add(self, e):
        """
        新增元素
        :param e:
        :return:
        """
        pass

    @abstractmethod
    def size(self):
        """
        获取树的大小
        :param e:
        :return:
        """
        pass

    @abstractmethod
    def contains(self, e):
        """
        查找元素是否存在
        :param e:
        :return:
        """
        pass

    @abstractmethod
    def beforeTraverse(self):
        """
                 5
               /   \
              3     7
             / \   / \
            2   4 6   9
        树的前序遍历，先遍历根节点，再遍历左子树，最后遍历右子树:5,3,2,4,7,6,9
        :return:
        """
        pass

    @abstractmethod
    def centerTraverse(self):
        """
                 5
               /   \
              3     7
             / \   / \
            2   4 6   9
        树的中序遍历，先遍历左子树，再遍历父节点，后遍历右子树:2,3,4,5,6,7,9
        :return:
        """
        pass

    @abstractmethod
    def afterTraverse(self):
        """
                 5
               /   \
              3     7
             / \   / \
            2   4 6   9
        树的后序遍历，先遍历左子树，再遍历右子树，最后遍历根节点:2,4,3,6,9,7,5
        :return:
        """
        pass
