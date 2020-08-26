from django.urls import path
from . import views
urlpatterns = [
    path('',views.Home),
    path('heart/',views.Heart,),
    path('malaria/',views.Malaria),
    path('liver/',views.Liver)
]