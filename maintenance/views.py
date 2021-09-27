from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import auth,User
from .models import issues
from .models import council_member
from .models import contactus
# Create your views here.
def home(request):
	return render(request,'home.html')   
def user_login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password'] 
		user = auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			ids =  issues.objects.filter(issue_by=username)
			return render(request,'user_spec.html',{'username': username,
                                           'ids': ids})
		else:
			messages.info(request,'Invalid Credentials')
			return redirect('user_login')
	else:
		return render(request, 'user_login.html')
def submit_issue(request):
	title = request.POST['title']
	department = request.POST['department']
	discription = request.POST['discription']
	status = 'submitted'
	name = request.POST['user']
	new_issue = issues(  issue_depart = department,
	issue_title  = title,
	issue_disc   = discription,
	issue_status = status,
	issue_by = name)
	new_issue.save()
	ids =  issues.objects.filter(issue_by=name)
	return render(request,'user_spec.html',{'username': name,
                                           'ids': ids})
    		
def user_signup(request):
	if request.method == 'POST':
		email = request.POST['email']
		username = request.POST['username']
		password1 = request.POST['password1']
		password2 = request.POST['password2']
		if password1 == password2:
			if User.objects.filter(email=email):
				messages.info(request,'email already exist')
				return redirect('user_signup')
			elif User.objects.filter(username=username):
				messages.info(request,'username already taken')
				return redirect('user_signup')
			else:
				user = User.objects.create_superuser(username=username,email=email,password=password1)
				user.save()
				return render(request,'user_spec.html',{'username': username})
		else:
			messages.info(request,'password did not match')
			return redirect('user_signup')
	else:
		return render(request, 'user_signup.html')
def check(request):
    ids = request.POST['issues']
    data = issues.objects.get(id=ids)
    return render(request,'user_spec1.html',{'data': data})
def maintenance(request):
	if request.method == "POST":
		m_id = request.POST['username']
		password = request.POST['password']
		if council_member.objects.get(muser_id=m_id):
			data = council_member.objects.get(muser_id=m_id)
			if password == data.password:
				data1 = issues.objects.filter(issue_depart=data.department)
				return render(request,'maintenance_spec.html',{'data': data,'data1': data1})
			else:
				messages.info(request,'password incorrect')
		else:
			messages.info(request,"council member id doesn't exist")       
	else:
		return render(request,'maintenance_login.html')
def maintenance1(request):
	if request.method == "POST":
		m_user = request.POST['m_user']
		status = request.POST['status']
		dep = council_member.objects.get(muser_id=m_user)
		depart = dep.department
		print(depart)
		data = issues.objects.filter(issue_status=status,issue_depart=depart)
		print(data)
		return render(request,'maintenance_spec1.html',{'data': data})
def maintenance2(request):
		if request.method == "POST":
			ids = request.POST['id']
			details = issues.objects.get(id=ids)
			return render(request,'maintenance_spec2.html',{'details': details})
def maintenance3(request):
			if request.method == "POST":
				ids = request.POST['id']
				status = request.POST['status']
				remark = request.POST['remark']
				pre_data = issues.objects.get(id=ids)
				data = issues.objects.filter(issue_depart=pre_data.issue_depart,issue_status=pre_data.issue_status)
				pre_data.issue_status = status
				pre_data.issue_remark = remark
				pre_data.save()
				
				return render(request,'maintenance_spec1.html',{'data': data})
    
def contactus_form(request):
	name = request.POST['name']
	email = request.POST['email']
	message = request.POST['message']
	data = contactus(name=name,email=email,message=message)
	data.save()
	return render(request,'home.html')
def user_home(request):
	return render(request,'home.html')