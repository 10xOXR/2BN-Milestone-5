from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as urls_accounts
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import index, superuser

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin/', superuser, name="superuser"),
    url(r'^$', index, name='index'),
    url(r'^accounts/', include(urls_accounts)),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
        )
