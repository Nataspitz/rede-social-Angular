from django.urls import path
from .views import CreateListUserView, RetriveUpdateDeleteUserView


urlpatterns = [
    path('users/', CreateListUserView.as_view()),
    path('users/<str:uid>/', RetriveUpdateDeleteUserView.as_view()),
    # path('users/<str:uid>/', UpdateDeleteUserView.as_view()),
]