from django.db import models
from accounts.models import User
import json

class Product(models.Model):
    name = models.CharField(max_length=100)  
    description = models.TextField()  
    price = models.DecimalField(max_digits=10, decimal_places=3)  
    image = models.ImageField(upload_to='products/')  

    class Meta:
        abstract = True  

    def __str__(self):
        return self.name


class Drink_cold(Product):
    class Meta:
        verbose_name = " نوشیدنی سرد"
        verbose_name_plural = "نوشیدنی سرد"


class Drink_hot(Product):
    class Meta:
        verbose_name = " نوشیدنی گرم"
        verbose_name_plural = "نوشیدنی گرم"

class Food(Product):
    class Meta:
        verbose_name = "غذا"
        verbose_name_plural = "غذاها"

class Hookah(Product):
    class Meta:  
        verbose_name = "قلیون"
        verbose_name_plural = "قلیون‌ها"


class Order_food(models.Model):
    STATUS_CHOICES = [
        ('pending', 'در انتظار'),
        ('processing', 'در حال پردازش'),
        ('shipped', 'ارسال شده'),
        ('delivered', 'تحویل داده شده'),
        ('canceled', 'لغو شده'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart_items = models.TextField()  # تغییر به TextField
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Order {self.id} - {self.user.email}"

    def set_cart_items(self, cart_items):
        """ذخیره داده‌های JSON در TextField"""
        self.cart_items = json.dumps(cart_items)

    def get_cart_items(self):
        """بازیابی داده‌های JSON از TextField"""
        return json.loads(self.cart_items)

class OrderItem_food(models.Model):
    order = models.ForeignKey(Order_food, on_delete=models.CASCADE, related_name='items')
    product_name = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.product_name} in order {self.order.id}"
    
    

# class Cart(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return f'Cart for {self.user.email}'

# class CartItem(models.Model):
#     CART_ITEM_TYPES = [
#         ('drink_cold', 'Cold Drink'),
#         ('drink_hot', 'Hot Drink'),
#         ('food', 'Food'),
#         ('hookah', 'Hookah'),
#     ]
    
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
#     item_type = models.CharField(max_length=20, choices=CART_ITEM_TYPES)
#     item_id = models.PositiveIntegerField()
#     quantity = models.PositiveIntegerField(default=1)
    
#     def get_item(self):
#         if self.item_type == 'drink_cold':
#             from .models import Drink_cold
#             return Drink_cold.objects.get(id=self.item_id)
#         elif self.item_type == 'drink_hot':
#             from .models import Drink_hot
#             return Drink_hot.objects.get(id=self.item_id)
#         elif self.item_type == 'food':
#             from .models import Food
#             return Food.objects.get(id=self.item_id)
#         elif self.item_type == 'hookah':
#             from .models import Hookah
#             return Hookah.objects.get(id=self.item_id)

#     def __str__(self):
#         return f'{self.get_item().name} - {self.quantity}'

# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     ordered_at = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed'), ('cancelled', 'Cancelled')])
    
#     def __str__(self):
#         return f'Order {self.id} by {self.user.username}'

# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     item_type = models.CharField(max_length=20, choices=CartItem.CART_ITEM_TYPES)
#     item_id = models.PositiveIntegerField()
#     quantity = models.PositiveIntegerField()
    
#     def get_item(self):
#         if self.item_type == 'drink_cold':
#             from .models import Drink_cold
#             return Drink_cold.objects.get(id=self.item_id)
#         elif self.item_type == 'drink_hot':
#             from .models import Drink_hot
#             return Drink_hot.objects.get(id=self.item_id)
#         elif self.item_type == 'food':
#             from .models import Food
#             return Food.objects.get(id=self.item_id)
#         elif self.item_type == 'hookah':
#             from .models import Hookah
#             return Hookah.objects.get(id=self.item_id)
    
#     def __str__(self):
#         return f'{self.get_item().name} - {self.quantity}'