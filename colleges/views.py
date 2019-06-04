from django.shortcuts import render
from .models import CollegeInfo, AcademyInfo, MajorInfo, GradeInfo, ClassInfo, StudentInfo
from .forms import CollegeEntryForm, CollegeForm, AcademyForm, MajorForm, GradeForm, ClassForm


# Create your views here.


def show_college_entry(request):
    college_entry_form = CollegeEntryForm()
    # 生成学校信息列表，添加到学校选项中
    choice_list = []
    colleges_info = CollegeInfo.objects.all()
    for college_name in colleges_info['colleges_name']:
        choice_list.append([college_name, college_name])
    college_entry_form.college_choice_list(choice_list)
    return render(request, 'colleges/collegeEntry.html', {'college_entry_form': college_entry_form})


def show_college(request):
    college_form = CollegeForm()
    choice_list = []
    college_name = ''

    if request.method == 'POST':
        college_name = request.POST['college_name']

    college_info = get_college_info(college_name)
    for academy_name in college_info['academies_name']:
        choice_list.append([academy_name, academy_name])
    college_form.academyChoiceSet(choice_list)
    return render(request, 'colleges/collegeInfo.html', {'collegeForm': college_form, 'college': college_info})


def show_academy(request):
    academy_form = AcademyForm()
    choice_list = []
    academy_name = ''

    if request.method == 'POST':
        academy_name = request.POST['academy_name']

    academy_info = get_academy_info(academy_name)
    for major_name in academy_info['majors_name']:
        choice_list.append([major_name, major_name])
    academy_form.majorChoiceSet(choice_list)

    context = {'academyForm': academy_form, 'academy': academy_info}
    return render(request, 'colleges/academyInfo.html', context)


def show_major(request):
    major_form = MajorForm()
    choice_list = []
    major_name = ''

    if request.method == 'POST':
        major_name = request.POST['major_name']

    major_info = get_major_info(major_name)
    for grade_id in range(1, major_info['grades_num'] + 1):
        choice_list.append([grade_id, grade_id])
    major_form.gradeChoiceSet(choice_list)
    context = {'majorForm': major_form, 'major': major_info}
    return render(request, 'colleges/majorInfo.html', context)


def show_grade(request):
    grade_form = GradeForm()
    choice_list = []
    grade_id = 0

    if request.method == 'POST':
        grade_id = int(request.POST['grade_id'])

    grade_info = get_grade_info(grade_id)
    for class_id in range(1, grade_info['classes_num'] + 1):
        choice_list.append([class_id, class_id])
    grade_form.classChoiceSet(choice_list)

    context = {'gradeForm': grade_form, 'grade': grade_info}
    return render(request, 'colleges/gradeInfo.html', context)


def show_class(request):
    class_id = 0
    if request.method == 'POST':
        class_id = int(request.POST['class_id'])
    class_info = get_class_info(class_id)
    context = {'classs': class_info}
    return render(request, 'colleges/classInfo.html', context)


# @login_required
def show_student(request, student_id):
    student = get_student_info(int(student_id))
    context = {'student': student}
    return render(request, 'colleges/studentInfo.html', context)


def show_teacher(request, teacher_id):
    teacher = get_student_info(teacher_id)
    context = {'teacher': teacher}
    return render(request, 'colleges/classInfo.html', context)
