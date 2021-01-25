from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse
import requests


def index(request):
    product = requests.get("http://127.0.0.1:9000/products/")
    partner = requests.get("http://127.0.0.1:7000/partners/")
    res = {
        'objeto': product.json(),
        'partner': partner.json(),
    }
    return render(request, 'website/index.html', res)


def login_user(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('core:index'))

    if 'next' in request.GET:
        request.session['redirect'] = request.GET['next']
    
    if request.POST:
        email = request.POST['email']
        email = email.lower()
        senha = request.POST['password']
        try:
            user = User.objects.get(email=email)
            if user:
                user = authenticate(request, username=user.username, password=senha)
                if user is not None:
                    login(request, user)
                    if 'redirect' in request.session:
                        redirect = request.session['redirect']
                        del request.session['redirect']
                        return HttpResponseRedirect(redirect)

                    return HttpResponseRedirect(reverse('core:index'))
                else:
                    return render(request, 'website/login.html', {'message': 'E-mail ou senha incorretos.', 'class': 'has-text-danger'})    

        except User.DoesNotExist:
            return render(request, 'website/login.html', {'message': 'E-mail ou senha incorretos.', 'class': 'has-text-danger'})    
        
    if 'message' in request.session:
        message = request.session['message']
        class_name = request.session['class']
        del request.session['message']
        del request.session['class']
        return render(request, 'website/login.html', {'message': message, 'class': class_name})

    return render(request, 'website/login.html')


def product_list(request):
    product = requests.get("http://127.0.0.1:9000/products/")
    res = {
        'objeto':product.json(),
    }
    return render(request, 'website/list-product.html', res)


def partner_list(request):
    partner = requests.get("http://127.0.0.1:7000/partners/")
    res = {
        'partner':partner.json(),
    }
    return render(request, 'website/list-partner.html', res)
