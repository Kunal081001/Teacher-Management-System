from django.contrib import admin
from django.urls import path
from home import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.homepage, name="home"),
    path('registration', views.registrationuser, name="registration"),
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('teacherform', views.teacherform, name="teacherform"),
    path('about', views.aboutus, name="about"),
    path('inner_login', views.inner_login, name="inner_login"),
    path('contact', views.contactus, name="contact"),
    path('super_user', views.super_user, name="super_user"),
    path('show_more/<int:id>', views.show_more, name="show_more"),
    path('edit/<int:pk>', views.edit, name="edit"),
    path('update/<int:pk>', views.update, name="update"),
    path('delete/<int:pk>', views.destroy, name="delete"),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

