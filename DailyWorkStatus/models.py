from django.db import models
from django.contrib.auth.models import User
# for signals concept
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.



class Exfd(models.Model):
	g=[('M','male'),('FM','Female')]
	clg=[('AANM','AANM VVRSR POLYTECHNIC - GVL'),('SVGP','SV GOVT POLYTECHNIC'),('AANMR','AANM VVRSR POLYTECHNIC - RJYD')]
	d=models.OneToOneField(User,on_delete=models.CASCADE)
	age=models.IntegerField(null=True)
	gender=models.CharField(max_length=10,choices=g)
	rollno=models.CharField(max_length=15)
	collegename=models.CharField(max_length=7,choices=clg)
	impf=models.ImageField(upload_to="profile/",default="profile.png")

@receiver(post_save,sender=User)
def crpf(sender,instance,created,**kwargs):
	if created:
		Exfd.objects.create(d=instance)



class Worklog(models.Model):
	wks=[('Yes','Completed'),('No',"Not Completed")]
	date=models.DateField()
	description=models.TextField()
	workstatus=models.CharField(max_length=5,choices=wks)
	m=models.ForeignKey(User,on_delete=models.CASCADE)




class Contact_Model(models.Model):


	name=models.CharField(max_length=25)
	email=models.EmailField()
	subject=models.CharField(max_length=25)
	query=models.TextField()

	def __str__(self):
		return (self.name+' '+self.email)

	class Meta:
		db_table="contact_Info"