from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("recrutamento/", include("recrutamento.urls")),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path("admin/", admin.site.urls),

]