from django.urls import path
from . import views

urlpatterns = [
		path('', views.index, name = 'index'),
		path('band/', views.band, name = 'band'),
		path('gigs/', views.gigs, name = 'gigs'),
		path('fans/', views.fans, name = 'fans'),
		path('merchandise/', views.merchandise, name = 'merchandise'),
		]
