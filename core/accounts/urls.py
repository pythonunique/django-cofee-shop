from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',first_page,name='home_view'),
    path('signup/', signup_email, name='signup_email'),
    path('signup/code/', signup_code, name='signup_code'),
    path('signup/password/', signup_password, name='signup_password'),
    path('signup/create_user/', create_user, name='create_user'),
    path('login/',login_view,name='login_user'),
     path('logout/', LogoutView.as_view(next_page='home_view'), name='logout'),
    # path('profile/setup/<int:user_id>/', profile_setup, name='profile_setup'),
    path('profile/set/', profile_setup, name='profile_set'),  # ویو پروفایل را باید ایجاد کنید
    path('profile/', profile_view, name='profile_view'),
    path('profile/edit/', profile_edit, name='profile_edit'),
    path('submit_cart/', submit_cart, name='submit_cart'),
    path('check_login_status/', check_login_status, name='check_login_status'),
]