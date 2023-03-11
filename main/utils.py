from .models import *

menu = [{'title': "Main page", 'url_name': 'home'},
        {'title': "About company", 'url_name': 'about'},
        {'title': "Contacts", 'url_name': 'contacts'},
        ]



class DataMixin:
    def get_user_context(self, *, object_list=None, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        context["menu"] = menu
        context["cats"] = cats
        for category in cats:
            context[category.name.lower()] = category
        return context