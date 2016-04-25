from django.shortcuts import render
from .forms import SignUpForm
from .models import SignUp

def home1(request):
	title = "my title"

	# if request.user.is_authenticated():
	# 	title = "my Tittle %s" %(request.user)
	# if request.method=="POST":	
	
	# 	print (request.POST)
	# 	print("\n\n")

	form = SignUpForm(request.POST or None)
	
	if form.is_valid():
		instance=form.save(commit=False)
		Full_Name=form.data['Full_Name']
		email=form.cleaned_data['email']
		new_SignUp , created=SignUp.objects.get_or_create(email=email,Full_Name=Full_Name)
		
		if created:
			print "hell ya bitch LOL"
			new_SignUp.save()
		
	context = {
	"template_title":title,
	"form":form

	}
	return render(request,"home1.html",context,)