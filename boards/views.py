from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView
from .models import Board, Post, Topic
from django.db.models import Count
# Create your views here.
class BoardListView(ListView):
    model = Board
    context_object_name = 'boards'
    template_name = 'boars.html'
	
def home(request):
	all_boards = Board.objects.all()
	boards_count = Board.objects.all().count()
	posts_count = Post.objects.all().count()
	return render(request, 'home.html',
	context ={'all_boards':all_boards, 'boards_count':boards_count})