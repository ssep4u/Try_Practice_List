from django.shortcuts import render
from django.views.generic import ListView

from .models import Bookmark


class BookmarkList(ListView):
  model = Bookmark
