from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core import serializers
from .models import Product
from .forms import ProductForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import datetime
import requests
from django.views.decorators.csrf import csrf_exempt
from django.utils.html import strip_tags
import json
from django.http import JsonResponse

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'

    raw_last_login = request.COOKIES.get("last_login", "Never")
    try:
        formatted_last_login = datetime.datetime.fromisoformat(raw_last_login).strftime("%Y-%m-%d %H:%M")
    except Exception:
        formatted_last_login = raw_last_login

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    context = {
        'npm': '2406431486',
        'name': 'Bintoro Nata Wijaya',
        'class': 'PBP B',
        'product_list': product_list,
        'last_login': formatted_last_login,
    }

    return render(request, "main.html", context)


@login_required(login_url='/login')
def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')
    context = {'form': form}
    return render(request, "create_product.html", context)


@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    context = {'product': product}
    return render(request, "product_detail.html", context)


def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")


def show_json(request):
    product_list = Product.objects.all()
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'category': product.category,
            # gunakan .thumbnail aja biar aman kalau bukan ImageField
            'thumbnail': product.thumbnail if product.thumbnail else "",
            'is_featured': product.is_featured,
            # pakai username karena user.id bisa None (CustomUser pakai username pk)
            'user_id': product.user.username if product.user else None,
        }
        for product in product_list
    ]
    return JsonResponse(data, safe=False)


def show_xml_by_id(request, product_id):
    try:
        Product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", Product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)


def show_json_by_id(request, product_id):
    try:
        product_item = Product.objects.get(pk=product_id)
        json_data = serializers.serialize("json", [product_item])
        return HttpResponse(json_data, content_type="application/json")
    except Product.DoesNotExist:
        return HttpResponse(status=404)


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form': form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response


def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "edit_product.html", context)


def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))


@login_required(login_url='/login')
def create_product_ajax(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return JsonResponse({
                "success": True,
                "message": "Product created successfully!",
                "product": {
                    "id": str(product.id),
                    "name": product.name,
                    "price": product.price,
                    "description": product.description,
                    "category": product.category,
                    "thumbnail": product.thumbnail or "",
                    "is_featured": product.is_featured,
                    "user_id": product.user.username if product.user else None,  
                },
            })
        else:
            return JsonResponse({"success": False, "errors": form.errors}, status=400)
    return JsonResponse({"success": False, "message": "Invalid request method"}, status=405)


@login_required(login_url='/login')
def update_product_ajax(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return JsonResponse({
                "success": True,
                "message": "Product updated successfully!",
                "product": {
                    "id": str(product.id),
                    "name": product.name,
                    "price": product.price,
                    "description": product.description,
                    "category": product.category,
                    "thumbnail": product.thumbnail or "",
                    "is_featured": product.is_featured,
                    "user_id": product.user.username if product.user else None,  
                },
            })
        else:
            return JsonResponse({"success": False, "errors": form.errors}, status=400)
    return JsonResponse({"success": False, "message": "Invalid request method"}, status=405)



@login_required(login_url='/login')
def delete_product_ajax(request, id):
    print("DEBUG: method =", request.method)
    print("DEBUG: POST =", request.POST)
    if request.method == "DELETE" or (request.method == "POST" and request.POST.get("_method") == "DELETE"):
        product = get_object_or_404(Product, pk=id)
        product.delete()
        return JsonResponse({"success": True, "message": "Product deleted successfully!"})
    return JsonResponse({"success": False, "message": f"Invalid request method {request.method}"}, status=405)



@login_required(login_url='/login')
def get_products_json(request):
    product_list = Product.objects.all()
    data = [
        {
            "id": str(p.id),
            "name": p.name,
            "price": p.price,
            "description": p.description,
            "category": p.category,
            "thumbnail": p.thumbnail if p.thumbnail else "",
            "is_featured": p.is_featured,
            "user_id": p.user.username if p.user else None,
        }
        for p in product_list
    ]
    return JsonResponse({"products": data})


def register_ajax(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True, "message": "Account created successfully!"})
        else:
            return JsonResponse({"success": False, "errors": form.errors}, status=400)
    return JsonResponse({"success": False, "message": "Invalid request"}, status=405)


def login_ajax(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = JsonResponse({"success": True, "message": "Login successful!"})
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            return JsonResponse({"success": False, "errors": form.errors}, status=400)
    return JsonResponse({"success": False, "message": "Invalid request"}, status=405)


@login_required(login_url='/login')
def logout_ajax(request):
    logout(request)
    response = JsonResponse({"success": True, "message": "Logout successful!"})
    response.delete_cookie('last_login')
    return response

def proxy_image(request):
    image_url = request.GET.get('url')
    if not image_url:
        return HttpResponse('No URL provided', status=400)
    
    try:
        # Fetch image from external source
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        
        # Return the image with proper content type
        return HttpResponse(
            response.content,
            content_type=response.headers.get('Content-Type', 'image/jpeg')
        )
    except requests.RequestException as e:
        return HttpResponse(f'Error fetching image: {str(e)}', status=500)

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = strip_tags(data.get("name", ""))  # Strip HTML tags
        price = data.get("price")
        if price is None:
            return JsonResponse({"status": "error", "message": "Price is required"}, status=400)
        description = strip_tags(data.get("description", ""))  # Strip HTML tags
        category = data.get("category", "")
        thumbnail = data.get("thumbnail", "")
        is_featured = data.get("is_featured", False)
        user = request.user
        
        new_product = Product(
            name=name, 
            price=int(price),
            description=description,
            category=category,
            thumbnail=thumbnail,
            is_featured=is_featured,
            user=user
        )
        new_product.save()
        
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
    
