from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.home, name='home'),

    path('products/', views.products, name='products'),

    path('register/', views.register, name='register'),

    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='shop/login.html'
        ),
        name='login'
    ),

    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),
]