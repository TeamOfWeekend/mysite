#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : imStudent.py
@Software: PyCharm Community Edition
@Time    : 2018/7/24 22:28
"""

import random
import datetime

from pypinyin import pinyin, NORMAL
from enum import Enum, unique

from ..vv_person import baijiaxing, person
from . import m_class


@unique
class MaleHobbies(Enum):
    篮球 = 1
    足球 = 2
    网球 = 3
    排球 = 4
    羽毛球 = 5
    台球 = 6
    玩游戏 = 7
    看书 = 8
    写代码 = 9
    看电影 = 10
    旅游 = 11


@unique
class FemaleHobbies(Enum):
    逛街 = 1
    买买买 = 2
    看书 = 3
    看电影 = 4
    旅游 = 5
    化妆 = 6


class ImStudent(person.Person):
    """大学生"""
    def __init__(self):
        # 继承父类的构造方法，两种方式
        # person.Person.__init__()
        super(ImStudent, self).__init__()
        self._id = 0                 # 学号
        self._name_pinyin = ''       # 名字拼音
        self._year_in_college = 0    # 入学年份
        self._cclass = None          # 所属班级
        self._hobbies = []           # 爱好

    def to_dict(self):
        """
        将属性放置在字典中
        :return:
        """
        attributes = {}
        attributes['id'] = self.id
        attributes['name'] = self.name
        attributes['name_pinyin'] = self.name_pinyin
        attributes['sex'] = self.sex.name
        attributes['age'] = self.age
        attributes['year_in_college'] = self.year_in_college
        attributes['height'] = self.height
        attributes['weight'] = self.weight
        attributes['id_number'] = self.id_number
        attributes['hobbies'] = ''
        attributes['bust'] = self.bust
        attributes['waist'] = self.waist
        attributes['hips'] = self.hips
        attributes['married'] = self.married.name
        attributes['class_id'] = self.cclass.id
        attributes['grade_id'] = self.cclass.grade.id
        attributes['major_name'] = self.cclass.grade.major.name
        attributes['academy_name'] = self.cclass.grade.major.academy.name
        attributes['college_name'] = self.cclass.grade.major.academy.college.name
        cnt = 0
        for hobby in self.hobbies:
            if 0 == cnt:
                attributes['hobbies'] += hobby.name
            else:
                attributes['hobbies'] += ('、' + hobby.name)
            cnt += 1
        return attributes

    def from_dict(self, attributes):
        """
        从字典中取值，填充实例属性
        :param attributes:
        :return:
        """
        attributes_num = 19
        if not isinstance(attributes, dict):
            raise TypeError('attributes')
        if attributes_num != len(attributes):
            raise ValueError('attributes number error')
        self.id = attributes['id']
        self.name = attributes['name']
        self.name_pinyin = attributes['name_pinyin']
        self.sex = person.SexEnum[attributes['sex']]
        self.age = attributes['age']
        self.year_in_college = attributes['year_in_college']
        self.height = attributes['height']
        self.weight = attributes['weight']
        self.id_number = attributes['id_number']
        self.bust = attributes['bust']
        self.waist = attributes['waist']
        self.hips = attributes['hips']
        self.married = person.MarriedEnum[attributes['married']]
        self.cclass.id = attributes['class_id']
        self.cclass.grade.id = attributes['grade_id']
        self.cclass.grade.major.name = attributes['major_name']
        self.cclass.grade.major.academy.name = attributes['academy_name']
        self.cclass.grade.major.academy.college.name = attributes['college_name']
        if len(attributes['hobbies']) > 0:
            hobbies_name = attributes['hobbies'].split('、')
            for hobby_name in hobbies_name:
                if self.sex is person.SexEnum.男:
                    self.add_hobby(MaleHobbies[hobby_name])
                elif self.sex is person.SexEnum.女:
                    self.add_hobby(FemaleHobbies[hobby_name])

    def get_random_name(self):
        """随机获取一个名字"""
        self.name = baijiaxing.get_random_name()
        # 将汉字转换为拼音，pinyin()转换后是列表，不加style转换后带声调
        pos = 1
        for piny in pinyin(self.name, style=NORMAL):
            piny = ''.join(piny)
            if (1 == pos) or (2 == pos):
                piny = piny.capitalize()
            self.name_pinyin += piny
            pos += 1
        # print(self.namePinYin)

    def get_random_sex(self):
        """随机获取性别"""
        random_int = random.randint(1, len(person.SexEnum))
        self.sex = person.SexEnum(random_int).name

    def get_random_hobbies(self):
        """获取随机爱好"""

        hobby_cnt = 0
        if person.SexEnum.男 == self.sex:
            ranInts = random.sample(range(1, len(MaleHobbies) + 1), random.randint(1, len(MaleHobbies)))
            for ranInt in ranInts:
                self.add_hobby(MaleHobbies(ranInt))
        else:
            ranInts = random.sample(range(1, len(FemaleHobbies) + 1), random.randint(1, len(FemaleHobbies)))
            for ranInt in ranInts:
                self.add_hobby(FemaleHobbies(ranInt))

    def create_id(self):
        """根据入学年份、学校、院系、专业，生成学号，如 2018 000011 002 03 05"""
        self.id = self.year_in_college * 10**13 +\
                  self.cclass.grade.major.academy.college.id * 10**7 +\
                  self.cclass.grade.major.academy.id * 10**4 +\
                  self.cclass.grade.major.id * 10**2 +\
                  self.id
        # print('%6s --> %d' % (self.name, self.id))

    def get_random_attributes(self):
        """创建随机属性"""
        if datetime.datetime.now().month < 6:
            self.year_in_college = datetime.datetime.now().year - self.cclass.grade.id
        else:
            self.year_in_college = datetime.datetime.now().year - self.cclass.grade.id + 1

        self.get_random_name()
        self.get_random_sex()
        self.get_random_hobbies()
        # self.createId()
        self.age = (datetime.datetime.now().year - self.year_in_college + 17)
        self.height = round(random.randint(130, 200) + random.random(), 1)
        self.weight = round(random.randint(30, 100) + random.random(), 1)

    def to_pinyin(self):
        """
        将名字转换为拼音
        :return:
        """
        # 将汉字转换为拼音，pinyin()转换后是列表，不加style转换后带声调
        pos = 1
        for piny in pinyin(self.name, style=NORMAL):
            piny = ''.join(piny)
            if (1 == pos) or (2 == pos):
                piny = piny.capitalize()
            self.name_pinyin += piny
            pos += 1
            # print(self.namePinYin)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, val):
        if not isinstance(val, int):
            raise TypeError('id')
        self._id = val

    @property
    def name_pinyin(self):
        return self._name_pinyin

    @name_pinyin.setter
    def name_pinyin(self, name_pinyin):
        if not isinstance(name_pinyin, str):
            raise TypeError('name_pinyin')
        self._name_pinyin = name_pinyin

    @property
    def year_in_college(self):
        return self._year_in_college

    @year_in_college.setter
    def year_in_college(self, year):
        if not isinstance(year, int):
            raise TypeError('year')
        self._year_in_college = year

    @property
    def cclass(self):
        return self._cclass

    @cclass.setter
    def cclass(self, cclass):
        if not isinstance(cclass, m_class.ImClass):
            raise TypeError('cclass')
        self._cclass = cclass

    @property
    def hobbies(self):
        return self._hobbies

    def add_hobby(self, hobby):
        if self.sex is person.SexEnum.男:
            if hobby in MaleHobbies.__members__.values():
                self._hobbies.append(hobby)
                return True
        elif self.sex is person.SexEnum.女:
            if hobby in FemaleHobbies.__members__.values():
                self._hobbies.append(hobby)
                return True
        raise TypeError('hobby')
