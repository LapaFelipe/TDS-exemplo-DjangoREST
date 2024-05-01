from app.views import ProdutoViewSet, EstoqueViewSet, index, create, update, delete
from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path("", index, name='listar_produtos'),
    path("api/", include("app.urls")),
    path('admin/', admin.site.urls),
    path("cadastro_produtos", create, name='cadastro_produtos'),
    path("update_produtos/<int:id>", update, name="update_produtos"),
    path("delete_produtos/<int:id>", delete, name="delete_produtos")
]
