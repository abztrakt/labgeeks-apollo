from django.conf.urls import *

urlpatterns = patterns('labgeeks_apollo.views',
                        url(r'^closing-procedures/$', 'closing_procedures'),
                        url(r'^printer-issue/$', 'printer_issue'),
                        url(r'^login-issue/$', 'login_issue'),
                        url(r'^$', 'tools_list'),
)
