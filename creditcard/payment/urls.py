from django.urls import path
from . import views

urlpatterns = [

path('',views.home,name='home'),
path('addpay/',views.addpay),
path('existpay/',views.existpay),
path('addpay/onaddpay',views.onaddpay),
path('existpay/success',views.final),

]
