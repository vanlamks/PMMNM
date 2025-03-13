#from django.html import HttpResponse
from django.shortcuts import render
def homepage(request):
    #return HttpResponse("Xin chào Django")
    return render(request, 'home.html')
def aboutpage(request):
    #return HttpResponse("Đây là trang giới thiệuthiệu")
    return render(request, 'about.html')
