from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('events.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
]
# Configure admin titles
admin.site.site_header = "Human Resource Management"
admin.site.site_title = "HR Management"
admin.site.index_title = "Welcome To The Admin"
