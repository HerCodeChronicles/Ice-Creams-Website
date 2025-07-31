from django.shortcuts import render
from .models import Contact  # ✅ Model imported
from django.contrib import messages

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, "services.html")


def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')  # ✅ Use correct field name

        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        messages.success(request, "Your message has been sent.")

    return render(request, 'contact.html')
