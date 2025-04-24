from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='Services'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('my-account/', views.myaccount, name='myaccount'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('about-us/', views.about_us, name='about_us'),
    path('services/', views.services, name='services'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
