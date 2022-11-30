from django.urls import path
from . import views

urlpatterns = [
    path('campos/', views.campos, name='campos'),
    path('campos/rio/', views.rio, name='rio'),
    path('campos/sp/', views.sao, name='Sao'),
    path('campos/bp/', views.bp, name='bp'),
    path('campos/rio/cbp/', views.rioreservcbp, name='rioreservcbp'),
    path('campos/rio/ssf/', views.rioreservssf, name='rioreservssf'),
    path('campos/rio/mdg/', views.rioreservmdg, name='rioreservmdg'),
    path('campos/sp/rb/', views.spreservrb, name='spreservrb'),
    path('campos/sp/asv/', views.spreservasv, name='spreservasv'),
    path('campos/sp/af/', views.spreservaf, name='spreservaf'),
    path('campos/bp/csc/', views.bpreservcsc, name='bpreservcsc'),
    path('campos/bp/bg/', views.bpreservbg, name='bpreservbg'),
    path('campos/bp/rsc/', views.bpreservrsc, name='bpreservrsc'),

]
