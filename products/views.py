from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from carts.models import Cart
from .models import Product


class ProductListView(ListView):
    template_name = 'products/product_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_queryset(self, *args, **kwargs):
        return Product.objects.all()


class ProductFeaturedListView(ListView):
    queryset = Product.objects.featured()
    template_name = 'products/product_list.html'

    # def get_queryset(self, *args, **kwargs):
    #     return Product.objects.featured()


class ProductDetailSlugView(DetailView):
    queryset = Product.objects.featured()
    template_name = 'products/product_details.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_object(self, queryset=None):
        request = self.request
        slug = self.kwargs.get('slug')

        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404('Not Found')
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=true)
            instance = qs.first()
        return instance


class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.featured()
    template_name = 'products/featured_details.html'

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     return Product.objects.featured()


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_details.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

    # def get_object(self, queryset=None):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #
    #     instance = Product.objects.get_by_id(pk)
    #     if instance is None:
    #         raise Http404("Product doesn't exist")
    #     return instance

    def get_queryset(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        return Product.objects.filter(pk=pk)


