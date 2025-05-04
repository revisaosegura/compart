from django.contrib import admin
from django.urls import path, re_path
from copart_clone import views  # ← Certifique-se que está importando corretamente

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.homepage, name="home"),
    path("sobre/", views.sobre, name="sobre"),
    path("lotes/", views.lotes, name="lotes"),
    path("contato/", views.contato, name="contato"),
    path("ajuda/", views.ajuda, name="ajuda"),
    path("termos/", views.termos, name="termos"),
    path("privacidade/", views.privacidade, name="privacidade"),
    path("login/", views.login, name="login"),
    re_path(r"^(?P<page>[\w-]+)/$", views.dynamic_template_view, name="pagina_dinamica"),
    path('admin/', admin.site.urls),
]
