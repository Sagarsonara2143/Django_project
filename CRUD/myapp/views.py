from django.shortcuts import render
from .models import Staff,Task

# Create your views here.

def index(request):
	staff=Staff.objects.all()
	task=Staff.objects.all()
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
	task=Staff.objects.all()
	return render(request,'index.html',{'staff':staff,'msg':msg,'task':task})

