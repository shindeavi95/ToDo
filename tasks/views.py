from django.shortcuts import render

def index(request):
    return render(request,'tasks/list.html')
