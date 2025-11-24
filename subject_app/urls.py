from rest_framework.urls import path
from .views import All_subjects

urlpatterns=[
    path('', All_subjects.as_view(), name='all_subjects')
]