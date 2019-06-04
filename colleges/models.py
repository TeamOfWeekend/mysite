from django.db import models

# Create your models here.


class CollegeInfo(models.Model):
    """大学信息模型"""
    COLLEGE_LEVELS = (
        (1, '双一流'),
        (2, '一本'),
        (3, '二本'),
        (4, '三本'),
        (5, '专科'),
    )

    name = models.CharField(max_length=20, verbose_name='学校名称')
    # 学校编号，不能为空，在表中具有唯一值
    collegeId = models.IntegerField(null=False, unique=True, verbose_name='学校编号')
    description = models.CharField(max_length=200, verbose_name='学校简介')
    address = models.TextField(blank=True, max_length=200, verbose_name='地址')
    level = models.IntegerField(choices=COLLEGE_LEVELS, verbose_name='学校级别', null=True)
    area = models.PositiveIntegerField(null=True, verbose_name='面积')
    birthday = models.DateField(auto_now=False, auto_created=False, auto_now_add=False, verbose_name='建校时间')
    headmaster = models.CharField(max_length=20, verbose_name='校长')
    academyNum = models.PositiveIntegerField(verbose_name='学院数量')
    majorNum = models.PositiveIntegerField(verbose_name='专业数量')
    teacherNum = models.PositiveIntegerField(verbose_name='教职工数量')
    studentNum = models.PositiveIntegerField(verbose_name='学生数量')

    class Meta:
        # 本类不是抽象基类
        abstract = False
        # 所属应用，在setting中未添加应用时使用
        # app_label = 'imagination'
        # 映射的数据表名
        db_table = 'colleges'
        # 定义按哪个字段值排列，以获得模型的开始或结束记录
        get_latest_by = 'collegeId'
        # manage.py命令行工具是否管理本模型
        managed = True
        # 按照某外键引用的关系排序
        # order_with_respect_to = ''
        # 默认排序字段，可设置多个，默认降序，如果升序需在前面加“-”号
        ordering = ['-collegeId']
        # 模型操作权限，默认为add、change、delete
        default_permissions = ('add', 'change', 'delete')
        # 本模型及所有继承自本模型的子模型是否为代理模型
        # proxy = True
        # 定义底层数据库所必须具备的特性，如下：只将本模型声称在满足gis_enabled特性的数据库中
        # required_db_features = ['gis_enabled']
        # 定义底层数据库的类型，比如SQLite、MySQL、Oracle。若定义本属性，模型智能在其声明的数据库中被维护
        # required_db_vendor = 'MySQL'
        # 设置不重复的字段组合，必须唯一，可以多个组合
        # unique_together = (('name', 'collegeId'),)
        # 定义联合索引的字段，可以设置多个
        index_together = [['name', 'collegeId'], ]
        # 指明一个易于理解和表述的单数形式的对象名称
        verbose_name = 'collegeInfo'
        # 指明一个易于理解和表述的附属形式的对象名称，若不指定，在类名后加s
        verbose_name_plural = 'collegeInfos'

    def __str__(self):
        return self.name


class AcademyInfo(models.Model):
    """大学学院模型"""
    name = models.CharField(max_length=20, verbose_name='学院名称')
    ownerCollege = models.ForeignKey(CollegeInfo, on_delete=models.CASCADE, verbose_name='所属学校')
    # 学院编号，不能为空，在表中具有唯一值
    academyId = models.IntegerField(null=False, unique=True, verbose_name='学院编号')
    majorNum = models.PositiveIntegerField(verbose_name='专业数量')
    teacherNum = models.PositiveIntegerField(verbose_name='教职工数量')
    studentNum = models.PositiveIntegerField(verbose_name='学生数量')

    class Meta:
        # 按照某外键引用的关系排序
        # order_with_respect_to = ''
        # 默认排序字段，可设置多个，默认降序，如果升序需在前面加“-”号
        ordering = ['-academyId']
        # 定义联合索引的字段，可以设置多个
        index_together = [['name', 'academyId'], ]
        # 指明一个易于理解和表述的单数形式的对象名称
        verbose_name = 'academyInfo'
        # 指明一个易于理解和表述的附属形式的对象名称，若不指定，在类名后加s
        verbose_name_plural = 'academyInfos'
        # 映射的数据表名
        db_table = 'colleges_academies'

    def __str__(self):
        return self.name


class MajorInfo(models.Model):
    """大学专业模型"""
    name = models.CharField(max_length=20, verbose_name='专业名称')
    ownerAcademy = models.ForeignKey(AcademyInfo, on_delete=models.CASCADE, verbose_name='所属学院')
    # 专业编号，不能为空，在表中具有唯一值
    majorId = models.IntegerField(null=False, unique=True, verbose_name='专业编号')
    gradeNum = models.PositiveIntegerField(verbose_name='年级数量')
    classNum = models.PositiveIntegerField(verbose_name='班级数量')
    teacherNum = models.PositiveIntegerField(verbose_name='教职工数量')
    studentNum = models.PositiveIntegerField(verbose_name='学生数量')

    class Meta:
        # 按照某外键引用的关系排序
        # order_with_respect_to = ''
        # 默认排序字段，可设置多个，默认降序，如果升序需在前面加“-”号
        ordering = ['-majorId']
        # 定义联合索引的字段，可以设置多个
        index_together = [['name', 'majorId'], ]
        # 指明一个易于理解和表述的单数形式的对象名称
        verbose_name = 'majorInfo'
        # 指明一个易于理解和表述的附属形式的对象名称，若不指定，在类名后加s
        verbose_name_plural = 'majorInfos'
        # 映射的数据表名
        db_table = 'colleges_majors'

    def __str__(self):
        return self.name


class GradeInfo(models.Model):
    """大学年级模型"""
    # 年级编号，不能为空，在表中具有唯一值
    gradeId = models.IntegerField(null=False, unique=True, verbose_name='年级编号')
    ownerMajor = models.ForeignKey(MajorInfo, on_delete=models.CASCADE, verbose_name='所属专业')
    classNum = models.PositiveIntegerField(verbose_name='班级数量')
    teacherNum = models.PositiveIntegerField(verbose_name='教职工数量')
    studentNum = models.PositiveIntegerField(verbose_name='学生数量')

    class Meta:
        # 按照某外键引用的关系排序
        # order_with_respect_to = ''
        # 默认排序字段，可设置多个，默认降序，如果升序需在前面加“-”号
        ordering = ['-gradeId']
        # 指明一个易于理解和表述的单数形式的对象名称
        verbose_name = 'gradeInfo'
        # 指明一个易于理解和表述的附属形式的对象名称，若不指定，在类名后加s
        verbose_name_plural = 'gradeInfos'
        # 映射的数据表名
        db_table = 'colleges_grades'

    def __str__(self):
        return self.gradeId


class ClassInfo(models.Model):
    """大学班级模型"""
    classId = models.IntegerField(null=False, unique=True, verbose_name='班级编号')
    ownerGrade = models.ForeignKey(GradeInfo, on_delete=models.CASCADE, verbose_name='所属年级')
    studentNum = models.PositiveIntegerField(verbose_name='学生数量')

    class Meta:
        # 按照某外键引用的关系排序
        # order_with_respect_to = ''
        # 默认排序字段，可设置多个，默认降序，如果升序需在前面加“-”号
        ordering = ['-classId']
        # 指明一个易于理解和表述的单数形式的对象名称
        verbose_name = 'classInfo'
        # 指明一个易于理解和表述的附属形式的对象名称，若不指定，在类名后加s
        verbose_name_plural = 'classInfos'
        # 映射的数据表名
        db_table = 'colleges_classes'

    def __str__(self):
        return self.classId


class StudentInfo(models.Model):
    """大学生模型"""
    # 学号，不能为空，在表中具有唯一值
    studentId = models.IntegerField(null=False, unique=True, verbose_name='学号')
    ownerClass = models.ForeignKey(ClassInfo, on_delete=models.CASCADE, verbose_name='所属班级')
    name = models.CharField(max_length=20, verbose_name='姓名')
    namePinYin = models.CharField(max_length=20, verbose_name='姓名拼音')
    idCardNum = models.CharField(max_length=20, verbose_name='身份证号')
    age = models.IntegerField(verbose_name='年龄')
    year_in_college = models.DateTimeField(verbose_name='入学年份')
    height = models.IntegerField(verbose_name='身高')
    weight = models.IntegerField(verbose_name='体重')
    bust = models.IntegerField(verbose_name='腰围')
    waist = models.IntegerField(verbose_name='腰围')
    hips = models.IntegerField(verbose_name='臀围')
    hobbies = models.CharField(max_length=200, verbose_name='爱好')
    married = models.BooleanField(verbose_name='婚姻状态')

    class Meta:
        # 按照某外键引用的关系排序
        # order_with_respect_to = ''
        # 默认排序字段，可设置多个，默认降序，如果升序需在前面加“-”号
        ordering = ['-studentId']
        # 定义联合索引的字段，可以设置多个
        index_together = [['name', 'studentId'], ]
        # 指明一个易于理解和表述的单数形式的对象名称
        verbose_name = 'studentInfo'
        # 指明一个易于理解和表述的附属形式的对象名称，若不指定，在类名后加s
        verbose_name_plural = 'studentInfos'
        # 映射的数据表名
        db_table = 'colleges_students'

    def __str__(self):
        return self.name
