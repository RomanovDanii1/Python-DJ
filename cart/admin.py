from django.contrib import admin

from cart.models import *

admin.site.register(Payment)
admin.site.register(Order)
admin.site.register(OrderItem)
