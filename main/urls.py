from django.urls import path
from .views import *

urlpatterns = [
    path("say_hello/", say_hello),
    path ("profile/", user_profile),
    path("filter_query/<int:id>/", filter_queries),
    path("queries/", QueryView.as_view()), #.as_view renders every query function as part of the url
]