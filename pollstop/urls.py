from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from tags import views as tv


router = routers.SimpleRouter()

router.register(r'tags', tv.TagViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/auth/', include('rest_framework.urls',
                                  namespace='rest_framework')),
    url(r'^api/v1/', include(router.urls, namespace='apiv1')),
]
