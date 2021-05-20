from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Talk


class TalkListView(ListView):
    model = Talk
    context_object_name = "talks"


class TalkSearchView(TalkListView):
    template_name = "talks/talk_table.html"

    def get_queryset(self):
        talks = super().get_queryset()
        if "search" in self.request.GET:
            search = self.request.GET["search"]
            talks = talks.filter(
                Q(title__icontains=search) | Q(description__icontains=search)
            )
        return talks


class TalkDetailView(DetailView):
    model = Talk


class TalkCreateView(CreateView):
    model = Talk
    fields = ["title", "description", "speaker", "tags"]


class TalkUpdateView(UpdateView):
    model = Talk
    fields = ["title", "description", "speaker", "tags"]


class TalkDeleteView(DeleteView):
    model = Talk
    success_url = reverse_lazy("talk_list")
