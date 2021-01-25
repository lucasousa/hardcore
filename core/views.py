from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import requests


def index(request):
    products = requests.get("http://127.0.0.1:9000/products/")
    partners = requests.get("http://127.0.0.1:7000/partners/")
    context = {
        'product': len(products.json()),
        'partner': len(partners.json())
    }
    return render(request, "core/index.html", context)


@require_POST
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('website:index'))


# Functions of the service partner
def manage_partner(request):
    object_list = requests.get("http://127.0.0.1:7000/partners/")
    return render(request, 'partner/manage_partner.html', {'objetos': object_list.json()})


def add_partner(request):
    if request.POST:
        logo = request.FILES['logo']
        description = request.POST['description']
        name = request.POST['name']
        content = {"name": name, "description": description, "id_athletic": 1}
        r = requests.post("http://127.0.0.1:7000/partners/", data=content, files={"logo": logo})
        return HttpResponseRedirect(reverse('core:manage_partners'))
    return render(request, 'partner/add_partner.html')


def views_partner(request, id):
    query = {"id": id}
    partner = requests.get("http://127.0.0.1:7000/partners/", params=query)
    print((partner.json()))

    res = {
        'objeto': partner.json()
    }
    return render(request, 'partner/partner_detail.html', res)
# End functions partner


# Functions of the service Product
def manage_products(request):
    object_list = requests.get("http://127.0.0.1:9000/products/")
    return render(request, 'product/manage_products.html', {'objetos': object_list.json()})


def add_product(request):
    if request.POST:
        logo = request.FILES['image']
        name = request.POST['name']
        value = request.POST['value']
        content = {"name": name, "value": value, "id_athletic": 1}
        r = requests.post("http://127.0.0.1:9000/products/", data=content, files={"image": logo})
        return HttpResponseRedirect(reverse('core:manage_products'))
    return render(request, 'product/add_product.html')


def views_product(request, id):
    print("Id - ", id)
    query = {"id": id}
    product = requests.get("http://127.0.0.1:9000/products/", params=query)
    print((product.json()))

    res = {
        'objeto': product.json()
    }
    return render(request, 'product/product_detail.html', res)