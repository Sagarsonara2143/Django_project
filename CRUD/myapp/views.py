from django.shortcuts import render
from .models import Staff,Task

# Create your views here.

def index(request):
	staff=Staff.objects.all()
	return render(request,'index.html',{'staff':staff})

def add_task():
	pk=int(request.POST['staff'])

	staff = Staff.objects.get(pk=pk)
	Task.objects.create(
		staff=staff,
		remark = request.POST['remark'],
		data=request.POST['date']
		)

	msg="Task Completed Successfully..!"
	staff=staff.objects.all()
	return render(request,'index.html',{'staff':staff,'msg':msg})