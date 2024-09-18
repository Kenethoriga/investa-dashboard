from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),            # Admin route
    path('', include('accounts.urls')),         # Include the accounts app's URLs
]
