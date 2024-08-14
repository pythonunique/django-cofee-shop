from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmailForm,CodeForm,PasswordForm,ProfileForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import User,Profile


def first_page(request):
    return render(request, 'index.html')


def signup_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            # ایمیل را در session ذخیره می‌کنیم تا در مرحله بعد استفاده شود
            request.session['email'] = form.cleaned_data['email']
            return redirect('signup_code')
    else:
        form = EmailForm()
    return render(request, 'signup_email.html', {'form': form})

def signup_code(request):
    if request.method == 'POST':
        form = CodeForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            if code == '123456':
                return redirect('signup_password')
            else:
                form.add_error('code', 'کد شما اشتباه است!')
    else:
        form = CodeForm()
    return render(request, 'signup_code.html', {'form': form})



def signup_password(request):
    if request.method == 'POST':
        form = PasswordForm(request.POST)
        if form.is_valid():
            password1 = form.cleaned_data['password1']
            request.session['password'] = password1
            # پسورد تایید شده، می‌توانید کاربر را به صفحه پروفایل هدایت کنید
            return redirect('create_user')  # 'profile' را با نام صفحه پروفایل خود جایگزین کنید
    else:
        form = PasswordForm()
    return render(request, 'signup_password.html', {'form': form})


@login_required
def profile_setup(request):
    user_id = request.session.get('user_id')
    user = User.objects.get(id = user_id) 
    profile, created = Profile.objects.get_or_create(user=user)  # پروفایل را دریافت کنید یا ایجاد کنید

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES,instance=profile)
        if form.is_valid():
            print(profile.last_name)
            form.save() 
            return redirect('profile')  
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'profile_setup.html', {'form': form})




# views.py
def create_user(request):
    email = request.session.get('email')
    password = request.session.get('password')

    if email and password:
        # ساخت کاربر
        user = User.objects.create_user(email=email, password=password)
        # پاک کردن اطلاعات از سشن
        request.session['email'] = None
        request.session['password'] = None
        request.session['user_id'] = user.id
        # هدایت کاربر به صفحه تکمیل پروفایل
        return redirect('profile')

    return redirect('signup_email')  # در صورت عدم وجود اطلاعات لازم، بازگشت به صفحه ثبت ایمیل

