from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='Services'),
    path('register/', views.register, name='register'),
    path('my-appointment-ongoing/', views.ongoing, name='ongoing'),
    path('my-appointment-completed/', views.completed, name='completed'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
