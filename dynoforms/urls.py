from django.conf.urls import url
from dynoforms import views

urlpatterns = [
    url(r'^schemes/(?P<schema_pk>\d+)/new-data$', views.DynoFormCreateData.as_view(), name='dynoforms-entry-create'),
    url(r'^entries/(?P<pk>\d+)/detail/$', views.DynoFormEntryDetail.as_view(), name='dynoforms-entry-detail'),
]
