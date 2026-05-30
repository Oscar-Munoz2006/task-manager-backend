from django.contrib import admin
from django.urls import path, include
from .views import LoginView, LogoutView, RefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('tasks.urls')),
    path('api/v1/login/', LoginView.as_view(), name='login'),
    path('api/v1/logout/', LogoutView.as_view(), name='logout'),
    path('api/v1/refresh/', RefreshView.as_view(), name='refresh'),
]