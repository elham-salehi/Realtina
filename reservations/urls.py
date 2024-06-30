from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .reports import report
from .views import ListViewSet, ReservationViewSet

router = DefaultRouter()
router.register(r'lists', ListViewSet)
router.register(r'reservations', ReservationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('report/', report, name='report'),
]
