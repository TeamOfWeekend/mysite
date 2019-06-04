#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : imGrade.py
@site    : 
@Time    : 2018/7/25 10:09
@Software: PyCharm Community Edition
"""

from . import m_class
from . import m_major


class ImGrade:
    """年级类"""
    def __init__(self):
        self._id = 0            # 年级编号
        self._students_num = 0  # 学生数量
        self._classes_num = 0   # 包含的班级数量
        self._classes = {}      # 存放班级的字典
        self._major = None      # 所属的专业

    def to_dict(self):
        """
        将所有属性放在一个字典中
        :return:
        """
        attributes = {}
        attributes['id'] = self.id
        attributes['students_num'] = self.students_num
        attributes['classes_num'] = self.classes_num
        attributes['major_name'] = self.major.name
        attributes['academy_name'] = self.major.academy.name
        attributes['college_name'] = self.major.academy.college.name
        return attributes

    def from_dict(self, attributes):
        """
        从字典中取值，填充实例属性
        :param attributes:
        :return:
        """
        attributes_num = 6
        if not isinstance(attributes, dict):
            raise TypeError('attributes')
        if attributes_num != len(attributes):
            raise ValueError('attributes number error')
        self.id = attributes['id']
        self.students_num = attributes['students_num']
        self.classes_num = attributes['classes_num']
        self.major.name = attributes['major_name']
        self.major.academy.name = attributes['academy_name']
        self.major.academy.college.name = attributes['college_name']

    def add_class(self, classs):
        if not isinstance(classs, m_class.ImClass):
            raise TypeError('classs')
        if classs.id not in self.classes.keys():
            classs.grade = self
            self.classes[classs.id] = classs
            self.classes_num += 1
            self.students_num += classs.students_num
            self.major.students_num += classs.students_num
            self.major.academy.students_num += classs.students_num
            self.major.academy.college.students_num += classs.students_num

    def del_class(self, class_id):
        if not isinstance(class_id, int):
            raise TypeError('class_id')
        if class_id not in self.classes.keys():
            classs = self.classes[class_id]
            self.classes_num -= 1
            self.students_num -= classs.students_num
            self.major.students_num -= classs.students_num
            self.major.academy.students_num -= classs.students_num
            self.major.academy.college.students_num -= classs.students_num
            del self.classes[class_id]

    def get_class(self, class_id):
        """
        根据班级编号获取班级对象
        :param class_id:
        :return:
        """
        if not isinstance(class_id, int):
            raise TypeError('class_id')
        if class_id in self.classes.keys():
            return self.classes[class_id]
        else:
            return None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, val):
        if not isinstance(val, int):
            raise TypeError('val')
        self._id = val

    @property
    def students_num(self):
        return self._students_num

    @students_num.setter
    def students_num(self, students_num):
        if not isinstance(students_num, int):
            raise TypeError('students_num')
        self._students_num = students_num

    @property
    def classes_num(self):
        return self._classes_num

    @classes_num.setter
    def classes_num(self, classes_num):
        if not isinstance(classes_num, int):
            raise TypeError('classes_num')
        self._classes_num = classes_num

    @property
    def classes(self):
        return self._classes

    @classes.setter
    def classes(self, classes):
        if not isinstance(classes, dict):
            raise TypeError('classes')
        self._classes = classes

    @property
    def major(self):
        return self._major

    @major.setter
    def major(self, major):
        if not isinstance(major, m_major.ImMajor):
            raise TypeError('major')
        self._major = major
