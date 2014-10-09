from django.conf.urls import *

urlpatterns = patterns('labgeeks_apollo.views',
                        url(r'^$', 'tools_list'),
                        url('(?P<formid>[0-9]+)/$', 'tool'),
)
