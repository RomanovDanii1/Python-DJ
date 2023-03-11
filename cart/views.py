from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import DeleteView

from .forms import AddQuantityForm
from .models import *
from main.views import *


def find_cart(self):
    cart_number = Order.objects_filter(user=self.user, status=Order.STATUS_CART).count()
    return cart_number


@login_required(login_url=reverse_lazy('login'))
def add_item_to_cart(request, slug):
    if request.method == 'POST':
        cart = Order.get_cart(request.user)
        product = get_object_or_404(Pet, slug=slug)
        cart_item = cart.orderitem_set.filter(product=product).first()
        if cart_item:
            # If the product already exists in the cart, increase its quantity by 1
            cart_item.quantity += 1
            cart_item.save()
        else:
            # If the product does not exist in the cart, create a new cart item
            cart.orderitem_set.create(product=product,
                                      quantity=1,
                                      price=product.price,
                                      photo=product.photo)
        cart.save()
        return redirect('cart')
    else:
        return redirect('home')



@login_required(login_url=reverse_lazy('login'))
def cart_view(request):
    cart = Order.get_cart(request.user)
    items = cart.orderitem_set.all()
    context = {
        'cart': cart,
        'items': items,
        'menu': menu,
    }
    return render(request, 'cart/index.html', context)


@method_decorator(login_required, name='dispatch')
class CartDeleteItem(DeleteView):
    model = OrderItem
    template_name = 'cart/index.html'
    success_url = reverse_lazy('cart')

    def get_queryset(self):
        qs = super().get_queryset()
        qs.filter(order__user=self.request.user)
        return qs


@login_required(login_url=reverse_lazy('login'))
def make_order(request):
    cart = Order.get_cart(request.user)
    cart.make_order()
    return redirect('cart')
