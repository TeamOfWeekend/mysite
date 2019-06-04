#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : imTypes.py
@site    : 
@Time    : 2018/7/25 11:19
@Software: PyCharm Community Edition
"""


class CollegeInformation:
    """
    学校信息类，存放各个学校信息，包括学校名称、每个学校包含的学院、每个学院包含的专业、
    每个专业包含的年级、每个年级包含的班级
    """
    def __init__(self):
        self._information = {}
        self._college_num = 0
        self._academy_num = 0
        self._major_num = 0
        self._grade_num = 0
        self._class_num = 0

    def add_college_info(self, college_name):
        """
        增加一项学校信息
        :param college_name: 学校名称
        :return:
        """
        if not isinstance(college_name, str):
            raise TypeError('college_name')
        if college_name in self.information.keys():
            return False
        else:
            self.information[college_name] = {}
            self._college_num += 1
            return True

    def del_college_info(self, college_name):
        """
        删除一项学校信息
        :param college_name:
        :return:
        """
        if not isinstance(college_name, str):
            raise TypeError('college_name')
        if college_name in self.information.keys():
            del self.information[college_name]
            self._college_num -= 1
            return True
        return False

    def add_academy_info(self, college_name, academy_name):
        """
        增加一项学院信息
        :param college_name: 学校名称
        :param academy_name: 学院名称
        :return:
        """
        if not isinstance(college_name, str):
            raise TypeError('college_name')
        if not isinstance(academy_name, str):
            raise TypeError('academy_name')
        if college_name in self.information.keys():
            college_into = self.information[college_name]
            if academy_name not in college_into.keys():
                college_into[academy_name] = {}
                self._academy_num += 1
                return True
        return False

    def del_academy_info(self, college_name, academy_name):
        """
        删除一项学院信息
        :param college_name:
        :param academy_name:
        :return:
        """
        if not isinstance(college_name, str):
            raise TypeError('college_name')
        if not isinstance(academy_name, str):
            raise TypeError('academy_name')
        if college_name in self.information.keys():
            college_into = self.information[college_name]
            if academy_name in college_into.keys():
                del college_into[academy_name]
                self._academy_num -= 1
                return True
        return False

    def add_major_info(self, college_name, academy_name, major_name):
        """
        增加一项专业信息
        :param college_name:
        :param academy_name:
        :param major_name:
        :return:
        """
        if not isinstance(college_name, str):
            raise TypeError('college_name')
        if not isinstance(academy_name, str):
            raise TypeError('academy_name')
        if not isinstance(major_name, str):
            raise TypeError('major_name')
        if college_name in self.information.keys():
            college_into = self.information[college_name]
            if academy_name in college_into.keys():
                academy_info = college_into[academy_name]
                if major_name not in academy_info.keys():
                    academy_info[major_name] = {}
                    self._major_num += 1
                    return True
        return False

    def del_major(self, college_name, academy_name, major_name):
        """
        删除一项专业信息
        :param college_name:
        :param academy_name:
        :param major_name:
        :return:
        """
        if not isinstance(college_name, str):
            raise TypeError('college_name')
        if not isinstance(academy_name, str):
            raise TypeError('academy_name')
        if not isinstance(major_name, str):
            raise TypeError('major_name')
        if college_name in self.information.keys():
            college_info = self.information[college_name]
            if academy_name in college_info.keys():
                academy_info = college_info[academy_name]
                if major_name in academy_info.keys():
                    del academy_info[major_name]
                    self._major_num -= 1
                    return True
        return False

    def add_grade_info(self, college_name, academy_name, major_name, grade_id):
        """
        增加一项年级信息
        :param college_name:
        :param academy_name:
        :param major_name:
        :param grade_id:
        :return:
        """
        if not isinstance(college_name, str):
            raise TypeError('college_name')
        if not isinstance(academy_name, str):
            raise TypeError('academy_name')
        if not isinstance(major_name, str):
            raise TypeError('major_name')
        if not isinstance(grade_id, int):
            raise TypeError('grade_id')
        if college_name in self.information.keys():
            college_info = self.information[college_name]
            if academy_name in college_info.keys():
                academy_info = college_info[academy_name]
                if major_name in academy_info.keys():
                    major_info = academy_info[major_name]
                    if grade_id not in major_info.keys():
                        major_info[grade_id] = []
                        self._grade_num += 1
                        return True
        return False

    def del_grade_info(self, college_name, academy_name, major_name, grade_id):
        """
        删除一项年级信息
        :param college_name:
        :param academy_name:
        :param major_name:
        :param grade_id:
        :return:
        """
        if not isinstance(college_name, str):
            raise TypeError('college_name')
        if not isinstance(academy_name, str):
            raise TypeError('academy_name')
        if not isinstance(major_name, str):
            raise TypeError('major_name')
        if not isinstance(grade_id, int):
            raise TypeError('grade_id')
        if college_name in self.information.keys():
            college_info = self.information[college_name]
            if academy_name in college_info.keys():
                academy_info = college_info[academy_name]
                if major_name in academy_info.keys():
                    major_info = academy_info[major_name]
                    if grade_id in major_info.keys():
                        del major_info[grade_id]
                        self._grade_num -= 1
                        return True
        return False

    def add_class_info(self, college_name, academy_name, major_name, grade_id, class_id):
        """
        增加一个班级信息，班级使用list存储
        :param college_name:
        :param academy_name:
        :param major_name:
        :param grade_id:
        :param class_id:
        :return:
        """
        if not isinstance(college_name, str):
            raise TypeError('college_name')
        if not isinstance(academy_name, str):
            raise TypeError('academy_name')
        if not isinstance(major_name, str):
            raise TypeError('major_name')
        if not isinstance(grade_id, int):
            raise TypeError('grade_id')
        if not isinstance(class_id, int):
            raise TypeError('class_id')
        if college_name in self.information.keys():
            college_info = self.information[college_name]
            if academy_name in college_info.keys():
                academy_info = college_info[academy_name]
                if major_name in academy_info.keys():
                    major_info = academy_info[major_name]
                    if grade_id in major_info.keys():
                        grade_info = major_info[grade_id]
                        if class_id not in grade_info:
                            grade_info.append(class_id)
                            self._class_num += 1
                            return True
        return False

    def del_class_info(self, college_name, academy_name, major_name, grade_id, class_id):
        """
        增加一个班级信息，班级使用list存储
        :param college_name:
        :param academy_name:
        :param major_name:
        :param grade_id:
        :param class_id:
        :return:
        """
        if not isinstance(college_name, str):
            raise TypeError('college_name')
        if not isinstance(academy_name, str):
            raise TypeError('academy_name')
        if not isinstance(major_name, str):
            raise TypeError('major_name')
        if not isinstance(grade_id, int):
            raise TypeError('grade_id')
        if not isinstance(class_id, int):
            raise TypeError('class_id')
        if college_name in self.information.keys():
            college_info = self.information[college_name]
            if academy_name in college_info.keys():
                academy_info = college_info[academy_name]
                if major_name in academy_info.keys():
                    major_info = academy_info[major_name]
                    if grade_id in major_info.keys():
                        grade_info = major_info[grade_id]
                        if class_id in grade_info:
                            grade_info.remove(class_id)
                            self._class_num -= 1
                            return True
        return False

    @property
    def information(self):
        return self._information

    @information.setter
    def information(self, information):
        if not isinstance(information, dict):
            raise TypeError('information')
        self._information = information

    @property
    def college_num(self):
        return self._college_num

    @property
    def academy_num(self):
        return self._academy_num

    @property
    def major_num(self):
        return self._major_num

    @property
    def grade_num(self):
        return self._grade_num

    @property
    def class_num(self):
        return self._class_num
