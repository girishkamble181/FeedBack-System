from django.shortcuts import render
from .forms import FbForm

# Create your views here.

def home(request):	
	if request.method=="POST":	
		n= request.POST.get('name')
		f= request.POST.get('feedback')
		print(n,f)
		fm= FbForm()
		return render(request,'home.html',{'fm':fm,'msg':'thanks for the feedback'})
	else:
		fm= FbForm()
		return render(request,'home.html',{'fm':fm})