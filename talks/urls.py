from django.urls import path

from .views import (
    TalkCreateView,
    TalkDeleteView,
    TalkDetailView,
    TalkListView,
    TalkSearchView,
    TalkUpdateView,
)

urlpatterns = [
    path("", TalkListView.as_view(), name="talk_list"),
    path("search/", TalkSearchView.as_view(), name="talk_search"),
    path("new/", TalkCreateView.as_view(), name="talk_create"),
    path("<int:pk>/", TalkDetailView.as_view(), name="talk_detail"),
    path("<int:pk>/edit", TalkUpdateView.as_view(), name="talk_update"),
    path("<int:pk>/delete", TalkDeleteView.as_view(), name="talk_delete"),
]
