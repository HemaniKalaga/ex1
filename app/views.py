from django.shortcuts import render

# Create your views here.
def forloop(request):
    
    d={'Name':'Hemani'}
    return render(request,'forloop.html',d)


