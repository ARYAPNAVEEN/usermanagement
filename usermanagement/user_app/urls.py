"""
URL configuration for usermanagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import register  # Import your views
from .views import login_user
from .views import profile
from .views import admin_login
from .views import dashboard
from .views import edit
from .views import logout_user
from .views import update
from .views import get_user
from .views import delete
from .views import delete
from .views import search_user


from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', login_user,name='login'),  # Home route
    path('register/', register, name='register'),
    # path('',login_user,name="login"),
    path('profile/',profile,name="profile"),
    path('admin_login/',admin_login,name="adminlogin"),
    path('dashboard/',dashboard,name="dashboard"),
    path('edit/',edit,name="edit"),
    path('logout/',logout_user,name='logout'),
    path('get_user/<int:id>/',get_user,name='get_user'),
    path('update/<int:id>/',update,name='update'),
    path('delete/<int:id>/',delete,name='delete'),
    path('search/',search_user,name='search'),


]










# from django.contrib import admin
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('',views.display,name="display"),
#     path('login/',views.login,name="login"),
#     path('register/',views.register,name="register"),
#     path('create/',views.create_todo,name='create'),
#     path('get/<int:id>/',views.get_todo,name='get'),
#     path('update/<int:id>/',views.update,name="update"),
#     path('delete/<int:id>/',views.delete,name="delete")
    
# ]