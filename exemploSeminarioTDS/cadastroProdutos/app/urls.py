from app.views import ProdutoViewSet, EstoqueViewSet
from django.template.defaulttags import url
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"produto", ProdutoViewSet)
router.register(r"estoque", EstoqueViewSet)
urlpatterns = router.urls



