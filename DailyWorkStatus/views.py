from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
# acessing Usreg present in DailyWorkStatus.forms
from DailyWorkStatus.forms import Usregis,Upd,Pad,WrkForm


from DailyWorkStatus.models import Contact_Model

from DailyWorkStatus.models import Exfd,Worklog
from django.contrib.auth.models import User
# Create your views here.

# for sending mail
from WorkLog import settings
from django.core.mail import send_mail

# to restrict aecess to url
from django.contrib.auth.decorators import login_required


from django.contrib import messages


def home(request):
	return render(request,'html/home.html')


def about(request):
	return render(request,'html/about.html')


def contact(request):


	if request.method=="POST":
		name=request.POST['name']
		email=request.POST['email']
		subject=request.POST['subject']
		query=request.POST['query']
		obj=Contact_Model(name=name,email=email,subject=subject,query=query)
		obj.save()
		

		# to display user added succesfully
		# return HttpResponse("<h1>User Registration of {} done successfully</h1>".format(obj.name))
		messages.success(request,"Query sent successfully")
		# return redirect('/pf')

	return render(request,'html/contact_us.html')

def register(request):
	if request.method=="POST":
		y=Usregis(request.POST)
		if y.is_valid():
			p=y.save(commit=False)
			rc = p.email
			sb = "Testing Email to register for Worklog Project"
			mg = "Hi Welcome {} you have successfully registered in our portal with password: {}".format(p.username,p.password)
			sd = settings.EMAIL_HOST_USER
			snt = send_mail(sb,mg,sd,[rc])
			if snt == 1:
				p.save()
				messages.success(request,"please check ur mail {} for login credentials".format(rc))
				return redirect('/lg')
			return messages.danger(request,"please enter correct username")
	y=Usregis()
	return render(request,'html/register.html',{'t':y})


@login_required
def dashboard(request):
	# id=request.user.id
	# p=Worklog.objects.filter(Worklog.m_id=id)
	p=Worklog.objects.filter(m_id=request.user.id)
	total=len(p)
	# q=Worklog.objects.filter(Worklog.m_id==id and Worklog.workstatus=="No")
	q=Worklog.objects.filter(m_id=request.user.id,workstatus="Yes")
	complete=len(q)
	pending=total-complete
	print(total,complete,pending)
	dict={}
	dict['complete']=complete
	dict['pending']=pending
	return render(request,'html/dashboard.html',{'values':dict})


@login_required
def prfle(request):
	return render(request,'html/profile.html')

@login_required
def updf(request):
	
	if request.method=="POST":
		p=Upd(request.POST,instance=request.user)
		t=Pad(request.POST,request.FILES,instance=request.user.exfd)
		if p.is_valid() and t.is_valid():
			p.save()
			t.save()
			messages.success(request,"{} your profile updated successfully".format(request.user.username))
			return redirect('/pf')
	p=Upd(instance=request.user)
	t=Pad(instance=request.user.exfd)
	return render(request,"html/updateprofile.html",{'r':p,'q':t})





@login_required
def wrklg(request):
	p=Worklog.objects.filter(m_id=request.user.id)
	# print(len(p))

	return render(request,'html/worklog.html',{'y':p})






def creationwk(request):

	if request.method=='POST':
		m=Worklog.objects.filter(m_id=request.user.id,date=request.POST['date'])
		if len(m)==0:
			r=WrkForm(request.POST)
			if r.is_valid():
				t=r.save(commit=False)
				t.m_id=request.user.id
				t.save()
				messages.success(request,"succesfully uploaded")
				return redirect('/wrk')
		messages.info(request,"sorry you have already submitted worklog for today")
		return redirect('/wrk')

		
	r=WrkForm()
	return render(request,'html/crwrk.html',{'d':r})








