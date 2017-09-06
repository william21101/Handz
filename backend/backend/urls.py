from django.conf.urls import url, include

urlpatterns = [
    url(r'^api/', include('api.urls')),
    url(r'^chat/', include('channels_app.urls', namespace='channels_app')),
]

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
