from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import  Drink_cold, Drink_hot, Food, Hookah
from django.contrib.auth.decorators import login_required

# @csrf_exempt
# def update_quantity(request):
#     if request.method == 'POST':
#         import json
#         data = json.loads(request.body)
#         product_id = data.get('product_id')
#         product_type = data.get('product_type')
#         quantity_change = data.get('quantity_change')
        
#         cart, created = Cart.objects.get_or_create(user=request.user)
#         if product_type == 'drink_cold':
#             product = get_object_or_404(Drink_cold, id=product_id)
#         elif product_type == 'drink_hot':
#             product = get_object_or_404(Drink_hot, id=product_id)
#         elif product_type == 'food':
#             product = get_object_or_404(Food, id=product_id)
#         elif product_type == 'hookah':
#             product = get_object_or_404(Hookah, id=product_id)
#         else:
#             return JsonResponse({'success': False, 'message': 'Invalid product type'}, status=400)
        
#         cart_item, created = CartItem.objects.get_or_create(
#             cart=cart,
#             item_type=product_type,
#             item_id=product_id
#         )
        
#         if not created:
#             new_quantity = cart_item.quantity + quantity_change
#             if new_quantity <= 0:
#                 cart_item.delete()
#             else:
#                 cart_item.quantity = new_quantity
#                 cart_item.save()
        
#         quantity = cart_item.quantity if not created else max(quantity_change, 0)
#         return JsonResponse({'success': True, 'quantity': quantity})
#     return JsonResponse({'success': False, 'message': 'Invalid request'}, status=400)


# @login_required
# def view_cart(request):
#     cart, created = Cart.objects.get_or_create(user=request.user)
#     items = CartItem.objects.filter(cart=cart)
#     return render(request, 'index.html', {'cart': cart, 'items': items})

# @login_required
# def remove_from_cart(request, item_id):
#     cart_item = get_object_or_404(CartItem, id=item_id)
#     cart_item.delete()
#     return redirect('view_cart')

# @login_required
# def checkout(request):
#     cart, created = Cart.objects.get_or_create(user=request.user)
#     if request.method == 'POST':
#         order = Order.objects.create(user=request.user, status='pending')
#         for cart_item in CartItem.objects.filter(cart=cart):
#             OrderItem.objects.create(
#                 order=order,
#                 item_type=cart_item.item_type,
#                 item_id=cart_item.item_id,
#                 quantity=cart_item.quantity
#             )
#         cart.cartitem_set.all().delete()  # Empty the cart after checkout
#         return redirect('order_detail', order_id=order.id)
#     return render(request, 'checkout.html')

# @login_required
# def order_detail(request, order_id):
#     order = get_object_or_404(Order, id=order_id)
#     order_items = OrderItem.objects.filter(order=order)
#     return render(request, 'index.html', {'order': order, 'order_items': order_items})