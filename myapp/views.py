from django.shortcuts import render



# Create your views here.
def Home(request):
          return render(request,'index.html')

def Signup(request):
        return render(request,'auth/Signup.html')

def Login(request):
        return render(request, 'auth/Login.html')

def Member(request):
          return render(request,'members.html')