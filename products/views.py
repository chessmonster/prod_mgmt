from django.urls import reverse_lazy
from vanilla import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import ProductForm
from .models import Product

from django.utils import translation

class ProductList(ListView):
    model = Product
    paginate_by = 20

    def dispatch(self, request, *args, **kwargs):
        # translation.activate('fi')
        # request.session[translation.LANGUAGE_SESSION_KEY] = 'fi'

        if translation.LANGUAGE_SESSION_KEY in request.session:
            del request.session[translation.LANGUAGE_SESSION_KEY]

        return super(ProductList, self).dispatch(request, *args, **kwargs)


class ProductCreate(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('products:list')

    def get_form_class(self):
        """Return the form class to use."""
        print(dir(self.form_class))
        print((self.form_class.get_initial_for_field))



        return self.form_class

class ProductDetail(DetailView):
    model = Product


class ProductUpdate(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('products:list')


class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('products:list')
