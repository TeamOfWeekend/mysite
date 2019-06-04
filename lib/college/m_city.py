#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : m_city.py
@site    : 
@Time    : 2018/9/6 14:00
@Software: PyCharm Community Edition
"""

from enum import Enum, unique


@unique
class CityLevel(Enum):
    直辖市 = 1
    省会 = 2
    地级市 = 3
    县级市 = 4
    乡镇 = 5
    村 = 6


class ImCity:
    """城市类"""

    def __init__(self):
        self._name = ''         # 城市名
        self._province = ''     # 所在省
        self._level = 0         # 行政级别

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('name')
        self._name = name

    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, province):
        if not isinstance(province, str):
            raise TypeError('province')
        self._province = province

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        if level not in CityLevel.__members__.items():
            raise ValueError('level')
        self._level = level.name
