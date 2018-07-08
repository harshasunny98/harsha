from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
	return HttpResponse('home page!')
	
def login(request):
	return render(request, 'myapps/login.html')