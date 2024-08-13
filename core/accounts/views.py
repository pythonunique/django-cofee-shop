from django.shortcuts import render
from django.http import HttpResponse
from .forms import Emailform




def first_page(request):
    return render(request,'index.html')

def email_form_view(request):
    if request.method=='POST':
        form = Emailform(request)















#this is for smtp server :)
#i will make it after :)
# def send_test_email(request):
#     subject = 'hack shodi dadash'
#     message = 'This is a test email sent using Sendinblue SMTP from Django.'
#     from_email = 'v.yazdani79@gmail.com'
#     recipient_list = ['sohrabj926@gmail.com']

#     try:
#         send_mail(subject, message, from_email, recipient_list)
#         return HttpResponse('Email sent successfully!')
#     except Exception as e:
#         return HttpResponse(f'Error: {e}')