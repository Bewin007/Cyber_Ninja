# from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', include('api.urls'))
    path ('ttt/',nmap_api.as_view(),name='test' ),
]
