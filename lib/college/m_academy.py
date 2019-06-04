#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : imAcademy.py
@Software: PyCharm Community Edition
@Time    : 2018/7/24 22:29
"""

from . import m_major
from . import m_college


class ImAcademy:
    """学院"""
    def __init__(self):
        self._name = ''             # 名称
        self._id = 0                # 编号
        self._description = ''      # 学院概述
        self._majors_num = 0        # 专业数量
        self._majors_name = []      # 专业名称
        self._majors = {}           # 专业
        self._students_num = 0      # 学生数量
        self._teachers_num = 0      # 教师数量
        self._college = None        # 所属学校

    def to_dict(self):
        """
        将所有属性放在一个字典中
        :return:
        """
        attributes = {}
        attributes['name'] = self.name
        attributes['id'] = self.id
        attributes['description'] = self.description
        attributes['majors_num'] = self.majors_num
        attributes['majors_name'] = self.majors_name
        attributes['teachers_num'] = self.teachers_num
        attributes['students_num'] = self.students_num
        attributes['college_name'] = self.college.name
        return attributes
    
    def from_dict(self, attributes):
        """
        从字典中取值，填充实例属性
        :param attributes:
        :return:
        """
        attributes_num = 8
        if not isinstance(attributes, dict):
            raise TypeError('attributes')
        if attributes_num != len(attributes):
            raise ValueError('attributes number error')
        self.name = attributes['name']
        self.id = attributes['id']
        self.description = attributes['description']
        self.majors_num = attributes['majors_num']
        self.majors_name = attributes['majors_name']
        self.teachers_num = attributes['teachers_num']
        self.students_num = attributes['students_num']
        self.college.name = attributes['college_name']

    def add_major(self, major):
        if not isinstance(major, m_major.ImMajor):
            raise TypeError('major')
        if major.name not in self.majors.keys():
            major.academy = self
            self.majors[major.name] = major
            self.majors_num += 1
            self.majors_name.append(major.name)
            self.students_num += major.students_num
            self.teachers_num += major.teachers_num
            self.college.majors_num += 1
            self.college.students_num += major.students_num
            self.college.teachers_num += major.teachers_num

    def del_major(self, major_name):
        if not isinstance(major_name, str):
            raise TypeError('major_name')
        if major_name in self.majors.keys():
            major = self.majors[major_name]
            self.majors_num -= 1
            self.majors_name.remove(major.name)
            self.students_num -= major.students_num
            self.teachers_num -= major.teachers_num
            self.college.majors_num -= 1
            self.college.students_num -= major.students_num
            self.college.teachers_num -= major.teachers_num
            del self.majors[major_name]

    def get_major(self, major_name):
        """
        根据专业名获取专业对象
        :param major_name:
        :return:
        """
        if not isinstance(major_name, str):
            raise TypeError('major_name')
        if major_name in self.majors.keys():
            return self.majors[major_name]
        else:
            return None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('name')
        self._name = name

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, val):
        if not isinstance(val, int):
            raise TypeError('id')
        self._id = val

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        if not isinstance(description, str):
            raise TypeError('description')
        self._description = description

    @property
    def majors_num(self):
        return self._majors_num

    @majors_num.setter
    def majors_num(self, majors_num):
        if not isinstance(majors_num, int):
            raise TypeError('majors_num')
        self._majors_num = majors_num

    @property
    def majors_name(self):
        return self._majors_name

    @majors_name.setter
    def majors_name(self, majors_name):
        if not isinstance(majors_name, list):
            raise TypeError('majors_name')
        self._majors_name = majors_name

    @property
    def majors(self):
        return self._majors

    @majors.setter
    def majors(self, majors):
        if not isinstance(majors, dict):
            raise TypeError('major_dict')
        self._majors = majors

    @property
    def students_num(self):
        return self._students_num

    @students_num.setter
    def students_num(self, students_num):
        if not isinstance(students_num, int):
            raise TypeError('students_num')
        self._students_num = students_num

    @property
    def teachers_num(self):
        return self._teachers_num

    @teachers_num.setter
    def teachers_num(self, teachers_num):
        if not isinstance(teachers_num, int):
            raise TypeError('teachers_num')
        self._teachers_num = teachers_num

    @property
    def college(self):
        return self._college

    @college.setter
    def college(self, college):
        if not isinstance(college, m_college.ImCollege):
            raise TypeError('college')
        self._college = college
