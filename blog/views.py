from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Post
from .forms import Postform


def post_list(request):
    posts = Post.objects.filter(publised_date__lte=timezone.now()).order_by('publised_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html',{'post':post})

def post_new(request):
    if request.method=='POST':
        form = Postform(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publised_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = Postform()
    return render(request, 'blog/post_edit.html',{'form':form})