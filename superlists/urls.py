from django.conf.urls import url, include
from django.contrib import admin
from lists import views as list_wiews
from lists import urls as list_urls

urlpatterns = [
    url(r'^$', list_wiews.home_page, name='home'),
    url(r'^lists/', include(list_urls)),
    url(r'^admin/', admin.site.urls),
]
