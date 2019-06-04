"""定义learning_logs的URL模式"""

from django.urls import path
# from django.views.decorators.csrf import csrf_exempt

from . import views

# 命名空间
app_name = 'colleges'


urlpatterns = [
	# 学校入口页面
	path('collegeEntry/', views.show_college_entry, name='collegeEntry'),
	# 学校信息页面
	path('collegeInfo/', views.show_college, name='collegeInfo'),
	path('academyInfo/', views.show_academy, name='academyInfo'),
	path('majorInfo/', views.show_major, name='majorInfo'),
	path('gradeInfo/', views.show_grade, name='gradeInfo'),
	path('classInfo/', views.show_class, name='classInfo'),
	path('studentInfo/<int:student_id>/', views.show_student, name='studentInfo'),
	path('teacherInfo/<int:teacher_id>/', views.show_teacher, name='teacherInfo'),
]
