from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from scpca_portal.views import SampleViewSet, ExperimentViewSet

router = DefaultRouter()
router.register(r'samples', SampleViewSet, basename='sample')
router.register(r'experiments', ExperimentViewSet, basename='experiment')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
