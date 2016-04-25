from django import forms

from .models import SignUp

class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['email',"Full_Name"]


	# def clean_email(self):
	# 	email = self.cleaned_data.get('email')
	# 	email_base , providers  = email.split("@")
	# 	domain ,extension = provider.split('.')
	# 	# if not domain =='USC':
	# 	# 	raise forms.ValidationError("plse use usr email")
	# 	if not extension == "com":
	# 	 	raise forms.ValidationError("please use a valid clg email address")
	# 	return email

	# def clean_full_name(self):
	# 	full_name = self.cleaned_data('full_name')
	# 	return full_name