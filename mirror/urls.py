from django.contrib import admin
from django.urls import path
from mirror import views

urlpatterns = [
    path('', views.home_redirect, name='mirror-home'),
    path('admin/', admin.site.urls),  # Usando o admin padrão do Django
    path('mirror/', include('mirror.urls')),  # URLs específicas do app mirror
    path('<path:path>/', views.serve_cloned_page, name='cloned-page'),
]
