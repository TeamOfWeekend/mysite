#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : data_api.py
@Software: PyCharm Community Edition
@Time    : 2018/8/30 22:26
"""

from .m_college import ImCollege
from .m_academy import ImAcademy
from .m_major import ImMajor
from .m_grade import ImGrade
from .m_class import ImClass
from .m_student import ImStudent
from .m_teacher import ImTeacher


class ImColleges:
    """
    学校集合类
    """
    def __init__(self):
        self._colleges_num = 0
        self._colleges_name = []
        self._colleges = {}

    def to_dict(self):
        """
        将属性放置于字典中
        :return:
        """
        attributes = {}
        attributes['colleges_num'] = self.colleges_num
        attributes['colleges_name'] = self.colleges_name
        return attributes

    def from_dict(self, attributes):
        """
        从字典中取值，填充实例属性
        :param attributes:
        :return:
        """
        attributes_num = 2
        if not isinstance(attributes, dict):
            raise TypeError('attributes')
        if attributes_num != len(attributes):
            raise ValueError('attributes number error')
        self.colleges_num = attributes['colleges_num']
        self.colleges_name = attributes['colleges_name']

    def add_college(self, college):
        """
        向colleges数据库中添加一项college数据
        :param self:
        :param college:
        :return:
        """
        if not isinstance(college, ImCollege):
            raise TypeError('college must be a sample of ImCollege')
        if (college.name not in self.colleges_name) and (college.name not in self.colleges.keys()):
            self.colleges_num += 1
            self.colleges_name.append(college.name)
            self.colleges[college.name] = college
            return True
        else:
            return False

    def del_college(self, college_name):
        """
        删除一项学校信息
        :param college_name:
        :return:
        """
        if not isinstance(college_name, str):
            raise TypeError('college_name')
        if (college_name in self.colleges_name) and (college_name in self.colleges.keys()):
            self.colleges_num -= 1
            self.colleges_name.remove(college_name)
            del self.colleges[college_name]
            return True
        else:
            return False

    def get_college(self, college_name):
        """
        从colleges数据库中获取一项college数据
        :param self:
        :param college_name:
        :return:
        """
        if not isinstance(college_name, str):
            raise TypeError('college_name')
        if (college_name in self.colleges_name) and (college_name in self.colleges.keys()):
            return self.colleges[college_name]
        return None

    def add_academy(self, college_name, academy):
        """
        向学校中添加一项学院数据
        :param self:
        :param college_name:
        :param academy: sample of ImAcademy
        :return:
        """
        if not isinstance(college_name, str):
            raise TypeError('college_name')
        if not isinstance(academy, ImAcademy):
            raise TypeError('academy')
        college = self.get_college(college_name)
        if college is None:
            return False
        else:
            college.add_academy(academy.name)
            return True

    def del_academy(self, college_name, academy_name):
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
        college = self.get_college(college_name)
        if college is None:
            return False
        else:
            college.del_academy(academy_name)
            return True

    def get_academy(self, college_name, academy_name):
        """
        根据学校、学院名称获取学院信息
        :param self:
        :param college_name:
        :param academy_name:
        :return:
        """
        if not isinstance(college_name, str):
            raise TypeError('college_name')
        if not isinstance(academy_name, str):
            raise TypeError('academy_name')
        college = self.get_college(college_name)
        if college is None:
            return None
        else:
            return college.get_academy(academy_name)

    def add_major(self, college_name, academy_name, major):
        """
        根据学校、学院名称、专业名称获取专业信息
        :param self:
        :param college_name:
        :param academy_name:
        :param major:
        :return:
        """
        if not isinstance(college_name, str):
            raise TypeError('college_name')
        if not isinstance(academy_name, str):
            raise TypeError('academy_name')
        if not isinstance(major, ImMajor):
            raise TypeError('major')
        academy = self.get_academy(college_name, academy_name)
        if academy is None:
            return False
        else:
            academy.add_major(major)
            return True

    def del_major(self, college_name, academy_name, major_name):
        """
        删除一个专业
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
        academy_name = self.get_academy(college_name, academy_name)
        if academy_name is None:
            return False
        else:
            academy_name.del_major(major_name)
            return True

    def get_major(self, college_name, academy_name, major_name):
        """
        根据学校、学院名称、专业名称获取专业信息
        :param self:
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
        academy = self.get_academy(college_name, academy_name)
        if academy is None:
            return None
        else:
            return academy.get_major(major_name)

    def add_teacher(self, college_name, academy_name, major_name, teacher):
        """
        根据学校、学院名称、专业名称获取专业，再添加一个教师
        :param college_name:
        :param academy_name:
        :param major_name:
        :param teacher:
        :return:
        """
        if not isinstance(college_name, str):
            raise TypeError('college_name')
        if not isinstance(academy_name, str):
            raise TypeError('academy_name')
        if not isinstance(major_name, str):
            raise TypeError('major_name')
        if not isinstance(teacher, ImTeacher):
            raise TypeError('teacher')
        major = self.get_major(college_name, academy_name, major_name)
        if major is None:
            return False
        else:
            major.add_teacher(teacher)
            return True

    def del_teacher(self, college_name, academy_name, major_name, teacher_name):
        """
        删除一个教师
        :param college_name:
        :param academy_name:
        :param major_name:
        :param teacher_name:
        :return:
        """
        if not isinstance(college_name, str):
            raise TypeError('college_name')
        if not isinstance(academy_name, str):
            raise TypeError('academy_name')
        if not isinstance(major_name, str):
            raise TypeError('major_name')
        if not isinstance(teacher_name, str):
            raise TypeError('teacher_name')
        major = self.get_major(college_name, academy_name, major_name)
        if major is None:
            return False
        else:
            major.del_teacher(teacher_name)
            return True

    def get_teacher(self, college_name, academy_name, major_name, teacher_name):
        """
        根据学校、学院名称、专业名称、教师名称获取教师对象
        :param college_name:
        :param academy_name:
        :param major_name:
        :param teacher_name:
        :return:
        """
        if not isinstance(college_name, str):
            raise TypeError('college_name')
        if not isinstance(academy_name, str):
            raise TypeError('academy_name')
        if not isinstance(major_name, str):
            raise TypeError('major_name')
        if not isinstance(teacher_name, str):
            raise TypeError('teacher_name')
        major = self.get_major(college_name, academy_name, major_name)
        if major is None:
            return None
        else:
            return major.get_teacher(teacher_name)

    def add_grade(self, college_name, academy_name, major_name, grade):
        """
        根据学校、学院名称、专业、年级号名称获取年级信息
        :param self:
        :param college_name:
        :param academy_name:
        :param major_name:
        :param grade:
        :return:
        """
        if not isinstance(college_name, str):
            raise TypeError('college_name')
        if not isinstance(academy_name, str):
            raise TypeError('academy_name')
        if not isinstance(major_name, str):
            raise TypeError('major_name')
        if not isinstance(grade, ImGrade):
            raise TypeError('grade')
        major = self.get_major(college_name, academy_name, major_name)
        if major is None:
            return False
        else:
            major.add_grade(grade)
            return True

    def del_grade(self, college_name, academy_name, major_name, grade_id):
        """
        删除一个年级
        :param self:
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
        major = self.get_major(college_name, academy_name, major_name)
        if major is None:
            return False
        else:
            major.del_grade(grade_id)
            return True

    def get_grade(self, college_name, academy_name, major_name, grade_id):
        """
        根据学校、学院名称、专业、年级号名称获取年级信息
        :param self:
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
        major = self.get_major(college_name, academy_name, major_name)
        return major.get_grade(grade_id)

    def add_classs(self, college_name, academy_name, major_name, grade_id, classs):
        """
        根据学校、学院名称、专业名称、年级号、班级号获取班级信息
        :param self:
        :param college_name:
        :param academy_name:
        :param major_name:
        :param grade_id:
        :param classs:
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
        if not isinstance(classs, ImClass):
            raise TypeError('classs')
        grade = self.get_grade(college_name, academy_name, major_name, grade_id)
        if grade is None:
            return False
        else:
            grade.add_class(classs)
            return True

    def del_classs(self, college_name, academy_name, major_name, grade_id, class_id):
        """
        根据学校、学院名称、专业名称、年级号、班级号获取班级信息
        :param self:
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
        grade = self.get_grade(college_name, academy_name, major_name, grade_id)
        if grade is None:
            return False
        else:
            grade.del_class(class_id)
            return True

    def get_classs(self, college_name, academy_name, major_name, grade_id, class_id):
        """
        根据学校、学院名称、专业名称、年级号、班级号获取班级信息
        :param self:
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
        grade = self.get_grade(college_name, academy_name, major_name, grade_id)
        if grade is None:
            return None
        else:
            return grade.get_class(class_id)

    def add_student(self, college_name, academy_name, major_name, grade_id, class_id, student):
        """
        根据学校、学院名称、专业名称、年级号、班级号、学号获取学生信息
        :param self:
        :param college_name:
        :param academy_name:
        :param major_name:
        :param grade_id:
        :param class_id:
        :param student:
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
        if not isinstance(student, ImStudent):
            raise TypeError('student')
        classs = self.get_classs(college_name, academy_name, major_name, grade_id, class_id)
        if classs is None:
            return False
        else:
            classs.add_student(student)
            return True

    def del_student(self, college_name, academy_name, major_name, grade_id, class_id, student_id):
        """
        根据学校、学院名称、专业名称、年级号、班级号、学号获取学生信息
        :param self:
        :param college_name:
        :param academy_name:
        :param major_name:
        :param grade_id:
        :param class_id:
        :param student_id:
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
        if not isinstance(student_id, int):
            raise TypeError('student_id')
        classs = self.get_classs(college_name, academy_name, major_name, grade_id, class_id)
        if classs is None:
            return False
        else:
            classs.del_student(student_id)
            return True

    def get_student(self, college_name, academy_name, major_name, grade_id, class_id, student_id):
        """
        根据学校、学院名称、专业名称、年级号、班级号、学号获取学生信息
        :param self:
        :param college_name:
        :param academy_name:
        :param major_name:
        :param grade_id:
        :param class_id:
        :param student_id:
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
        if not isinstance(student_id, int):
            raise TypeError('student_id')
        classs = self.get_classs(college_name, academy_name, major_name, grade_id, class_id)
        if classs is None:
            return None
        else:
            return classs.get_student(student_id)

    @property
    def colleges_num(self):
        return self._colleges_num

    @colleges_num.setter
    def colleges_num(self, num):
        if not isinstance(num, int):
            raise TypeError('num')
        self._colleges_num = num

    @property
    def colleges_name(self):
        return self._colleges_name

    @colleges_name.setter
    def colleges_name(self, colleges_name):
        if not isinstance(colleges_name, list):
            raise TypeError('colleges_name')
        self._colleges_name = colleges_name

    @property
    def colleges(self):
        return self._colleges

    @colleges.setter
    def colleges(self, colleges):
        if not isinstance(colleges, dict):
            raise TypeError('colleges')
        self._colleges = colleges
