from django.urls import path
from . import views

urlpatterns = [
    path('homepage/',views.homepage_view),
    path('hydjobs/',views.hydJobs_view,name='hydJobs_view'),
    path('bangjobs/',views.bengalurujobs_view,name='bengalurujobs_view'),
    path('punejobs/',views.punejobs_view,name='punejobs_view')
]