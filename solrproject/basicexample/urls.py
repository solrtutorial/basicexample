from django.conf.urls import include, patterns, url

urlpatterns = patterns(
    'basicexample.views',
    url(r'^status/$',
        'introduction',
        name='introduction'),
)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
