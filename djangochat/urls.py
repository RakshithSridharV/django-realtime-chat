from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from chat import views   # ✅ FIXED

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chat.urls')),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)