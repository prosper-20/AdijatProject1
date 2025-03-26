from django.shortcuts import render,redirect
from .models import Product
from .forms import ProductForm



def list_products (request):
    all_products = Product.objects.all()
    # return render(request, "products/all_products.html", {"all_products": all_products})
    return render(request, "products/new_templates.html", {"all_products": all_products})


def retrieve_product (request, id):
    product = Product.objects.get(id=id)
    return render(request, "products/one_product.html", {"product": product})


# def create_product (request):
#     form = ProductForm()
#     return render(request, "products/create_product.html", {"form": form})


def create_product(request):
    if request.method == "GET":
        form = ProductForm()
    else:
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect("/products")
    return render(request, "products/create_product.html", {"form": form})