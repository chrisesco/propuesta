from django.urls import path
from propuestaApp import views


urlpatterns = [
    path('',views.HomeView.as_view(),name="home"),
    path('sobremi/',views.SobreMiView.as_view(),name="sobremi"),
    path('propuestavalor/',views.PropuestaValorView.as_view(),name="propuestavalor")
]
