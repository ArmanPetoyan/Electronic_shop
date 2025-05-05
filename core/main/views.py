from django.shortcuts import render, redirect
from .models import Info, Slider, Product, Brand_Product, Contact
# Create your views here.
def index(request):

    if request.method == 'POST':
        contact_name = request.POST.get('contact_name')
        contact_email = request.POST.get('contact_email')
        contact_message = request.POST.get('contact_message')
        contact_phone = request.POST.get('contact_phone')

        Contact.objects.create(
            name=contact_name,
            email=contact_email,
            phone=contact_phone,
            message=contact_message
        )
        return redirect('contact')

    info = Info.objects.first()
    slider_active = Slider.objects.first()
    slider = Slider.objects.all()[1:]
    product = Product.objects.all()

    return render(request, 'index.html', context={
        'active_list': 'active_list',
        'info': info,
        'slider_active': slider_active,
        'slider': slider,
        'product': product

    })


def about(request):

    info = Info.objects.first()

    return render(request, 'about.html', context={
        'info': info, 

    })


def brand(request):

    info = Info.objects.first()
    brand_product = Brand_Product.objects.all()

    return render(request, 'brand.html', context={
        'info':info,
        'brand_product': brand_product

    })


def contact(request):
    if request.method == 'POST':
        contact_name = request.POST.get('contact_name')
        contact_email = request.POST.get('contact_email')
        contact_message = request.POST.get('contact_message')
        contact_phone = request.POST.get('contact_phone')

        Contact.objects.create(
            name=contact_name,
            email=contact_email,
            phone=contact_phone,
            message=contact_message
        )
        return redirect('contact')
    
    info = Info.objects.first()
    return render(request, 'contact.html', context={'info': info})



def special(request):

    info = Info.objects.first()
    slider_active = Slider.objects.first()
    slider = Slider.objects.all()[1:]

    return render(request, 'special.html', context={
        'info':info,
        'slider_active': slider_active,
        'slider': slider,
    })