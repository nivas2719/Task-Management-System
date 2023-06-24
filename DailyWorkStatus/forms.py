# accessing existing table from admin
from django.contrib.auth.models import User

from django import forms

# it is used to create forms same as user registration in admin site
from django.contrib.auth.forms import UserCreationForm


from DailyWorkStatus.models import Exfd,Worklog

class Usregis(UserCreationForm):
	password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":'form-control m-2',"placeholder":"enter ur password","required":True,}))
	password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":'form-control m-2',"placeholder":"confirm ur password","required":True,}))
	class Meta:
		model=User
		fields=["first_name","last_name","email","username"]
		widgets={
		"first_name":forms.TextInput(attrs={
			"class":"form-control m-2",
			"placeholder":"enter your firstname",
			"required":True,
			}),
		"last_name":forms.TextInput(attrs={
			"class":"form-control m-2",
			"placeholder":"enter your lastname",
			"required":True,
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control m-2",
			"placeholder":"enter your email id",
			"required":True,
			}),
		"username":forms.TextInput(attrs={
			"class":"form-control m-2",
			"placeholder":"enter your username",
			"required":True,
			}),
		}




class Upd(forms.ModelForm):
	class Meta:
		model=User
		fields=['first_name','last_name','username','email']
		widgets={
		'username':forms.TextInput(attrs={
			'class':'form-control',
			}),
		'first_name':forms.TextInput(attrs={
			"class":"form-control",
			}),
		'last_name':forms.TextInput(attrs={
			"class":"form-control",
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control",
			}),
		}

class Pad(forms.ModelForm):
	class Meta:
		model=Exfd
		fields=["age","gender","impf",]# u can iclude clg name, roolno if included
		widgets={
		"age":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"update ur age",
			}),
		"gender":forms.Select(attrs={
			"class":"form-control",
			"title":"Select your gender",
			}),
		"rollno":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"update ur rollno",
			}),
		"collegename":forms.Select(attrs={
			"class":"form-control",
			"title":"Select your college",

			}),
		}




class WrkForm(forms.ModelForm):
	class Meta:
		model=Worklog
		fields=["date","description","workstatus"]
		widgets={
		'date':forms.DateInput(attrs={
			"class":"form-control",
			"type":"date",
			}),
		"description":forms.Textarea(attrs={
			"class":"form-control",
			"rows":5,
			"cols":10,
			"placeholder":"Enter your task:"
			}),
		"workstatus":forms.Select(attrs={
			"class":"form-control",
			}),
		}



# 9849708630