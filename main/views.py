from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import redirect, get_object_or_404

from django.shortcuts import render
from django.http import HttpResponse

from .forms import *
from .models import *
from .utils import DataMixin


menu = [{'title': "Main page", 'url_name': 'home'},
        {'title': "About company", 'url_name': 'about'},
        {'title': "Contacts", 'url_name': 'contacts'},
        ]


class MainIndex(DataMixin, ListView):
    model = Pet
    template_name = "main/index.html"
    context_object_name = "posts"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Main")
        return dict(list(context.items()) + list(c_def.items()))


class MainAbout(DataMixin, ListView):
    model = Pet
    template_name = 'main/about.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="About")
        return dict(list(context.items()) + list(c_def.items()))


class MainCategory(DataMixin, ListView):
    model = Category
    template_name = "main/category.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Pet.objects.filter(cat__slug=self.kwargs['cat_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Category',
                                      cat_selected=context['posts'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))


# def authorization(request):
#     return HttpResponse("Авторизация")

def buy_information(request):
    return render(request, 'main/how_buy.html', {'menu': menu, 'title': 'How_buy'})


class MainPost(DataMixin,DetailView):
    model = Pet
    template_name = 'main/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Post')
        return dict(list(context.items()) + list(c_def.items()))


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Register")
        return dict(list(context.items()) + list(c_def.items()))


class LoginUser(DataMixin, LoginView):
    form_class = LoginForm
    template_name = 'main/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Login")
        return dict(list(context.items()) + list(c_def.items()))

    # def get_success_url(self):
    #     return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('/')