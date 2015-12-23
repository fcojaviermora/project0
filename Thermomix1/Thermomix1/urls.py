from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
# Uncomment the next two lines to enable the admin:
import xadmin

from xadmin.plugins import xversion
xversion.register_models()

from django.contrib import admin

urlpatterns = patterns('',
    (r'^recipes/', include('recipes.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(xadmin.site.urls))
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 