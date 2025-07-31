from django.contrib import admin
from django.urls import path
from home import views  # import views from your app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),           # Home page
    path('contact/', views.contact_view, name='contact'),  # Contact page
    path('about/', views.about, name='about'),     # About page
    path('services/', views.services, name='services'),  # Services page
]
