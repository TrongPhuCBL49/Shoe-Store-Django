from django.http import Http404
# from django.views import ListView
from django.views.generic import ListView, DetailView
from django.shortcuts import render


from .models import Product

class ProductFeaturedListView(ListView):
    template_name = "homepage/home.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all().featured()


class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.all().featured()
    template_name = "products/product-detail.html"

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     return Product.objects.featured()

class ProductListView(ListView):
    template_name = "homepage/home.html"
    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "homepage/home.html", context)

# class HomeView(View):
#     def get(self, request):
#         Active_Products = filter(lambda product: product.active, Product.objects.all())
#         Products = {'Products': Active_Products}
#         return render(request, 'homepage/home.html', Products) 

class ProductDetailView(DetailView):
    template_name = "products/product-detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Product doesn't exist")
        return instance


def product_detail_view(request, pk=None, *args, **kwargs):
    instance = Product.objects.get_by_id(pk)
    if instance is None:
        raise Http404("Product doesn't exist")
    context = {
        'object': instance
    }
    return render(request, "products/product-detail.html", context)
