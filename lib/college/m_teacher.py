#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : teacher.py
@site    : 
@Time    : 2018/8/31 16:39
@Software: PyCharm Community Edition
"""
from enum import Enum, unique

from ..vv_person.person import Person, SexEnum
from . import m_major


@unique
class Position(Enum):
    """
    行政职位
    """
    校长 = 1
    副校长 = 2
    教务处主任 = 3
    政教处主任 = 4
    院长 = 5
    专业负责人 = 6
    班主任 = 7


@unique
class Title(Enum):
    """
    职称/头衔
    """
    工程院院士 = 1
    科学院院士 = 2
    长江学者 = 3
    教授 = 4
    副教授 = 5
    讲师 = 6
    助教 = 7


class ImTeacher(Person):
    """
    Teacher类
    """
    def __init__(self):
        super(ImTeacher, self).__init__()
        self._title = 0             # 职称
        self._position = 0          # 职位
        self._major = None         # 所属专业
        self._grade = {}            # 负责教授的年级/班级字典，key为年级编号，value为班级编号列表
        self._curricula = []        # 负责教授的课程

    def __str__(self):
        return self.name

    def to_dict(self):
        """
        将属性放置在字典中
        :return:
        """
        attributes = {}
        attributes['name'] = self.name
        attributes['sex'] = self.sex.name
        attributes['title'] = self.title
        attributes['position'] = self.position
        attributes['curricula'] = self.curricula
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
        attributes_num = 8
        if not isinstance(attributes, dict):
            raise TypeError('attributes')
        if attributes_num != len(attributes):
            raise ValueError('attributes number error')
        self.name = attributes['name']
        self.sex = SexEnum[attributes['sex']]
        self.title = attributes['title']
        self.position = attributes['position']
        self.curricula = attributes['curricula']
        self.major.name = attributes['major_name']
        self.major.academy.name = attributes['academy_name']
        self.major.academy.college.name = attributes['college_name']

    def add_curriculum(self, curriculum):
        if not isinstance(curriculum, str):
            raise TypeError('curriculum')
        self.curricula.append(curriculum)

    def del_curriculum(self, curriculum):
        if curriculum in self.curricula:
            self.curricula.remove(curriculum)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if title not in Title.__members__.values():
            raise TypeError('title')
        self._title = title

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        if position not in Position.__members__.values():
            raise TypeError('position')
        self._position = position

    @property
    def major(self):
        return self._major

    @major.setter
    def major(self, major):
        if not isinstance(major, m_major.ImMajor):
            raise TypeError('major')
        self._major = major

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        if isinstance(grade, dict):
            raise TypeError('grade')
        self._grade = grade

    @property
    def curricula(self):
        return self._curricula

    @curricula.setter
    def curricula(self, curricula):
        if isinstance(curricula, list):
            raise TypeError('curricula')
        self._curricula = curricula
