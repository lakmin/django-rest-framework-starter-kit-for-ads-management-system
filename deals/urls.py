from django.contrib import admin
from django.urls import path, include
from .views import (
    DealListApiView,
    # DealDetailApiView
)
urlpatterns = [
    path('', DealListApiView.as_view()),
    # path('<int:todo_id>/', DealDetailApiView.as_view()),
]