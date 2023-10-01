from django.urls import path, include
from . import views, admin

urlpatterns = [
    path('one/', views.one, name="one"),
    path('createNewUser/', views.createNewUser),

]
