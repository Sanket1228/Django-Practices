from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Order, OrderUpdate
from math import ceil
import json
# Create your views here.


def index(request):
    allProds = []
    catProds = Product.objects.values('category', 'id')
    cats = {item["category"] for item in catProds}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {"allProds": allProds}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone_number = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email,
                          phone_number=phone_number, msg=desc)
        contact.save()
    return render(request, 'shop/contact.html')


def tracker(request):
    if request.method == "POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Order.objects.filter(order_id=orderId)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text':item.update_desc,'time':item.timestamp})
                    response = json.dumps([updates,order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('else')
        except Exception as e:
            return Exception

    return render(request, 'shop/tracker.html')


def search(request):
    return HttpResponse("We are at search")


def productView(request, myid):
    product = Product.objects.filter(id=myid)
    return render(request, 'shop/prodView.html', {'product': product[0]})


def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('add1', '') + " " + request.POST.get('add2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '') 
        phone_number = request.POST.get('phone', '')
        

        order = Order(items_json=items_json,name=name, email=email,address=address,city=city,state=state,zip_code=zip_code,
                          phone_number=phone_number)
        order.save()
        update = OrderUpdate(order_id = order.order_id,update_desc="The Order has been placed")
        update.save()
        thanks = True
        id = order.order_id
        return render(request, 'shop/checkout.html',{"thanks":thanks,"id":id})

    return render(request, 'shop/checkout.html')
