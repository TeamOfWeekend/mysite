"""定义learning_logs的URL模式"""

from django.urls import path, re_path

from . import views

# 命名空间
app_name = 'learning_logs'


# 注意path于re_path的用法区别
# path 用于不含参数方法的URL映射
# re_path 用于含参数方法的URL映射

urlpatterns = [
	# 显示所有的主题
	path('topics/', views.topics, name='topics'),

	# 显示指定主题的细节
	path('topic/<int:topic_id>/', views.topic, name='topic'),

	# 用于添加新主题的网页
	path('new_topic/', views.new_topic, name='new_topic'),

	# 用于添加新条目的页面
	path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

	# 用于编辑条目的页面
	path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
