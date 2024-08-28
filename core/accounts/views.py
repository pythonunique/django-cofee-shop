from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmailForm,CodeForm,PasswordForm,ProfileForm,CustomPasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import User,Profile
from products.models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash


def first_page(request):
    foods = Food.objects.all()
    cold_drink = Drink_cold.objects.all()
    hot_drink = Drink_hot.objects.all()
    hookah = Hookah.objects.all()
    context = {'foods':foods,'cold_drinks':cold_drink,'hot_drinks':hot_drink,'hookahs':hookah}
    return render(request, 'index.html',context)


def signup_email(request):
    if request.user.is_authenticated:
        return redirect('home_view')
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email_addr_user = form.cleaned_data['email']
            if User.objects.filter(email=email_addr_user).exists():
                return redirect('login_user')
            request.session['email'] = form.cleaned_data['email']
            return redirect('signup_code')
    else:
        form = EmailForm()
    return render(request, 'signup_email.html', {'form': form})

def signup_code(request):
    if 'email' not in request.session:
        return redirect('signup_email')
    if request.user.is_authenticated:
        return redirect('home_view')
    if request.method == 'POST':
        form = CodeForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            if code == '123456':
                request.session['code'] = code
                return redirect('signup_password')
            else:
                form.add_error('code', 'کد شما اشتباه است!')
    else:
        form = CodeForm()
    return render(request, 'signup_code.html', {'form': form})



def signup_password(request):
    if 'email' not in request.session or 'code' not in request.session:
        return redirect('signup_email')
    if request.user.is_authenticated:
        return redirect('home_view')
    if request.method == 'POST':
        form = PasswordForm(request.POST)
        if form.is_valid():
            password1 = form.cleaned_data['password1']
            request.session['password'] = password1
            return redirect('create_user')
    else:
        form = PasswordForm()
    return render(request, 'signup_password.html', {'form': form})

def profile_setup(request):
    if ('email' not in request.session) or ('code' not in request.session) or ('password' not in request.session):
        return redirect('signup_email')
    if request.user.is_authenticated:
        return redirect('home_view')
    user_id = request.session.get('user_id')
    user = User.objects.get(id = user_id) 
    profile, created = Profile.objects.get_or_create(user=user) 

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES,instance=profile)
        if form.is_valid():
            auth_login(request,user)
            request.session['email'] = None
            request.session['password'] = None
            form.save() 
            return redirect('home_view')  
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'profile_setup.html', {'form': form})




def create_user(request):
    email = request.session.get('email')
    password = request.session.get('password')

    if email and password:
        user = User.objects.create_user(email=email, password=password)
        request.session['user_id'] = user.id
        return redirect('profile_set')

    return redirect('signup_email')  # در صورت عدم وجود اطلاعات لازم، بازگشت به صفحه ثبت ایمیل


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home_view')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # احراز هویت موفقیت‌آمیز
            user = form.get_user()
            auth_login(request, user)
            return redirect('home_view')  # به صفحه‌ی اصلی یا هر صفحه‌ی دیگر ریدایرکت شوید
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


@login_required
def profile_view(request):
    user = request.user
    profile = Profile.objects.filter(user=user).first()

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        password_form = CustomPasswordChangeForm(user, request.POST)

        if profile_form.is_valid():
            profile_form.save()

        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)  # به‌روزرسانی session کاربر
            return redirect('profile')  # بازگشت به صفحه پروفایل

    else:
        profile_form = ProfileForm(instance=profile)
        password_form = CustomPasswordChangeForm(user)

    return render(request, 'profile.html', {
        'profile_form': profile_form,
        'password_form': password_form
    })