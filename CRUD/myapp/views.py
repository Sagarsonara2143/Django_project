from django.shortcuts import render,redirect
from .models import Staff,Task

# Create your views here.

def index(request):
	staff=Staff.objects.all()
	task=Task.objects.all().order_by('-id')
	return render(request,'index.html',{'staff':staff,'task':task})

def add_task(request):
	pk=int(request.POST['staff'])

	staff = Staff.objects.get(pk=pk)
	Task.objects.create(
		staff=staff,
		remarks=request.POST['remarks'],
		date=request.POST['date'],
		status=request.POST['status']
		)
	msg="Task Completed Successfully..!"
	staff=Staff.objects.all()
	task=Task.objects.all().order_by('-id')
	return render(request,'index.html',{'staff':staff,'msg':msg,'task':task})

def complete_task(request):
	id=int(request.POST['id'])
	task=Task.objects.get(pk=id)
	task.status="completed"
	task.save()
	return redirect('index')

def all(request):
	return redirect('index')

def completed(request):
	task=Task.objects.filter(status='completed').order_by('-id')[:3]
	staff = Staff.objects.all()
	return render(request,'index.html',{'staff':staff,'task':task})

def pending(request):
	task=Task.objects.filter(status='pending')[:3]
	staff=Staff.objects.all()
	return render(request,'index.html',{'staff':staff,'task':task})