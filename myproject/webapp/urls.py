from django.conf.urls import include , url
from django.urls import path
from django.urls import reverse
from . import views
from .views import user_in,utables,index,model,HRlogmodel,impression,reach,ut1

urlpatterns= [

    #path('', views.index, name='index'),
    url('^$', views.model, name='model'),
    path('index/',index, name='index'),
    path('userins/', user_in),
    path('utables/', utables),
    path('impressions/', impression),
    path('reaches/', reach),
    path('genderdist/', ut1),
    path('model/', model),
    path('HRlogmodel',views.HRlogmodel,name='HRlogmodel'),

]

