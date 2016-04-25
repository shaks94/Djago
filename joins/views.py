from django.shortcuts import render,HttpResponseRedirect, Http404
from .forms import JoinForm
from .models import Join
# form django.conf import settings


def get_ip(request):
	try:
		x_forward=request.META.get("HTTP_x_FORWAREDE_FOR");
		if x_forward :
			ip=x_forward.split(",")[0]
		else:
			ip=request.META.get("REMOTE_ADDR")
	except:
		ip=""
	
 	return ip

import uuid
def get_ref_id():
	ref_id=str(uuid.uuid4())[:11].replace('-','').lower()
	try:
		id_exists=Join.objects.get(ref_id=ref_id)
		get_ref_id()
	# except Join.DoesNotExist:
	# 	raise Http404
	except :
		return ref_id
def  share(request,ref_id):
	try:
		join_obj = Join.objects.get(ref_id=ref_id)#tels the initial value enter to join
		# print "intitially entered "+str(join_obj) 
		friends_referred = Join.objects.filter(friend=join_obj)#it's filterign friends with that particular ref id 
		#or say which is child of this parent id entered to join
		# print "child of this parent id entered to join ==="+str(friends_referred)
		count = join_obj.referral.all().count() 
		ref_url = "http://127.0.0.1:8000/?ref=%s" %(join_obj.ref_id)
	#	ref_url = settings.SHARE_URL + str(join_obj.ref_id) 
		context={"ref_id":ref_id,"count":count,"ref_url":ref_url}
		template="share.html"
		return render(request,template,context)
	except:
		raise Http404
def home(request):
	try:
		join_id=request.session['join_id_ref']#shows master id 
		obj=Join.objects.get(id=join_id)
		# print "formed as sub child of parent id ==="+str(obj)#formed from sub child of parent id
		# print "major source === "+str(join_id) #major source 

	except:
		obj=None
	

	form = JoinForm(request.POST or None)

	if form.is_valid(): 
		new_join=form.save(commit=False)
		email=form.cleaned_data['email']
		new_join_old , created=Join.objects.get_or_create(email=email)
	
		if created:
			new_join_old.ref_id=get_ref_id()

			new_join_old.ip_address=get_ip(request)
			if not obj ==None:
				new_join_old.friend = obj
			new_join_old.save()

		# print "ultimate child=== %s" %(Join.objects.filter(friend=obj).count())#if one to one v could have use get
		#ultimate child
		# print "this is ==="+ str(obj.referral.all())#referal is the related name of friend
		return HttpResponseRedirect("/%s" %(new_join_old.ref_id))
		# new_join.ip_address=get_ip(request)
		# new_join=form.save()
	
	context = {"form":form}
	template = "home.html"
	return render(request ,template, context)























	# if form.is_valid():
 # 		new_join = form.save(commit = False )
 # 		email= form.cleaned_data['email']
 		#email= new_join.email
 		# new_join,created = Join.objects.get_or_create(email=email)
 		# print new_join,created
 		# if created :
 		# 	print "this obj was created"
# -------------------------------------------------
	# print request.META.get("REMOTE_ADDR");
	# print request.META.get("HTTP_x_FORWAREDE_FOR") its  also a way to get ip address
# ---------------------------------------------------
    # form  = EmailForm(request.POST )
  	# if form.is_valid():
	# 	email = form.cleaned_data['email']
	# 	new_join, created = Join.objects.get_or_create(email=email)
	# 	print new_join,created
	# 	print new_join.timestamp
	#this is using mode form not regular form