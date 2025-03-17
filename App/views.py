#from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.


class PostListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

#view to list posts by a particular user
class UserPostListView(ListView):
    model = Post
    template_name = 'user_posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'object'
    
    def get_context_data(self, **kwargs):
        datas = super().get_context_data(**kwargs)
        datas['comments'] = Comment.objects.filter(post=datas['object'])

        likes_connected = get_object_or_404(Post, id= self.kwargs['pk'])
        liked=False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        datas['number_of_likes'] =  likes_connected.number_of_likes()
        datas['post_is_liked'] = liked

        return datas
    


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_form.html'
    fields = ['title','content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
#    success_url=

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'post_form.html'
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    #Function to ensure the user is the author of that post and not some other user
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_confirmed_delete.html'
    success_url = '/'

    #Function to ensure the user is the author of that post and not some other user
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
    
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'comment_form.html'
    fields = ['content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        path = self.request.path
        pri_key = path[path.find('t/')+2:-9]
        posts = Post.objects.get(pk=pri_key)
        form.instance.post = posts
        return super().form_valid(form)
def about(request):
    return render(request,'about.html',{'title':'About'})

def PostLike(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.likes.filter(id = request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))