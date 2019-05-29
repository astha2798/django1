from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from customer.models import customer
import hashlib
# Create your views here.
@csrf_exempt
def signup(request):
	if request.method =='POST':
		username=request.POST.get("username","")
		email=request.POST.get("email","")
		password=request.POST.get("password","")
		hash_object = hashlib.sha1(password.encode())
		hex_pass = hash_object.hexdigest()

		print(username,' ',email,' ',password)
		#dob=request.POST.get("dob","")
		user = customer.objects.filter(username = username,email=email)
		if not user:
			user =customer(username=username,email=email,password=hex_pass)
			user.save()
			return JsonResponse({'output':'successfully created'})
		else:
			return JsonResponse({'output':'user exist'})

	else:
		return JsonResponse({'output':'error creating the user'})




@csrf_exempt
def login(request):

	if request.method == 'POST':
		username = request.POST.get("username", "")
		password = request.POST.get("password", "")
		hash_object = hashlib.sha1(password.encode())
		hex_pass = hash_object.hexdigest()

		user = customer.objects.filter(username = username,password=hex_pass)
		print(user)
		if not user:
			return JsonResponse({'output':'wrong username or password'})
			
			
		else:
			request.session['username'] = username
			print(request.session['username'])
			return JsonResponse({'output':'successfully logged in','username':request.session['username']})
			


	else:
		return JsonResponse({'output':'invalid'})


