from django.contrib import admin
from .models import Drink_cold, Food, Hookah,Drink_hot

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'image')  # ستونی که نمایش داده می‌شود
    search_fields = ('name', 'description')  # جستجو بر اساس این فیلدها
    list_filter = ('price',)  # فیلتر بر اساس قیمت

class Drink_hotAdmin(ProductAdmin):
    class Meta:
        model = Drink_hot
        verbose_name = "نوشیدنی گرم"
        verbose_name_plural = "نوشیدنی گرم"
        
class Drink_coldAdmin(ProductAdmin):
    class Meta:
        model = Drink_cold
        verbose_name = "نوشیدنی سرد"
        verbose_name_plural = "نوشیدنی سرد"

class FoodAdmin(ProductAdmin):
    class Meta:
        model = Food
        verbose_name = "غذا"
        verbose_name_plural = "غذاها"

class HookahAdmin(ProductAdmin):
    class Meta:
        model = Hookah
        verbose_name = "قلیون"
        verbose_name_plural = "قلیون‌ها"


admin.site.register(Drink_hot, Drink_hotAdmin)
admin.site.register(Drink_cold, Drink_coldAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Hookah, HookahAdmin)