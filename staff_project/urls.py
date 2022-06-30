"""staff_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from staff import views

urlpatterns = [
    # path('admin/', admin.site.urls),

    # 部门管理
    path('depart/list/', views.depart_list),
    path('depart/add/', views.depart_add, ),
    path('depart/delete/', views.depart_delete, ),
    path('depart/<int:nid>/edit/', views.depart_edit, ),

    # 用户管理
    path('user/list/', views.user_list, ),
    path('user/add/', views.user_add, ),
    path('user/<int:nid>/edit/', views.user_edit, ),
    path('user/<int:nid>/delete/', views.user_delete, ),

    # 靓号管理
    path('phone/list/', views.phone_list),
    path('phone/add/', views.phone_add),
    path('phone/<int:nid>/edit/', views.phone_edit),
    path('phone/<int:nid>/delete/', views.phone_delete),

    # 管理员管理
    path('admin/list/', views.admin_list),
    path('admin/add/', views.admin_add),
    path('admin/<int:nid>/edit/', views.admin_edit),
    path('admin/<int:nid>/delete/', views.admin_delete),

    # 登录
    path('login/',views.login),
    path('logout/',views.logout),
]
