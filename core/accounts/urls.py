from django.urls import path
from .views import *

urlpatterns = [
    path('',first_page,name='home_view'),
    path('signup/', signup_email, name='signup_email'),
    path('signup/code/', signup_code, name='signup_code'),
    path('signup/password/', signup_password, name='signup_password'),
    path('signup/create_user/', create_user, name='create_user'),
    # path('profile/setup/<int:user_id>/', profile_setup, name='profile_setup'),
    path('profile/', profile_setup, name='profile'),  # ویو پروفایل را باید ایجاد کنید
]