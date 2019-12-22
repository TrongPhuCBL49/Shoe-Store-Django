# from django.views import ListView
from django.views.generic import ListView, DetailView
from django.shortcuts import render


from .models import Product


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "homepage/home.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context


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
    queryset = Product.objects.all()
    template_name = "products/product-detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        # context['abc'] = 123
        return context


def product_detail_view(request, pk=None, *args, **kwargs):
    #instance = Product.objects.get(pk=pk) #id
    instance = get_object_or_404(Product, pk=pk)
    context = {
        'object': instance
    }
    return render(request, "products/product-detail.html", context)
