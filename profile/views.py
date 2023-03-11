from django.contrib.auth.views import PasswordChangeView
from django.db.models import Q
from django.views.generic import UpdateView
from cart.views import *

from profile.models import EditProfileForm, ChangePasswordForm


def profile_view(request):
    context = {
        'menu': menu,
    }
    return render(request, 'profile/main.html', context)





class EditProfileView(UpdateView):
    form_class = EditProfileForm
    template_name = 'profile/edit.html'
    success_url = reverse_lazy('home')
    context = {
        'menu': menu,
    }

    def get_object(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        return context


class ChangePasswordView(PasswordChangeView):
    form_class = ChangePasswordForm
    template_name = 'profile/change_password.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        return context




def orders_view(request):
    orders = Order.objects.filter(
        Q(status=Order.STATUS_WAITING_FOR_PAYMENT) | Q(status=Order.STATUS_PAID),
        user=request.user)
    cart = Order.get_cart(request.user)
    items = cart.orderitem_set.all()
    context = {
        'menu': menu,
        'orders': orders,
        'cart': cart,
        'items': items,
    }
    return render(request, 'profile/orders.html', context)
