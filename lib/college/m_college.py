#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : imCollege.py
@Software: PyCharm Community Edition
@Time    : 2018/7/24 22:07
"""
from enum import Enum, unique
# import random

from . import m_academy
from . import m_teacher
from . import m_city


@unique
class CollegeLevel(Enum):
    """学校级别"""
    未知 = 1
    双一流 = 2
    普通一本 = 3
    二本 = 4
    三本 = 5
    专科 = 6


class ImCollege:
    """大学"""

    def __init__(self):
        """学校属性"""
        self._name = ''  # 学校名称
        self._id = 0  # 学校编号
        self._description = ''  # 学校简介
        self._city = m_city.ImCity()  # 所在城市
        self._address = ''  # 学校地址
        self._level = CollegeLevel.未知  # 学校级别
        self._area = 0  # 校园面积
        self._headmaster = m_teacher.ImTeacher()  # 校长
        self._birthday = ''  # 学院数量
        self._academies_num = 0  # 学院数量
        self._academies_name = []  # 学院名称列表
        self._academies = {}  # 学院信息字典，key为学院名，value为学院对象
        self._majors_num = 0  # 专业数量
        self._teachers_num = 0  # 教师数量
        self._students_num = 0  # 学生数量

    def to_dict(self):
        """
        将ImCollege实例的属性按顺序放置在字典中
        :return:
        """
        attributes = {}
        attributes['name'] = self.name
        attributes['id'] = self.id
        attributes['description'] = self.description
        attributes['address'] = self.address
        attributes['level'] = self.level.value
        attributes['area'] = self.area
        attributes['headmaster_name'] = self.headmaster.name
        attributes['birthday'] = self.birthday
        attributes['academies_num'] = self.academies_num
        attributes['majors_num'] = self.majors_num
        attributes['students_num'] = self.students_num
        attributes['teachers_num'] = self.teachers_num
        attributes['academies_name'] = self.academies_name
        return attributes

    def from_dict(self, attributes):
        """
        从字典中取值，填充实例属性
        :param attributes:
        :return:
        """
        attributes_num = 13
        if not isinstance(attributes, dict):
            raise TypeError('attributes')
        if attributes_num != len(attributes):
            raise ValueError('attributes number error')
        self.name = attributes['name']
        self.id = attributes['id']
        self.description = attributes['description']
        self.address = attributes['address']
        self.level = CollegeLevel(attributes['level'])
        self.area = attributes['area']
        self.headmaster.name = attributes['headmaster_name']
        self.birthday = attributes['birthday']
        self.academies_num = attributes['academies_num']
        self.academies_name = attributes['academies_name']
        self.majors_num = attributes['majors_num']
        self.students_num = attributes['students_num']
        self.teachers_num = attributes['teachers_num']

    def add_academy(self, academy):
        """
        增加一个学院
        :param academy: ImAcademy实例对象
        :return:
        """
        if not isinstance(academy, m_academy.ImAcademy):
            raise TypeError('academy')
        if (academy.name in self.academies.keys()) or (academy.name in self._academies_name):
            raise ValueError('academy exists, add failed')
        academy.college = self
        self.academies_num += 1
        self.academies_name.append(academy.name)
        self.academies[academy.name] = academy
        self.teachers_num += academy.teachers_num
        self.students_num += academy.students_num
        self.majors_num += academy.majors_num

    def del_academy(self, academy_name):
        """
        删除一个学院
        :param academy_name: 学院名称
        :return:
        """
        if not isinstance(academy_name, str):
            raise TypeError('academy_name')
        if (academy_name not in self._academies_name) or (academy_name not in self.academies.keys()):
            raise ValueError('%s not exists, del failed' % academy_name)
        academy = self.academies[academy_name]
        self.academies_num -= 1
        self.teachers_num -= academy.teachers_num
        self.students_num -= academy.students_num
        self.majors_num -= academy.majors_num
        self.academies_name.remove(academy_name)
        del self.academies[academy_name]

    def get_academy(self, academy_name):
        """
        根据学院名获取学院对象
        :param academy_name:
        :return:
        """
        if not isinstance(academy_name, str):
            raise TypeError('academy_name')
        if academy_name in self.academies.keys():
            return self.academies[academy_name]
        else:
            return None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('college name must be type of str')
        self._name = name

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, val):
        if not isinstance(val, int):
            raise TypeError('college id must be type of int')
        self._id = val

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        if not isinstance(description, str):
            raise TypeError('college description must be type of str')
        self._description = description

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        if not isinstance(city, m_city.ImCity):
            raise TypeError('city')
        self._city = city

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        if not isinstance(address, str):
            raise TypeError('college address must be type of str')
        self._address = address

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        if level not in CollegeLevel.__members__.values():
            raise TypeError('college address must be member of CollegeLevel')
        self._level = level

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, val):
        if not isinstance(val, int):
            raise TypeError('area must be type of int')
        self._area = val

    @property
    def headmaster(self):
        return self._headmaster

    @headmaster.setter
    def headmaster(self, headmaster):
        if not isinstance(headmaster, m_teacher.ImTeacher):
            raise TypeError('headmaster')
        self._headmaster = headmaster

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, date):
        if not isinstance(date, str):
            raise TypeError('date')
        self._birthday = date

    @property
    def academies_num(self):
        return self._academies_num

    @academies_num.setter
    def academies_num(self, academies_num):
        if not isinstance(academies_num, int):
            raise TypeError('academies_num')
        self._academies_num = academies_num

    @property
    def majors_num(self):
        return self._majors_num

    @majors_num.setter
    def majors_num(self, num):
        if not isinstance(num, int):
            raise TypeError('num')
        self._majors_num = num

    @property
    def students_num(self):
        return self._students_num

    @students_num.setter
    def students_num(self, num):
        if not isinstance(num, int):
            raise TypeError('num')
        self._students_num = num

    @property
    def teachers_num(self):
        return self._teachers_num

    @teachers_num.setter
    def teachers_num(self, num):
        if not isinstance(num, int):
            raise TypeError('num')
        self._teachers_num = num

    @property
    def academies_name(self):
        return self._academies_name

    @academies_name.setter
    def academies_name(self, academies_name):
        if not isinstance(academies_name, list):
            raise TypeError('academies_name')
        self._academies_name = academies_name

    @property
    def academies(self):
        return self._academies

    @academies.setter
    def academies(self, academies):
        if not isinstance(academies, dict):
            raise TypeError('academies must be type of dict')
        self._academies = academies

