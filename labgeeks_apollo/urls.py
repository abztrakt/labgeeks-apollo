from django.conf.urls import *

urlpatterns = patterns('labgeeks_apollo.views',
                        url(r'^closing-procedures', 'views.closing_procedures'),
)
