from django.urls import path

from command import views

urlpatterns = [
    path('', views.personal_page),
    path('hello',views.F001),
path('hello',views.F002),
path('hello',views.F003),
path('hello',views.F004),
path('hello',views.F005),
path('hello',views.F006),
path('hello',views.F007),
path('hello',views.F007_1),
path('hello',views.F008),

]
