from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from users import urls as urls_users
from tickets import urls as urls_tickets
from charts import urls as urls_charts
from users.views import index, superuser

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin/', superuser, name="superuser"),
    url(r'^$', index, name='index'),
    url(r'^users/', include(urls_users)),
    url(r'^tickets/', include(urls_tickets)),
    url(r'^charts/', include(urls_charts)),
]
urlpatterns += static(settings.MEDIA_URL)

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
        )
