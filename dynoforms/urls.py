from django.conf.urls import url
from dynoforms import views

urlpatterns = [
    url(r'^schemes/$', views.Schemes.as_view() , name='dynoforms-schemes'),
    url(r'^schemes/(?P<pk>\d+)/new-entry/$', views.NewEntry.as_view(), name='dynoforms-new-entry'),
    url(r'^entries/(?P<pk>\d+)/detail/$', views.EntryDetail.as_view(), name='dynoforms-entry-detail'),
]
