from . import views
from django.urls import path

urlpatterns = [
    path('signup/', views.SingUp.as_view(), name='signup'),
]
