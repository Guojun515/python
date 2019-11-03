#!/usr/bin/env python 
# -*- coding:utf-8 -*-


class Parent:
    """
    这里是类注释
    Python个面向对象的内容
    """

    TOTAL_COUNT = 0  # Parent类的全局变量

    def __init__(self):
        self.desc = "爸爸"  # 成员属性
        self._sex = "男"  # protected属性
        self.__name = "张三"  # private属性

    # 定义一个类方法（只能类调用）
    @classmethod
    def getTotalCount(cls):
        return cls.TOTAL_COUNT

    # 实例方法，修改成员变量
    def setSex(self, sex):
        self._sex = sex

    # 实例方法，获取私有变量的值
    def getName(self):
        return self.__name

    # 静态方法，可以类调用与成员调用
    @staticmethod
    def sum(a, b):
        return a + b

    @property
    def sex(self):
        return self._sex


if __name__ == "__main__":
    p = Parent()
    print(p.getName())

    p.setSex("女")
    print(p.sex)

    print(p.desc)

    print(Parent.getTotalCount())

    print(p.sum(1, 2))
    print(Parent.sum(3, 4))

    print(Parent.__doc__)
    print(Parent.__module__)
    print(Parent.__name__)
    print(Parent.__dict__)
    print(Parent.__bases__)
