from django.urls import path
from app1.views import *
app_name = 'nothing'

urlpatterns = [
    path('first_1/',first_1,name='first_1'),
    path('second_1/',second_1,name='second_1'),
    path('third_1/',third_1,name='third_1'),
]