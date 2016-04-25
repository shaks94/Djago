from django import forms
from .models import Join
class EmailForm(forms.Form):
	name   = forms.CharField(required = False)
	#age =    forms.FloatField()
	email  = forms.EmailField() 
	


class JoinForm(forms.ModelForm):
	
	class Meta:
		model = Join
		fields = ['email']
		


	# def clean_email(self):
	# 	email = self.cleaned_data.get('email')
	# 	email_base , provider  = email.split("@")
	# 	domain ,extension = provider.split('.')
	# 	# if not domain =='USC':
	# 	# 	raise forms.ValidationError("plse use usr email")
	# 	if not extension == "com":
	# 	 	raise forms.ValidationError("please use a valid clg email address")
	# 	return email	

