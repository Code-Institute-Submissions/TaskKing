from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todolist.urls')),
    path('login/', LoginView.as_view(template_name='todolist/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]