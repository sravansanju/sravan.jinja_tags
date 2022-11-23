from django.shortcuts import render

# Create your views here.
def sravan(request):
    d={'name':'sravan','age':22}
    return render(request,'sravan.html',d)