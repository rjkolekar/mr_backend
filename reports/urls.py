from django.urls import path
from . import views

urlpatterns = [
    path('reports/', views.report_list),
    path('reports/<int:pk>/', views.report_detail),
]
