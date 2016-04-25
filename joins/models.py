from django.db import models

# Create your models here.

class Join(models.Model):
	email = models.EmailField()#unique=True
	friend = models.ForeignKey("self",related_name="referral",null=True,blank=True)
	ref_id= models.CharField(max_length=20,default='ABC',unique=True)
	ip_address=models.CharField(max_length=128,default='ABC')
	timestamp = models.DateTimeField(auto_now_add = True , auto_now=False)
	updated = models.DateTimeField(auto_now_add = False , auto_now=True)

	def __unicode__(self):

		return self.email
	class Meta:
		unique_together=("email","ref_id",)

# class JoinFriends(models.Model):
# 	email=models.OneToOneField(Join,related_name="Sharer")

# 	friends = models.ManyToManyField(Join,related_name="Friend", \
# 											null=True,blank=True)
# 	emailall=models.ForeignKey(Join,related_name='emailall')

# 	def __unicode__(self):
# 		print self.emailall
# 		print self.emailall
# 		print "Friend are " , self.friends.all()
		# return self.email.email








		# email=models.ForeignKey(Join)

