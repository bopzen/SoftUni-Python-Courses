import os
import django
from django.db.models import Q, Count, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
# Create and run your queries within functions

from main_app.models import Profile, Product, Order

# print(Profile.objects.get_regular_customers())


def get_profiles(search_string=None):
    if search_string is None:
        return ""
    query = Q()
    if search_string is not None:
        query = Q(full_name__icontains=search_string) | Q(email__icontains=search_string) | Q(phone_number__icontains=search_string)
    profiles = Profile.objects.filter(query).order_by('full_name')
    if not profiles:
        return ""

    result = []
    for profile in profiles:
        result.append(f"Profile: {profile.full_name}, email: {profile.email}, phone number: {profile.phone_number}, orders: {profile.orders.count()}")

    return "\n".join(result)


# print(get_profiles('A'))


def get_loyal_profiles():
    loyal_profiles = Profile.objects.get_regular_customers()
    if not loyal_profiles:
        return ""
    result = [
        f"Profile: {profile.full_name}, orders: {profile.orders.count()}"
        for profile in loyal_profiles
    ]
    return "\n".join(result)


# print(get_loyal_profiles())


def get_last_sold_products():
    last_order = Order.objects.prefetch_related('products').order_by('id').last()
    if not last_order:
        return ""
    products = last_order.products.order_by('name')
    return f"Last sold products: {', '. join(product.name for product in products)}"


# print(get_last_sold_products())


def get_top_products():
    products = Product.objects.prefetch_related('orders').annotate(product_count=Count('orders')).filter(product_count__gt=0).order_by('-product_count', 'name')[:5]
    if not products:
        return ""
    result = ['Top products:']
    for product in products:
        result.append(f"{product.name}, sold {product.product_count} times")

    return '\n'.join(result)


# print(get_top_products())


def apply_discounts():
    updated_orders = Order.objects.annotate(
        products_count=Count('products')
    ).filter(
        products_count__gt=2, is_completed=False
    ).update(
        total_price=F('total_price') * 0.9
    )

    return f"Discount applied to {updated_orders} orders."


def complete_order():
    order = Order.objects.prefetch_related('products').filter(is_completed=False).order_by('creation_date').first()
    if not order:
        return ""

    for product in order.products.all():
        product.in_stock -= 1
        if product.in_stock == 0:
            product.is_available = False
        product.save()
    order.is_completed = True
    order.save()
    return f"Order has been completed!"