from django.urls import path,include
from django.contrib.auth.views import LoginView
from django.conf.urls.static import static
from django.conf import settings
from .import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('login/', LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('', views.home, name='home')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)