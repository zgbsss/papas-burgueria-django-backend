"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView)
from rest_framework.routers import DefaultRouter
from papasburgueria.views import (
    HamburguerViewSet,
    BebidaViewSet,
    IngredienteViewSet,
    LucroViewSet,
    ComandaViewSet,
)
from usuario.router import router as usuario_router
from uploader.router import router as uploader_router
from usuario.views import UsuarioViewSet

router = DefaultRouter()
router.register(r"hamburgueres", HamburguerViewSet)
router.register(r"bebidas", BebidaViewSet)
router.register(r"ingredientes", IngredienteViewSet)
router.register(r"lucros", LucroViewSet)
router.register(r"comandas", ComandaViewSet)
router.register(r"usuarios", UsuarioViewSet)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/usuarios", include(usuario_router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/media/", include(uploader_router.urls)),
    # OpenAPI
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/router", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]

urlpatterns += static(
    settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT
)
