from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import Bookmark


class BookmarkList(ListView):
  model = Bookmark


class BookmarkCreateView(CreateView):
  model = Bookmark
  fields = ['site_name', 'url']
  success_url = reverse_lazy('bookmark:list')
  template_name_suffix = '_create'
