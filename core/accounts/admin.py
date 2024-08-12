from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Profile



class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['email','is_staff','is_active']
    list_filter = ['email','is_staff','is_active']
    search_fields = ['email']
    ordering = ['email']

    fieldsets = (
      ('Personal', {
          'fields': ('email','password')
      }),
      ('Authentications', {
          'fields': ('is_staff','is_superuser')
      }),
              ('important dates', {
          'fields': ('last_login',)
      }),
        ('Permissions', {
          'fields': ('groups','user_permissions')
      }),
   )
    

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2',),}),)


admin.site.register(User,CustomUserAdmin)
admin.site.register(Profile)

