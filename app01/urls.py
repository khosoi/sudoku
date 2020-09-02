from django.conf.urls import url
from django.urls import path
from . import views
 
app_name = 'app01'
 
urlpatterns = [
    path('sudoku', views.app_sudoku, name='sudoku'),
    path('sudoku_solve', views.app_sudoku_solve, name='sudoku_solve'),
    path('user', views.app_user, name='user'),
    path('icons', views.app_icons, name='icons'),
    path('map', views.app_map, name='map'),
    path('maps', views.app_maps, name='maps'),
    path('notifications', views.app_notifications, name='notifications'),
    path('rtl', views.app_rtl, name='rtl'),
    path('tables', views.app_tables, name='tables'),
    path('typography', views.app_typography, name='typography'),
    path('upgrade', views.app_upgrade, name='upgrade'),
]
