from dataclasses import field, fields
from tkinter.tix import Form
from urllib import request
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import View
from .models import Post, Comment, UserProfile
from .forms import PostForm, CommentForm
from django.views.generic.edit import UpdateView, DeleteView
# Create your views here.

class PostListView(View):
    def get(self,request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm()

        context ={
            'post_list': posts,
            'fm': form,
        }

        return render(request,'social/post_list.html', context)
    
    def post(self,request,*args,**kwargs):
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()


        context ={
            'post_list': posts,
            'fm': form
        }

        return render(request,'social/post_list.html', context)

class PostDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm()
        
        comments = Comment.objects.filter(post=post).order_by('-created_on')

        context = {
            'post':post,
            'form':form,
            'comments':comments,
        }

        return render(request,'social/post_detail.html', context)
    
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.save()

        comments = Comment.objects.filter(post=post).order_by('-created_on')

        context = {
            'post':post,
            'form':form,
            'comments':comments,
        }

        return render(request,'social/post_detail.html', context)

class PostEditView(UpdateView):
    model = Post
    fields = ['body']
    template_name = 'social/post_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('post-detail',kwargs={'pk': pk}) 

class PostDeleteView(DeleteView):
    model = Post 
    template_name = 'social/post_delete.html'
    success_url = reverse_lazy('post-list')

class ProfileView(View):
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        user = profile.user
        posts = Post.objects.filter(author=user).order_by('-created_on')

        context ={
            'user':user,
            'profile':profile,
            'posts':posts,
        }

        print(profile)
        print(user)

        return render(request, 'social/profile.html', context)