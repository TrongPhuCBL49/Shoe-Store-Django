# from django.views import ListView
from django.views.generic import ListView
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
