# from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path ('nmap/',nmap_api.as_view(),name='test' ),
    path ('volatility/', volatality_api.as_view() ),
    path ('wireshark/', wireshark_api.as_view()),
    path ('exiftool/',exiftool_api.as_view()),
    path ('strings/',Strings_api.as_view()),
    path ('binwalk/',Binwalk_api.as_view()),
    path ('remove/',RemoveContentFromTestHTML.as_view()),
    path('process-html/', ProcessHTMLView.as_view()),
    path ('cmd/',execute_command),
    path('fsstat/', Fsstat.as_view()),
    path('live/', live_analysis.as_view()),
    path ('cmd/',upload_file),
]
