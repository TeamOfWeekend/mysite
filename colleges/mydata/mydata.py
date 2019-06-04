#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author     :Leo
@Connect    :lipf0627@163.com
@File       :mydata.py
@Site       :
@Time       :2019/5/28 22:28
@Software   :PyCharm
"""
from colleges.models import CollegeInfo, AcademyInfo, MajorInfo, GradeInfo, ClassInfo, StudentInfo
import random, datetime
from pypinyin import pinyin, NORMAL
from .baijiaxing import get_random_name


ACADEMY_MAJORS = {'计算机学院': {'id': 1, 'majors': {'软件工程': {'id': 1},
                                                '计算机科学与技术': {'id': 2},
                                                '计算机软件': {'id': 3}}},
                  '信息工程学院': {'id': 2, 'majors': {'信息工程': {'id': 1},
                                                 '通信工程': {'id': 2},
                                                 '电子信息工程': {'id': 3}}},
                  '电气工程学院': {'id': 3, 'majors': {'电气工程及其自动化': {'id': 1},
                                                 '自动化': {'id': 2},
                                                 '生物医学工程': {'id': 3}}},
                  '医学院': {'id': 4, 'majors': {'基础医学': {'id': 1},
                                              '预防医学': {'id': 2},
                                              '临床医学': {'id': 3},
                                              '麻醉学': {'id': 4},
                                              '医学影像': {'id': 5}}},
                  '土木工程学院': {'id': 5, 'majors': {'土木工程': {'id': 1},
                                                 '水务工程': {'id': 2}}},
                  '机械工程学院': {'id': 6, 'majors': {'机械设计制造及自动化': {'id': 1},
                                                 '材料成型机控制工程': {'id': 2},
                                                 '工业设计': {'id': 3}}},
                  '理学院': {'id': 7, 'majors': {'数学与应用数学': {'id': 1},
                                              '信息与计算科学': {'id': 2},
                                              '数理基础科学': {'id': 3}}},
                  '文学院': {'id': 8, 'majors': {'图书馆学': {'id': 1},
                                              '档案学': {'id': 2},
                                              '汉语言文学': {'id': 3}}},
                  '历史学院': {'id': 9, 'majors': {'历史学': {'id': 1},
                                               '考古学': {'id': 2},
                                               '世界历史': {'id': 3},
                                               '民族学': {'id': 4}}}}

COLLEGES_INFO = {'清华大学': {'name': '清华大学', 'id': 10003, 'description': '', 'birthday': '1911-4-26',
                          'address': '北京市海淀区清华大学', 'level': CollegeInfo.COLLEGE_LEVELS[0][0], 'area': 5000,
                          'headmaster': '邱勇'},
                 '北京大学': {'name': '北京大学', 'id': 10001, 'description': '', 'birthday': '1898-7-3',
                          'address': '北京市海淀区颐和园路5号', 'level': CollegeInfo.COLLEGE_LEVELS[0][0], 'area': 5000,
                          'headmaster': '林建华'},
                 '中国人民大学': {'name': '中国人民大学', 'id': 10002, 'description': '', 'birthday': '1937-10-3',
                            'address': '北京市海淀区中关村大街59号', 'level': CollegeInfo.COLLEGE_LEVELS[0][0], 'area': 5000,
                            'headmaster': '刘伟'},
                 '北京航空航天大学': {'name': '北京航空航天大学', 'id': 10006, 'description': '', 'birthday': '1952-10-25',
                              'address': '北京市海淀区学院路37号', 'level': CollegeInfo.COLLEGE_LEVELS[0][0], 'area': 3000,
                              'headmaster': '徐惠彬'},
                 '郑州大学': {'name': '郑州大学', 'id': 10459, 'description': '', 'birthday': '1954-9-15',
                          'address': '郑州市高新技术开发区科学大道100号', 'level': CollegeInfo.COLLEGE_LEVELS[0][0], 'area': 5700,
                          'headmaster': '刘炯天'},
                 }

# 每个专业每级班级数的最大最小值
CLASS_PER_MAJOR_MIN = 1
CLASS_PER_MAJOR_MAX = 10

# 每个班学生数量的最大最小值
STUDENTS_PER_CLASS_MAX = 50
STUDENTS_PER_CLASS_MIN = 5

# 每个专业教师数量的最大值和最小值
TEACHERS_PET_MAJOR_MAX = 50
TEACHERS_PET_MAJOR_MIN = 20


class MyData:

    @staticmethod
    def create_colleges():
        print('Create colleges ------------')
        for college_name in COLLEGES_INFO.keys():
            college = CollegeInfo()
            college.name = college_name
            college.collegeId = COLLEGES_INFO[college_name]['id']
            college.level = COLLEGES_INFO[college_name]['level']
            college.birthday = COLLEGES_INFO[college_name]['birthday']
            college.academyNum = len(COLLEGES_INFO)
            college.majorNum = 0
            for academy in ACADEMY_MAJORS.values():
                college.majorNum += len(academy['majors'])
            college.teacherNum = 0
            college.studentNum = 0
            college.save()
            for academy_name, majors in ACADEMY_MAJORS.items():
                academy = AcademyInfo()
                academy.name = academy_name
                academy.academyId = ACADEMY_MAJORS[academy_name]['id']
                academy.majorNum = len(ACADEMY_MAJORS[academy_name]['majors'])
                academy.teacherNum = 0
                academy.studentNum = 0
                academy.ownerCollege = college
                academy.save()
                for major_name, major_info in majors['majors'].items():
                    major = MajorInfo()
                    major.name = major_name
                    major.majorId = major_info['id']
                    major.gradeNum = 4
                    major.classNum = 4*major.gradeNum
                    major.teacherNum = 0
                    major.studentNum = 0
                    major.ownerAcademy = academy
                    major.save()
                    for i in range(1, 5):
                        grade = GradeInfo()
                        grade.gradeId = i
                        grade.classNum = 4
                        grade.teacherNum = 0
                        grade.studentNum = 0
                        grade.ownerMajor = major
                        grade.save()
                        for j in range(1, 5):
                            mclass = ClassInfo()
                            mclass.classId = j
                            mclass.studentNum = 0
                            mclass.ownerGrade = grade
                            mclass.save()

    @staticmethod
    def create_random_student():
        student = StudentInfo()
        student.name = get_random_name()
        # 随机大学、学院、专业名字
        college_name = random.sample(COLLEGES_INFO.keys(), 1)[0]
        academy_name = random.sample(ACADEMY_MAJORS.keys(), 1)[0]
        major_name = random.sample(ACADEMY_MAJORS[academy_name]['majors'].keys(), 1)[0]
        # 随机id
        class_id = random.randint(1, 4)
        grade_id = random.randint(1, 4)
        major_id = ACADEMY_MAJORS[academy_name]['majors'][major_name]['id']
        academy_id = ACADEMY_MAJORS[academy_name]['id']
        # college_id = COLLEGES_INFO[college_name]['id']

        try:
            student.ownerClass = ClassInfo.objects.get(classId=class_id)
            student.ownerClass.ownerGrade = GradeInfo.objects.get(gradeId=grade_id)
            student.ownerClass.ownerGrade.ownerMajor = MajorInfo.objects.get(name=major_name)
            student.ownerClass.ownerGrade.ownerMajor.ownerAcademy = AcademyInfo.objects.get(name=academy_name)
            student.ownerClass.ownerGrade.ownerMajor.ownerAcademy.ownerCollege = \
                CollegeInfo.objects.get(name=college_name)
        except Exception as e:
            print(e)
            return
        if student.ownerClass.ownerGrade.ownerMajor.ownerAcademy.ownerCollege.studentNum > 10000:
            return
        # 学号：xxxx-xxx-xxx-xx-xx-xxx，年份-学院号-专业号-年级-班级-班内编号
        student.year_in_college = (datetime.datetime.now().year - grade_id + 1)
        student.studentId = student.year_in_college * 10000000000000 + academy_id * 10000000000 + major_id * 10000000 +\
            grade_id * 100000 + class_id * 1000 + student.ownerClass.studentNum + 1

        print('Create student: %s[%d]-%s-%s-%s-%d年级%d班' % (student.name, student.studentId, college_name,
                                                           academy_name, major_name, grade_id, class_id))

        student.ownerClass.studentNum += 1
        student.ownerClass.ownerGrade.studentNum += 1
        student.ownerClass.ownerGrade.ownerMajor.studentNum += 1
        student.ownerClass.ownerGrade.ownerMajor.ownerAcademy.studentNum += 1
        student.ownerClass.ownerGrade.ownerMajor.ownerAcademy.ownerCollege.studentNum += 1

        student.save()
        student.ownerClass.save()
        student.ownerClass.ownerGrade.save()
        student.ownerClass.ownerGrade.ownerMajor.save()
        student.ownerClass.ownerGrade.ownerMajor.ownerAcademy.save()
        student.ownerClass.ownerGrade.ownerMajor.ownerAcademy.ownerCollege.save()

