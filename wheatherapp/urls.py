from django.urls import path
from django.conf  import settings
from wheatherapp import views
from django.conf.urls.static import  static

urlpatterns = [
       path('',views.home)

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


 
