from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.homepage),
    path('home/post_event/', views.postEvent),
    path('home/browse_event/', views.browseEvents),
    path('home/browse_event/<id>', views.register),
    path('registration_done/', views.regDone),
    path('hosting_done/', views.hostDone)
    
]