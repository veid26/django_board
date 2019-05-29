from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView
from .models import Board, Post, Topic
from django.db.models import Count
# Create your views here.
class BoardListView(ListView):
    model = Board
    context_object_name = 'boards'
    template_name = 'home.html'
	
def home(request):
	"""board = Board.object.all()"""
	board = Board.object.all()
	return render(request, 'home.html', {'boards':boards})