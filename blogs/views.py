from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic
from .forms import TopicForm, EntryForm, Entry

# Create your views here.

# render()：用数据渲染Html文件
# reverse()：反向解析，从html文件名反向解析到url


# @login_required -- 注释掉该修饰器，否则用户未登录时不能进行跳转
def topics(request):
	"""显示所有的主题"""
	if request.user.is_authenticated:
		# 从数据库中查找某用户的所有主题，并按添加日期降序排列
		topics = Topic.objects.filter(owner=request.user).order_by('date_added')
		context = {'topics': topics}
		return render(request, 'learning_logs/topics.html', context)
	else:
		return render(request, 'users/login.html')


@login_required
def topic(request, topic_id):
	"""显示单个主题及其所有的条目"""
	topic = Topic.objects.get(id=topic_id)
	# 确认请求的主题是否属于当前用户
	if topic.owner != request.user:
		return Http404

	# '-'表示降序排列
	entries = topic.entry_set.order_by('-date_added')
	context = {'topic':topic, 'entries':entries}
	return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
	"""添加新主题"""
	if request.method != 'POST':
		# 未完成提交：创建一个新表单
		form = TopicForm()
	else:
		# POST提交的数据，对数据进行处理
		form = TopicForm(request.POST)
		if form.is_valid():
			new_topic = form.save(commit=False)
			new_topic.owner = request.user
			new_topic.save()
			return HttpResponseRedirect(reverse('learning_logs:topics'))
			
	context = {'form': form}
	return render(request, 'learning_logs/new_topic.html', context)
			
		
@login_required			
def new_entry(request, topic_id):
	"""在特定的主题中添加新的条目"""
	topic = Topic.objects.get(id=topic_id)
	
	if request.method != 'POST':
		# 未提交数据，创建一个新的表单
		form = EntryForm()
	else:
		# POST提交的数据，对数据进行处理
		form = EntryForm(data=request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)
			new_entry.topic = topic
			new_entry.save()
			return HttpResponseRedirect(reverse('learning_logs:topic',
												args=[topic_id]))
	
	context = {'topic': topic, 'form': form}
	return render(request, 'learning_logs/new_entry.html', context)
	

@login_required	
def edit_entry(request, entry_id):
	"""编辑既有条目"""
	entry = Entry.objects.get(id=entry_id)
	topic = entry.topic
	# 判断当前用户是否为该主题的所有者
	if topic.owner != request.user:
		return Http404
		
	if request.method != 'POST':
		# 初次请求，使用当前条目填充表单
		form = EntryForm(instance=entry)
	else:
		# POST提交的数据，对数据进行处理
		form = EntryForm(instance=entry, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('learning_logs:topic',
												args=[topic.id]))
												
	context = {'entry': entry, 'topic': topic, 'form': form}
	return render(request, 'learning_logs/edit_entry.html',context)
