from django.urls import path
from .views import MatchesTodayView

urlpatterns = [
    path('today/', MatchesTodayView.as_view(), name='matches-today'),
]
