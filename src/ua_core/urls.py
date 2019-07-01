from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as urls_accounts
from accounts.views import index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^accounts/', include(urls_accounts)),
]
