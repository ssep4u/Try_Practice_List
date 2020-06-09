from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from .models import Bookmark


class BookmarkList(ListView):
  model = Bookmark
  paginate_by = 3


class BookmarkSearchList(ListView):
  model = Bookmark
  template_name = 'bookmark/bookmark_list.html'
  paginate_by = 3

  def get_queryset(self):
    search_site_name = self.request.GET.get('search_site_name', '')

    if search_site_name == '':
      bookmark_list = self.model.objects.all()
    else:
      bookmark_list = self.model.objects.filter(site_name__contains=search_site_name)

    return bookmark_list


class BookmarkCreateView(CreateView):
  model = Bookmark
  fields = ['site_name', 'url']
  success_url = reverse_lazy('bookmark:list')
  template_name_suffix = '_create'


class BookmarkDetailView(DetailView):
  model = Bookmark


class BookmarkUpdateView(UpdateView):
  model = Bookmark
  fields = ['site_name', 'url']
  template_name_suffix = '_update'


class BookmarkDeleteView(DeleteView):
  model = Bookmark
  success_url = reverse_lazy('bookmark:list')
