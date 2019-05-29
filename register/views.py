from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate

# Create your views here
@csrf_exempt
def signup(request):
	if request.method =='POST':
		username=request.POST.get("username","")
		email=request.POST.get("email","")
		password=request.POST.get("password","")
		print(username,' ',email,' ',password)
		#dob=request.POST.get("dob","")
		user = User.objects.create_user(username, email,password)
		user.save()
		return JsonResponse({'output':'successfully created'})
	else:
		return JsonResponse({'output':'error creating the user'})

@csrf_exempt
def login(request):

	if request.method == 'POST':
		username = request.POST.get("username", "")
		password = request.POST.get("password", "")

		user = authenticate(username = username , password = password)

		if user == None:
			return JsonResponse({'output':'wrong username or password'})
			
		else:
			request.session['username'] = username
			print(request.session['username'])
			return JsonResponse({'output':'successfully logged in','username':request.session['username']})


	else:
		return JsonResponse({'output':'invalid'})

@csrf_exempt
def formView(request):
	if request.method == 'POST':

	    #if request.session.has_key('username'):
	    if(request.session['username']== None):
	    	return JsonResponse({"username":null})
	    else:
	    	username=request.session['username']
	    	return JsonResponse({"username":username})
	else:
		return JsonResponse({"requesttype":post})

@csrf_exempt
def logout(request):
    del request.session['username']
    return HttpResponse("<strong>You are logged out.</strong>")


      