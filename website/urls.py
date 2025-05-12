from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('avalie/', views.avalie, name='avalie'),
    path('avalie_enviar/', views.avalie_view, name='avalie_view'),

]
