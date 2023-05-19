from django.urls import path
from django.urls import path
from producer.views import add_performances

#
# urlpatterns = [
#     path('<slug:slug>', views.performance_detail, name='performance_detail'),
#     path('', views.performance_all, name='performance_all'),
#
# ]

app_name = 'producer'

urlpatterns = [
    path('add-performances/', add_performances, name='add_performances'),

]