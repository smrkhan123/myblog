from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User,auth
from .models import post,like,comment
# Create your views here.
def index(request):
	Post=post.objects.all()
	return render(request,'index.html',{'blogs':Post})

def register(request):
	if request.method=="POST":
		fname=request.POST['firstname']
		lname=request.POST['lastname']
		uname=request.POST['username']
		email=request.POST['email']
		password=request.POST['password']
		cpassword=request.POST['confirmpassword']

		if password==cpassword:
			if User.objects.filter(username=uname).exists():
				messages.error(request,'Username Taken')
				return redirect('register')
			elif User.objects.filter(email=email).exists():
				messages.error(request,'Email Already Exists')
				return redirect('register')
			else:
				user = User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,password=password)
				user.save();
				messages.success(request,'Account Created Succesfully')
				return redirect('login')
		else:
			messages.error(request,'Password and Confirm Password did not matched!')
			return redirect('register')
	return render(request,'register.html')

def login(request):
	if request.method=="POST":
		uname=request.POST['username']
		password=request.POST['password']
		user =  auth.authenticate(username=uname,password=password)
		if user is not None:
			auth.login(request,user)
			return redirect('index')
		else:
			messages.error(request,'Username Or Password Is Incorrect')
			return redirect('login')
	return render(request,'login.html')


def logout(request):
	auth.logout(request)
	return redirect('index')

def myblog(request):
	if User.is_authenticated():
		print(User['username'])
	Posts=post.objects.all()
	return render(request,'myblog.html',{'posts':Posts,})

def myaccount(request):
	if request.session._session:
		return render(request,'myaccount.html')
	else:
		return render(request,'login.html')

def addpost(request):
	if request.session._session:
		if request.method=="POST":
			mypost=post()
			mypost.title=request.POST['title']
			mypost.body=request.POST['body']
			mypost.image=request.FILES['img']
			mypost.category=request.POST['category']
			mypost.user=request.POST['user']
			mypost.save();
			return redirect('myblog')
		return render(request,'addpost.html')
	else:
		return render(request,'login.html')


def delete(request,id):
	Posts=post.objects.get(pk=id)
	Posts.delete()
	return redirect('myblog')



def edit(request,id):
	Posts=post.objects.get(pk=id)
	if request.method=="POST":
		Posts.title=request.POST['title']
		Posts.body=request.POST['body']
		Posts.image=request.FILES['img']
		Posts.category=request.POST['category']
		Posts.save()
		return redirect('myblog')
	return render(request,'edit.html',{'posts':Posts})

def viewblog(request,id):
	Post=post.objects.get(pk=id)
	likes=like.objects.all()
	comm=comment.objects.all()
	listt=[]
	for i in comm:
		di={}
		if i.title==Post.title:
			di.update({'id':i.id,'user':i.user,'comments':i.comments})
			lis=list(di.values())
			#print(lis)
			listt.append(lis)
	#print(listt)
	for i in listt:
		print(i[0],i[1],i[2])
	
	a=0
	for i in likes:
		if i.title==Post.title:
			a=a+1	
	return render(request,'viewblog.html',{'post':Post,'c':a,'comm':listt})

def likes(request,id):
	if request.session._session:
		Post=post.objects.get(pk=id)
		likes=like.objects.all()
		a=f'/viewblog/{id}'
		Like=like()
		Like.title=Post.title
		Like.user=Post.user
		#print(Like.user)
		for i in likes:
			
			if i.user==Like.user:
				pass
			else:
				Like.save()
		return redirect(a) 
	else:
		return render(request,'login.html')

def comments(request,id):
	if request.session._session:
		Post=post.objects.get(pk=id)
		#comments=comment.objects.all()
		comm=comment()
		if request.method=="POST":
			comm.title=Post.title
			comm.comments=request.POST['comment']
			comm.user=request.POST['user']
			comm.save()
		return redirect(f'/viewblog/{id}')
	else:
		return render(request,'login.html')



def entertainment(request):
	Post=post.objects.all()
	list=[]
	for i in Post:
		l={}
		if i.category=='entertainment':
			l.update({'id':i.id,'title':i.title,'image':i.image,'category':i.category,'user':i.user,'date':i.date})
			list.append(l)
	return render(request,'entertainment.html',{'ent':list})




def sports(request):
	Post=post.objects.all()
	list=[]
	for i in Post:
		l={}
		if i.category=='sports':
			l.update({'id':i.id,'title':i.title,'image':i.image,'category':i.category,'user':i.user,'date':i.date})
			list.append(l)
	return render(request,'sports.html',{'ent':list})


def travel(request):
	Post=post.objects.all()
	list=[]
	for i in Post:
		l={}
		if i.category=='travel':
			l.update({'id':i.id,'title':i.title,'image':i.image,'category':i.category,'user':i.user,'date':i.date})
			list.append(l)
	return render(request,'travel.html',{'ent':list})


def personal_life(request):
	Post=post.objects.all()
	list=[]
	for i in Post:
		l={}
		if i.category=='personal_life':
			l.update({'id':i.id,'title':i.title,'image':i.image,'category':i.category,'user':i.user,'date':i.date})
			list.append(l)
	return render(request,'personal_life.html',{'ent':list})


def health(request):
	Post=post.objects.all()
	list=[]
	for i in Post:
		l={}
		if i.category=='health':
			l.update({'id':i.id,'title':i.title,'image':i.image,'category':i.category,'user':i.user,'date':i.date})
			list.append(l)
	return render(request,'health.html',{'ent':list})




