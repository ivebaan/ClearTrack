from django.shortcuts import render

# Create your views here.
def req_home(request):
    return render(request,'base.html', {'name':'Semm'})