# from django.conf.urls import url
from testapp import views
from django.urls import path

urlpatterns = [
    path('first/',views.firstView),
    path('second/',views.secondView),
    path('third/',views.thirdView),
    path('fourth/',views.fourthView),
    path('fifth/',views.fifthView),
]
