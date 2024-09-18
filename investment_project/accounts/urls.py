from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InvestmentAccountViewSet, TransactionViewSet, dashboard

router = DefaultRouter()
router.register(r'accounts', InvestmentAccountViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    #path('', dashboard, name='dashboard'),  # Ensure the comma here
    path('', include(router.urls)),     # Correct API path
]
