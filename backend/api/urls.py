# from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', include('api.urls'))
    path ('namp/',nmap_api.as_view(),name='test' ),
    path ('volatility/', volatality_api.as_view() ),
    path ('wireshark/', wireshark_api.as_view()),
]
