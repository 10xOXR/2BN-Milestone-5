from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from users import urls as urls_users
from tickets import urls as urls_tickets
from charts import urls as urls_charts
from users.views import index, superuser

urlpatterns = [
    path("admin/", admin.site.urls),
    path("admin/", superuser, name="superuser"),
    path("", index, name='index'),
    path("users/", include(urls_users)),
    path("tickets/", include(urls_tickets)),
    path("charts/", include(urls_charts)),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
