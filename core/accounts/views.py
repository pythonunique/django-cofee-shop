from django.shortcuts import render



def first_page(request):
    return render(request,'index.html')
