from django import forms
from django.forms import widgets
from .models import CollegeInfo, AcademyInfo, MajorInfo, GradeInfo, ClassInfo, StudentInfo


# Form 仅做表单数据验证
# ModelForm 做数据库与表单数据验证

# class CollegeForm(forms.ModelForm):
#     """大学表单"""
#     class Meta:
#         # 表单对应的模型
#         model = CollegeInfo
#         # 引入的模型的属性
#         fields = ['name', 'collegeId', 'address', 'level', 'area', 'academyNum']
#         # 配置上述属性的html属性
#         # widgets = {'text': forms.Textarea(attrs={'cols': 80})}
#         widgets = {
#             'name': forms.TextInput(attrs={'class': "form-control",
#                                            'id': "collegeName",
#                                            'readonly': 'true',
#                                            'style': 'background:#FFFFFF; color:#000000; font-size:11pt',
#                                            'placeholder': '学校名称',
#                                            }),
#
#             'collegeId': forms.TextInput(attrs={'class': "form-control",
#                                                    'id': "collegeId",
#                                                    'readonly': 'true',
#                                                    'style': 'background:#FFFFFF; color:#000000; font-size:11pt',
#                                                    'placeholder': '学校编号',
#                                                    }),
#
#             'address': forms.TextInput(attrs={'class': "form-control",
#                                               'id': "address",
#                                               'readonly': 'true',
#                                               'style': 'background:#FFFFFF; color:#000000; font-size:11pt',
#                                               'placeholder': '学校地址',
#                                               }),
#
#             'level': forms.TextInput(attrs={'class': "form-control",
#                                             'id': "level",
#                                             'readonly': 'true',
#                                             'choice': COLLEGE_LEVELS,
#                                             'style': 'background:#FFFFFF; color:#000000; font-size:11pt',
#                                             'placeholder': '学校等级',
#                                             }),
#
#             'area': forms.TextInput(attrs={'class': "form-control",
#                                               'id': "area",
#                                               'readonly': 'true',
#                                               'style': 'background:#FFFFFF; color:#000000; font-size:11pt',
#                                               'placeholder': '学校面积',
#                                               }),
#
#             'academyNum': forms.TextInput(attrs={'class': "form-control",
#                                                     'id': "academyNum",
#                                                     'readonly': 'true',
#                                                     'style': 'background:#FFFFFF; color:#000000; font-size:11pt',
#                                                     'placeholder': '学院数量',
#                                                     }),
#         }
#
#

    # collegeName = forms.CharField(min_length = 10,
    #                            strip = True,
    #                            error_messages = {
    #                                'required':'该字段不能为空',
    #                                'min_length':'字符串长度不能小于1'
    #                            },
    #                            widget = widgets.Textarea(attrs={
    #                                'class':'form-control',
    #                                'id':'strInput',
    #                                'rows':'6',
    #                                'style':'background:#FFFFFF; color:#000000; font-size:11pt',
    #                                'placeholder':'请输入一个字符串',
    #                            }))
    # strOutput = forms.CharField(min_length = 1,
    #                            strip = True,
    #                            error_messages = None,
    #                            widget = widgets.Textarea(attrs={
    #                                'class':'form-control',
    #                                'id':'strOutput',
    #                                'rows':'6',
    #                                'style':'background:#DCDCDC; color:#000000; font-size:11pt',
    #                                'placeholder':'等待计算结果',
    #                                'readonly':'true'
    #                            }))


class CollegeEntryForm(forms.Form):
    """大学表单"""
    college_name = forms.ChoiceField(label='选择学校',
                                     widget=widgets.Select(attrs={
                                         'class': 'form-control',
                                         'id': 'college_name',
                                         'style': 'background:#FFFFFF; color:#000000; font-size:11pt',
                                         #  'placeholder':'请输入学校名字',
                                         })
                                     )

    def __init__(self, *args, **kwargs):
        # 实时更新，拷贝所有的静态字段，复制给self.fields
        super(CollegeEntryForm, self).__init__(*args, **kwargs)
        # choice_list = []
        # for item in CollegeEnum:
        #     choice_list.append([item.value, item.name])
        # self.fields['collegeName'].widget.choices = choice_list

    def college_choice_list(self, choice_list):
        self.fields['college_name'].widget.choices = choice_list


class CollegeForm(forms.Form):
    """大学表单"""
    academy_name = forms.ChoiceField(label='选择学院',
                                     widget=widgets.Select(attrs={
                                         'class': 'form-control',
                                         'id': 'academy_name',
                                         'style': 'background:#FFFFFF; color:#000000; font-size:11pt',
                                         #  'placeholder':'请输入学校名字',
                                         })
                                     )

    def __init__(self, *args, **kwargs):
        # 实时更新，拷贝所有的静态字段，复制给self.fields
        super(CollegeForm, self).__init__(*args, **kwargs)
        # choice_list = []
        # for item in AcademyEnum:
        #     choice_list.append([item.value, item.name])
        # self.fields['academyName'].widget.choices = choice_list

    def academy_choice_set(self, choice_list):
        self.fields['academy_name'].widget.choices = choice_list


class AcademyForm(forms.Form):
    """学院表单"""
    major_name = forms.ChoiceField(label='选择专业',
                                   widget=widgets.Select(attrs={
                                       'class': 'form-control',
                                       'id': 'major_name',
                                       'style': 'background:#FFFFFF; color:#000000; font-size:11pt',
                                       #  'placeholder':'请输入学校名字',
                                       })
                                   )

    def major_choice_set(self, choice_list):
        self.fields['major_name'].widget.choices = choice_list


class MajorForm(forms.Form):
    """专业表单"""
    grade_id = forms.ChoiceField(label='选择年级',
                                 widget=widgets.Select(attrs={
                                     'class': 'form-control',
                                     'id': 'grade_id',
                                     'style': 'background:#FFFFFF; color:#000000; font-size:11pt',
                                     #  'placeholder':'请输入学校名字',
                                     })
                                 )

    def grade_choice_set(self, choice_list):
        self.fields['grade_id'].widget.choices = choice_list


class GradeForm(forms.Form):
    """年级表单"""
    class_id = forms.ChoiceField(label='选择班级',
                                 widget=widgets.Select(attrs={
                                     'class': 'form-control',
                                     'id': 'class_id',
                                     'style': 'background:#FFFFFF; color:#000000; font-size:11pt',
                                     #  'placeholder':'请输入学校名字',
                                     })
                                 )

    def class_choice_set(self, choice_list):
        self.fields['class_id'].widget.choices = choice_list


class ClassForm(forms.Form):
    """班级表单"""
    student_name = forms.CharField(min_length=1,
                                   strip=True,
                                   error_messages=None,
                                   widget=widgets.TextInput(attrs={
                                       'class': 'form-control',
                                       'id': 'student_name',
                                       'rows': '6',
                                       'style': 'background:#DCDCDC; color:#000000; font-size:11pt',
                                       'placeholder': '-',
                                       'readonly': 'true'
                                   }))
    student_id = forms.CharField(min_length=1,
                                 strip=True,
                                 error_messages=None,
                                 widget=widgets.TextInput(attrs={
                                     'class': 'form-control',
                                     'id': 'student_id',
                                     'rows': '6',
                                     'style': 'background:#DCDCDC; color:#000000; font-size:11pt',
                                     'placeholder': '-',
                                     'readonly': 'true'
                                 }))
    student_sex = forms.CharField(min_length=1,
                                  strip=True,
                                  error_messages=None,
                                  widget=widgets.TextInput(attrs={
                                      'class': 'form-control',
                                      'id': 'student_sex',
                                      'rows': '6',
                                      'style': 'background:#DCDCDC; color:#000000; font-size:11pt',
                                      'placeholder': '-',
                                      'readonly': 'true'
                                  }))
