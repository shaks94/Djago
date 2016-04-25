from django.db import models

# Create your models here.
class SignUp(models.Model):
	email  = models.EmailField(unique=True)
	Full_Name=models.CharField(max_length=120,blank = False, null=True)#can also use default = somethign 
	timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
	updated = models.DateTimeField(auto_now_add=False,auto_now=True)

	
	def __str__(me):
		
			return me.email
			return me.Full_Name
	