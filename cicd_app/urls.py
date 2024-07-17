from django.urls import path
from cicd_app import views
urlpatterns = [
    path('have_a_great_day',views.MorningAPI.as_view()),
]