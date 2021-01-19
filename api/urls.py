
from django.urls import path

from api import views

app_name = 'api'

urlpatterns = [
    path('users/',views.UserAPIView.as_view()),
    # path('computers/',views.ComputerAPIView.as_view())
]