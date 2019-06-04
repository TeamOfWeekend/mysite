#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : imMajor.py
@Software: PyCharm Community Edition
@Time    : 2018/7/24 22:30
"""


from . import m_grade
from . import m_academy
from . import m_teacher


class ImMajor:
    """专业"""
    def __init__(self):
        self._name = ''             # 名称
        self._id = 0                # 编号
        self._teachers_num = 0      # 专业教师数量
        self._teachers_name = []    # 教师姓名列表
        self._teachers = {}         # 教师
        self._students_num = 0      # 学生数量
        self._grades_num = 0        # 年级数量
        self._grades = {}           # 年级对象字典
        self._academy = None        # 所属学院

    def to_dict(self):
        """
        将所有属性放在字典中
        :return:
        """
        attributes = {}
        attributes['name'] = self.name
        attributes['id'] = self.id
        attributes['teachers_num'] = self.teachers_num
        attributes['teachers_name'] = self.teachers_name
        attributes['grades_num'] = self.grades_num
        attributes['students_num'] = self.students_num
        attributes['academy_name'] = self.academy.name
        attributes['college_name'] = self.academy.college.name
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
        self.teachers_num = attributes['teachers_num']
        self.teachers_name = attributes['teachers_name']
        self.grades_num = attributes['grades_num']
        self.students_num = attributes['students_num']
        self.academy.name = attributes['academy_name']
        self.academy.college.name = attributes['college_name']

    def add_grade(self, grade):
        if not isinstance(grade, m_grade.ImGrade):
            raise TypeError('grade')
        if grade.id not in self.grades.keys():
            grade.major = self
            self.grades[grade.id] = grade
            self.grades_num += 1
            self.students_num += grade.students_num

    def del_grade(self, grade_id):
        if not isinstance(grade_id, int):
            raise TypeError('grade_id')
        if grade_id in self.grades.keys():
            grade = self.grades[grade_id]
            self.grades_num -= 1
            self.students_num -= grade.students_num
            del self.grades[grade_id]

    def get_grade(self, grade_id):
        """
        根据年级编号获取年级对象
        :param grade_id:
        :return:
        """
        if not isinstance(grade_id, int):
            raise TypeError('grade_id')
        if grade_id in self.grades.keys():
            return self.grades[grade_id]
        else:
            return None

    def add_teacher(self, teacher):
        if not isinstance(teacher, m_teacher.ImTeacher):
            raise TypeError('teacher')
        if teacher.name not in self.teachers.keys():
            teacher.major = self
            self.teachers[teacher.name] = teacher
            self.teachers_num += 1
            self.academy.teachers_num += 1
            self.academy.college.teachers_num += 1

    def del_teacher(self, teacher_name):
        if not isinstance(teacher_name, str):
            raise TypeError('teacher_name')
        if teacher_name in self.teachers.keys():
            self.teachers_num -= 1
            self.academy.teachers_num -= 1
            self.academy.college.teachers_num -= 1
            del self.teachers[teacher_name]

    def get_teacher(self, teacher_name):
        """
        根据教师姓名获取教师对象
        :param teacher_name:
        :return:
        """
        if not isinstance(teacher_name, str):
            raise TypeError('teacher_name')
        if teacher_name in self.teachers.keys():
            return self.teachers[teacher_name]
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
    def teachers_num(self):
        return self._teachers_num

    @teachers_num.setter
    def teachers_num(self, teachers_num):
        if not isinstance(teachers_num, int):
            raise TypeError('teachers_num')
        self._teachers_num = teachers_num

    @property
    def teachers_name(self):
        return self._teachers_name

    @teachers_name.setter
    def teachers_name(self, teachers_name):
        if not isinstance(teachers_name, list):
            raise TypeError('teachers_name')
        self._teachers_name = teachers_name

    @property
    def teachers(self):
        return self._teachers

    @teachers.setter
    def teachers(self, teachers):
        if not isinstance(teachers, dict):
            raise TypeError('teachers')
        self._teachers = teachers

    @property
    def students_num(self):
        return self._students_num

    @students_num.setter
    def students_num(self, students_num):
        if not isinstance(students_num, int):
            raise TypeError('students_num')
        self._students_num = students_num

    @property
    def grades_num(self):
        return self._grades_num

    @grades_num.setter
    def grades_num(self, grades_num):
        if not isinstance(grades_num, int):
            raise TypeError('grades_num')
        self._grades_num = grades_num

    @grades_num.setter
    def grades_num(self, grades_num):
        if not isinstance(grades_num, int):
            raise TypeError('grades_num')
        self._grades_num = grades_num

    @property
    def grades(self):
        return self._grades

    @grades.setter
    def grades(self, grades):
        if not isinstance(grades, dict):
            raise TypeError('grades')
        self._grades = grades

    @property
    def academy(self):
        return self._academy

    @academy.setter
    def academy(self, academy):
        if not isinstance(academy, m_academy.ImAcademy):
            raise TypeError('academy')
        self._academy = academy
